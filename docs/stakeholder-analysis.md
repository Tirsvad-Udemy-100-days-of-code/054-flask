# Stakeholder Analysis: Flask Backend Basics

## Metadata
| Key | Value |
| --- | --- |
| ID | SA-001 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-06 | Accepted | Jens Tirsvad Nielsen | S01 | Initial version | [73a5a95] |

---

## Purpose

Identify who is affected by the Flask Day 54 repository and what each needs from it. The method is a power/interest grid; concerns are mapped to FURPS+.

## Stakeholder Summary Table

| ID | Name | Role/Title | Organization | Power Level | Interest Level | Quadrant | Primary Concern (Business Language) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S01 | Jens Tirsvad Nielsen | Course participant, Product Owner, developer, reviewer | Tirsvad | HIGH | HIGH | Manage Closely | A correct, reviewed record of the assignment that he can reuse |
| S02 | Udemy coursists | Fellow course participants | Udemy course community | LOW | HIGH | Keep Informed | Readable, runnable code with the assignment's function names and run instructions |
| S03 | GitHub viewers | Repository visitors | Public | LOW | LOW | Monitor | A clear description, topics and README, and no runtime dependencies |

## Power/Interest Classification Rationale

- **Manage Closely (S01):** decides scope, writes, reviews and accepts every artifact.
- **Keep Informed (S02):** cannot change the project but depends on the quality of the shared code; served by README and wiki.
- **Monitor (S03):** casual visitors served by the repository description, topics and README. The brief names S03's power and interest as given by the Product Owner; both are classed LOW because visitors have no stake beyond browsing.

## Primary Concerns and FURPS+ Mapping

| Concern ID | Stakeholder | Concern | FURPS+ attribute |
| --- | --- | --- | --- |
| CN-001 | S01 | Work is planned and reviewed before code is written | Functionality |
| CN-002 | S01 | Tests prove the lecture examples behave as described | Reliability |
| CN-003 | S02 | Code is readable and uses the assignment's function names | Usability |
| CN-004 | S02 | Instructions to create a `.venv`, run the app and run the tests work first time | Usability |
| CN-005 | S03 | The repository explains itself in its description, topics and README | Usability |
| CN-006 | S03 | Nothing heavy has to be installed to read or run the pure-Python parts | Supportability |
| CN-007 | S01 | Wiki exists in English, Danish and Bahasa Malaysia | Functionality |

## Communication Requirements

| ID | Channel | Frequency | Deliverable | Phase / Milestone |
| --- | --- | --- | --- | --- |
| CM-001 | Pull request on the git host | One per milestone | Reviewed change and run summary | All milestones |
| CM-002 | README | Updated per milestone | Run and test instructions, screenshots | MIL-002 to MIL-005 |
| CM-003 | Wiki (en, da, ms) | Once, at the documentation milestone | What each lecture taught, with screenshots | MIL-005 |
| CM-004 | Repository description and topics | Once | Short description, topics | MIL-001 |

## Conflicting Interests and Mitigations

| Conflict | Stakeholders | Mitigation |
| --- | --- | --- |
| S03 wants no runtime dependencies, but the assignment is a Flask application | S01, S03 | Flask is declared only as the optional extra `web`; the pure-Python lecture modules and their tests need nothing installed |
| S02 wants the assignment's function names, the coding conventions prefer other names for some | S01, S02 | Keep the assignment names for public functions; document them in Doxygen comments |

## Traceability Analysis

### Business Goal Alignment

| Stakeholder | Concern | Business Case objective |
| --- | --- | --- |
| S01 | CN-001, CN-002 | [BC-001] objectives 1 to 3 |
| S02 | CN-003, CN-004 | [BC-001] objectives 1, 2 and 4 |
| S03 | CN-005, CN-006 | [BC-001] objectives 4 and 5 |
| S01 | CN-007 | [BC-001] objective 4 |

## Sign-Off

Product Owner and reviewer: S01.

---

[BC-001]: ./business-case.md
[73a5a95]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/054-flask/commit/73a5a95d28db041e4f27342cc552e18f7d386410
