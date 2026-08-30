# Inspect Visual Evidence for Codex

[![Validate](https://github.com/jying3040-cmd/codex-inspect-visual-evidence/actions/workflows/validate.yml/badge.svg)](https://github.com/jying3040-cmd/codex-inspect-visual-evidence/actions/workflows/validate.yml)
[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

**Make Codex visual findings traceable, not merely plausible.**

It helps Codex choose the smallest reliable evidence source, preserve URLs and timestamps, and say clearly what was observed, inferred, or still unknown.

~~~mermaid
flowchart LR
    Q[Question] --> S{Structured evidence enough?}
    S -->|Yes| D[DOM, text, metadata, transcript]
    S -->|No| V[Targeted screenshot, crop, or frames]
    D --> R[Traceable finding]
    V --> R
    R --> U[Explicit uncertainty]
~~~

## Why install it?

| Without a deliberate evidence workflow | With Inspect Visual Evidence |
| --- | --- |
| Screenshots are taken before checking page state | DOM, accessibility, text, and metadata are checked first |
| A full screen or long video is inspected indiscriminately | The relevant element, crop, or time interval is isolated |
| Visible results are confused with the input that caused them | State, input events, inference, and unknowns stay separate |
| Conclusions lose their source context | Important claims retain URLs, regions, or timestamps |

This is useful for UI review, screenshot diagnosis, visual QA, screen-recording analysis, and evidence-backed bug reports. It is not a computer-vision library or a replacement for browser, OCR, transcript, or media tools.

## Before and after

These examples show the reporting difference the skill is designed to create. They are illustrative, not benchmark results.

### Web defect

| Generic finding | Evidence-first finding |
| --- | --- |
| “The checkout button is broken.” | **Finding:** “Place order” remains disabled after valid card input. **Evidence:** checkout URL, payment panel, after the postal-code field loses focus. **Inference:** client-side validation may not be re-running. **Limit:** no console or network trace was inspected. |

### Ambiguous screenshot

| Generic finding | Evidence-first finding |
| --- | --- |
| “The text is clipped.” | **Finding:** the final line of the card title is cut at the lower edge. **Evidence:** rightmost card, title region, supplied screenshot. **Inference:** fixed height or line clamping is likely. **Limit:** viewport size and DOM styles are unavailable from the image alone. |

### Long screen recording

| Generic finding | Evidence-first finding |
| --- | --- |
| “The save action failed near the end.” | **Finding:** the spinner disappears without confirmation. **Evidence:** `02:14–02:19`, settings panel after “Save” is selected. **Inference:** the request may fail or the success state may be missing. **Limit:** frames do not expose the response status. |

The improvement is not greater confidence; it is a smaller claim with a source, a boundary, and a clear next check.

## Benchmark roadmap

The repository does not yet claim measured quality gains. A useful public benchmark should include fixed web, screenshot, OCR-failure, and long-video cases, then compare:

- evidence traceability: claims with a URL, region, state, or timestamp;
- unsupported-claim rate: conclusions not justified by the inspected source;
- localization accuracy: whether the reported element or interval contains the defect;
- uncertainty quality: whether missing coverage and inference are labeled;
- inspection cost: screenshots, frames, and tool calls used per resolved question.

Contributions of reproducible cases and expected reports are especially welcome.

## Install

### Recommended: ask Codex

In a Codex task, say:

~~~text
Use $skill-installer to install the skill from
https://github.com/jying3040-cmd/codex-inspect-visual-evidence
~~~

Codex detects installed skill changes automatically. If the skill does not appear, restart Codex.

### Manual local install

Clone the repository, then copy this directory:

~~~text
skills/inspect-visual-evidence
~~~

to your personal skills directory:

~~~text
$HOME/.agents/skills/inspect-visual-evidence
~~~

Repository-scoped skills can instead live under:

~~~text
<repository>/.agents/skills/inspect-visual-evidence
~~~

These locations follow the current [official OpenAI skill documentation](https://learn.chatgpt.com/docs/build-skills).

## Use

Invoke it explicitly when you want a review:

~~~text
Use $inspect-visual-evidence to inspect this screenshot.
Separate observations from inference and cite the exact region.
~~~

~~~text
Use $inspect-visual-evidence to review this screen recording.
Build a coarse timeline first, then inspect the interval around the failure.
~~~

It can also activate automatically when a request clearly depends on appearance, layout, spatial relationships, or temporal change.

## What a result looks like

A formal report uses four compact parts:

1. **Finding** — the answer or defect.
2. **Evidence** — the URL, region, timestamp, or application state.
3. **Inference** — labeled separately when needed.
4. **Limit** — uncertainty or missing coverage.

See the [illustrative evidence report](examples/evidence-report.md).

## Repository layout

~~~text
.
├── .codex-plugin/plugin.json
├── skills/
│   └── inspect-visual-evidence/
│       ├── SKILL.md
│       ├── agents/openai.yaml
│       └── references/video-inspection.md
├── examples/evidence-report.md
├── scripts/validate.py
└── .github/workflows/validate.yml
~~~

The repository includes a plugin manifest for distribution and a standalone skill directory for local or repository-scoped use.

## Validate

~~~bash
python scripts/validate.py
~~~

The check verifies the plugin manifest, required skill metadata, UI metadata, referenced files, and unfinished placeholders. CI runs the same check on every push and pull request.

## Scope and trust

- No network service, MCP server, browser extension, or telemetry is included.
- The skill contains instructions and one supporting reference; it does not execute bundled code.
- Tool permissions and user authorization remain controlled by Codex and the active environment.
- Visual evidence can still be incomplete. The skill requires uncertainty to be reported when it matters.

## License

[MIT](LICENSE)
