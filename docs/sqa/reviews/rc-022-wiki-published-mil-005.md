# Review of MIL-005

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-022 |
| CrossReference | [MIL-005], [QC-WIKI-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-06 | Proposed | <author> | AI as stand-in for S01 | Initial version | [7de7bd5] |

---

## Artifact Under Review

- Instance reviewed: [MIL-005]
- Checklist used: [QC-WIKI-001]
- Scope: re-review of criterion 14 on the published wiki (earlier record RC-019)
- Language and domain: n/a
- Language reviewer: none (the reviewer reads English and knows the IT domain)
- Mode: autonomous, not independent (AI as stand-in for S01)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | The wiki has a `_Sidebar.md`, because the host lists subpages only through it | Pass | docs/wiki/_Sidebar.md exists. |
| 2 | The sidebar starts with the wiki's title in bold, then one list of the pages in the primary language (English), `Home` first | Pass | Starts with **Flask Day 54**, then one English page list with Home first. |
| 3 | The page list holds a link to every English page of the wiki, and no link points to a page that does not exist | Pass | Eight English pages are all linked; check_wiki.py found no dead link. |
| 4 | A `**Related**` section follows the page list only when the wiki has related wikis (for example the checklists wiki for a framework wiki); each entry is a link to that wiki's Home. A wiki with nothing related has no such section | N-A | The wiki has no related wikis, so there is no Related section. |
| 5 | A `**Languages**` section is the last section of the sidebar. It has one line per language, the language written in that language, linking to that language's `Home` page | Pass | Languages section is last: English, Dansk and Bahasa Melayu, each linking to its Home page. |
| 6 | The sidebar does not repeat the page list per language | Pass | The page list appears once. |
| 7 | A sidebar produced by a generator carries a comment that says so and names the generator; the generator is changed, not the page | N-A | The sidebar is written by hand, not generated. |
| 8 | The wiki has a `Languages` line on each page (criterion 11), so the sidebar is not the only way to switch language | Pass | Every page has the language line. |
| 9 | Every wiki exists in English and, as a minimum, in the language the project's registry names as the PO language; further languages are added on top, never instead of English | Pass | English plus Danish and Bahasa Malaysia; the PO language is English. |
| 10 | Every English page has a page in each other language of the wiki: the page sets are identical | Pass | Eight pages in each of the three languages (24 files); check_wiki.py confirms parity. |
| 11 | Every page starts with the language line, with the current language in bold and a link to the same page in each other language | Pass | Line 3 of every page has the bold current language and links to the other two. |
| 12 | A page in a language other than English is named `<Page>-<code>.md`, with a BCP 47 code; English has no suffix | Pass | Files are <Page>-da.md and <Page>-ms.md; English has no suffix. |
| 13 | Code blocks, commands, file names and IDs stay in English in every language | Pass | check_wiki.py: code blocks and image links are identical in all three languages. |
| 14 | The sidebar, every page and every link were checked on the published wiki after the change, not only in the repository | Pass | After the merge (commit bf2c82a) the publish workflow published 26 pages; the 24 content pages each answer HTTP 200 on the host, every lecture image resolves, and the Home page shows the sidebar entries and the Danish and Bahasa Malaysia links. |
| 15 | A change to the layout rules (sections, order, naming) is made in the generator or template and in this checklist's source rules together | N-A | No layout rule is changed. |
| 16 | The wiki folder (`docs/wiki/`) is flat: every page, `Home.md` and `_Sidebar.md` included, is directly in it, and languages are told apart by file name, never by a subfolder | Pass | docs/wiki/ is flat; no subfolder. |

## Overall Verdict

Go — Re-review of criterion 14 after publishing; all other results are unchanged from RC-019. The native-reader action item from RC-019 stays open for S01 and does not block.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| Have a native reader confirm the Danish and Bahasa Malaysia wording (from RC-019, not independent so far) | S01 | 2026-11-10 |

---

[MIL-005]: ../../milestones/mil-005-docs-wiki.md
[QC-WIKI-001]: ../../../framework/qc/artifacts/qc-wiki.md
[7de7bd5]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/054-flask/commit/7de7bd50d8d12e77a2419ff253319732a1337e28
