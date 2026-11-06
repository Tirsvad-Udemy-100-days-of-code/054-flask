# MIL-003 Command line and __main__

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-003 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-06 | Accepted | Jens Tirsvad Nielsen | S01 | Initial version | [73a5a95] |

---

## Purpose

Decide whether lectures 3 and 4 (the command line and the `__name__` / `__main__` idiom) are implemented, tested and illustrated.

## Deliverable

`hello.py` starts through `python src/hello.py` guarded by `if __name__ == "__main__"`, `src/cli_basics.py` and `src/name_demo.py` with tests, and screenshots for lectures 3 and 4.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | `python src/hello.py` starts the server; importing `hello` does not start it (tested) | Met | Not met |
| 2 | `name_demo` reports the main program versus an imported module (tested) | Met | Not met |
| 3 | `cli_basics` lists the lecture's commands with their Windows and macOS/Linux forms (tested) | Met | Not met |
| 4 | Screenshots `lecture-03.png` and `lecture-04.png` exist in `docs/images/` and are shown in the README | Met | Not met |

## Dependencies

| Depends on | Reason |
| --- | --- |
| MIL-002 | Extends hello.py |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objectives 1 to 3 | BC-001 |
| CN-002, CN-003 | SA-001 |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-11-08 - within the Business Case constraints.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Guard app.run with __main__ | Add a `main()` function that calls `app.run` with the host, port and debug flag from `constants.py`, called only under `if __name__ == "__main__"`. Tests use a stub so no server is started. | No | |
| 2 | Add name_demo module | Add a function that explains whether a module name means the file is the main program or an import, mirroring lecture 4, with tests. | No | |
| 3 | Add cli_basics module | Add the lecture's commands (pwd, ls, cd, mkdir, touch, rm) with Windows and macOS/Linux equivalents and a warning for destructive ones, with tests. | No | |
| 4 | Screenshot lecture 3: command line | Run the lecture's commands in a temporary folder, render the real transcript and capture it headlessly. | No | |
| 5 | Screenshot lecture 4: __main__ and app.run | Capture the real output of `python src/name_demo.py` and of the server start from `python src/hello.py`. | No | |
| 6 | README section for lectures 3 and 4 | Add the two screenshots and the two ways to start the server (`flask run` versus `python src/hello.py`). | No | |

---

[BC-001]: ../business-case.md
[73a5a95]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/054-flask/commit/73a5a95d28db041e4f27342cc552e18f7d386410
