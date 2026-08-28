# codex-inspect-visual-evidence

A Codex-only skill for inspecting web pages, images, videos, and screen recordings with evidence-first visual analysis.

## What it does

This skill helps Codex:

- Prefer DOM, accessibility, text, metadata, and application state before screenshots.
- Use targeted screenshots and crops when appearance or spatial detail matters.
- Analyze videos with metadata, transcripts, scene-aware sampling, and local frame re-checks.
- Keep timestamps, URLs, and uncertainty attached to important conclusions.
- Avoid treating pixels alone as proof of unseen input events.

## Repository contents

- SKILL.md — the Codex skill definition.
- CHANGELOG.md — release history.
- LICENSE — repository license.

## Installation

Clone or download this repository, then place SKILL.md in a Codex skill directory under a folder named inspect-visual-evidence.

On Windows, the typical user-level location is:

    %USERPROFILE%\.codex\skills\inspect-visual-evidence\SKILL.md

On macOS/Linux:

    ~/.codex/skills/inspect-visual-evidence/SKILL.md

The exact discovery location can vary by Codex surface and version. After installation, start a new Codex task and verify that the skill is available.

## Scope

This repository contains a Codex skill only. It does not provide an MCP server, browser extension, API, desktop application, or general-purpose computer-vision library.

## License

See LICENSE.
