# ADR-0001 Layered package layout under src/flask_day_54

## Metadata
| Key | Value |
| --- | --- |
| ID | ADR-0001 |
| CrossReference | [BC-001], [PP-001], [MIL-001], [MIL-002], [MIL-003], [MIL-004] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-06 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | [0f4e36b] |

Allowed Status values: `Proposed`, `Accepted`, `Rejected`, `Deprecated`, `Superseded by ADR-NNNN`.

---

## Context

The Python quality checklist (QC-PY-001, criterion 17) and the `clean-architecture` skill ask for source in the layers `domain`, `application`, `infrastructure` and `presentation`, and tests in `unit`, `integration` and `e2e`. The lectures are small, and the first plan named flat modules such as `src/hello.py`. Forces: the checklist is mandatory; the lecture names (`hello.py`, `calculate`) must stay visible to course participants (S02); the repository should stay easy to read (S03); `domain` must import no framework.

Options:

1. Flat modules in `src/`, with an ADR that merges all layers. The checklist forbids merging `domain` with code that does input or output, and a flat layout hides the idea of the dependency rule.
2. Layered package `src/flask_day_54/<layer>/`, one module per lecture topic, tests in `tests/unit` and `tests/e2e`.

## Decision

Use option 2: the package `flask_day_54` with the layers `domain`, `application`, `infrastructure` and `presentation`. The pure lecture code (`first_class_functions`, `decorators`, `name_demo`, `cli_basics`) is in `domain`, the greeting use case in `application`, the server settings in `infrastructure`, and the Flask application `hello.py` in `presentation`. Each layer that needs constants has its own `constants.py`. `tests/unit` tests `domain` and `application`; `tests/e2e` tests the Flask application through its test client; `tests/integration` is created only when a test needs it.

## Consequences

**Positive:**

- The code meets QC-PY-001 criterion 17 without a merged layer.
- `domain` is importable and testable with no package installed (no Flask), which serves S03.
- The lecture module names are kept inside their layers.

**Negative:**

- Longer import and run paths: `flask --app flask_day_54.presentation.hello run` instead of `flask run` in a folder with `hello.py`.
- More folders than a lecture of this size strictly needs.

## Affected Artifacts

- [MIL-001] — paths and `constants.py` locations change
- [MIL-002] — `hello.py` lives in `presentation`
- [MIL-003] — the `__main__` start command and `name_demo` / `cli_basics` locations change
- [MIL-004] — the lecture modules live in `domain`
- [BC-001] — scope and constraints unchanged
- [PP-001] — gateways and dates unchanged

---

[BC-001]: ../business-case.md
[PP-001]: ../project-plan.md
[MIL-001]: ../milestones/mil-001-foundation.md
[MIL-002]: ../milestones/mil-002-hello-flask.md
[MIL-003]: ../milestones/mil-003-cli-and-main.md
[MIL-004]: ../milestones/mil-004-functions-decorators.md
[0f4e36b]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/054-flask/commit/0f4e36b68282be23a71aa6684af01ca85a1e9473
