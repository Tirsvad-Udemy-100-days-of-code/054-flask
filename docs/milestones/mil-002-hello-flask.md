# MIL-002 Backend basics and Hello Flask

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-002 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-06 | Accepted | Jens Tirsvad Nielsen | S01 | Initial version | [73a5a95] |

---

## Purpose

Decide whether lectures 1 and 2 (frontend versus backend, and the first Flask server) are implemented, tested and illustrated.

## Deliverable

`src/hello.py` with a Flask `app` and a home route returning the greeting, tests of that route, a screenshot for lecture 1 (client, server, database and the request-response cycle) and for lecture 2 (the browser showing the greeting), and README text for both.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | `flask --app hello run` serves the greeting on the configured port | Met | Not met |
| 2 | A pytest test requests `/` with the Flask test client and gets status 200 and the greeting | Met | Not met |
| 3 | Screenshots `lecture-01.png` and `lecture-02.png` exist in `docs/images/` and are shown in the README | Met | Not met |
| 4 | Doxygen comments exist on every public name in `hello.py` | Met | Not met |

## Dependencies

| Depends on | Reason |
| --- | --- |
| MIL-001 | Needs the project configuration and test tooling |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objectives 1, 2 and 3 | BC-001 |
| CN-002, CN-003 | SA-001 |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-11-07 - within the Business Case constraints.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Implement hello.py | Create the minimal Flask application with a home route that returns the greeting from `constants.py`. The file is named `hello.py`, as the lecture does, so it cannot clash with the Flask library. | No | |
| 2 | Test the home route | Add a pytest test that uses the Flask test client; it is skipped with a clear message when the `web` extra is not installed. | No | |
| 3 | Screenshot lecture 1: backend overview | Render a diagram of client, server and database with the request-response cycle (restaurant analogy) and capture it with a headless browser, never on the host desktop. | No | |
| 4 | Screenshot lecture 2: Hello World in the browser | Start the application and capture the page in a headless browser to show the greeting served from the local server. | No | |
| 5 | README section for lectures 1 and 2 | Add the two screenshots and short run instructions, including the `FLASK_APP` variable for macOS/Linux and Windows. | No | |

---

[BC-001]: ../business-case.md
[73a5a95]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/054-flask/commit/73a5a95d28db041e4f27342cc552e18f7d386410
