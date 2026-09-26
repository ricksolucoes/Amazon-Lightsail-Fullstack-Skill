#!/usr/bin/env python3
"""
Internal contract validator for amazon-lightsail-fullstack.

This script uses only the Python standard library.

It intentionally DOES NOT classify prompts and DOES NOT emulate the host's
semantic skill router. Real activation evaluation must use
tests/router-eval-cases.json in the target host/evaluation harness.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "SKILL.md"
POLICY = ROOT / "references" / "activation-policy.md"
CASES = ROOT / "tests" / "router-eval-cases.json"

REQUIRED_DESCRIPTION_FRAGMENTS = [
    "Amazon Lightsail",
    "Ubuntu Server",
    "Use esta skill somente quando",
    "explicitamente Amazon Lightsail",
    "ao menos um componente da stack aprovada",
    "Não use para Ubuntu/Nginx/UFW/systemd genéricos",
]

REQUIRED_CASE_IDS = {
    "activate-lightsail-provisioning",
    "activate-lightsail-502",
    "activate-ubuntu-next",
    "activate-ubuntu-nest",
    "activate-ubuntu-postgres",
    "activate-ubuntu-prisma-prod",
    "noactivate-lambda",
    "noactivate-react",
    "noactivate-prisma-local",
    "noactivate-postgres-notebook",
    "noactivate-github-actions",
    "noactivate-ubuntu-samba",
    "noactivate-nginx-python",
    "noactivate-systemd-django",
    "noactivate-ufw-generic",
    "noactivate-postgres-java",
}


def extract_front_matter(skill_text: str) -> str:
    match = re.match(r"^---\r?\n(.*?)\r?\n---\r?\n", skill_text, re.DOTALL)
    if not match:
        raise ValueError("SKILL.md front matter not found.")
    return match.group(1)


def parse_simple_yaml_front_matter(front_matter: str) -> dict[str, Any]:
    """
    Parse only the YAML subset used by this skill, using the standard library.

    Supported:
    - top-level scalar key: value
    - folded/literal block scalars using >-, >, |-, or |
    - one-level nested mappings (used by metadata)

    This is intentionally NOT a general YAML parser.
    """
    lines = front_matter.splitlines()
    result: dict[str, Any] = {}
    i = 0

    while i < len(lines):
        raw = lines[i]

        if not raw.strip() or raw.lstrip().startswith("#"):
            i += 1
            continue

        # Top-level key only.
        if raw.startswith((" ", "\t")):
            raise ValueError(f"Unexpected indentation at front-matter line {i + 1}: {raw!r}")

        match = re.match(r"^([A-Za-z0-9_-]+):(?:\s*(.*))?$", raw)
        if not match:
            raise ValueError(f"Unsupported front-matter syntax at line {i + 1}: {raw!r}")

        key = match.group(1)
        value = (match.group(2) or "").strip()

        # Folded/literal scalar.
        if value in {">-", ">", "|-", "|"}:
            block_lines: list[str] = []
            i += 1

            while i < len(lines):
                candidate = lines[i]
                if not candidate.startswith((" ", "\t")):
                    break

                if candidate.startswith("  "):
                    block_lines.append(candidate[2:])
                elif candidate.startswith("\t"):
                    block_lines.append(candidate[1:])
                else:
                    block_lines.append(candidate.lstrip())

                i += 1

            if value.startswith(">"):
                # YAML folded style: single newlines become spaces.
                text = " ".join(part.strip() for part in block_lines).strip()
            else:
                text = "\n".join(block_lines)

            if value.endswith("-"):
                text = text.rstrip("\n")

            result[key] = text
            continue

        # Nested mapping, e.g. metadata:
        if value == "":
            nested: dict[str, str] = {}
            i += 1

            while i < len(lines):
                candidate = lines[i]
                if not candidate.startswith((" ", "\t")):
                    break

                stripped = candidate.strip()
                if not stripped or stripped.startswith("#"):
                    i += 1
                    continue

                nested_match = re.match(r"^([A-Za-z0-9_-]+):\s*(.*)$", stripped)
                if not nested_match:
                    raise ValueError(
                        f"Unsupported nested front-matter syntax at line {i + 1}: {candidate!r}"
                    )

                nested_key = nested_match.group(1)
                nested_value = nested_match.group(2).strip()

                # Strip matching single or double quotes for simple scalars.
                if (
                    len(nested_value) >= 2
                    and nested_value[0] == nested_value[-1]
                    and nested_value[0] in {"'", '"'}
                ):
                    nested_value = nested_value[1:-1]

                nested[nested_key] = nested_value
                i += 1

            result[key] = nested
            continue

        # Simple scalar.
        if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
            value = value[1:-1]

        result[key] = value
        i += 1

    return result


def main() -> int:
    errors: list[str] = []

    try:
        skill_text = SKILL.read_text(encoding="utf-8")
        policy_text = POLICY.read_text(encoding="utf-8")
        front_matter = parse_simple_yaml_front_matter(extract_front_matter(skill_text))
    except (OSError, ValueError) as exc:
        print(f"FAIL: unable to parse skill contract: {exc}", file=sys.stderr)
        return 1

    description = str(front_matter.get("description", "")).strip()
    metadata = front_matter.get("metadata")

    if front_matter.get("name") != "amazon-lightsail-fullstack":
        errors.append("front matter name must be amazon-lightsail-fullstack")

    if not isinstance(metadata, dict) or metadata.get("version") != "6.0.0":
        errors.append("front matter metadata.version must be 6.0.0")

    if not description:
        errors.append("description is required")
    elif len(description) > 1024:
        errors.append("description exceeds 1024 characters")

    for fragment in REQUIRED_DESCRIPTION_FRAGMENTS:
        if fragment not in description:
            errors.append(f"description missing required scope fragment: {fragment}")

    if "references/activation-policy.md" not in skill_text:
        errors.append("SKILL.md does not reference references/activation-policy.md")

    if "Não mantenha um classificador paralelo hardcoded" not in policy_text:
        errors.append("activation-policy.md is missing the no-parallel-router rule")

    try:
        cases = json.loads(CASES.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        errors.append(f"unable to load router eval cases: {exc}")
        cases = []

    if not isinstance(cases, list):
        errors.append("router-eval-cases.json must contain a JSON array")
        cases = []

    ids = {case.get("id") for case in cases if isinstance(case, dict)}
    missing = sorted(REQUIRED_CASE_IDS - ids)
    if missing:
        errors.append("missing router eval cases: " + ", ".join(missing))

    positives = 0
    negatives = 0

    for case in cases:
        if not isinstance(case, dict):
            errors.append("all router eval cases must be JSON objects")
            continue

        case_id = case.get("id", "<missing-id>")

        if not isinstance(case.get("expected_activation"), bool):
            errors.append(f"{case_id}: expected_activation must be boolean")
            continue

        if not isinstance(case.get("prompt"), str) or not case["prompt"].strip():
            errors.append(f"{case_id}: prompt is required")

        if not isinstance(case.get("reason"), str) or not case["reason"].strip():
            errors.append(f"{case_id}: reason is required")

        if case["expected_activation"]:
            positives += 1
        else:
            negatives += 1
            if case.get("expected_state") is not None:
                errors.append(f"{case_id}: negative case must have expected_state=null")

    if positives < 4:
        errors.append("insufficient positive router eval cases")

    if negatives < 8:
        errors.append("insufficient negative/boundary router eval cases")

    if errors:
        for error in errors:
            print("FAIL:", error, file=sys.stderr)
        return 1

    print("Skill contract validation: PASS")
    print(f"Description length: {len(description)}")
    print(f"Router eval cases: {len(cases)} ({positives} positive / {negatives} negative)")
    print("External Python dependencies: NONE")
    print("Host semantic routing was NOT simulated.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
