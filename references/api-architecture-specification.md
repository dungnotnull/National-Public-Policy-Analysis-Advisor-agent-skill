# API-First Architecture Specification

## Overview

This specification defines the RESTful API architecture for the Public Policy Analysis Advisor, enabling programmatic access to policy analysis capabilities for integration with larger systems.

## Architecture Principles

1. **API-First Design:** API definition drives implementation
2. **RESTful Architecture:** Resource-oriented design with HTTP verbs
3. **JSON Payloads:** Standard JSON request/response format
4. **Versioning:** Semantic versioning with URL versioning
5. **Statelessness:** No server-side session state
6. **Security:** Authentication and authorization for all endpoints
7. **Documentation:** OpenAPI/Swagger specification
8. **Error Handling:** Consistent error response format

## Base Architecture

### Base URL

```
Production: https://api.policy-analysis.ai/v1
Development: https://dev.api.policy-analysis.ai/v1
Staging: https://staging.api.policy-analysis.ai/v1
```

### Versioning Strategy

**URL Versioning:**
- v1: Initial stable release
- v2: Breaking changes with backward compatibility support
- Support current + previous version

**Deprecation Policy:**
- 12-month deprecation notice
- Sunset warnings in response headers
- Migration documentation provided

## Authentication & Authorization

### Authentication Methods

**API Key Authentication:**
```
Header: Authorization: Bearer {api_key}
```

**OAuth 2.0:**
```
Endpoint: POST /oauth/token
Grant types: api_key, client_credentials
```

### Authorization Levels

| Level | Access | Rate Limit |
|-------|---------|------------|
| Basic | Standard analysis endpoints | 100 requests/hour |
| Professional | All endpoints + priority queue | 1000 requests/hour |
| Enterprise | All + custom integrations | Unlimited |

## Core API Endpoints

### Analysis Endpoints

#### POST /analyze

**Description:** Submit policy analysis request

**Request:**
```json
{
  "analysis_type": "full|problem_definition|stakeholder_analysis|alternatives_evaluation|evidence_synthesis|policy_cycle|behavioral|climate",
  "policy_issue": "string (required)",
  "country": "string (required, ISO-2 code)",
  "context": {
    "user_goal": "string",
    "audience": "string",
    "constraints": ["array"],
    "timeframe": "string"
  },
  "preferences": {
    "detail_level": "brief|standard|detailed",
    "output_format": "narrative|structured|both",
    "include_recommendations": boolean
  },
  "specific_focus": ["array of focus areas"],
  "options": {
    "behavioral_insights": boolean,
    "climate_specialization": boolean,
    "cognitive_mapping": boolean
  }
}
```

**Response:**
```json
{
  "request_id": "uuid",
  "status": "submitted|processing|completed|failed",
  "estimated_completion": "ISO-8601 timestamp",
  "message": "status message"
}
```

#### GET /analyze/{request_id}

**Description:** Retrieve analysis results

**Response:**
```json
{
  "request_id": "uuid",
  "status": "completed",
  "result": {
    "analysis": {},
    "metadata": {
      "frameworks_used": [],
      "confidence_level": "High|Moderate|Low",
      "data_quality": "High|Medium|Low",
      "processing_time_ms": number
    },
    "disclaimer_included": true
  },
  "timestamp": "ISO-8601"
}
```

### Framework-Specific Endpoints

#### POST /analyze/problem-definition

**Description:** Problem definition and framing analysis

**Request:**
```json
{
  "policy_issue": "string",
  "country": "string",
  "framing_depth": "basic|advanced|expert",
  "include_stakeholder_perspectives": boolean
}
```

#### POST /analyze/stakeholder-analysis

**Description:** Stakeholder mapping and analysis

**Request:**
```json
{
  "policy_issue": "string",
  "country": "string",
  "stakeholder_categories": ["government", "private", "civil_society"],
  "power_analysis": boolean,
  "coalition_analysis": boolean,
  "cognitive_mapping": boolean
}
```

#### POST /analyze/alternatives-evaluation

**Description:** Policy alternatives MCDA evaluation

**Request:**
```json
{
  "policy_issue": "string",
  "country": "string",
  "alternatives": ["alternative list"],
  "criteria": ["criteria list"],
  "criteria_weights": {"criterion": weight},
  "scoring_method": "additive|multiplicative|geometric"
}
```

### Specialized Endpoints

#### POST /analyze/behavioral

**Description:** Behavioral policy analysis

**Request:**
```json
{
  "policy_issue": "string",
  "country": "string",
  "behavioral_assessment": {
    "target_behavior": "string",
    "biases_analyzed": ["availability", "status_quo", "loss_aversion"],
    "nudge_opportunities": boolean
  }
}
```

#### POST /analyze/climate

**Description:** Climate policy specialized analysis

**Request:**
```json
{
  "climate_issue": "mitigation|adaptation|finance|technology",
  "country": "string",
  "temperature_target": "1.5°C|2.0°C",
  "carbon_budget_analysis": boolean,
  "just_transition_analysis": boolean
}
```

### Template & Schema Endpoints

#### GET /templates

**Description:** List available templates

**Response:**
```json
{
  "templates": [
    {
      "type": "problem-definition",
      "name": "Problem Definition Template",
      "description": "Template for problem framing analysis",
      "version": "1.0"
    }
  ]
}
```

#### GET /templates/{template_type}

**Description:** Get specific template schema

**Response:**
```json
{
  "template": {},
  "structure": {},
  "requirements": {},
  "examples": []
}
```

#### POST /templates/render

**Description:** Render template with data

**Request:**
```json
{
  "template_type": "string",
  "data": {}
}
```

### Validation Endpoints

#### POST /validate/input

**Description:** Validate analysis request

**Request:**
```json
{
  "analysis_request": {}
}
```

**Response:**
```json
{
  "valid": boolean,
  "errors": [],
  "warnings": []
}
```

#### POST /validate/output

**Description:** Validate analysis output

**Request:**
```json
{
  "analysis_output": {}
}
```

### Batch Processing

#### POST /batch

**Description:** Submit batch analysis requests

**Request:**
```json
{
  "requests": [
    {"analysis_request": {}},
    {"analysis_request": {}}
  ],
  "callback_url": "string",
  "priority": "normal|high"
}
```

**Response:**
```json
{
  "batch_id": "uuid",
  "request_count": number,
  "estimated_completion": "ISO-8601"
}
```

#### GET /batch/{batch_id}

**Description:** Get batch processing status

**Response:**
```json
{
  "batch_id": "uuid",
  "status": "processing|completed|failed",
  "completed": number,
  "total": number,
  "results": [{"request_id": "uuid", "status": "completed"}]
}
```

## Error Handling

### Error Response Format

```json
{
  "error": {
    "code": "ERROR_CODE",
    "message": "Human-readable error message",
    "details": {},
    "request_id": "uuid",
    "timestamp": "ISO-8601"
  }
}
```

### Error Codes

| Code | HTTP Status | Description |
|------|------------|-------------|
| INVALID_REQUEST | 400 | Malformed request |
| UNAUTHORIZED | 401 | Authentication failed |
| FORBIDDEN | 403 | Insufficient permissions |
| NOT_FOUND | 404 | Resource not found |
| RATE_LIMIT_EXCEEDED | 429 | Too many requests |
| INVALID_INPUT | 422 | Input validation failed |
| INTERNAL_ERROR | 500 | Server error |
| SERVICE_UNAVAILABLE | 503 | Service temporarily unavailable |

### Rate Limiting

**Headers:**
```
X-RateLimit-Limit: 1000
X-RateLimit-Remaining: 950
X-RateLimit-Reset: 1634567890
```

**Response (Rate Limited):**
```json
{
  "error": {
    "code": "RATE_LIMIT_EXCEEDED",
    "message": "Rate limit exceeded",
    "retry_after": 3600
  }
}
```

## Webhooks

### Webhook Configuration

**Endpoint:** POST /webhooks

**Request:**
```json
{
  "url": "https://your-server.com/webhook",
  "events": ["analysis.completed", "analysis.failed"],
  "secret": "webhook_secret_key"
}
```

**Webhook Payload:**
```json
{
  "event": "analysis.completed",
  "timestamp": "ISO-8601",
  "data": {
    "request_id": "uuid",
    "status": "completed",
    "result_url": "https://api.policy-analysis.ai/v1/analyze/{request_id}"
  },
  "signature": "HMAC-SHA256"
}
```

## OpenAPI Specification

### OpenAPI 3.0

**Endpoint:** GET /openapi.yaml

**Content:** Full OpenAPI 3.0 specification

### Swagger UI

**Endpoint:** GET /docs

**Interactive API documentation**

## SDK Generation

### Language Support

- **Python:** pip install policy-analysis-sdk
- **JavaScript:** npm install @policy-analysis/sdk
- **Java:** Maven dependency
- **Go:** go get github.com/policy-analysis/sdk

### SDK Features

- Authentication handling
- Request/response serialization
- Error handling
- Retry logic
- Async support

## Integration Examples

### Python SDK

```python
from policy_analysis import PolicyAnalysisClient

client = PolicyAnalysisClient(api_key="your_key")

response = client.analyze(
    analysis_type="full",
    policy_issue="Carbon pricing policy",
    country="CA",
    options={
        "behavioral_insights": True,
        "climate_specialization": True
    }
)

result = response.get_result(timeout=300)
print(result.analysis)
```

### JavaScript SDK

```javascript
const PolicyAnalysis = require('@policy-analysis/sdk');

const client = new PolicyAnalysis.Client({
  apiKey: 'your_key'
});

const response = await client.analyze({
  analysisType: 'stakeholder',
  policyIssue: 'Minimum wage policy',
  country: 'US'
});

const result = await response.getResult();
console.log(result.analysis);
```

## Deployment Architecture

### Microservices Architecture

**Services:**
- **API Gateway:** Request routing, authentication
- **Analysis Service:** Core policy analysis logic
- **Template Service:** Template rendering
- **Validation Service:** Input/output validation
- **Queue Service:** Asynchronous processing
- **Notification Service:** Webhook delivery
- **Monitoring Service:** Metrics and logging

### Infrastructure

**Container Orchestration:**
- Docker containers
- Kubernetes orchestration
- Service mesh (Istio)
- Ingress controllers

**Database:**
- PostgreSQL (relational data)
- Redis (caching, queues)
- Elasticsearch (logs, search)

**Message Queue:**
- RabbitMQ or Kafka
- Job queues
- Dead letter queues

### Scalability

**Horizontal Scaling:**
- Auto-scaling groups
- Load balancing
- Service discovery

**Vertical Scaling:**
- Resource allocation
- Performance optimization
- Cost optimization

## Monitoring & Observability

### Metrics

**System Metrics:**
- Request rate, latency, errors
- Queue depth, processing time
- Resource utilization
- Service health

**Business Metrics:**
- Analysis type distribution
- User patterns
- API key usage
- Feature utilization

### Logging

**Structured Logging:**
```json
{
  "timestamp": "ISO-8601",
  "level": "info|warn|error",
  "service": "api-gateway",
  "request_id": "uuid",
  "user_id": "uuid",
  "method": "POST",
  "path": "/analyze",
  "status_code": 200,
  "latency_ms": 1250,
  "message": "Analysis completed successfully"
}
```

**Log Aggregation:**
- ELK Stack (Elasticsearch, Logstash, Kibana)
- Centralized logging
- Log retention policies

### Tracing

**Distributed Tracing:**
- OpenTelemetry
- Jaeger or Zipkin
- Trace propagation
- Performance analysis

## Security

### HTTPS Only

**Enforced:**
- TLS 1.2+
- Certificate pinning
- HSTS headers
- Secure cookie handling

### Input Validation

**Strict Validation:**
- JSON Schema validation
- SQL injection prevention
- XSS protection
- CSRF protection

### Rate Limiting

**Per-Endpoint Limits:**
- Different limits for different endpoints
- Tiered pricing
- Burst capacity

### DDoS Protection

**Mitigation:**
- Cloudflare or AWS Shield
- Rate limiting
- IP blacklisting
- Challenge mechanisms

## Testing

### API Testing

**Automated Testing:**
- Unit tests
- Integration tests
- Contract tests
- End-to-end tests

**Load Testing:**
- Locust or k6
- Performance benchmarks
- Capacity planning

### Documentation Testing

**Examples:**
- Request/response examples
- Error scenarios
- Edge cases
- Integration patterns

## API Documentation

### Swagger/OpenAPI

**Interactive Documentation:**
- Try-it-out functionality
- Schema definitions
- Example requests/responses
- Error codes

### Developer Portal

**Resources:**
- Getting started guides
- Authentication guide
- Rate limiting info
- Best practices
- Troubleshooting

### SDK Documentation

**Language-Specific:**
- Installation instructions
- Code examples
- API reference
- Migration guides

## Client Integration

### Authentication Setup

**Python:**
```python
client = PolicyAnalysisClient(
    api_key=os.environ['POLICY_ANALYSIS_API_KEY'],
    base_url='https://api.policy-analysis.ai/v1'
)
```

### Error Handling

**Best Practices:**
```python
try:
    result = client.analyze(...)
except PolicyAnalysisError as e:
    if e.code == 'RATE_LIMIT_EXCEEDED':
        time.sleep(e.retry_after)
    else:
        logger.error(f"Analysis failed: {e}")
```

### Retry Logic

**Exponential Backoff:**
```python
from tenacity import retry, stop_after_attempt, wait_exponential

@retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=4, max=10))
def call_analysis():
    return client.analyze(...)
```

This API-first architecture enables seamless integration of policy analysis capabilities into any system, from individual research tools to large-scale policy platforms, providing programmatic access to rigorous policy analysis frameworks and methodologies.
