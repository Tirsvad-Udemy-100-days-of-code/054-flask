# MIL-005 Documentation, wiki and release check

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-005 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-06 | Accepted | Jens Tirsvad Nielsen | S01 | Initial version | [73a5a95] |

---

## Purpose

Decide whether the repository is ready to be shared: three-language wiki, final README, generated API docs and a code review.

## Deliverable

Wiki pages in English, Danish and Bahasa Malaysia in `docs/wiki/` with a screenshot and a what-we-gained text per lecture, a final README with all screenshots, Doxygen output without warnings and a recorded code review.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | `docs/wiki/` holds the same page set in en, da and ms (`Home`, `Home-da`, `Home-ms` and the lecture pages) | Met | Not met |
| 2 | Every lecture page shows its screenshot and a section on what was gained | Met | Not met |
| 3 | `_Sidebar.md` follows `framework/process/wiki.md` | Met | Not met |
| 4 | `doxygen Doxyfile` finishes without warnings | Met | Not met |
| 5 | `python -m pytest` passes and the code review against `qc-programming-python` is `Go` | Met | Not met |
| 6 | `check-readme.sh` and `check-plan.sh` pass | Met | Not met |

## Dependencies

| Depends on | Reason |
| --- | --- |
| MIL-004 | Needs all lectures implemented and illustrated |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objectives 4 and 5 | BC-001 |
| CN-005, CN-007 | SA-001 |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-11-10 - within the Business Case constraints.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Write English wiki | Create `Home.md`, six lecture pages, `_Sidebar.md` and `_Footer.md` in `docs/wiki/`; each lecture page has the screenshot and a section explaining what was gained. | No | |
| 2 | Write Danish wiki | Translate every English page to Danish (`-da` suffix) with the same page set and the language line. | No | |
| 3 | Write Bahasa Malaysia wiki | Translate every English page to Bahasa Malaysia (`-ms` suffix) with the same page set and the language line. | No | |
| 4 | Check wiki structure and links | Verify page set parity, relative image paths and sidebar rules against `QC-WIKI-001`. | No | |
| 5 | Generate and check Doxygen | Run `doxygen Doxyfile` and fix every warning in the source comments. | No | |
| 6 | Review code against qc-programming-python | Review `src/` and `tests/` against the Python checklist and record an RC. | No | |

---

[BC-001]: ../business-case.md
[73a5a95]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/054-flask/commit/73a5a95d28db041e4f27342cc552e18f7d386410
