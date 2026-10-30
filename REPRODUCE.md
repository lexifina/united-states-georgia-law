# How this repository was made (Georgia)

This file is written by the build on 2026-10-30, the day the source data was retrieved.

## Sources

| Source | Address | Retrieved | Licence |
| --- | --- | --- | --- |
| Georgia Commons: Official Code of Georgia Annotated (CC0 corpus, 2025 supplement) | <https://georgiacommons.org/code> | 2026-10-30 | CC0-1.0 |

Every word of law in this repository comes from these sources. Lexifina reads them and records each act's dated versions, and the laws that made each change, in one corpus file. This repository is built from that file.

## What is in it

| Act | Title | Versions | Span |
| --- | --- | ---: | --- |
| `constitution` | Constitution of the State of Georgia (1983) | 1 | 2025-12-31 to 2025-12-31 |
| `contracts` | Official Code of Georgia Annotated, Title 13. Contracts | 1 | 2025-12-31 to 2025-12-31 |
| `corporations` | Official Code of Georgia Annotated, Title 14. Corporations, Partnerships, and Associations | 1 | 2025-12-31 to 2025-12-31 |
| `crimes` | Official Code of Georgia Annotated, Title 16. Crimes and Offenses | 1 | 2025-12-31 to 2025-12-31 |
| `property` | Official Code of Georgia Annotated, Title 44. Property | 1 | 2025-12-31 to 2025-12-31 |

The build made 5 commits:

| Commits | Kind |
| ---: | --- |
| 5 | first version of an act |
| 0 | one law on its in-force day |
| 0 | changes no amendment note explains, credited to the publisher |

Other counts:
- 0 commits on the branch `future`: laws not yet in force on 2026-10-30.
- 0 commits dated 1 January 1970: in force before 1970, with the real day in their `In-force` trailer.
- 0 laws in the record.
- 5 tags.

## Dates

Each commit is dated at noon (America/New_York) on the day the change took effect. The other dates, enacted and published, are trailers.

When a law gives no date of its own, the default rule applies: Georgia Acts take effect as the enacting act provides; absent a provision, 1 July after the session. https://georgiacommons.org/code/about.md

## How the history is built

`tools/build.py` turns the corpus into this history in one pass: one commit per law, on the day it took effect. The same corpus always gives the same commit hashes. `tools/check_repo.py` reads every version back from git and compares it with the corpus. `tools/on.py` shows the law as it stood on any date. The corpus format is described in `tools/SCHEMA.md`.

- Corpus: sha256 `970c64acb52231a3e9c87ad563489a0e148d9b43da1d002e1e20e7b357e5bc76` (5078205 bytes).
- Builder blob hashes (`git hash-object`): `build.py` `a4faa25af85facb64b956b372f6b528aafdd7ec1`, `check.py` `3e59cb6f05eccb94a9ec14431a7f6781221e83ef`, `on.py` `644a6c0857fbcc72562032b58d57aa113fee0641`.
- Python 3.12.10; git version 2.46.0.windows.1.

## Checks

Not yet run for this build.

No second build of this corpus has been compared yet.

## Decisions made by hand

- Only the `text` field of each section is used. History lines, notes, cross-references, case annotations and editorial notes are never copied (the annotations Georgia v. Public.Resource.Org made public domain are out of scope here).
- Sections whose status is reserved, repealed, redesignated, superseded or note-only carry no statute text and are left out.
- The volumes give their currency only as "Including Acts of the 2025 Regular Session of the General Assembly" (and, for some, "of the 2025 Session"), with no day. Each act is one "oldest version available" version dated 2025-12-31, the release date of the corpus that carries them, credited to the publisher.
- Where the code prints one section twice with different effective dates (16-5-100, 16-13-121, 44-1-13, 44-14-63), the text whose "Effective" date is the latest on or before 2026-10-30 is used. 44-2-39 prints two texts with no qualifier; the later one in the corpus is used.
- Catchlines are not enacted text in Georgia (O.C.G.A. 1-1-1(c)) but are kept as the first line of each file for navigation.
- Georgia Commons carries the bytes; the text originates in the volumes the State publishes at legis.ga.gov. The LexisNexis public-access site was not used.

## What AI did and did not do

The scripts that read the sources and build this repository were written by Claude Code running Claude Opus 5.5 (`claude-opus-5-5`) under Lexifina's direction.

No model wrote, translated or corrected legal text. No model runs at build time. Every word of law in this repository comes from the official sources above.

The commit messages are written by `build.py` from the source data.

Model use at data-build time:
- Claude Code wrote the parse script; it wrote or changed no legal text. The script is deterministic and runs no model.
