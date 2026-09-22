#!/usr/bin/env python3
"""Small dependency-free checks for the public Application Agent Kit."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS = {
    "application-agent-setup",
    "apply-person",
    "check-application-status",
}
FORBIDDEN_TEXT = (
    "[" + "TODO:",
    "drive.google.com/",
    "docs.google.com/",
    "Alex Hayrapetyan",
    "Alexan Hayrapetyan",
)


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def validate_manifest() -> None:
    path = ROOT / ".codex-plugin" / "plugin.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    if data.get("name") != "application-agent-kit":
        fail("plugin name must be application-agent-kit")
    if not re.fullmatch(r"\d+\.\d+\.\d+", str(data.get("version", ""))):
        fail("plugin version must use strict semver")
    if data.get("skills") != "./skills/":
        fail("plugin must expose ./skills/")


def validate_skills() -> None:
    actual = {p.name for p in (ROOT / "skills").iterdir() if p.is_dir()}
    if actual != SKILLS:
        fail(f"expected skills {sorted(SKILLS)}, found {sorted(actual)}")
    for name in sorted(SKILLS):
        path = ROOT / "skills" / name / "SKILL.md"
        text = path.read_text(encoding="utf-8")
        if not text.startswith("---\n"):
            fail(f"{path} is missing YAML frontmatter")
        match = re.search(r"^name:\s*([^\n]+)$", text, re.MULTILINE)
        if not match or match.group(1).strip() != name:
            fail(f"{path} name does not match its folder")
        if not re.search(r"^description:\s*\S", text, re.MULTILINE):
            fail(f"{path} needs a description")


def validate_public_content() -> None:
    text_suffixes = {".md", ".yaml", ".yml", ".json", ".py", ".txt"}
    for path in ROOT.rglob("*"):
        if not path.is_file() or ".git" in path.parts:
            continue
        if path.suffix.lower() not in text_suffixes and path.name != "LICENSE":
            continue
        text = path.read_text(encoding="utf-8")
        for forbidden in FORBIDDEN_TEXT:
            if forbidden in text:
                fail(f"forbidden private or scaffold text found in {path}")


def main() -> None:
    validate_manifest()
    validate_skills()
    validate_public_content()
    print("Application Agent Kit validation passed.")


if __name__ == "__main__":
    main()
