#!/usr/bin/env python3
"""
Policy Analysis Skill Evaluator

This script evaluates the Public Policy Analysis Advisor skill against test cases
and generates performance metrics and quality assessments.
"""

import json
import sys
from pathlib import Path
from typing import Dict, Any, List, Tuple
from datetime import datetime


class PolicyAnalysisEvaluator:
    """Evaluator for policy analysis skill outputs."""

    def __init__(self, evals_path: Path, workspace_path: Path):
        """Initialize the evaluator.

        Args:
            evals_path: Path to evals.json file
            workspace_path: Path to workspace for results
        """
        self.evals_path = evals_path
        self.workspace_path = workspace_path
        self.results = []

    def load_test_cases(self) -> List[Dict[str, Any]]:
        """Load test cases from evals.json."""
        try:
            with open(self.evals_path, 'r') as f:
                data = json.load(f)
            return data.get('evals', [])
        except Exception as e:
            print(f"Error loading test cases: {e}", file=sys.stderr)
            return []

    def evaluate_output(self, output_path: Path, test_case: Dict[str, Any]) -> Dict[str, Any]:
        """Evaluate a single output against test case assertions.

        Args:
            output_path: Path to output file
            test_case: Test case with expected outputs and assertions

        Returns:
            Evaluation result dictionary
        """
        result = {
            'test_case_id': test_case.get('id'),
            'test_case_name': test_case.get('name', 'Unknown'),
            'passed': False,
            'score': 0.0,
            'assertion_results': [],
            'qualitative_assessment': {}
        }

        # Load output
        try:
            with open(output_path, 'r') as f:
                output = json.load(f)
        except Exception as e:
            result['error'] = str(e)
            return result

        # Evaluate assertions
        assertions = test_case.get('assertions', [])
        if not assertions:
            result['passed'] = True  # No assertions means automatic pass
            result['score'] = 1.0
            return result

        passed_count = 0
        for assertion in assertions:
            assertion_result = self._evaluate_assertion(output, assertion)
            result['assertion_results'].append(assertion_result)
            if assertion_result.get('passed', False):
                passed_count += 1

        # Calculate score
        result['score'] = passed_count / len(assertions) if assertions else 1.0
        result['passed'] = result['score'] >= 0.7  # 70% pass threshold

        return result

    def _evaluate_assertion(self, output: Dict[str, Any], assertion: Dict[str, Any]) -> Dict[str, Any]:
        """Evaluate a single assertion.

        Args:
            output: Output to evaluate
            assertion: Assertion to check

        Returns:
            Assertion result with 'passed' boolean
        """
        result = {
            'assertion': assertion.get('description', 'Unknown'),
            'passed': False,
            'evidence': None
        }

        assertion_type = assertion.get('type')

        if assertion_type == 'contains':
            # Check if output contains specified text
            text = assertion.get('text', '')
            output_str = json.dumps(output).lower()
            result['passed'] = text.lower() in output_str
            result['evidence'] = f"Text '{text}' {'found' if result['passed'] else 'not found'} in output"

        elif assertion_type == 'field_exists':
            # Check if field exists in output
            field_path = assertion.get('field', '').split('.')
            value = output
            for field in field_path:
                if isinstance(value, dict) and field in value:
                    value = value[field]
                else:
                    value = None
                    break
            result['passed'] = value is not None
            result['evidence'] = f"Field '{assertion.get('field')}' {'exists' if result['passed'] else 'does not exist'}"

        elif assertion_type == 'field_equals':
            # Check if field equals expected value
            field_path = assertion.get('field', '').split('.')
            expected = assertion.get('expected')
            value = output
            for field in field_path:
                if isinstance(value, dict) and field in value:
                    value = value[field]
                else:
                    value = None
                    break
            result['passed'] = value == expected
            result['evidence'] = f"Field value {value} {'equals' if result['passed'] else 'does not equal'} expected {expected}"

        elif assertion_type == 'min_length':
            # Check minimum length of array or string
            field_path = assertion.get('field', '').split('.')
            min_length = assertion.get('min_length', 0)
            value = output
            for field in field_path:
                if isinstance(value, dict) and field in value:
                    value = value[field]
                else:
                    value = None
                    break
            if value is not None:
                length = len(value) if isinstance(value, (list, str)) else 0
                result['passed'] = length >= min_length
                result['evidence'] = f"Length {length} {'meets' if result['passed'] else 'below'} minimum {min_length}"
            else:
                result['passed'] = False
                result['evidence'] = f"Field not found"

        elif assertion_type == 'disclaimer_included':
            # Check if mandatory disclaimer is included
            output_str = json.dumps(output).lower()
            disclaimer_keywords = ['educational', 'analytical', 'professional', 'qualified', 'verify']
            result['passed'] = all(keyword in output_str for keyword in disclaimer_keywords)
            result['evidence'] = f"Disclaimer keywords {'all found' if result['passed'] else 'not all found'}"

        else:
            result['error'] = f"Unknown assertion type: {assertion_type}"

        return result

    def run_evaluation(self) -> Dict[str, Any]:
        """Run full evaluation suite.

        Returns:
            Summary of evaluation results
        """
        test_cases = self.load_test_cases()
        if not test_cases:
            return {'error': 'No test cases found'}

        summary = {
            'total_tests': len(test_cases),
            'passed': 0,
            'failed': 0,
            'average_score': 0.0,
            'results': []
        }

        total_score = 0.0

        for test_case in test_cases:
            test_id = test_case.get('id')
            test_name = test_case.get('name', f'Test {test_id}')

            # Find output file
            output_dir = self.workspace_path / f'eval-{test_id}' / 'with_skill' / 'outputs'
            output_file = output_dir / 'result.json'

            if not output_file.exists():
                # Try without_skill directory
                output_dir = self.workspace_path / f'eval-{test_id}' / 'without_skill' / 'outputs'
                output_file = output_dir / 'result.json'

            if output_file.exists():
                result = self.evaluate_output(output_file, test_case)
                summary['results'].append(result)

                if result['passed']:
                    summary['passed'] += 1
                else:
                    summary['failed'] += 1

                total_score += result['score']
            else:
                summary['results'].append({
                    'test_case_id': test_id,
                    'test_case_name': test_name,
                    'error': f'Output file not found at {output_file}'
                })
                summary['failed'] += 1

        summary['average_score'] = total_score / len(test_cases) if test_cases else 0.0
        summary['pass_rate'] = summary['passed'] / len(test_cases) if test_cases else 0.0

        return summary

    def save_results(self, summary: Dict[str, Any]):
        """Save evaluation results to file.

        Args:
            summary: Summary of evaluation results
        """
        results_path = self.workspace_path / 'evaluation-summary.json'
        with open(results_path, 'w') as f:
            json.dump(summary, f, indent=2)

        print(f"\n✓ Results saved to {results_path}")

    def print_summary(self, summary: Dict[str, Any]):
        """Print evaluation summary.

        Args:
            summary: Summary of evaluation results
        """
        print("\n" + "="*60)
        print("POLICY ANALYSIS SKILL EVALUATION SUMMARY")
        print("="*60)

        if 'error' in summary:
            print(f"\n✗ Error: {summary['error']}")
            return

        print(f"\nTotal Tests: {summary['total_tests']}")
        print(f"Passed: {summary['passed']}")
        print(f"Failed: {summary['failed']}")
        print(f"Pass Rate: {summary['pass_rate']:.1%}")
        print(f"Average Score: {summary['average_score']:.2f}/1.00")

        print("\nDetailed Results:")
        print("-" * 60)

        for result in summary['results']:
            test_name = result.get('test_case_name', 'Unknown')
            if 'error' in result:
                print(f"\n✗ {test_name}: {result['error']}")
            else:
                status = "✓ PASS" if result['passed'] else "✗ FAIL"
                print(f"\n{status} {test_name}: {result['score']:.2f}")

                if result.get('assertion_results'):
                    print("  Assertions:")
                    for assertion in result['assertion_results']:
                        assert_status = "✓" if assertion.get('passed') else "✗"
                        print(f"    {assert_status} {assertion.get('assertion', 'Unknown')}")

        print("\n" + "="*60)


def main():
    """Main evaluation function."""
    # Get paths
    project_root = Path(__file__).parent.parent
    evals_path = project_root / 'evals' / 'evals.json'
    workspace_path = Path.cwd()  # Assumes running from workspace

    if not evals_path.exists():
        print(f"✗ Test cases file not found at {evals_path}", file=sys.stderr)
        return 1

    # Run evaluation
    evaluator = PolicyAnalysisEvaluator(evals_path, workspace_path)
    summary = evaluator.run_evaluation()

    # Print and save results
    evaluator.print_summary(summary)
    evaluator.save_results(summary)

    return 0 if summary.get('pass_rate', 0) >= 0.7 else 1


if __name__ == "__main__":
    sys.exit(main())
