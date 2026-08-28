---
name: inspect-visual-evidence
description: Choose the smallest reliable combination of page structure, metadata, screenshots, crops, transcripts, OCR, and video frames to understand web pages, images, videos, and screen recordings.
---

# Inspect Visual Evidence

Use structured evidence first. Use visual evidence when the requested fact depends on appearance, layout, spatial relationships, canvas content, or temporal change.

Keep the evidence scope narrow, preserve uncertainty, and increase sampling only when the question requires more detail.

## Evidence priority

Prefer evidence in this order, unless a more reliable source is available:

1. Page text, DOM, accessibility tree, URLs, metadata, links, and application state.
2. Structured Markdown or other compact page extraction.
3. A targeted element screenshot, image crop, or browser viewport.
4. A full-screen capture only when system UI, a native dialog, or cross-application context matters.

Do not inspect the whole desktop when the answer is available from the page or application state.

## Browser pages

Before taking a screenshot:

- Inspect the DOM or accessibility tree when available.
- Locate controls by role, accessible name, visible text, URL, or state.
- Extract page text, tables, links, and metadata directly.
- Wait for dynamic, lazy-loaded, or virtualized content before concluding that content is absent.
- Use a targeted screenshot for layout, color, imagery, hover state, canvas content, or other visual facts.
- Verify downloads and other state-changing actions through the page, download state, or filesystem.

For image-search pages, first collect candidate titles, source pages, image URLs, and result metadata. Inspect the original candidate images only when visual content or similarity is relevant.

## Images

Analyze the complete image first to establish context. Then crop or enlarge only the region needed for small text, fine detail, or an ambiguous object.

Keep spatial relationships intact when they affect the answer. Separate what is visibly supported from interpretation, and mention limitations caused by resolution, cropping, occlusion, or compression.

## Videos and screen recordings

Use layered temporal coverage:

1. Read duration, frame rate, dimensions, and audio availability.
2. Obtain a timestamped transcript when speech or system audio matters.
3. Sample representative frames to build a coarse timeline.
4. Add uniform or denser sampling for scrolling, subtitles, static screen recordings, or changes without scene cuts.
5. For a user-specified interval, inspect a short burst of neighboring frames.
6. Crop and enlarge small UI text while retaining its timestamp.
7. Re-check nearby frames when an event is fleeting, ambiguous, occluded, or important.

Fuse transcript, OCR, metadata, frame evidence, and timing. Do not treat any one channel as complete.

Use the least expensive mode that can answer the question:

- Topic or summary: metadata, transcript, and coarse visual sampling.
- UI or spoken change: transcript plus scene-aware sampling and local re-check.
- Fast motion, animation, scrolling, or transient detail: dense sampling or a local frame burst.
- Exact frame-by-frame behavior: narrowly bounded, high-density inspection with an explicit scope and cost note.

## State and input boundaries

Distinguish:

- Page state: DOM, accessibility tree, text, URLs, and browser events.
- Visual state: pixels, layout, color, imagery, and position.
- Application state: windows, dialogs, downloads, focus, and process transitions.
- User input events: keyboard or mouse events generated outside the controlled interaction.

Do not claim to have observed a user input event unless the active tool or a reliable application event log exposes it. A visible result can confirm the resulting state, but not necessarily the exact input that caused it.

## Quality checks

Before visual processing, ask:

- Can structured page data or a transcript answer the question?
- Is a crop sufficient instead of a full-screen capture?
- Does the question require appearance, position, motion, or temporal continuity?
- Could lazy loading, OCR failure, missing audio, compression, or sampling gaps create a false negative?

After analysis, verify that:

- The evidence covers the requested scope.
- Important claims retain their URL, timestamp, or source context.
- Conclusions do not depend on an unobserved input event.
- Uncertainty and evidence limitations are stated when material.
