#!/usr/bin/env python3
"""
Skill Validator for Public Policy Analysis Advisor

This script validates the skill structure, completeness, and compliance
with production standards.
"""

import json
import sys
from pathlib import Path
from typing import Dict, Any, List, Tuple
from datetime import datetime


class SkillValidator:
    """Validator for skill structure and quality."""

    def __init__(self, skill_path: Path):
        """Initialize the validator.

        Args:
            skill_path: Path to skill directory
        """
        self.skill_path = skill_path
        self.errors = []
        self.warnings = []
        self.checks_passed = 0
        self.checks_total = 0

    def validate_all(self) -> Dict[str, Any]:
        """Run all validation checks.

        Returns:
            Validation result dictionary
        """
        print("Starting skill validation...\n")

        # Run all validation checks
        self._validate_structure()
        self._validate_skill_md()
        self._validate_references()
        self._validate_templates()
        self._validate_schemas()
        self._validate_config()
        self._validate_scripts()
        self._validate_evals()
        self._validate_documentation()
        self._check_completeness()

        # Generate report
        report = self._generate_report()

        return report

    def _validate_structure(self):
        """Validate directory structure."""
        print("Checking directory structure...")
        self.checks_total += 1

        required_dirs = ['references', 'assets', 'config', 'scripts', 'evals']
        required_subdirs = [
            'assets/templates',
            'assets/schemas',
            'config'
        ]

        missing = []
        for dir_name in required_dirs:
            dir_path = self.skill_path / dir_name
            if not dir_path.exists() or not dir_path.is_dir():
                missing.append(f"Missing directory: {dir_name}")

        for subdir in required_subdirs:
            subdir_path = self.skill_path / subdir
            if not subdir_path.exists() or not subdir_path.is_dir():
                missing.append(f"Missing subdirectory: {subdir}")

        if missing:
            self.errors.extend(missing)
        else:
            self.checks_passed += 1
            print("  ✓ Directory structure valid")

    def _validate_skill_md(self):
        """Validate SKILL.md file."""
        print("Checking SKILL.md...")
        self.checks_total += 1

        skill_md = self.skill_path / 'SKILL.md'
        if not skill_md.exists():
            self.errors.append("SKILL.md not found")
            return

        try:
            with open(skill_md, 'r', encoding='utf-8') as f:
                content = f.read()

            # Check for required frontmatter
            required_fields = ['name', 'description']
            missing_fields = []

            for field in required_fields:
                if f'{field}:' not in content[:200]:  # Check in frontmatter area
                    missing_fields.append(field)

            if missing_fields:
                self.errors.append(f"SKILL.md missing frontmatter fields: {', '.join(missing_fields)}")
            else:
                # Check content sections
                required_sections = [
                    'Mandatory Disclaimer',
                    'When to Use This Skill',
                    'Core Methodologies',
                    'Analysis Workflow',
                    'Quality Standards'
                ]

                missing_sections = []
                for section in required_sections:
                    if section not in content:
                        missing_sections.append(section)

                if missing_sections:
                    self.warnings.append(f"SKILL.md missing recommended sections: {', '.join(missing_sections)}")

                self.checks_passed += 1
                print("  ✓ SKILL.md valid")

        except Exception as e:
            self.errors.append(f"Error reading SKILL.md: {e}")

    def _validate_references(self):
        """Validate reference files."""
        print("Checking reference files...")
        self.checks_total += 1

        refs_dir = self.skill_path / 'references'
        if not refs_dir.exists():
            self.errors.append("references directory not found")
            return

        required_refs = [
            'problem-definition.md',
            'stakeholder-analysis.md',
            'alternatives-evaluation.md',
            'evidence-synthesis.md',
            'policy-cycle.md',
            'guardrails.md'
        ]

        missing = []
        for ref_file in required_refs:
            ref_path = refs_dir / ref_file
            if not ref_path.exists():
                missing.append(ref_file)

        if missing:
            self.errors.append(f"Missing reference files: {', '.join(missing)}")
        else:
            self.checks_passed += 1
            print(f"  ✓ All {len(required_refs)} required reference files present")

    def _validate_templates(self):
        """Validate template files."""
        print("Checking template files...")
        self.checks_total += 1

        templates_dir = self.skill_path / 'assets' / 'templates'
        if not templates_dir.exists():
            self.errors.append("assets/templates directory not found")
            return

        required_templates = [
            'problem-definition-template.json',
            'stakeholder-map-template.json',
            'alternatives-matrix-template.json',
            'evidence-table-template.json',
            'policy-cycle-template.json'
        ]

        missing = []
        invalid = []
        for template_file in required_templates:
            template_path = templates_dir / template_file
            if not template_path.exists():
                missing.append(template_file)
            else:
                # Validate JSON structure
                try:
                    with open(template_path, 'r') as f:
                        template = json.load(f)
                    if 'template_type' not in template or 'structure' not in template:
                        invalid.append(template_file)
                except Exception:
                    invalid.append(template_file)

        if missing:
            self.errors.append(f"Missing template files: {', '.join(missing)}")
        if invalid:
            self.errors.append(f"Invalid template files: {', '.join(invalid)}")
        elif not missing and not invalid:
            self.checks_passed += 1
            print(f"  ✓ All {len(required_templates)} required templates valid")

    def _validate_schemas(self):
        """Validate schema files."""
        print("Checking schema files...")
        self.checks_total += 1

        schemas_dir = self.skill_path / 'assets' / 'schemas'
        if not schemas_dir.exists():
            self.errors.append("assets/schemas directory not found")
            return

        required_schemas = [
            'input-schema.json',
            'output-schema.json',
            'evaluation-schema.json'
        ]

        missing = []
        for schema_file in required_schemas:
            schema_path = schemas_dir / schema_file
            if not schema_path.exists():
                missing.append(schema_file)

        if missing:
            self.warnings.append(f"Missing schema files: {', '.join(missing)}")
        else:
            self.checks_passed += 1
            print(f"  ✓ All {len(required_schemas)} required schemas present")

    def _validate_config(self):
        """Validate configuration files."""
        print("Checking configuration files...")
        self.checks_total += 1

        config_dir = self.skill_path / 'config'
        if not config_dir.exists():
            self.errors.append("config directory not found")
            return

        required_config = [
            'schema.json',
            'default.json',
            'validation.py'
        ]

        missing = []
        for config_file in required_config:
            config_path = config_dir / config_file
            if not config_path.exists():
                missing.append(config_file)

        if missing:
            self.errors.append(f"Missing config files: {', '.join(missing)}")
        else:
            self.checks_passed += 1
            print(f"  ✓ All {len(required_config)} required config files present")

    def _validate_scripts(self):
        """Validate script files."""
        print("Checking script files...")
        self.checks_total += 1

        scripts_dir = self.skill_path / 'scripts'
        if not scripts_dir.exists():
            self.errors.append("scripts directory not found")
            return

        required_scripts = [
            'evaluator.py',
            'template-renderer.py',
            'skill-validator.py'
        ]

        missing = []
        for script_file in required_scripts:
            script_path = scripts_dir / script_file
            if not script_path.exists():
                missing.append(script_file)

        if missing:
            self.warnings.append(f"Missing script files: {', '.join(missing)}")
        else:
            self.checks_passed += 1
            print(f"  ✓ All {len(required_scripts)} required scripts present")

    def _validate_evals(self):
        """Validate evaluation files."""
        print("Checking evaluation files...")
        self.checks_total += 1

        evals_dir = self.skill_path / 'evals'
        if not evals_dir.exists():
            self.warnings.append("evals directory not found")
            return

        required_evals = ['evals.json']

        missing = []
        for eval_file in required_evals:
            eval_path = evals_dir / eval_file
            if not eval_path.exists():
                missing.append(eval_file)

        if missing:
            self.warnings.append(f"Missing eval files: {', '.join(missing)}")
        else:
            # Validate evals.json structure
            evals_path = evals_dir / 'evals.json'
            try:
                with open(evals_path, 'r') as f:
                    evals_data = json.load(f)

                if 'evals' not in evals_data or not isinstance(evals_data['evals'], list):
                    self.errors.append("evals.json missing valid 'evals' array")
                else:
                    self.checks_passed += 1
                    print("  ✓ Evaluation files valid")
            except Exception as e:
                self.errors.append(f"Error validating evals.json: {e}")

    def _validate_documentation(self):
        """Validate documentation files."""
        print("Checking documentation files...")
        self.checks_total += 1

        required_docs = [
            'README.md',
            'CLAUDE.md',
            'PROJECT-detail.md',
            'DEVELOPMENT-TASK-BY-PHASES.md',
            'PROJECT-DEVELOPMENT-PHASE-TRACKING.md',
            'SECOND-BRAIN-KNOWLEDGE-PAPER.md'
        ]

        missing = []
        for doc_file in required_docs:
            doc_path = self.skill_path / doc_file
            if not doc_path.exists():
                missing.append(doc_file)

        if missing:
            self.warnings.append(f"Missing documentation files: {', '.join(missing)}")
        else:
            self.checks_passed += 1
            print("  ✓ All documentation files present")

    def _check_completeness(self):
        """Check for placeholders and incomplete content."""
        print("Checking for placeholders and incomplete content...")
        self.checks_total += 1

        placeholder_patterns = [
            'TODO',
            'FIXME',
            'PLACEHOLDER',
            'Not implemented',
            'Coming soon'
        ]

        issues = []

        # Check markdown files
        for md_file in self.skill_path.rglob('*.md'):
            try:
                with open(md_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                    for pattern in placeholder_patterns:
                        if pattern in content:
                            issues.append(f"{md_file.relative_to(self.skill_path)}: Contains '{pattern}'")
            except Exception:
                pass

        # Check JSON files for empty structures
        for json_file in self.skill_path.rglob('*.json'):
            try:
                with open(json_file, 'r') as f:
                    data = json.load(f)
                    if isinstance(data, dict) and not data:
                        issues.append(f"{json_file.relative_to(self.skill_path)}: Empty object")
            except Exception:
                pass

        if issues:
            self.warnings.extend(issues[:5])  # Limit to first 5
            if len(issues) > 5:
                self.warnings.append(f"... and {len(issues) - 5} more placeholder issues")
        else:
            self.checks_passed += 1
            print("  ✓ No placeholders found")

    def _generate_report(self) -> Dict[str, Any]:
        """Generate validation report.

        Returns:
            Validation report dictionary
        """
        pass_rate = self.checks_passed / self.checks_total if self.checks_total > 0 else 0

        report = {
            'timestamp': datetime.now().isoformat(),
            'skill_path': str(self.skill_path),
            'summary': {
                'checks_total': self.checks_total,
                'checks_passed': self.checks_passed,
                'checks_failed': self.checks_total - self.checks_passed,
                'pass_rate': pass_rate,
                'errors_count': len(self.errors),
                'warnings_count': len(self.warnings)
            },
            'status': 'passed' if len(self.errors) == 0 and pass_rate >= 0.8 else 'failed',
            'errors': self.errors,
            'warnings': self.warnings
        }

        return report


def main():
    """Main validation function."""
    # Get paths
    project_root = Path(__file__).parent.parent

    # Run validation
    validator = SkillValidator(project_root)
    report = validator.validate_all()

    # Print summary
    print("\n" + "="*60)
    print("SKILL VALIDATION REPORT")
    print("="*60)

    summary = report['summary']
    print(f"\nChecks Passed: {summary['checks_passed']}/{summary['checks_total']}")
    print(f"Pass Rate: {summary['pass_rate']:.1%}")
    print(f"Errors: {summary['errors_count']}")
    print(f"Warnings: {summary['warnings_count']}")
    print(f"Status: {report['status'].upper()}")

    if report['errors']:
        print("\nErrors:")
        for error in report['errors']:
            print(f"  ✗ {error}")

    if report['warnings']:
        print("\nWarnings:")
        for warning in report['warnings']:
            print(f"  ⚠ {warning}")

    print("\n" + "="*60)

    return 0 if report['status'] == 'passed' else 1


if __name__ == "__main__":
    sys.exit(main())
