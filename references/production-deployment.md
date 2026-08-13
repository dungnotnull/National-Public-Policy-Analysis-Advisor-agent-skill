# Production Deployment Guide

## Deployment Architecture

### Container-Based Deployment

**Docker Compose Production:**
```yaml
version: '3.8'

services:
  # API Gateway
  api-gateway:
    image: policy-analysis/api-gateway:1.0
    ports:
      - "80:80"
      - "443:443"
    environment:
      - ENV=production
      - LOG_LEVEL=info
    deploy:
      replicas: 3
      resources:
        limits:
          cpus: '0.5'
          memory: 512M
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:80/health"]
      interval: 30s
      timeout: 10s
      retries: 3

  # Analysis Service
  analysis-service:
    image: policy-analysis/analysis-service:1.0
    environment:
      - LOG_LEVEL=info
      - MODEL_TIMEOUT=120
    deploy:
      replicas: 5
      resources:
        limits:
          cpus: '2.0'
          memory: 2048M
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8080/health"]
      interval: 30s
      timeout: 10s
      retries: 3

  # Worker Service
  worker-service:
    image: policy-analysis/worker:1.0
    environment:
      - CONCURRENCY=4
      - QUEUE_MAX_SIZE=1000
    deploy:
      replicas: 3
      resources:
        limits:
          cpus: '1.0'
          memory: 1024M

  # PostgreSQL
  postgres:
    image: postgres:14-alpine
    environment:
      - POSTGRES_DB=policy_analysis
      - POSTGRES_USER=policy_user
      - POSTGRES_PASSWORD=${DB_PASSWORD}
    volumes:
      - postgres_data:/var/lib/postgresql/data
    deploy:
      resources:
        limits:
          cpus: '1.0'
          memory: 1024M
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U policy_user"]
      interval: 10s
      timeout: 5s
      retries: 5

  # Redis
  redis:
    image: redis:7-alpine
    command: redis-server --appendonly yes
    volumes:
      - redis_data:/data
    deploy:
      resources:
        limits:
          cpus: '0.5'
          memory: 512M
    healthcheck:
      test: ["CMD", "redis-cli", "ping"]
      interval: 10s
      timeout: 5s
      retries: 5

  # Monitoring Stack
  prometheus:
    image: prom/prometheus:latest
    ports:
      - "9090:9090"
    volumes:
      - ./prometheus.yml:/etc/prometheus/prometheus.yml
      - prometheus_data:/prometheus
    command:
      - '--config.file=/etc/prometheus/prometheus.yml'
      - '--storage.tsdb.path=/prometheus'
      - '--web.console.libraries=/etc/prometheus/console_libraries'
      - '--web.console.libraries=/etc/prometheus/console_libraries'
      - '--storage.tsdb.retention.time=200h'
      - '--web.external.url=http://prometheus:9090'

  grafana:
    image: grafana/grafana:latest
    ports:
      - "3000:3000"
    environment:
      - GF_SECURITY_ADMIN_PASSWORD=${GRAFANA_PASSWORD}
      - GF_USERS_ALLOW_SIGN_UP=false
    volumes:
      - grafana_data:/var/lib/grafana
      - ./grafana/provisioning:/etc/grafana/provisioning

volumes:
  postgres_data:
  redis_data:
  prometheus_data:
  grafana_data:
```

### Kubernetes Deployment

**Namespace Configuration:**
```yaml
apiVersion: v1
kind: Namespace
metadata:
  name: policy-analysis
  labels:
    name: policy-analysis
    environment: production
```

**Deployment:**
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: analysis-service
  namespace: policy-analysis
spec:
  replicas: 5
  selector:
    matchLabels:
      app: analysis-service
  template:
    metadata:
      labels:
        app: analysis-service
        version: v1.0.0
    spec:
      containers:
      - name: analysis-service
        image: policy-analysis/analysis-service:1.0.0
        ports:
        - containerPort: 8080
          name: http
        env:
        - name: ENV
          value: "production"
        - name: LOG_LEVEL
          value: "info"
        - name: DATABASE_URL
          valueFrom:
            secretKeyRef:
              name: database-secrets
              key: url
        resources:
          requests:
            memory: "512Mi"
            cpu: "500m"
          limits:
            memory: "2048Mi"
            cpu: "2000m"
        livenessProbe:
          httpGet:
            path: /health/live
            port: 8080
          initialDelaySeconds: 30
          periodSeconds: 10
        readinessProbe:
          httpGet:
            path: /health/ready
            port: 8080
          initialDelaySeconds: 10
          periodSeconds: 5
```

**Service:**
```yaml
apiVersion: v1
kind: Service
metadata:
  name: analysis-service
  namespace: policy-analysis
spec:
  selector:
    app: analysis-service
  ports:
  - protocol: TCP
    port: 80
    targetPort: 8080
  type: ClusterIP
```

**Ingress:**
```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: api-ingress
  namespace: policy-analysis
  annotations:
    cert-manager.io/cluster-issuer: letsencrypt-prod
    nginx.ingress.kubernetes.io/rate-limit: "100"
spec:
  tls:
  - hosts:
    - api.policy-analysis.ai
    secretName: api-tls
  rules:
  - host: api.policy-analysis.ai
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: api-gateway
            port:
              number: 80
```

## Infrastructure Setup

### Cloud Provider Options

**AWS Architecture:**
```
┌─────────────────────────────────────────────────┐
│                  Route 53                       │
│              (DNS Management)                    │
└─────────────────────────────────────────────────┘
                    ↕
┌─────────────────────────────────────────────────┐
│               CloudFront CDN                     │
│             (Global Content Delivery)            │
└─────────────────────────────────────────────────┘
                    ↕
┌─────────────────────────────────────────────────┐
│          Application Load Balancer               │
│              (SSL Termination)                   │
└─────────────────────────────────────────────────┘
                    ↕
┌─────────────────────────────────────────────────┐
│           ECS / EKS Cluster                       │
│  ┌──────────────┐  ┌──────────────┐             │
│  │   API GW     │  │  Analysis    │             │
│  │  Container   │  │  Container   │             │
│  └──────────────┘  └──────────────┘             │
└─────────────────────────────────────────────────┘
                    ↕
┌─────────────────────────────────────────────────┐
│              RDS PostgreSQL                      │
│            (Multi-AZ, Read Replicas)             │
└─────────────────────────────────────────────────┘
                    ↕
┌─────────────────────────────────────────────────┐
│                 ElastiCache                       │
│              (Redis Cluster)                     │
└─────────────────────────────────────────────────┘
```

**GCP Architecture:**
```
┌─────────────────────────────────────────────────┐
│            Cloud Load Balancing                  │
└─────────────────────────────────────────────────┘
                    ↕
┌─────────────────────────────────────────────────┐
│         Google Kubernetes Engine (GKE)           │
│  ┌──────────────┐  ┌──────────────┐             │
│  │   API GW     │  │  Analysis    │             │
│  │  Container   │  │  Container   │             │
│  └──────────────┘  └──────────────┘             │
└─────────────────────────────────────────────────┘
                    ↕
┌─────────────────────────────────────────────────┐
│            Cloud SQL (PostgreSQL)                │
└─────────────────────────────────────────────────┘
                    ↕
┌─────────────────────────────────────────────────┐
│           Memorystore (Redis)                    │
└─────────────────────────────────────────────────┘
```

**Azure Architecture:**
```
┌─────────────────────────────────────────────────┐
│           Azure Front Door                      │
└─────────────────────────────────────────────────┘
                    ↕
┌─────────────────────────────────────────────────┐
│         Azure Load Balancer                     │
└─────────────────────────────────────────────────┘
                    ↕
┌─────────────────────────────────────────────────┐
│         Azure Kubernetes Service (AKS)          │
│  ┌──────────────┐  ┌──────────────┐             │
│  │   API GW     │  │  Analysis    │             │
│  │  Container   │  │  Container   │             │
│  └──────────────┘  └──────────────┘             │
└─────────────────────────────────────────────────┘
                    ↕
┌─────────────────────────────────────────────────┐
│        Azure Database for PostgreSQL              │
└─────────────────────────────────────────────────┘
                    ↕
┌─────────────────────────────────────────────────┐
│              Azure Cache for Redis               │
└─────────────────────────────────────────────────┘
```

## CI/CD Pipeline

### GitHub Actions Workflow

**.github/workflows/deploy.yml:**
```yaml
name: Deploy Production

on:
  push:
    tags:
      - 'v*'

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      
      - name: Install dependencies
        run: |
          pip install -r requirements.txt
          pip install pytest pytest-cov
      
      - name: Run tests
        run: |
          pytest --cov=policy_analysis --cov-report=xml
      
      - name: Upload coverage
        uses: codecov/codecov-action@v3
        with:
          file: ./coverage.xml

  build:
    needs: test
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Configure AWS credentials
        uses: aws-actions/configure-aws-credentials@v2
        with:
          aws-access-key-id: ${{ secrets.AWS_ACCESS_KEY_ID }}
          aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
          aws-region: us-east-1
      
      - name: Login to Amazon ECR
        id: login-ecr
        uses: aws-actions/amazon-ecr-login@v1
      
      - name: Build and push images
        env:
          ECR_REGISTRY: ${{ steps.login-ecr.outputs.registry }}
          IMAGE_TAG: ${{ github.ref_name }}
        run: |
          docker build -t $ECR_REGISTRY/policy-analysis:$IMAGE_TAG .
          docker push $ECR_REGISTRY/policy-analysis:$IMAGE_TAG
          docker tag $ECR_REGISTRY/policy-analysis:$IMAGE_TAG $ECR_REGISTRY/policy-analysis:latest
          docker push $ECR_REGISTRY/policy-analysis:latest

  deploy:
    needs: build
    runs-on: ubuntu-latest
    steps:
      - name: Deploy to ECS
        run: |
          aws ecs update-service --cluster policy-analysis-prod \
            --service analysis-service --force-new-deployment
      
      - name: Run smoke tests
        run: |
          ./scripts/smoke-test.sh
```

## Database Setup

### PostgreSQL Configuration

**Production Settings:**
```sql
-- PostgreSQL Configuration
ALTER SYSTEM SET max_connections = 200;
ALTER SYSTEM SET shared_buffers = '2GB';
ALTER SYSTEM SET effective_cache_size = '6GB';
ALTER SYSTEM SET maintenance_work_mem = '512MB';
ALTER SYSTEM SET checkpoint_completion_target = 0.9;
ALTER SYSTEM SET wal_buffers = '16MB';
ALTER SYSTEM SET default_statistics_target = 100;
ALTER SYSTEM SET random_page_cost = 1.1;

-- Enable extensions
CREATE EXTENSION IF NOT EXISTS pg_stat_statements;
CREATE EXTENSION IF NOT EXISTS pg_trgm;
```

**Backup Strategy:**
```bash
# Automated backups
pg_dump -Fc policy_analysis > backup_$(date +%Y%m%d).dump

# WAL archiving
archive_mode = on
archive_command = 'cp %p /var/lib/postgresql/archive/%f'
```

## Security Hardening

### SSL/TLS Configuration

**Nginx Configuration:**
```nginx
server {
    listen 443 ssl http2;
    server_name api.policy-analysis.ai;

    ssl_certificate /etc/ssl/certs/api.policy-analysis.ai.crt;
    ssl_certificate_key /etc/ssl/certs/api.policy-analysis.ai.key;
    
    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_ciphers ECDHE-RSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-GCM-SHA384;
    ssl_prefer_server_ciphers off;
    
    ssl_session_cache shared:SSL:10m;
    ssl_session_timeout 10m;
    
    add_header Strict-Transport-Security "max-age=31536000; includeSubDomains" always;
    add_header X-Frame-Options DENY;
    add_header X-Content-Type-Options nosniff;
}
```

### Firewall Rules

**Security Groups:**
```yaml
Inbound:
  - Port 443 (HTTPS) from 0.0.0.0/0
  - Port 22 (SSH) from office IP range
  - Port 9090 (Prometheus) from monitoring IP range
  
Outbound:
  - All traffic (for external APIs)
```

### Secrets Management

**AWS Secrets Manager:**
```bash
# Store database credentials
aws secretsmanager create-secret \
  --name policy-analysis/database \
  --secret-string file://db-credentials.json

# Store API keys
aws secretsmanager create-secret \
  --name policy-analysis/api-keys \
  --secret-string file://api-keys.json
```

## Performance Optimization

### Caching Strategy

**Redis Caching:**
```python
import redis
import json

cache = redis.Redis(host='redis', port=6379, db=0)

def cache_analysis_result(request_id, result, ttl=3600):
    """Cache analysis result for 1 hour"""
    cache.setex(
        f"analysis:{request_id}",
        ttl,
        json.dumps(result)
    )

def get_cached_result(request_id):
    """Retrieve cached result if available"""
    cached = cache.get(f"analysis:{request_id}")
    if cached:
        return json.loads(cached)
    return None
```

### Database Optimization

**Indexing Strategy:**
```sql
-- Indexes for common queries
CREATE INDEX idx_analysis_requests_user ON analysis_requests(user_id);
CREATE INDEX idx_analysis_requests_type ON analysis_requests(analysis_type);
CREATE INDEX idx_analysis_requests_status ON analysis_requests(status);
CREATE INDEX idx_analysis_requests_created ON analysis_requests(created_at);

-- Composite indexes
CREATE INDEX idx_analysis_user_type ON analysis_requests(user_id, analysis_type);
```

### Connection Pooling

**PgBouncer Configuration:**
```ini
[databases]
policy_analysis = host=/var/run/postgresql port=5432 dbname=policy_analysis

[pgbouncer]
pool_mode = transaction
max_client_conn = 1000
default_pool_size = 25
reserve_pool_size = 5
reserve_pool_timeout = 3
max_db_connections = 100
idle_timeout = 600
```

## Monitoring Setup

### Prometheus Configuration

**prometheus.yml:**
```yaml
global:
  scrape_interval: 15s
  evaluation_interval: 15s

scrape_configs:
  - job_name: 'policy-analysis'
    static_configs:
      - targets: ['api-gateway:9090', 'analysis-service:9090']
    metrics_path: '/metrics'
    scrape_interval: 30s

  - job_name: 'postgres'
    static_configs:
      - targets: ['postgres-exporter:9187']

  - job_name: 'redis'
    static_configs:
      - targets: ['redis-exporter:9121']
```

### Grafana Dashboards

**Import Dashboard:**
```bash
curl -X POST \
  -H "Authorization: Bearer ${GRAFANA_API_KEY}" \
  -H "Content-Type: application/json" \
  -d @dashboard.json \
  http://grafana:3000/api/dashboards/db
```

## Disaster Recovery

### Backup Strategy

**Database Backups:**
```bash
# Daily full backups
0 2 * * * pg_dump -Fc policy_analysis > /backup/daily/dump_$(date +\%Y\%m\%d).sql

# Weekly full backups to S3
0 3 * * 0 aws s3 cp /backup/daily/dump_*.sql s3://backups/postgres/
```

**Infrastructure as Code:**
```bash
# Terraform state backup
terraform state pull > backup/terraform_$(date +%Y%m%d).tfstate
```

### High Availability

**Multi-Region Deployment:**
- Primary region: us-east-1
- Disaster recovery region: us-west-2
- Data replication: Async replication
- DNS failover: Route 53 health checks

## Cost Optimization

### Resource Rightsizing

**Instance Types:**
- Development: t3.medium (cost-effective)
- Staging: t3.large (balanced)
- Production: m5.xlarge (compute optimized)

**Auto-Scaling:**
```yaml
autoscaling:
  minimum: 3 instances
  maximum: 10 instances
  target_cpu: 70%
  target_memory: 80%
  scale_up_cooldown: 300s
  scale_down_cooldown: 300s
```

### Reserved Instances

**Cost Savings:**
- Purchase reserved instances for baseline load
- Use spot instances for batch processing
- Utilize savings plans for predictable workloads

## Compliance

### SOC 2 Compliance

**Controls:**
- Access logging and monitoring
- Change management procedures
- Incident response plan
- Data encryption at rest and in transit
- Regular security assessments

### GDPR Compliance

**Data Protection:**
- Data minimization
- Right to deletion
- Data portability
- Privacy by design
- Data processing agreements

This deployment guide ensures production-grade reliability, security, and performance for the Public Policy Analysis Advisor across multiple deployment environments.
