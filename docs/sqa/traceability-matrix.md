# Traceability Matrix

## Metadata
| Key | Value |
| --- | --- |
| ID | TM-001 |
| CrossReference | [BC-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-06 | Proposed | Jens Tirsvad Nielsen | S01 | Initial version | [73a5a95] |

---

## Purpose

Tracks backward/forward links between artifact instances so that the Business Case's
cross-artifact traceability success criterion is measurable. A row is added or
updated whenever an artifact instance is created or reviewed.

## Traceability Table

| Artifact Instance | Type | Language | Domain | Upstream (Backward Link) | Downstream (Forward Link) | Last Reviewed (RC-ID) |
| --- | --- | --- | --- | --- | --- | --- |
| [BC-001] | BC | en | it | - | [SA-001], [PP-001] | [RC-001] |
| [SA-001] | SA | en | it | [BC-001] | [BC-001] | [RC-002] |
| [PP-001] | PP | en | it | [BC-001], [SA-001] | [MIL-001] to [MIL-005] | [RC-003] |
| [DICT-001] | DICT | en | it | [BC-001], [SA-001] | - | [RC-004] |
| [MIL-001] | MIL | en | it | [BC-001], [PP-001] | - | [RC-005] |
| [MIL-002] | MIL | en | it | [BC-001], [PP-001] | - | [RC-006] |
| [MIL-003] | MIL | en | it | [BC-001], [PP-001] | - | [RC-007] |
| [MIL-004] | MIL | en | it | [BC-001], [PP-001] | - | [RC-008] |
| [MIL-005] | MIL | en | it | [BC-001], [PP-001] | - | [RC-009] |

## Concern Coverage

| Concern (CN-ID) | Views that answer it | Decisions (ADR) | Quality check (TP) | Status |
| --- | --- | --- | --- | --- |
| CN-001 | [PP-001], [MIL-001] | - | - | Covered |
| CN-002 | [MIL-002] to [MIL-004] | - | - | Covered |
| CN-003 | [MIL-004] | - | - | Covered |
| CN-004 | [MIL-001] | - | - | Covered |
| CN-005 | [MIL-001], [MIL-005] | - | - | Covered |
| CN-006 | [MIL-001] | - | - | Covered |
| CN-007 | [MIL-005] | - | - | Covered |

## Open Inconsistencies

| # | Views | Inconsistency | Found in (RC-ID) | Status | Resolved in |
| --- | --- | --- | --- | --- | --- |
| - | - | None found | - | Closed | - |

---

[BC-001]: ../business-case.md
[SA-001]: ../stakeholder-analysis.md
[PP-001]: ../project-plan.md
[DICT-001]: ../dictionary.md
[MIL-001]: ../milestones/mil-001-foundation.md
[MIL-002]: ../milestones/mil-002-hello-flask.md
[MIL-003]: ../milestones/mil-003-cli-and-main.md
[MIL-004]: ../milestones/mil-004-functions-decorators.md
[MIL-005]: ../milestones/mil-005-docs-wiki.md
[RC-001]: ./reviews/rc-001-business-case.md
[RC-002]: ./reviews/rc-002-stakeholder-analysis.md
[RC-003]: ./reviews/rc-003-project-plan.md
[RC-004]: ./reviews/rc-004-dictionary.md
[RC-005]: ./reviews/rc-005-mil-001-foundation.md
[RC-006]: ./reviews/rc-006-mil-002-hello-flask.md
[RC-007]: ./reviews/rc-007-mil-003-cli-and-main.md
[RC-008]: ./reviews/rc-008-mil-004-functions-decorators.md
[RC-009]: ./reviews/rc-009-mil-005-docs-wiki.md
[73a5a95]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/054-flask/commit/73a5a95d28db041e4f27342cc552e18f7d386410
