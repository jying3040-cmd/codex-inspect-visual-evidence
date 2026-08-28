# Video and screen-recording inspection

Use layered temporal coverage instead of decoding every frame by default.

## Evidence sequence

1. Read duration, frame rate, dimensions, and audio availability.
2. Obtain a timestamped transcript when speech or system audio matters.
3. Sample representative frames to build a coarse timeline.
4. Add uniform or denser sampling for scrolling, subtitles, static recordings, or changes without scene cuts.
5. For a user-specified interval, inspect a short burst of neighboring frames.
6. Crop and enlarge small UI text while retaining its timestamp.
7. Re-check nearby frames when an event is fleeting, ambiguous, occluded, or important.

Fuse transcript, OCR, metadata, frame evidence, and timing. No single channel should be treated as complete.

## Match effort to the question

- Topic or summary: metadata, transcript, and coarse sampling.
- UI or spoken change: transcript plus scene-aware sampling and local re-check.
- Fast motion, animation, scrolling, or transient detail: dense sampling or a local frame burst.
- Exact frame-by-frame behavior: a narrowly bounded interval with explicit coverage and cost.

Report sampling gaps and missing audio when either could create a false negative.
