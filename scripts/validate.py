#!/usr/bin/env python3
"""Validate the repository's plugin and skill packaging without dependencies."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / ".codex-plugin" / "plugin.json"
SKILL_DIR = ROOT / "skills" / "inspect-visual-evidence"
SKILL = SKILL_DIR / "SKILL.md"
OPENAI_YAML = SKILL_DIR / "agents" / "openai.yaml"
VIDEO_REFERENCE = SKILL_DIR / "references" / "video-inspection.md"
EXAMPLE = ROOT / "examples" / "evidence-report.md"


def fail(message: str) -> None:
    raise ValueError(message)


def require_file(path: Path) -> str:
    if not path.is_file():
        fail(f"missing required file: {path.relative_to(ROOT)}")
    return path.read_text(encoding="utf-8")


def parse_frontmatter(text: str) -> dict[str, str]:
    match = re.match(r"^---\n(?P<body>.*?)\n---\n", text, re.DOTALL)
    if not match:
        fail("SKILL.md must start with YAML frontmatter")

    values: dict[str, str] = {}
    for line in match.group("body").splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        values[key.strip()] = value.strip().strip('"')
    return values


def main() -> int:
    manifest_text = require_file(MANIFEST)
    skill_text = require_file(SKILL)
    openai_yaml = require_file(OPENAI_YAML)
    require_file(VIDEO_REFERENCE)
    require_file(EXAMPLE)

    combined = "\n".join((manifest_text, skill_text, openai_yaml))
    if "[TODO:" in combined:
        fail("unfinished scaffold placeholder found")

    manifest = json.loads(manifest_text)
    if manifest.get("name") != "inspect-visual-evidence":
        fail("plugin name must be inspect-visual-evidence")
    if not re.fullmatch(r"\d+\.\d+\.\d+", str(manifest.get("version", ""))):
        fail("plugin version must use strict semantic versioning")
    if manifest.get("skills") != "./skills/":
        fail("plugin skills path must be ./skills/")

    interface = manifest.get("interface")
    if not isinstance(interface, dict):
        fail("plugin interface metadata is required")
    for key in ("displayName", "shortDescription", "longDescription", "developerName", "category"):
        if not interface.get(key):
            fail(f"plugin interface.{key} is required")

    prompts = interface.get("defaultPrompt")
    if not isinstance(prompts, list) or not 1 <= len(prompts) <= 3:
        fail("plugin interface.defaultPrompt must contain 1 to 3 prompts")
    if any(len(prompt) > 128 for prompt in prompts):
        fail("plugin default prompts must be at most 128 characters")

    frontmatter = parse_frontmatter(skill_text)
    if frontmatter.get("name") != "inspect-visual-evidence":
        fail("SKILL.md name must match the plugin")
    if len(frontmatter.get("description", "")) < 40:
        fail("SKILL.md description must explain its trigger clearly")

    for needle in ("display_name:", "short_description:", "default_prompt:"):
        if needle not in openai_yaml:
            fail(f"agents/openai.yaml is missing {needle}")

    print("VALIDATION OK")
    print(f"plugin: {manifest['name']} {manifest['version']}")
    print(f"skill: {frontmatter['name']}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (ValueError, json.JSONDecodeError) as error:
        print(f"VALIDATION FAILED: {error}", file=sys.stderr)
        raise SystemExit(1)
