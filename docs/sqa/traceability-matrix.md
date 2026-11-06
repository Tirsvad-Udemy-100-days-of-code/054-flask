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
| [PP-001] | PP | en | it | [BC-001], [SA-001] | [MIL-001] to [MIL-005] | [RC-021] |
| [ADR-0001] | ADR | - | - | [BC-001], [PP-001] | [MIL-001] to [MIL-004] | [RC-010] |
| [DICT-001] | DICT | en | it | [BC-001], [SA-001] | - | [RC-004] |
| [MIL-001] | MIL | en | it | [BC-001], [PP-001], [ADR-0001] | - | [RC-011], [RC-015] |
| [MIL-002] | MIL | en | it | [BC-001], [PP-001], [ADR-0001] | - | [RC-012], [RC-016] |
| [MIL-003] | MIL | en | it | [BC-001], [PP-001], [ADR-0001] | - | [RC-013], [RC-017] |
| [MIL-004] | MIL | en | it | [BC-001], [PP-001], [ADR-0001] | - | [RC-014], [RC-018] |
| [MIL-005] | MIL | en | it | [BC-001], [PP-001] | - | [RC-009], [RC-019], [RC-020], [RC-022] |

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
[ADR-0001]: ../adr/adr-0001-layered-package-layout.md
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
[RC-010]: ./reviews/rc-010-adr-0001.md
[RC-011]: ./reviews/rc-011-mil-001-foundation-delta.md
[RC-012]: ./reviews/rc-012-mil-002-hello-flask-delta.md
[RC-013]: ./reviews/rc-013-mil-003-cli-and-main-delta.md
[RC-014]: ./reviews/rc-014-mil-004-functions-decorators-delta.md
[RC-015]: ./reviews/rc-015-code-mil-001-foundation.md
[RC-016]: ./reviews/rc-016-code-mil-002-hello-flask.md
[RC-017]: ./reviews/rc-017-code-mil-003-cli-and-main.md
[RC-018]: ./reviews/rc-018-code-mil-004-functions-decorators.md
[RC-019]: ./reviews/rc-019-wiki-mil-005.md
[RC-020]: ./reviews/rc-020-code-mil-005-docs-wiki.md
[RC-021]: ./reviews/rc-021-project-plan-delta.md
[RC-022]: ./reviews/rc-022-wiki-published-mil-005.md
