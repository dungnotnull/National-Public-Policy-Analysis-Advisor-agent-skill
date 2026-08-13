# SKILL_REGISTRY.md — Skill Registration and Execution System

## Overview

This document describes how skills are registered, resolved, executed, and validated within the Public Policy Analysis Advisor system. The skill registry provides a type-safe, validated framework for managing policy analysis capabilities.

## Skill Registration

### Registration Schema

Every skill must declare itself using the following schema:

```json
{
  "name": "skill-identifier",
  "version": "1.0.0",
  "description": "When to trigger this skill",
  "compatibility": {
    "required_tools": ["tool1", "tool2"],
    "dependencies": ["dependency1"]
  },
  "execution": {
    "handler": "handler_function",
    "timeout_ms": 30000,
    "retry_policy": "exponential_backoff"
  },
  "validation": {
    "input_schema": "schemas/input-schema.json",
    "output_schema": "schemas/output-schema.json"
  }
}
```

### Registration Process

1. **Skill Discovery**
   - Skills are auto-discovered from the skill directory
   - SKILL.md frontmatter is parsed for metadata
   - Compatibility requirements are validated

2. **Schema Validation**
   - Input/output schemas are validated against JSON Schema Draft 7
   - Type safety is enforced at registration time
   - Invalid schemas prevent registration

3. **Handler Resolution**
   - Execution handler functions are located and validated
   - Handler signatures are checked against input schemas
   - Dependency injection is configured

## Skill Resolution

### Resolution Algorithm

When a user request is received, the system resolves skills using:

1. **Keyword Matching**
   - User input is tokenized and normalized
   - Skill descriptions are scanned for keyword matches
   - Relevance scores are computed

2. **Contextual Inference**
   - Conversation history is analyzed for intent
   - Previous skill usage influences resolution
   - Domain-specific patterns are detected

3. **Confidence Scoring**
   - Matches are scored by relevance and confidence
   - Top-scoring skills above threshold are candidates
   - Multiple skills may be resolved for composition

### Resolution Caching

- Skill resolutions are cached for performance
- Cache key includes: normalized input + conversation state
- Cache TTL: 5 minutes
- Cache invalidation: skill registration changes

## Skill Execution

### Execution Flow

```
User Request → Skill Resolution → Input Validation → Handler Execution → Output Validation → Response Formatting
```

### Execution Context

Each skill executes with a structured context:

```json
{
  "request_id": "unique-identifier",
  "user_input": "original request text",
  "resolved_skills": ["skill1", "skill2"],
  "conversation_history": ["previous messages"],
  "user_context": {
    "user_id": "identifier",
    "preferences": {},
    "permissions": []
  },
  "system_context": {
    "timestamp": "ISO-8601",
    "model_version": "model-id",
    "execution_environment": "environment"
  }
}
```

### Error Handling

Errors during execution follow this hierarchy:

1. **Validation Errors** (400)
   - Input doesn't match schema
   - Missing required fields
   - Type mismatches

2. **Execution Errors** (500)
   - Handler failures
   - External dependency failures
   - Resource constraints

3. **Timeout Errors** (408)
   - Execution exceeds timeout
   - Graceful degradation attempted
   - Partial results returned if available

### Graceful Fallbacks

When failures occur:

1. **Validation Failure**
   - Return specific validation error messages
   - Suggest corrections to user input
   - Provide schema requirements

2. **Execution Failure**
   - Attempt alternative handlers
   - Return cached results if available
   - Degrade to simpler skill version

3. **Timeout Failure**
   - Return partial results with timeout notice
   - Suggest retry with different parameters
   - Offer asynchronous execution option

## Input/Output Validation

### Input Validation Schema

Inputs are validated against strict schemas:

```json
{
  "type": "object",
  "properties": {
    "policy_issue": {
      "type": "string",
      "minLength": 10,
      "description": "The policy issue to analyze"
    },
    "country": {
      "type": "string",
      "pattern": "^[A-Z]{2}$",
      "description": "ISO country code"
    },
    "analysis_type": {
      "type": "string",
      "enum": ["full", "problem_definition", "stakeholder_analysis", "alternatives_evaluation", "evidence_synthesis", "policy_cycle"],
      "description": "Type of analysis requested"
    },
    "context": {
      "type": "object",
      "properties": {
        "user_goal": {"type": "string"},
        "audience": {"type": "string"},
        "constraints": {"type": "array"}
      }
    }
  },
  "required": ["policy_issue", "country", "analysis_type"]
}
```

### Output Validation Schema

Outputs are validated against result schemas:

```json
{
  "type": "object",
  "properties": {
    "request_id": {"type": "string"},
    "status": {
      "type": "string",
      "enum": ["success", "partial", "error"]
    },
    "result": {
      "type": "object",
      "properties": {
        "analysis": {},
        "metadata": {
          "type": "object",
          "properties": {
            "frameworks_used": {"type": "array"},
            "confidence_score": {"type": "number"},
            "data_quality": {"type": "string"}
          }
        },
        "disclaimer_required": {"type": "boolean"}
      }
    },
    "errors": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "code": {"type": "string"},
          "message": {"type": "string"},
          "field": {"type": "string"}
        }
      }
    }
  },
  "required": ["request_id", "status"]
}
```

## Skill Composition

### Composition Patterns

Multiple skills can be composed for complex analyses:

1. **Sequential Composition**
   - Skills execute in order, passing outputs as inputs
   - Each skill's output validates against next skill's input schema

2. **Parallel Composition**
   - Skills execute simultaneously
   - Results are merged at composition point

3. **Conditional Composition**
   - Skills execute based on conditions
   - Branching logic directs execution flow

### Composition Example

```
User Request: "Analyze housing policy in Canada"

Resolution:
1. problem-definition (sequential) → stakeholder-analysis (parallel with)
2. alternatives-evaluation → evidence-synthesis (sequential) → policy-cycle (final)

Execution Flow:
problem-definition → [stakeholder-analysis, alternatives-evaluation] → evidence-synthesis → policy-cycle
```

## Performance Optimization

### Optimization Strategies

1. **Caching**
   - Skill resolution results cached
   - Common analysis patterns cached
   - Template rendering results cached

2. **Lazy Loading**
   - Reference files loaded on demand
   - Templates loaded when needed
   - Handlers initialized at execution time

3. **Batching**
   - Multiple skill validations batched
   - Template renders batched
   - Schema compilations batched

### Monitoring Metrics

Key metrics tracked:

- **Resolution Time**: Time to resolve skills
- **Validation Time**: Time to validate inputs/outputs
- **Execution Time**: Time to execute handlers
- **Cache Hit Rate**: Percentage of cache hits
- **Error Rate**: Percentage of failed executions

## Security Considerations

### Input Sanitization

All inputs are sanitized:

- Remove potentially malicious content
- Escape special characters
- Validate against strict schemas
- Limit input sizes

### Output Filtering

All outputs are filtered:

- Remove sensitive information
- Apply content policies
- Validate against output schemas
- Sanitize formatting

### Permission Checks

Execution requires permissions:

- Read access to reference files
- Write access to output locations
- Network access for external calls
- Resource allocation quotas

## Debugging and Troubleshooting

### Debug Mode

Enable debug mode for detailed logging:

```json
{
  "debug": true,
  "log_level": "verbose",
  "include_stack_traces": true
}
```

### Common Issues

**Skill not resolving:**
- Check description keywords
- Verify registration status
- Review compatibility requirements

**Validation failures:**
- Review input schema requirements
- Check data types and formats
- Validate required fields

**Execution failures:**
- Check handler implementation
- Verify dependencies
- Review error logs

### Diagnostic Tools

Use these scripts for diagnostics:

- `scripts/skill-validator.py` - Validate skill registration
- `scripts/evaluator.py` - Test skill execution
- `scripts/template-renderer.py` - Test template rendering

## Extending the System

### Adding New Skills

To add a new skill:

1. Create skill directory structure
2. Write SKILL.md with proper metadata
3. Implement handler function
4. Define input/output schemas
5. Register skill in registry
6. Run validation tests

### Adding New Frameworks

To add a new analysis framework:

1. Create reference file in `references/`
2. Define methodology steps
3. Create template in `assets/templates/`
4. Update SKILL.md to reference new framework
5. Add test cases to `evals/evals.json`

### Adding New Templates

To add a new template:

1. Create template in `assets/templates/`
2. Define JSON structure
3. Add rendering logic to `scripts/template-renderer.py`
4. Update documentation
5. Test with sample data

## Best Practices

1. **Schema Design**
   - Use strict validation for security
   - Provide clear error messages
   - Document all fields and constraints

2. **Handler Implementation**
   - Keep handlers focused and simple
   - Handle all error cases
   - Log execution for debugging

3. **Template Design**
   - Use consistent structure
   - Provide clear field names
   - Include validation constraints

4. **Documentation**
   - Document all components
   - Provide examples
   - Keep docs synchronized with code
