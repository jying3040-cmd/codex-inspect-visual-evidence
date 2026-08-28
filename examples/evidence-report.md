# Example evidence report

This is an illustrative output shape, not a benchmark result.

## Request

> Check whether the confirmation banner remains visible after the form is submitted.

## Finding

The confirmation banner is visible after submission, but its text is partially clipped at a narrow viewport.

## Evidence

| Source | Location | Observation |
| --- | --- | --- |
| DOM snapshot | Post-submit page state | A status element with the confirmation text exists. |
| Targeted screenshot | Confirmation region, narrow viewport | The rightmost part of the text is outside the visible banner bounds. |

## Inference

The submission probably succeeded because the post-submit status is present. The screenshot establishes the clipping defect, not the exact input event that caused submission.

## Limit

No keyboard or pointer event log was available, so the report does not claim which input method triggered the form.
