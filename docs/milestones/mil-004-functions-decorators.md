# MIL-004 First-class functions and decorators

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-004 |
| CrossReference | [BC-001], [ADR-0001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-06 | Deprecated | Jens Tirsvad Nielsen | S01 | Initial version | [73a5a95] |
| 2026-11-06 | Accepted | Jens Tirsvad Nielsen | S01 | Paths follow the layered layout of ADR-0001 | pending |

---

## Purpose

Decide whether lectures 5 and 6 (functions as first-class objects, nested and returned functions, decorators) are implemented, tested and illustrated.

## Deliverable

`src/flask_day_54/domain/first_class_functions.py` (`add`, `subtract`, `calculate`, nested and returned functions) and `src/flask_day_54/domain/decorators.py` (the @ syntax) with tests, and screenshots for lectures 5 and 6.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | `calculate(add, 2, 3)` returns 5 and `calculate(subtract, 5, 3)` returns 2 (tested) | Met | Not met |
| 2 | A nested function is returned and called independently of its parent (tested) | Met | Not met |
| 3 | A decorator applied with the @ syntax wraps the home greeting without changing the wrapped function's name (tested) | Met | Not met |
| 4 | Screenshots `lecture-05.png` and `lecture-06.png` exist in `docs/images/` and are shown in the README | Met | Not met |

## Dependencies

| Depends on | Reason |
| --- | --- |
| MIL-003 | Builds on the finished application and test setup |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objectives 1 and 3 | BC-001 |
| CN-002, CN-003 | SA-001 |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-11-09 - within the Business Case constraints.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Implement first_class_functions | Create `add`, `subtract` and `calculate` that takes a function as argument, plus an outer function with a nested function and one that returns it, exactly as lecture 5 describes. | No | |
| 2 | Implement decorators | Create a decorator with the @ syntax that adds behaviour before and after a function, using functools.wraps, as lecture 6 recaps. | No | |
| 3 | Test both modules | Add pytest tests for the lecture examples, including that nested functions are not reachable from outside the parent. | No | |
| 4 | Screenshot lecture 5: functions as arguments | Capture the real output of running the module (calculate, nested and returned functions) in a rendered terminal transcript. | No | |
| 5 | Screenshot lecture 6: decorators | Capture the real output of the decorator demo. | No | |
| 6 | README section for lectures 5 and 6 | Add the two screenshots and a short explanation with the function names. | No | |

---

[BC-001]: ../business-case.md
[ADR-0001]: ../adr/adr-0001-layered-package-layout.md
[73a5a95]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/054-flask/commit/73a5a95d28db041e4f27342cc552e18f7d386410
