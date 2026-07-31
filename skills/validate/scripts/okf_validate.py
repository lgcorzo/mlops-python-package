#!/usr/bin/env python3
"""OKF v0.2 Conformance Checker for OpenWiki Documentation.

Validates that all Markdown files under the specified wiki directory
comply with the Open Knowledge Format (OKF) v0.2 schema and
ISO/IEC/IEEE 42010/15289 traceability requirements.

Usage:
    python3 okf_validate.py <wiki_path> [--strict]

Exit codes:
    0 — All validations passed.
    1 — One or more validations failed.
"""

import argparse
import glob
import os
import re
import sys
from typing import Any

# ---------------------------------------------------------------------------
# YAML parsing — try PyYAML first, fall back to a minimal inline parser
# ---------------------------------------------------------------------------
try:
    import yaml  # type: ignore[import-untyped]

    def _parse_yaml(text: str) -> dict[str, Any]:
        result = yaml.safe_load(text)
        return result if isinstance(result, dict) else {}

except ImportError:
    def _parse_yaml(text: str) -> dict[str, Any]:
        """Minimal YAML-like parser for key: value frontmatter."""
        data: dict[str, Any] = {}
        for line in text.splitlines():
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            if ":" in line:
                key, _, value = line.partition(":")
                key = key.strip()
                value = value.strip().strip('"').strip("'")
                if value.startswith("[") and value.endswith("]"):
                    value = [v.strip().strip('"').strip("'")
                             for v in value[1:-1].split(",")]
                data[key] = value
        return data


# ---------------------------------------------------------------------------
# Validation Rules
# ---------------------------------------------------------------------------

REQUIRED_FIELDS = {"type", "title", "description", "tags", "timestamp"}
STRICT_FIELDS = {"iso_doc_type", "iso_viewpoint"}
PROVENANCE_FIELDS = {"generated", "verified", "last_verified_commit"}

ABSOLUTE_PATH_PATTERN = re.compile(
    r"(?:/home/|/mnt/|/tmp/|/usr/|/var/|/opt/|C:\\|D:\\|E:\\)", re.IGNORECASE
)

VALID_ISO_DOC_TYPES = {
    "Description", "Specification", "Plan", "Policy",
    "Procedure", "Report", "Request",
}

VALID_ISO_VIEWPOINTS = {
    "ArchitectureDescription", "ContextView", "ComponentView",
    "SequenceView", "DeploymentView", "SecurityView", "QualityView",
    "ArchitectureDecision",
}


def extract_frontmatter(content: str) -> tuple[dict[str, Any], str]:
    """Split YAML frontmatter from Markdown body."""
    if not content.startswith("---"):
        return {}, content
    parts = content.split("---", 2)
    if len(parts) < 3:
        return {}, content
    fm = _parse_yaml(parts[1])
    body = parts[2]
    return fm, body


def check_frontmatter_fields(
    fm: dict[str, Any], filepath: str, strict: bool
) -> list[str]:
    """Validate required and optional frontmatter fields."""
    errors: list[str] = []
    for field in REQUIRED_FIELDS:
        if field not in fm:
            errors.append(f"{filepath}: Missing required field '{field}'")

    if strict:
        for field in STRICT_FIELDS:
            if field not in fm:
                errors.append(
                    f"{filepath}: [STRICT] Missing ISO field '{field}'"
                )
        for field in PROVENANCE_FIELDS:
            if field not in fm:
                errors.append(
                    f"{filepath}: [STRICT] Missing provenance field '{field}'"
                )

        # Validate iso_doc_type value
        iso_doc_type = fm.get("iso_doc_type", "")
        if iso_doc_type and iso_doc_type not in VALID_ISO_DOC_TYPES:
            errors.append(
                f"{filepath}: Invalid iso_doc_type '{iso_doc_type}'. "
                f"Must be one of: {', '.join(sorted(VALID_ISO_DOC_TYPES))}"
            )

        # Validate iso_viewpoint value
        iso_viewpoint = fm.get("iso_viewpoint", "")
        if iso_viewpoint and iso_viewpoint not in VALID_ISO_VIEWPOINTS:
            errors.append(
                f"{filepath}: Invalid iso_viewpoint '{iso_viewpoint}'. "
                f"Must be one of: {', '.join(sorted(VALID_ISO_VIEWPOINTS))}"
            )

    return errors


def check_absolute_paths(body: str, filepath: str) -> list[str]:
    """Detect absolute file paths in the document body."""
    errors: list[str] = []
    for i, line in enumerate(body.splitlines(), start=1):
        if ABSOLUTE_PATH_PATTERN.search(line):
            errors.append(
                f"{filepath}:L{i}: Absolute path detected — "
                f"use relative paths only"
            )
    return errors


def check_mermaid_syntax(body: str, filepath: str) -> list[str]:
    """Basic structural validation of Mermaid code blocks."""
    errors: list[str] = []
    in_mermaid = False
    mermaid_start_line = 0
    open_braces = 0
    open_brackets = 0
    open_parens = 0

    for i, line in enumerate(body.splitlines(), start=1):
        stripped = line.strip()

        if stripped.startswith("```mermaid"):
            in_mermaid = True
            mermaid_start_line = i
            open_braces = 0
            open_brackets = 0
            open_parens = 0
            continue

        if in_mermaid and stripped == "```":
            if open_braces != 0:
                errors.append(
                    f"{filepath}:L{mermaid_start_line}: "
                    f"Mermaid block has unbalanced braces "
                    f"({{}}): {open_braces}"
                )
            if open_brackets != 0:
                errors.append(
                    f"{filepath}:L{mermaid_start_line}: "
                    f"Mermaid block has unbalanced brackets "
                    f"([]): {open_brackets}"
                )
            if open_parens != 0:
                errors.append(
                    f"{filepath}:L{mermaid_start_line}: "
                    f"Mermaid block has unbalanced parentheses "
                    f"(()): {open_parens}"
                )
            in_mermaid = False
            continue

        if in_mermaid:
            # Skip comment lines
            if stripped.startswith("%%"):
                continue
            # Count delimiters (simplified — ignores strings)
            open_braces += stripped.count("{") - stripped.count("}")
            open_brackets += stripped.count("[") - stripped.count("]")
            open_parens += stripped.count("(") - stripped.count(")")

    if in_mermaid:
        errors.append(
            f"{filepath}:L{mermaid_start_line}: "
            f"Unterminated Mermaid code block"
        )

    return errors


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def validate_wiki(wiki_path: str, strict: bool = False) -> int:
    """Validate all .md files under wiki_path. Returns error count."""
    md_files = sorted(glob.glob(
        os.path.join(wiki_path, "**", "*.md"), recursive=True
    ))

    if not md_files:
        print(f"WARNING: No .md files found under {wiki_path}")
        return 0

    total_errors: list[str] = []
    files_checked = 0
    files_passed = 0

    for filepath in md_files:
        rel_path = os.path.relpath(filepath, start=os.getcwd())
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()
        except OSError as e:
            total_errors.append(f"{rel_path}: Cannot read file — {e}")
            continue

        if not content.strip():
            total_errors.append(f"{rel_path}: File is empty")
            continue

        files_checked += 1
        file_errors: list[str] = []

        fm, body = extract_frontmatter(content)

        if not fm:
            file_errors.append(
                f"{rel_path}: Missing or invalid YAML frontmatter"
            )
        else:
            file_errors.extend(
                check_frontmatter_fields(fm, rel_path, strict)
            )

        file_errors.extend(check_absolute_paths(body, rel_path))

        if strict:
            file_errors.extend(check_mermaid_syntax(body, rel_path))

        if not file_errors:
            files_passed += 1
        else:
            total_errors.extend(file_errors)

    # Report
    print(f"\n{'=' * 60}")
    print("OKF Conformance Report")
    print(f"{'=' * 60}")
    print(f"Wiki path:     {wiki_path}")
    print(f"Strict mode:   {'ON' if strict else 'OFF'}")
    print(f"Files checked: {files_checked}")
    print(f"Files passed:  {files_passed}")
    print(f"Files failed:  {files_checked - files_passed}")
    print(f"Total errors:  {len(total_errors)}")
    print(f"{'=' * 60}")

    if total_errors:
        print("\nERRORS:")
        for err in total_errors:
            print(f"  ✗ {err}")
        print(f"\nRESULT: FAIL ({len(total_errors)} errors)")
        return len(total_errors)
    else:
        print("\nRESULT: PASS ✓")
        return 0


def main() -> None:
    parser = argparse.ArgumentParser(
        description="OKF v0.2 Conformance Checker for OpenWiki"
    )
    parser.add_argument(
        "wiki_path",
        help="Path to the OpenWiki directory to validate"
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Enable strict mode: validate ISO fields, provenance, "
             "and Mermaid syntax"
    )
    args = parser.parse_args()

    if not os.path.isdir(args.wiki_path):
        print(f"ERROR: '{args.wiki_path}' is not a directory")
        sys.exit(1)

    error_count = validate_wiki(args.wiki_path, strict=args.strict)
    sys.exit(1 if error_count > 0 else 0)


if __name__ == "__main__":
    main()
