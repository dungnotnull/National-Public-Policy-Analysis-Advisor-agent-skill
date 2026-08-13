#!/usr/bin/env python3
"""
Configuration validation script for Public Policy Analysis Advisor.

This script validates configuration files against the schema and ensures
all required fields are present and valid.
"""

import json
import sys
from pathlib import Path
from typing import Dict, Any, Tuple

# Simple JSON schema validation without external dependencies
def validate_schema(config: Dict[str, Any], schema: Dict[str, Any]) -> Tuple[bool, list]:
    """
    Validate configuration against schema.

    Args:
        config: Configuration dictionary
        schema: Schema dictionary

    Returns:
        Tuple of (is_valid, list of errors)
    """
    errors = []

    def validate_value(value: Any, property_schema: Dict[str, Any], path: str = ""):
        """Validate a value against its property schema."""

        # Check required
        if property_schema.get("required", False) and value is None:
            errors.append(f"{path or 'root'}: Required field is missing")
            return

        if value is None:
            return  # Optional field that's None

        # Type validation
        expected_type = property_schema.get("type")
        if expected_type:
            if expected_type == "string" and not isinstance(value, str):
                errors.append(f"{path}: Expected string, got {type(value).__name__}")
            elif expected_type == "number" and not isinstance(value, (int, float)):
                errors.append(f"{path}: Expected number, got {type(value).__name__}")
            elif expected_type == "integer" and not isinstance(value, int):
                errors.append(f"{path}: Expected integer, got {type(value).__name__}")
            elif expected_type == "boolean" and not isinstance(value, bool):
                errors.append(f"{path}: Expected boolean, got {type(value).__name__}")
            elif expected_type == "array" and not isinstance(value, list):
                errors.append(f"{path}: Expected array, got {type(value).__name__}")
            elif expected_type == "object" and not isinstance(value, dict):
                errors.append(f"{path}: Expected object, got {type(value).__name__}")

        # String patterns
        if expected_type == "string" and "pattern" in property_schema:
            import re
            pattern = property_schema["pattern"]
            if not re.match(pattern, value):
                errors.append(f"{path}: Does not match pattern {pattern}")

        # Number ranges
        if expected_type in ("number", "integer") and value is not None:
            if "minimum" in property_schema and value < property_schema["minimum"]:
                errors.append(f"{path}: Value {value} below minimum {property_schema['minimum']}")
            if "maximum" in property_schema and value > property_schema["maximum"]:
                errors.append(f"{path}: Value {value} above maximum {property_schema['maximum']}")

        # String length
        if expected_type == "string":
            if "minLength" in property_schema and len(value) < property_schema["minLength"]:
                errors.append(f"{path}: String length {len(value)} below minimum {property_schema['minLength']}")
            if "maxLength" in property_schema and len(value) > property_schema["maxLength"]:
                errors.append(f"{path}: String length {len(value)} above maximum {property_schema['maxLength']}")

        # Array constraints
        if expected_type == "array":
            if "minItems" in property_schema and len(value) < property_schema["minItems"]:
                errors.append(f"{path}: Array length {len(value)} below minimum {property_schema['minItems']}")
            if "items" in property_schema and isinstance(value, list):
                for i, item in enumerate(value):
                    validate_value(item, property_schema["items"], f"{path}[{i}]")

        # Object properties
        if expected_type == "object" and "properties" in property_schema:
            required = property_schema.get("required", [])
            for prop_name, prop_schema in property_schema["properties"].items():
                prop_value = value.get(prop_name)
                prop_path = f"{path}.{prop_name}" if path else prop_name
                if prop_name in required and prop_value is None:
                    errors.append(f"{prop_path}: Required property missing")
                elif prop_value is not None:
                    validate_value(prop_value, prop_schema, prop_path)

    # Validate top-level properties
    if "properties" in schema:
        for prop_name, prop_schema in schema["properties"].items():
            prop_value = config.get(prop_name)
            if prop_name in schema.get("required", []) and prop_value is None:
                errors.append(f"root.{prop_name}: Required property missing")
            elif prop_value is not None:
                validate_value(prop_value, prop_schema, prop_name)

    return len(errors) == 0, errors


def main():
    """Main validation function."""
    # Get paths
    config_dir = Path(__file__).parent
    schema_path = config_dir / "schema.json"
    default_config_path = config_dir / "default.json"

    # Load schema
    try:
        with open(schema_path, 'r') as f:
            schema = json.load(f)
        print(f"✓ Loaded schema from {schema_path}")
    except Exception as e:
        print(f"✗ Error loading schema: {e}", file=sys.stderr)
        return 1

    # Load default config
    try:
        with open(default_config_path, 'r') as f:
            config = json.load(f)
        print(f"✓ Loaded configuration from {default_config_path}")
    except Exception as e:
        print(f"✗ Error loading configuration: {e}", file=sys.stderr)
        return 1

    # Validate
    print("\nValidating configuration against schema...")
    is_valid, errors = validate_schema(config, schema)

    if is_valid:
        print("✓ Configuration is valid!")
        print(f"\nSkill: {config['skill_metadata']['name']}")
        print(f"Version: {config['skill_metadata']['version']}")
        print(f"Timeout: {config['execution']['timeout']}ms")
        print(f"Min quality score: {config['quality_standards']['min_quality_score']}")
        return 0
    else:
        print(f"✗ Configuration validation failed with {len(errors)} error(s):")
        for error in errors:
            print(f"  • {error}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
