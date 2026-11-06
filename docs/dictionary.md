# Domain Dictionary

## Metadata
| Key | Value |
| --- | --- |
| ID | DICT-001 |
| CrossReference | [BC-001], [SA-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-06 | Accepted | Jens Tirsvad Nielsen | S01 | Initial version | [73a5a95] |

---

## Purpose and Scope

Maps each Product Owner (PO) term to its professional IT term. PO language:
English (`en`), domain `it`. The dictionary covers the terms of the lecture assignment that a visitor (S02, S03) might read differently in plain speech and in code..

## Dictionary

| PO term | Language | IT term | Definition | Used as PO term in | Used as IT term in |
| --- | --- | --- | --- | --- | --- |
| Assignment function | en | Public function | A function whose name is given by the course assignment and that code of the course participants calls. | none yet | none yet |
| Greeting | en | Response body | The text the home page shows to a visitor. | none yet | none yet |
| Home page | en | Route `/` | The page a visitor sees when opening the address of the application without a path. | none yet | none yet |
| Lecture step | en | Module | One part of the course whose code and screenshot are kept together. | none yet | none yet |
| Local environment | en | Virtual environment | The private folder in which the project's Python packages are installed. | none yet | none yet |
| Wrapper | en | Decorator | A function that adds behaviour around another function without changing it. | none yet | none yet |

## Rules

- The Domain Model, use cases and user stories use the PO term; the Operation
  Contract, Sequence Diagram, Design Class Diagram and ERD use the IT term.
- One IT term per PO term and one PO term per IT term; no synonyms.
- Rows are in ascending order of the PO term (case-insensitive, by the
  alphabet of the PO language), so a term is found without searching.

---

[BC-001]: ./business-case.md
[SA-001]: ./stakeholder-analysis.md
[73a5a95]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/054-flask/commit/73a5a95d28db041e4f27342cc552e18f7d386410
