# Business Case: Flask Backend Basics (100 Days of Code, Day 54)

## Metadata
| Key | Value |
| --- | --- |
| ID | BC-001 |
| CrossReference | [SA-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-06 | Accepted | Jens Tirsvad Nielsen | S01 | Initial version | pending |

---

## Executive Summary

This project turns the Day 54 lectures of Udemy's "100 Days of Code: The Complete Python Pro Bootcamp" (Flask basics, command line, `__name__`/`__main__`, first-class functions, decorators) into a small, readable and runnable Python repository. It gives the course participant a reviewed record of the assignment, gives fellow course participants code with the assignment's function names, and gives repository visitors a documented example in English, Danish and Bahasa Malaysia.

## Methodological and Standards Foundation

The project follows the SQA and QC framework mounted at `framework/` (plan first, review every artifact against its QC checklist, one pull request per milestone). Quality is stated with ISO/IEC 25010:2023 characteristics. Source code follows the `coding-conventions` skill for Python and the layering of the `clean-architecture` skill, scaled to a learning project.

## Problem Statement

A course lecture is watched once and is hard to revisit. Solutions shared between course participants differ in structure, miss run instructions and lack tests, so they are difficult to compare. The lecture content (what a backend is, how a Flask server starts, why `__name__ == "__main__"` is used, how functions are passed and decorated) has no durable, searchable summary with evidence that the code runs.

## Business Opportunity

A single repository can serve as a personal study record, a reference for other participants and a portfolio piece, at very low cost. Wiki pages in three languages widen the audience beyond English readers.

## Objectives

1. Deliver runnable Python code for each Day 54 lecture, using the function names of the assignment (`calculate`, `add`, `subtract`, nested and returned functions, a decorator).
2. Deliver a minimal Flask application that serves "Hello, World!" and starts either with `flask run` or with `python src/hello.py`.
3. Deliver automated tests (pytest) for all behaviour that can be tested without a user interface.
4. Deliver a README and a three-language wiki (en, da, ms) with one screenshot per lecture step and a short explanation of what the lecture taught.
5. Publish the repository with a description and topics.

## Scope

### In Scope

- Python source under `src/`, tests under `tests/`, documents under `docs/`.
- Project configuration in `pyproject.toml`, constants in `constants.py`, a Python `.gitignore`, a Doxyfile and Doxygen comments in the source.
- README from the framework template, including how to create and use a local `.venv`, upgrade pip, run the project and run the tests.
- Wiki in English, Danish and Bahasa Malaysia with screenshots for each lecture step.
- Repository description and topics on the Gitea host.

### Out of Scope

- Features beyond the lectures (database, authentication, templates, deployment).
- Django or any other framework.
- Importing, testing or documenting the personal `.env` file; it is for the author's own tooling only.
- Hosting the Flask application publicly.

## Expected Benefits

### Tangible Benefits

- A repository whose tests pass and whose run instructions work on a clean checkout.
- Screenshots and wiki pages that replace re-watching the lectures.

### Intangible Benefits

- Practice of a plan-first, reviewed workflow on a small project.
- A clearer shared reference for course participants and visitors.

## Strategic Alignment

The project supports the author's learning goal of completing the 100 Days of Code bootcamp with professional habits (tests, documentation, version control) and the open sharing of the results.

## Success Criteria

| # | Criterion | Target | Measure |
| --- | --- | --- | --- |
| 1 | Lectures covered by code | 6 of 6 lecture topics | Each topic has a module or section in `src/` |
| 2 | Tests pass | 100 % of pytest tests pass on Python 3.13 | `python -m pytest` exit code 0 |
| 3 | Runtime dependencies | Only Flask, as an optional extra; none for the pure-Python lectures | `pyproject.toml` |
| 4 | Screenshots | 1 per lecture step in README and in each wiki language | Count of images in README and wiki pages |
| 5 | Wiki languages | 3 (en, da, ms) with the same pages | Page list per language |
| 6 | Repository metadata | Description and at least 5 topics set | Gitea repository settings |

## Risks

| Risk | Impact | Mitigation |
| --- | --- | --- |
| Screenshots of a terminal or browser need a GUI | A GUI test on the host desktop would take the user's mouse and keyboard | Use a headless browser or a container, never the host desktop (`framework/process/gui-testing.md`) |
| Danish or Bahasa Malaysia text contains errors | Reduced trust in the wiki | Keep sentences short and technical; the author reviews the text |
| The token in `.env` leaks into the repository | Credential exposure | `.env` is in `.gitignore`; no code reads it; tokens are only read by the author's tooling from the environment |
| Python 3.13 is the only interpreter available | Wording "greater than 3.13" cannot be tested on a newer version | State `requires-python = ">=3.13"` and test on the installed 3.13 |

## Assumptions

- The Product Owner is S01 and also develops and reviews; S02 and S03 are reached through the published repository only.
- Python 3.13 and Doxygen are installed on the author's machine.
- The Gitea host offers a repository wiki and a REST API for description and topics.
- The lectures contain no code beyond what the summaries describe; the assignment function names follow the lecture text.

## Constraints

- Python 3.13 or newer, `venv`, `pytest`, `pyproject.toml`, `constants.py` for constants.
- Folder structure `src/`, `tests/`, `docs/`.
- One branch and pull request per milestone; no direct commits on `main`.
- Doxygen comments in the source and a Doxyfile.
- Product Owner language: English, domain IT.

## Cost–Benefit Assessment

| Costs | Benefits |
| --- | --- |
| About two working days of the author's time, no licence or hosting cost | A reviewed study record, a shareable reference and a portfolio entry |

The assessment is qualitative on purpose: the project earns no revenue and has no cash cost, so a monetary return on investment would be invented. The only measurable cost is the author's time, stated above.

## Stakeholders

| Stakeholder ID (SA) | Interest in this project |
| --- | --- |
| S01 | Owns the assignment, builds and reviews it |
| S02 | Reads and compares runnable solutions |
| S03 | Browses for ideas; needs clear description, topics and README |

## Recommendation

Proceed — the scope is small, the cost is low and every objective is verifiable by tests, screenshots or repository settings.

---

[SA-001]: ./stakeholder-analysis.md
