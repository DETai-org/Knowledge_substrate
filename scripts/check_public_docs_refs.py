#!/usr/bin/env python3
"""Fail a public MkDocs build on links to private implementation sources.

Everything below docs/ecosystem is published, regardless of front matter,
navigation placement, or robots metadata. This check deliberately scans raw
Markdown, including YAML and every human language.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "knowledge_core/source_of_truth/docs/ecosystem"

# The private repository list is explicit and intentionally fail-closed for
# these known owning systems. Extend it when a new private DETai repo is used.
PRIVATE_REPOS = {
    "psychology-in-quotes",
    "team-os",
    "sites",
    "ecosystem-runtime",
    "storytelling",
}

GITHUB_URL = re.compile(
    r"https?://(?:www\.)?github\.com/DETai-org/"
    r"(?P<repo>[\w.-]+)(?P<suffix>/[^\s<>\]\"')}]*)?",
    re.IGNORECASE,
)
RAW_GITHUB_URL = re.compile(
    r"https?://raw\.githubusercontent\.com/DETai-org/(?P<repo>[\w.-]+)",
    re.IGNORECASE,
)
TRANSIENT_GITHUB = re.compile(
    r"/(?:pull|commit)/"
    r"(?:\d+|[a-fA-F0-9]{7,40})(?:/|$|[#?])",
    re.IGNORECASE,
)
CONCRETE_PR_MARKER = re.compile(
    r"(?:\bPR\s*#\s*\d+|\b(?:PiQ|Team\s+OS)\s*#\s*\d+)",
    re.IGNORECASE,
)
PIQ_INTERNAL_PATH = re.compile(
    r"(?:contracts/piq-product/|config/piq-policy(?:\.v\d+)?\.json|"
    r"db/psychology_in_quotes/|docs/ADR/)",
    re.IGNORECASE,
)


def violations(path: Path) -> list[tuple[int, str]]:
    findings: list[tuple[int, str]] = []
    relative = path.relative_to(DOCS)
    product_piq = "products/psychology-in-quotes/" in relative.as_posix()

    for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        for match in GITHUB_URL.finditer(line):
            repo = match.group("repo").lower()
            suffix = match.group("suffix") or ""
            if repo in PRIVATE_REPOS:
                findings.append((number, f"private repository URL: DETai-org/{repo}"))
            elif TRANSIENT_GITHUB.search(suffix):
                findings.append((number, "direct implementation PR/commit link"))
        for match in RAW_GITHUB_URL.finditer(line):
            if match.group("repo").lower() in PRIVATE_REPOS:
                findings.append((number, "private raw GitHub file URL"))

        if CONCRETE_PR_MARKER.search(line):
            findings.append((number, "internal PR/implementation number in public copy"))
        if product_piq and PIQ_INTERNAL_PATH.search(line):
            findings.append((number, "internal implementation path in PiQ public copy"))

    return findings


def main() -> int:
    if not DOCS.is_dir():
        print(f"Public docs directory not found: {DOCS}", file=sys.stderr)
        return 2

    errors = []
    checked = 0
    for path in sorted(DOCS.rglob("*.md")):
        checked += 1
        for number, reason in violations(path):
            errors.append(f"{path.relative_to(ROOT)}:{number}: {reason}")

    if errors:
        print("Public documentation audit FAILED:\n" + "\n".join(errors), file=sys.stderr)
        print(
            "\nKeep private provenance in internal owning systems; link only to "
            "stable, accessible public pages.",
            file=sys.stderr,
        )
        return 1

    print(f"Public documentation audit OK: {checked} Markdown files checked.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
