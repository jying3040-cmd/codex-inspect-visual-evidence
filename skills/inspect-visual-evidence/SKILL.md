---
name: inspect-visual-evidence
description: Inspect web pages, screenshots, images, videos, and screen recordings with traceable evidence. Use when a request depends on appearance, layout, spatial relationships, visual state, or temporal change; do not use for facts already established by reliable structured data alone.
---

# Inspect Visual Evidence

Build the smallest evidence set that can answer the user's question. Prefer structured state before pixels, and keep observations separate from inference.

## Choose the evidence

Use the first reliable source that answers the question:

1. Page text, DOM, accessibility tree, URLs, metadata, and application state.
2. Structured Markdown, transcripts, media metadata, or other compact extraction.
3. A targeted element screenshot, image crop, or small set of timestamped frames.
4. A full-screen capture only when system UI, a native dialog, or cross-application context matters.

Do not take screenshots merely to confirm facts already exposed by a stronger structured source. Do not inspect the whole desktop when a page, element, crop, or bounded interval is sufficient.

## Inspect pages and images

- For browser pages, inspect semantic state before visual state. Account for dynamic, lazy-loaded, and virtualized content before concluding that something is absent.
- Use screenshots for appearance, layout, imagery, canvas content, hover state, or other pixel-dependent facts.
- Inspect the complete image once for context, then crop or enlarge only the region needed for small text or ambiguous detail.
- Preserve spatial relationships when they affect the answer.
- Treat OCR as fallible. Re-check important text against a clearer crop or structured source when available.

## Inspect video or screen recordings

When motion, speech, or timing matters, read [references/video-inspection.md](references/video-inspection.md).

## Respect evidence boundaries

Distinguish:

- **Observed state:** directly visible or exposed by the current tool.
- **Inference:** a conclusion supported by observations but not directly visible.
- **Unknown:** information the available evidence cannot establish.

Do not claim to have observed a keyboard or mouse event unless a reliable event log exposes it. A visible result can confirm the resulting state, but not necessarily the input that caused it.

Keep material claims attached to their source URL, region, timestamp, or application state. State uncertainty caused by low resolution, cropping, occlusion, compression, missing audio, lazy loading, or sparse sampling.

## Deliver the result

Match the output to the request. For a formal inspection report, use this compact structure:

1. **Finding** — the answer or defect, stated plainly.
2. **Evidence** — source, URL or timestamp, and the directly observed fact.
3. **Inference** — only when needed, labeled explicitly.
4. **Limit** — uncertainty or missing coverage that could change the conclusion.

Stop when the evidence answers the question. Add more crops, frames, or tools only when they could materially change the conclusion.
