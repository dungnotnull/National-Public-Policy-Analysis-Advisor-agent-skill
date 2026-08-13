#!/usr/bin/env python3
"""
Template Renderer for Policy Analysis Outputs

This script renders structured templates with analysis data to produce
consistent, validated outputs for the Public Policy Analysis Advisor.
"""

import json
import sys
from pathlib import Path
from typing import Dict, Any, List
from datetime import datetime


class TemplateRenderer:
    """Renderer for policy analysis templates."""

    def __init__(self, templates_dir: Path):
        """Initialize the template renderer.

        Args:
            templates_dir: Directory containing template files
        """
        self.templates_dir = templates_dir
        self.templates = {}
        self._load_templates()

    def _load_templates(self):
        """Load all templates from templates directory."""
        if not self.templates_dir.exists():
            print(f"Warning: Templates directory not found at {self.templates_dir}")
            return

        for template_file in self.templates_dir.glob('*.json'):
            try:
                with open(template_file, 'r') as f:
                    template = json.load(f)
                    template_type = template.get('template_type', template_file.stem)
                    self.templates[template_type] = template
                    print(f"Loaded template: {template_type}")
            except Exception as e:
                print(f"Error loading template {template_file}: {e}", file=sys.stderr)

    def render_template(self, template_type: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """Render a template with provided data.

        Args:
            template_type: Type of template to render
            data: Data to fill into template

        Returns:
            Rendered output dictionary
        """
        if template_type not in self.templates:
            raise ValueError(f"Template type '{template_type}' not found")

        template = self.templates[template_type]
        structure = template.get('structure', {})

        # Merge data into template structure
        rendered = self._merge_data_into_structure(structure, data)

        # Add metadata
        rendered['metadata'] = {
            'template_type': template_type,
            'rendered_at': datetime.now().isoformat(),
            'template_version': template.get('version', '1.0')
        }

        return rendered

    def _merge_data_into_structure(self, structure: Dict[str, Any], data: Dict[str, Any]) -> Dict[str, Any]:
        """Merge data into template structure recursively.

        Args:
            structure: Template structure
            data: Data to merge

        Returns:
            Merged dictionary
        """
        result = {}

        for key, value in structure.items():
            if key in data:
                # Use data value if provided
                result[key] = data[key]
            elif isinstance(value, dict):
                # Recursively process nested structures
                result[key] = self._merge_data_into_structure(value, data.get(key, {}))
            elif isinstance(value, list) and value and isinstance(value[0], dict):
                # Handle list of objects
                result[key] = data.get(key, [])
            else:
                # Use template default
                result[key] = value

        return result

    def validate_output(self, output: Dict[str, Any], template_type: str) -> Tuple[bool, List[str]]:
        """Validate output against template requirements.

        Args:
            output: Output to validate
            template_type: Type of template

        Returns:
            Tuple of (is_valid, list of errors)
        """
        if template_type not in self.templates:
            return False, [f"Template type '{template_type}' not found"]

        template = self.templates[template_type]
        requirements = template.get('output_requirements', {})
        required_sections = requirements.get('required_sections', [])

        errors = []

        for section in required_sections:
            if section not in output:
                errors.append(f"Required section '{section}' missing from output")

        quality_checks = requirements.get('quality_checks', [])
        for check in quality_checks:
            # This would need more sophisticated validation logic
            # For now, just log that checks exist
            pass

        return len(errors) == 0, errors

    def list_templates(self) -> List[str]:
        """List available template types.

        Returns:
            List of template type names
        """
        return list(self.templates.keys())

    def get_template_info(self, template_type: str) -> Dict[str, Any]:
        """Get information about a template.

        Args:
            template_type: Type of template

        Returns:
            Template information dictionary
        """
        if template_type not in self.templates:
            raise ValueError(f"Template type '{template_type}' not found")

        template = self.templates[template_type]
        return {
            'type': template.get('template_type'),
            'version': template.get('version'),
            'description': template.get('description'),
            'required_sections': template.get('output_requirements', {}).get('required_sections', []),
            'optional_sections': template.get('output_requirements', {}).get('optional_sections', [])
        }


def main():
    """Main template rendering function."""
    import argparse

    parser = argparse.ArgumentParser(description='Render policy analysis templates')
    parser.add_argument('--list', action='store_true', help='List available templates')
    parser.add_argument('--info', type=str, help='Show information about a template')
    parser.add_argument('--template', type=str, help='Template type to render')
    parser.add_argument('--data', type=str, help='JSON data file to merge into template')
    parser.add_argument('--output', type=str, help='Output file path')
    parser.add_argument('--validate', action='store_true', help='Validate output against template')

    args = parser.parse_args()

    # Get paths
    project_root = Path(__file__).parent.parent
    templates_dir = project_root / 'assets' / 'templates'

    # Initialize renderer
    renderer = TemplateRenderer(templates_dir)

    if args.list:
        print("\nAvailable templates:")
        for template_type in renderer.list_templates():
            print(f"  • {template_type}")
        return 0

    if args.info:
        try:
            info = renderer.get_template_info(args.info)
            print(f"\nTemplate: {info['type']}")
            print(f"Version: {info['version']}")
            print(f"Description: {info['description']}")
            print(f"\nRequired sections: {', '.join(info['required_sections'])}")
            print(f"Optional sections: {', '.join(info['optional_sections'])}")
            return 0
        except ValueError as e:
            print(f"Error: {e}", file=sys.stderr)
            return 1

    if args.template:
        # Load data
        if args.data:
            data_path = Path(args.data)
            try:
                with open(data_path, 'r') as f:
                    data = json.load(f)
            except Exception as e:
                print(f"Error loading data file: {e}", file=sys.stderr)
                return 1
        else:
            data = {}

        # Render template
        try:
            output = renderer.render_template(args.template, data)
        except ValueError as e:
            print(f"Error: {e}", file=sys.stderr)
            return 1

        # Validate if requested
        if args.validate:
            is_valid, errors = renderer.validate_output(output, args.template)
            if not is_valid:
                print("Validation errors:", file=sys.stderr)
                for error in errors:
                    print(f"  • {error}", file=sys.stderr)
                return 1

        # Write output
        if args.output:
            output_path = Path(args.output)
            output_path.parent.mkdir(parents=True, exist_ok=True)
            with open(output_path, 'w') as f:
                json.dump(output, f, indent=2)
            print(f"✓ Output written to {output_path}")
        else:
            print(json.dumps(output, indent=2))

        return 0

    parser.print_help()
    return 1


if __name__ == "__main__":
    sys.exit(main())
