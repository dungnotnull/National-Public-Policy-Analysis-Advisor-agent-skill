# Monitoring and Observability System

## Overview

Production-grade monitoring, logging, and observability system for the Public Policy Analysis Advisor, ensuring operational excellence, reliability, and performance optimization.

## System Architecture

### Monitoring Layers

```
┌─────────────────────────────────────────────────────────────┐
│                    User Interface Layer                       │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐    │
│  │  Dashboards  │  │    Alerts    │  │   Reports    │    │
│  └──────────────┘  └──────────────┘  └──────────────┘    │
└─────────────────────────────────────────────────────────────┘
                           ↕
┌─────────────────────────────────────────────────────────────┐
│                   Monitoring Platform                         │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐    │
│  │   Metrics    │  │    Logs      │  │    Traces    │    │
│  │  Collection  │  │ Collection   │  │  Collection  │    │
│  └──────────────┘  └──────────────┘  └──────────────┘    │
└─────────────────────────────────────────────────────────────┘
                           ↕
┌─────────────────────────────────────────────────────────────┐
│                  Application Services                        │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐    │
│  │   Analysis   │  │   Template   │  │ Validation   │    │
│  │   Service    │  │   Service    │  │   Service    │    │
│  └──────────────┘  └──────────────┘  └──────────────┘    │
└─────────────────────────────────────────────────────────────┘
```

## Metrics Collection

### Business Metrics

**Analysis Metrics:**
```yaml
analysis_requests_total:
  type: counter
  labels: [analysis_type, country, user_type]
  description: Total analysis requests

analysis_completion_time:
  type: histogram
  labels: [analysis_type]
  buckets: [1s, 5s, 10s, 30s, 60s, 300s]
  description: Analysis completion time

analysis_success_rate:
  type: gauge
  labels: [analysis_type]
  description: Success rate of analyses

framework_usage:
  type: counter
  labels: [framework, context]
  description: Framework usage frequency

template_rendering_time:
  type: histogram
  labels: [template_type]
  description: Template rendering performance
```

**User Metrics:**
```yaml
active_users:
  type: gauge
  description: Currently active users

user_retention:
  type: gauge
  labels: [period]
  description: User retention rates

feature_adoption:
  type: gauge
  labels: [feature]
  description: Feature adoption rates
```

### System Metrics

**Resource Metrics:**
```yaml
cpu_usage_percent:
  type: gauge
  labels: [service, instance]
  description: CPU utilization

memory_usage_bytes:
  type: gauge
  labels: [service, instance]
  description: Memory consumption

disk_usage_percent:
  type: gauge
  labels: [mount_point]
  description: Disk utilization

network_io:
  type: counter
  labels: [interface, direction]
  description: Network I/O
```

**Service Metrics:**
```yaml
request_rate:
  type: gauge
  labels: [endpoint, method]
  description: Request rate per second

error_rate:
  type: gauge
  labels: [endpoint, error_type]
  description: Error rate

latency:
  type: histogram
  labels: [endpoint]
  description: Request latency

queue_depth:
  type: gauge
  labels: [queue_name]
  description: Queue depth
```

### Custom Metrics

**Quality Metrics:**
```yaml
analysis_quality_score:
  type: gauge
  labels: [analysis_type]
  description: Analysis quality assessment

evidence_source_diversity:
  type: gauge
  description: Diversity of evidence sources used

framework_coverage:
  type: gauge
  labels: [analysis_type]
  description: Framework application completeness
```

## Logging System

### Log Levels

```python
DEBUG = 10    # Detailed diagnostic information
INFO = 20     # General operational information
WARNING = 30  # Unexpected but recoverable events
ERROR = 40    # Error conditions that prevent operation
CRITICAL = 50 # Critical conditions requiring immediate attention
```

### Log Format

**Structured JSON Logging:**
```json
{
  "timestamp": "2024-08-04T10:30:45.123Z",
  "level": "INFO",
  "service": "analysis-service",
  "request_id": "uuid",
  "user_id": "uuid",
  "correlation_id": "uuid",
  "event": "analysis_completed",
  "data": {
    "analysis_type": "full",
    "policy_issue": "Carbon pricing",
    "country": "CA",
    "duration_ms": 1250,
    "status": "success",
    "frameworks_used": ["problem_definition", "stakeholder_analysis"],
    "quality_score": 0.85
  },
  "context": {
    "version": "1.0.0",
    "environment": "production",
    "hostname": "analysis-prod-123",
    "pid": 4567
  }
}
```

### Logging Best Practices

**DO:**
- Use structured logging with consistent fields
- Include correlation IDs for request tracing
- Log at appropriate levels
- Include contextual information
- Use semantic event names

**DON'T:**
- Log sensitive information (PII, API keys)
- Log excessive detail at INFO level
- Log in loops (aggregate instead)
- Use string concatenation for logs
- Log without purpose

### Log Rotation

**Configuration:**
```yaml
logging:
  version: 1
  formatters:
    standard:
      format: '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
  handlers:
    file:
      class: logging.handlers.RotatingFileHandler
      formatter: standard
      filename: /var/log/policy-analysis/app.log
      maxBytes: 100MB
      backupCount: 10
    error_file:
      class: logging.handlers.RotatingFileHandler
      formatter: standard
      filename: /var/log/policy-analysis/error.log
      maxBytes: 100MB
      backupCount: 20
      level: ERROR
```

## Distributed Tracing

### OpenTelemetry Integration

**Trace Configuration:**
```python
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.jaeger.thrift import JaegerExporter

# Setup tracing
trace.set_tracer_provider(TracerProvider())
jaeger_exporter = JaegerExporter(
    agent_host_name="localhost",
    agent_port=6831,
)
trace.get_tracer_provider().add_span_processor(
    BatchSpanProcessor(jaeger_exporter)
)

tracer = trace.get_tracer(__name__)
```

### Span Creation

**Analysis Operation Tracing:**
```python
with tracer.start_as_current_span("analyze_policy") as span:
    span.set_attribute("analysis_type", analysis_type)
    span.set_attribute("policy_issue", policy_issue)
    span.set_attribute("country", country)

    with tracer.start_as_current_span("problem_definition"):
        result = problem_definition_analyzer.analyze(...)

    with tracer.start_as_current_span("stakeholder_analysis"):
        stakeholders = stakeholder_analyzer.analyze(...)
```

### Trace Propagation

**HTTP Headers:**
```
traceparent: 00-4bf92f3577b34da6a3ce929d0e0e4736-d1080145f10f0a7b-00
tracestate: rojo=00f067aa0ba902b7
```

## Health Check System

### Health Endpoints

**Liveness Probe:**
```yaml
GET /health/live
Response: 200 OK
Purpose: Container still running
```

**Readiness Probe:**
```yaml
GET /health/ready
Response:
  200 OK (ready)
  503 Service Unavailable (not ready)
Purpose: Service ready to accept traffic
```

**Health Check:**
```yaml
GET /health
Response:
  200 OK
  Body:
    {
      "status": "healthy",
      "timestamp": "2024-08-04T10:30:45Z",
      "checks": {
        "database": "healthy",
        "cache": "healthy",
        "queue": "healthy",
        "external_services": {
          "policy_api": "healthy"
        }
      },
      "version": "1.0.0"
    }
```

### Health Check Components

**Database Health:**
```python
def check_database():
    try:
        # Test database connection
        db.execute("SELECT 1")
        return {"status": "healthy", "latency_ms": latency}
    except Exception as e:
        return {"status": "unhealthy", "error": str(e)}
```

**Cache Health:**
```python
def check_cache():
    try:
        # Test cache operations
        cache.set("health_check", "ok", ttl=10)
        value = cache.get("health_check")
        return {"status": "healthy" if value == "ok" else "unhealthy"}
    except Exception as e:
        return {"status": "unhealthy", "error": str(e)}
```

**Queue Health:**
```python
def check_queue():
    try:
        depth = queue.depth()
        consumers = queue.consumer_count()
        return {
            "status": "healthy" if depth < 1000 else "degraded",
            "depth": depth,
            "consumers": consumers
        }
    except Exception as e:
        return {"status": "unhealthy", "error": str(e)}
```

## Alerting System

### Alert Rules

**Critical Alerts:**
```yaml
- name: HighErrorRate
  condition: error_rate > 0.05 (5%)
  for: 5m
  severity: critical
  annotations:
    summary: "High error rate detected"
    description: "Error rate is {{ $value }}% for the last 5 minutes"

- name: ServiceDown
  condition: up == 0
  for: 1m
  severity: critical
  annotations:
    summary: "Service is down"
    description: "{{ $labels.instance }} has been down for more than 1 minute"

- name: DatabaseConnectionFailed
  condition: database_health == 0
  for: 2m
  severity: critical
  annotations:
    summary: "Database connection failed"
```

**Warning Alerts:**
```yaml
- name: HighLatency
  condition: latency > 30s
  for: 10m
  severity: warning
  annotations:
    summary: "High analysis latency"
    description: "Average latency is {{ $value }}s"

- name: LowSuccessRate
  condition: success_rate < 0.95
  for: 15m
  severity: warning
  annotations:
    summary: "Low success rate"
    description: "Success rate is {{ $value }}%"
```

### Alert Channels

**Email Notifications:**
```yaml
receivers:
  - name: ops-team
    email_configs:
      - to: ops-team@example.com
        headers:
          subject: "[ALERT] {{ .GroupLabels.alertname }}"
```

**Slack Integration:**
```yaml
receivers:
  - name: slack-alerts
    slack_configs:
      - api_url: "https://hooks.slack.com/services/..."
        channel: "#alerts"
        title: "{{ .GroupLabels.alertname }}"
        text: "{{ range .Alerts }}{{ .Annotations.description }}{{ end }}"
```

**PagerDuty Integration:**
```yaml
receivers:
  - name: pagerduty
    pagerduty_configs:
      - service_key: "YOUR_SERVICE_KEY"
        description: "{{ .GroupLabels.alertname }}"
```

## Performance Monitoring

### APM Integration

**Application Performance Monitoring:**
```python
from opentelemetry.instrumentation.flask import FlaskInstrumentor
from opentelemetry.instrumentation.requests import RequestsInstrumentor

# Auto-instrument Flask
FlaskInstrumentor().instrument_app(app)

# Auto-instrument HTTP requests
RequestsInstrumentor().instrument()
```

### Performance Benchmarks

**Analysis Performance Targets:**
```yaml
problem_definition:
  p50: 5s
  p95: 10s
  p99: 15s

stakeholder_analysis:
  p50: 8s
  p95: 15s
  p99: 25s

alternatives_evaluation:
  p50: 15s
  p95: 30s
  p99: 45s

full_analysis:
  p50: 60s
  p95: 120s
  p99: 180s
```

### Performance Profiling

**Profiling Middleware:**
```python
import cProfile
import io
from contextlib import contextmanager

@contextmanager
def profile_middleware(request_id):
    profiler = cProfile.Profile()
    profiler.enable()
    try:
        yield
    finally:
        profiler.disable()
        profiler.dump_stats(f"/tmp/profile-{request_id}.prof")
```

## Dashboarding

### Grafana Dashboards

**System Overview Dashboard:**
- Request rate and latency
- Error rate by endpoint
- Resource utilization
- Queue depths
- Health status

**Business Metrics Dashboard:**
- Analysis requests by type
- User activity
- Feature adoption
- Quality scores
- Framework usage patterns

**Performance Dashboard:**
- Latency histograms
- Throughput metrics
- Database performance
- Cache hit rates
- External API performance

### Custom Metrics

**Analysis Quality Metrics:**
```python
def record_analysis_quality(analysis_type, quality_score):
    metrics.gauge(
        'analysis_quality_score',
        quality_score,
        tags={'analysis_type': analysis_type}
    )

def record_evidence_diversity(source_types, count):
    metrics.gauge(
        'evidence_source_diversity',
        len(source_types),
        tags={'total_sources': count}
    )
```

## Incident Response

### Incident Severity Levels

**P1 - Critical:**
- System completely down
- Data loss or corruption
- Security breach
- Impact: All users

**P2 - High:**
- Major functionality broken
- Performance severely degraded
- Data quality issues
- Impact: Many users

**P3 - Medium:**
- Minor functionality broken
- Performance degradation
- Non-critical bugs
- Impact: Some users

**P4 - Low:**
- Cosmetic issues
- Documentation gaps
- Enhancement requests
- Impact: Minimal

### Runbooks

**High Latency Runbook:**
1. Check system metrics (CPU, memory, I/O)
2. Check database performance
3. Check queue depths
4. Check external API status
5. Review recent deployments
6. Check for increased traffic

**High Error Rate Runbook:**
1. Check error logs for patterns
2. Check external service status
3. Review recent code changes
4. Check database connectivity
5. Review authentication system
6. Check rate limiting status

## Observability Stack

### Technology Choices

**Metrics:**
- Prometheus (metrics collection)
- Grafana (visualization)
- Alertmanager (alerting)

**Logging:**
- ELK Stack (Elasticsearch, Logstash, Kibana)
- Fluentd (log collection)
- Kibana (log visualization)

**Tracing:**
- Jaeger (distributed tracing)
- OpenTelemetry (instrumentation)
- Zipkin (alternative tracing)

**Dashboards:**
- Grafana (metrics dashboards)
- Kibana (log dashboards)
- Custom UI (business metrics)

### Deployment

**Docker Compose:**
```yaml
version: '3'
services:
  prometheus:
    image: prom/prometheus
    ports: ["9090:9090"]
    volumes:
      - ./prometheus.yml:/etc/prometheus/prometheus.yml

  grafana:
    image: grafana/grafana
    ports: ["3000:3000"]
    environment:
      - GF_SECURITY_ADMIN_PASSWORD=admin

  jaeger:
    image: jaegertracing/all-in-one
    ports: ["5775:5775", "16686:16686", "14268:14268"]

  elasticsearch:
    image: elasticsearch:7.10.0
    environment:
      - discovery.type=single-node
    ports: ["9200:9200"]

  kibana:
    image: kibana:7.10.0
    ports: ["5601:5601"]
    depends_on: [elasticsearch]
```

This comprehensive monitoring and observability system ensures production-grade reliability, performance optimization, and operational excellence for the Public Policy Analysis Advisor.
