#!/usr/bin/env python3
"""
Dataset validation script for JSONL files with JSON Schema.

Usage:
    python validate.py datasets/dataset-name
    python validate.py datasets/dataset-name --verbose
"""

import json
import sys
import os
from pathlib import Path
import argparse
from typing import List, Dict, Any, Tuple
import jsonschema
from jsonschema import Draft7Validator, ValidationError


class Colors:
    """ANSI color codes for terminal output"""
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'


def print_success(msg: str):
    """Print success message in green"""
    print(f"{Colors.GREEN}✓ {msg}{Colors.ENDC}")


def print_error(msg: str):
    """Print error message in red"""
    print(f"{Colors.RED}✗ {msg}{Colors.ENDC}")


def print_warning(msg: str):
    """Print warning message in yellow"""
    print(f"{Colors.YELLOW}⚠ {msg}{Colors.ENDC}")


def print_info(msg: str):
    """Print info message in blue"""
    print(f"{Colors.BLUE}ℹ {msg}{Colors.ENDC}")


def validate_schema_file(schema_path: Path) -> Tuple[bool, Dict[str, Any], List[str]]:
    """
    Validate that the schema file exists and is valid JSON Schema.

    Returns:
        Tuple of (is_valid, schema_dict, error_messages)
    """
    errors = []

    if not schema_path.exists():
        errors.append(f"Schema file not found: {schema_path}")
        return False, {}, errors

    try:
        with open(schema_path, 'r', encoding='utf-8') as f:
            schema = json.load(f)
    except json.JSONDecodeError as e:
        errors.append(f"Invalid JSON in schema file: {e}")
        return False, {}, errors
    except Exception as e:
        errors.append(f"Error reading schema file: {e}")
        return False, {}, errors

    # Validate the schema itself
    try:
        Draft7Validator.check_schema(schema)
    except jsonschema.SchemaError as e:
        errors.append(f"Invalid JSON Schema: {e.message}")
        return False, {}, errors

    return True, schema, errors


def validate_data_file(data_path: Path, schema: Dict[str, Any], verbose: bool = False) -> Tuple[bool, List[str], Dict[str, int]]:
    """
    Validate that the data file exists and all entries conform to the schema.

    Returns:
        Tuple of (is_valid, error_messages, statistics)
    """
    errors = []
    stats = {
        'total_records': 0,
        'valid_records': 0,
        'invalid_records': 0,
        'empty_lines': 0
    }

    if not data_path.exists():
        errors.append(f"Data file not found: {data_path}")
        return False, errors, stats

    validator = Draft7Validator(schema)

    try:
        with open(data_path, 'r', encoding='utf-8') as f:
            for line_num, line in enumerate(f, 1):
                line = line.strip()

                if not line:
                    stats['empty_lines'] += 1
                    continue

                stats['total_records'] += 1

                try:
                    record = json.loads(line)
                except json.JSONDecodeError as e:
                    errors.append(f"Line {line_num}: Invalid JSON - {e}")
                    stats['invalid_records'] += 1
                    if verbose:
                        print_error(f"  Line {line_num}: {line[:100]}...")
                    continue

                # Validate against schema
                validation_errors = list(validator.iter_errors(record))
                if validation_errors:
                    stats['invalid_records'] += 1
                    for error in validation_errors:
                        path = ' -> '.join(str(p) for p in error.path) if error.path else 'root'
                        errors.append(f"Line {line_num}, {path}: {error.message}")
                        if verbose:
                            print_error(f"  Line {line_num}, {path}: {error.message}")
                else:
                    stats['valid_records'] += 1

    except Exception as e:
        errors.append(f"Error reading data file: {e}")
        return False, errors, stats

    if stats['total_records'] == 0:
        errors.append("Data file is empty (no valid records found)")

    return len(errors) == 0, errors, stats


def validate_readme(readme_path: Path) -> Tuple[bool, List[str]]:
    """
    Validate that README exists and has minimum required content.

    Returns:
        Tuple of (is_valid, warning_messages)
    """
    warnings = []

    if not readme_path.exists():
        warnings.append(f"README.md not found: {readme_path}")
        return False, warnings

    try:
        with open(readme_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Check for minimum content
        if len(content.strip()) < 100:
            warnings.append("README.md seems too short (less than 100 characters)")

        # Check for recommended sections
        recommended_sections = ['source', 'description', 'license']
        content_lower = content.lower()
        missing_sections = [s for s in recommended_sections if s not in content_lower]

        if missing_sections:
            warnings.append(f"README.md may be missing sections: {', '.join(missing_sections)}")

    except Exception as e:
        warnings.append(f"Error reading README.md: {e}")
        return False, warnings

    return len(warnings) == 0, warnings


def validate_dataset(dataset_path: Path, verbose: bool = False) -> bool:
    """
    Validate a complete dataset directory.

    Returns:
        True if validation passes, False otherwise
    """
    print(f"\n{Colors.BOLD}Validating dataset: {dataset_path}{Colors.ENDC}")

    if not dataset_path.exists():
        print_error(f"Dataset directory not found: {dataset_path}")
        return False

    if not dataset_path.is_dir():
        print_error(f"Path is not a directory: {dataset_path}")
        return False

    # Define expected files
    schema_path = dataset_path / 'schema.json'
    data_path = dataset_path / 'data.jsonl'
    readme_path = dataset_path / 'README.md'

    overall_valid = True

    # Validate schema
    print_info("Checking schema.json...")
    schema_valid, schema, schema_errors = validate_schema_file(schema_path)
    if schema_valid:
        print_success("Schema is valid JSON Schema")
    else:
        overall_valid = False
        for error in schema_errors:
            print_error(error)

    # Validate data if schema is valid
    if schema_valid:
        print_info("Checking data.jsonl...")
        data_valid, data_errors, stats = validate_data_file(data_path, schema, verbose)

        # Print statistics
        print_info(f"Records processed: {stats['total_records']}")
        if stats['valid_records'] > 0:
            print_success(f"Valid records: {stats['valid_records']}")
        if stats['invalid_records'] > 0:
            print_error(f"Invalid records: {stats['invalid_records']}")
        if stats['empty_lines'] > 0:
            print_warning(f"Empty lines skipped: {stats['empty_lines']}")

        if data_valid:
            print_success("All data records are valid")
        else:
            overall_valid = False
            # Print first 10 errors if not verbose
            if not verbose:
                for error in data_errors[:10]:
                    print_error(error)
                if len(data_errors) > 10:
                    print_warning(f"... and {len(data_errors) - 10} more errors. Use --verbose to see all.")

    # Validate README
    print_info("Checking README.md...")
    readme_valid, readme_warnings = validate_readme(readme_path)
    if readme_valid:
        print_success("README.md exists and appears complete")
    else:
        for warning in readme_warnings:
            print_warning(warning)
        # README issues are warnings, not failures
        if not readme_path.exists():
            overall_valid = False

    # Final result
    print()
    if overall_valid:
        print_success(f"{Colors.BOLD}Dataset validation PASSED{Colors.ENDC}")
    else:
        print_error(f"{Colors.BOLD}Dataset validation FAILED{Colors.ENDC}")

    return overall_valid


def main():
    parser = argparse.ArgumentParser(
        description='Validate JSONL datasets against their JSON schemas'
    )
    parser.add_argument(
        'dataset_path',
        type=str,
        help='Path to the dataset directory (e.g., datasets/example-dataset)'
    )
    parser.add_argument(
        '--verbose',
        '-v',
        action='store_true',
        help='Show all validation errors (not just first 10)'
    )

    args = parser.parse_args()

    dataset_path = Path(args.dataset_path)

    # Validate and exit with appropriate code
    is_valid = validate_dataset(dataset_path, args.verbose)
    sys.exit(0 if is_valid else 1)


if __name__ == '__main__':
    main()
