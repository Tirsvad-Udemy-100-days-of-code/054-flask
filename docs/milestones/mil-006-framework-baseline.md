# MIL-006 Framework baseline

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-006 |
| CrossReference | [BC-001], [PP-001], [MIL-005] |
| Language | en |
| Domain | education |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-16 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version; accepted with the Go verdict of the review record (autonomous, not independent) | pending |

---

## Purpose

This gate decides whether the project has the baseline of the framework: the adopted framework release, the README in the framework template with an appendix that lists only the documents of the repository, licence and project URL metadata, the editor settings of the baseline, the environment template of the framework, a passing test suite, an updated plan and traceability matrix and reviewed documents, merged to the default branch with a green build. The wiki in English, Danish and Bahasa Malaysia already has a sidebar in the framework's shape; this gate checks it again against the current checklist and moves the language line to the first line of each page, as the checklist requires; no other wiki text changes. The work is delivered on the branch `mil-006-framework-baseline` and one pull request. It changes no behaviour of the program.

## Deliverable

A merged pull request that holds: the updated Business Case, Project Plan, Traceability Matrix and Artifact Registry, this milestone and the review records of the changed documents and of the wiki; the README without the private framework files in its appendix; `pyproject.toml` with the licence expression, the licence file, the project URLs and a build requirement that reads the licence expression; `.editorconfig`, `.env.example` and `.gitignore` of the framework baseline; and the framework release adopted by the project. The wiki pages with the language line as first line (no other wiki text changes). The program (`src/`), the tests (`tests/`) and the screenshots and their tool (`docs/images/`) do not change.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | BC-001, PP-001 and MIL-006 each have an `Accepted` Version History row and a review record, and the wiki has a review record | Verdict `Go` | Any missing or `No-Go` |
| 2 | `python -m pytest` runs (the tests use Flask's application object and a patched `run`, so they start no server) and `git diff origin/main --stat -- src tests docs/images` lists no file | Exit code 0 and an empty diff | Any failure or any change |
| 3 | `docs/wiki/` has `_Sidebar.md`, `_Footer.md` and the eight English pages (Home, Setup-and-Run and Lecture-1 to Lecture-6) in en, da and ms (24 pages), directly in the folder, each page starting with the language line (the first line of the file), and the sidebar has the title, one list of the English pages and the Languages section last; the published wiki is the same as the folder | 24 pages, the sidebar, the footer and the same content on the host | A page or language missing, a subfolder, a sidebar of another shape or a difference on the host |
| 4 | `framework/scripts/check-readme.sh`, `framework/scripts/check-languages.sh` and `framework/scripts/check-editorconfig.sh` run | Exit code 0 | Any finding |
| 5 | `pyproject.toml` has `license` (a licence expression) and `license-files`, sets the project URLs for the repository, the documentation and the issue tracker, and requires a setuptools version that reads the licence expression | All set | Any missing |
| 6 | `.env.example` is tracked and holds empty placeholders for the framework tokens; `.env` is not tracked | Present, no real value | Missing, a real value present or `.env` tracked |
| 7 | All CI checks of the pull request | Green | Red or pending |
| 8 | The pull request carries one `Closes #N` line per task of this milestone | Every issue is closed after the merge | An issue stays open |

## Dependencies

| Depends on | Reason |
| --- | --- |
| [MIL-005] accepted | Documents and baselines the finished program, its tests, its README and its wiki |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objectives 1 to 5 | Criterion 2 (the behaviour is unchanged and its tests pass) |
| Objective 6 | Criteria 1, 3, 4, 5, 6 and 8 (documents, wiki, README, metadata, environment template and issues) |
| Success criterion 7 | Criteria 1, 2, 3, 4 and 7 |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 (AI as stand-in, autonomous mode, not independent) |

## Target Date

2026-11-23: one week after the start, as the Business Case constraint for this milestone requires.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Adopt the framework release | Move the `framework/` submodule to the newest release, track `.gitmodules` (lowercase repository URL), install the skills and hooks, add the framework baseline `.editorconfig`, bring `.env.example` to the framework's template and let `.gitignore` keep `.env.example`, so the project follows the same rules as the other projects of the portfolio. | No | BC-001 objective 6 |
| 2 | Update and review the planning documents | Add this milestone to the Business Case, Project Plan and Traceability Matrix, set the domain of the changed documents and of the registry to education, name the PlantUML server in the Artifact Registry and review each changed document against its QC checklist, so the plan-first gate is met. | No | BC-001 objective 6 |
| 3 | Check the wiki against the current checklist | Compare the pages and the sidebar with the wiki checklist of the adopted framework release, move the language line to the first line of each page (criterion 11), read the published wiki back from the host after the merge and add a review record for the wiki. | No | BC-001 objectives 4 and 6 |
| 4 | Bring the README to the framework template | Keep the text of the README, describe the framework files in the overview, name the licence expression, remove the sentence that says the Flask application does not exist yet, state that the development server is for local use only and give the appendix only the documents that are in the repository, so the README is complete and checkable. | No | BC-001 objectives 4 and 6 |
| 5 | Complete the package metadata | Add `license-files` and the repository, documentation and issue tracker URLs to `pyproject.toml` and raise the build requirement to the setuptools version that reads a licence expression, so package tools can read them. | No | BC-001 objectives 3 and 6 |

---

[BC-001]: ../business-case.md
[PP-001]: ../project-plan.md
[MIL-005]: ./mil-005-docs-wiki.md
