# MIL-001 Project foundation

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-001 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-06 | Accepted | Jens Tirsvad Nielsen | S01 | Initial version | pending |

---

## Purpose

Decide whether the project skeleton (configuration, tooling, documentation baseline and repository metadata) is ready for the lecture code.

## Deliverable

A repository with `pyproject.toml`, `.gitignore`, `src/constants.py`, a Doxyfile, a README with `.venv` instructions, the repository description and topics, and a passing (empty-but-collecting) pytest run.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | `python -m pytest` runs and exits 0 on a fresh `.venv` | Met | Not met |
| 2 | `pyproject.toml` declares Python 3.13 or newer, the optional extras `web` and `dev`, and no mandatory runtime dependency | Met | Not met |
| 3 | `.gitignore` excludes `.venv/` and `.env` | Met | Not met |
| 4 | `doxygen Doxyfile` finishes without errors | Met | Not met |
| 5 | The repository has a description and at least 5 topics on the git host | Met | Not met |
| 6 | README follows the framework template and passes `check-readme.sh` | Met | Not met |

## Dependencies

| Depends on | Reason |
| --- | --- |
| None | First gateway after the accepted baseline (BC-001, SA-001, PP-001) |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objective 3 and 5; constraints on tooling | BC-001 |
| CN-004, CN-005, CN-006 | SA-001 |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-11-06 - same day as the plan; fits the Business Case effort estimate.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Add pyproject.toml | Configure the project with requires-python >=3.13, the optional extras `web` (Flask) and `dev` (pytest), and pytest settings so tests import modules from `src/`. Keeps the pure-Python lectures free of runtime dependencies (SA-001 CN-006). | No | |
| 2 | Add Python .gitignore | Ignore virtual environments, caches, build output, Doxygen output and the personal `.env` file so no token can be committed. | No | |
| 3 | Add constants.py and package layout | Create `src/constants.py` for all constants (greeting, host, port, command names) and the empty `tests/` folder, as the constraints require constants in one place. | No | |
| 4 | Add Doxyfile | Generate a Doxyfile that reads `src/`, writes to `docs/doxygen/` (ignored by git) and extracts documentation from Doxygen comments. | No | |
| 5 | Write README from the framework template | Use the framework README template; describe creating and activating a local `.venv`, running `python -m pip install --upgrade pip`, installing extras, running the app and running pytest. | No | |
| 6 | Set repository description and topics | Use the Gitea REST API with the token from the author's environment (never stored in the repository) to set a description and topics so visitors (S03) can find and understand the repository. | No | |
| 7 | Record the AI prompt log | Add `docs/ai-prompts/session-001/` as `framework/process/ai-prompt-log.md` requires. | No | |

---

[BC-001]: ../business-case.md
