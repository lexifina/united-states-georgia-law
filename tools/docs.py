"""Georgia: write repo/README.md, LICENSE, jurisdiction.json."""
import sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / 'world-law'))
import us_state_lib as L

README = """# Georgia: law history in git

Georgia's Constitution and the whole Official Code of Georgia Annotated (statute text) as a git repository: one file per provision, one paragraph per line, so `git blame` works line by line. It follows the shared design of [lexifina/global-law](https://github.com/lexifina/global-law).

**What is in it now**

TABLE_HERE

That is all the law this repository holds today: the Constitution and all 53 titles of the Code. Session laws, local and special laws and regulations are not in it.

## Where the text comes from

The State of Georgia publishes the Code as volume and supplement PDFs at legis.ga.gov. This build reads them through the [Georgia Commons](https://georgiacommons.org/code) corpus (an independent project, not the State), which separates the statute text of each section from the notes printed around it and releases it under CC0-1.0. Only the statute text is used. Case annotations, history lines, cross-references, editorial notes and law-review references are not copied. Georgia's own Code provides that the statutory text and its numbering are the enacted law and that annotations, catchlines and history lines are not (O.C.G.A. 1-1-1).

## Dates

- Each act is one version, dated **31 December 2025**: the volumes state only that they include "Acts of the 2025 Regular Session of the General Assembly", with no day, so the year-end release date of the corpus that carries them is used. It is the oldest version available; no earlier text is online in this form.
- The first commit is credited to the publisher as "oldest version available".
- Where the Code prints one section twice with different effective dates, the text in force on 30 October 2026 is used.

## What it does not show

- Any history before the 2025 supplement, and the 2026 session.
- Reserved, repealed and redesignated sections (they carry no text).
- Tables and forms inside statutes are shown as their lines, not as tables. Eleven of the State's 100 source files carry variances printed in the State's own pages; they are not corrected.
- A court decision can make a printed provision unenforceable without changing the volume; the volume does not record that.
- Nothing here is an official publication or legal advice.

## How it is checked

- Every unit is read back from git on its day and compared with the corpus (`tools/check_repo.py`; results in `REPRODUCE.md`).
- The source files are identified by their sha256, in `data/versions.json`.
"""

LICENSE = """The legal texts are the statutory text of the Constitution of the State of Georgia and of the Official Code of Georgia Annotated
as published by the State of Georgia (volumes and supplements at https://www.legis.ga.gov), in the 2025 supplement.

Statute text is not protected by copyright: the Supreme Court held in Georgia v. Public.Resource.Org, Inc., 590 U.S. 255 (2020), that
the Code's annotations are government edicts that cannot be copyrighted, and O.C.G.A. 1-1-1(b) enacts the statutory text and its
numbering as law. This repository copies the statute text only, never the annotations.

The bytes come from the Georgia Commons corpus (https://georgiacommons.org/code), an independent project that extracts the text from the
State's volumes and releases it under CC0 1.0 Universal (https://creativecommons.org/publicdomain/zero/1.0/legalcode). The State's own site,
legis.ga.gov, is a script-driven page whose terms could not be read here, and the LexisNexis public-access site was not used at all.
Georgia Commons is not the State and this repository is not an official publication.

Changes made by Lexifina: one Markdown file per provision, one paragraph per line, normalised spaces and quotation marks,
reserved and repealed sections left out. The wording of the law was not changed.

Lexifina's own contributions (the arrangement of the history, the commit messages, the tables and the tools) are dedicated to the
public domain under CC0 1.0 Universal: https://creativecommons.org/publicdomain/zero/1.0/legalcode
"""

import json as _j
_c = _j.loads((HERE / 'corpus.json').read_text('utf-8'))
_rows = ['| Folder | Act | Versions | History |', '| --- | --- | ---: | --- |']
for _a in _c['acts']:
    _n = len(_a['versions'][0]['units'])
    _rows.append('| `%s/` | %s, %d %s | 1 | %s |' % (_a['slug'], _a['title'].replace('Official Code of Georgia Annotated, ', 'O.C.G.A. '), _n, 'paragraphs' if _a['slug'] == 'constitution' else 'sections', 'Oldest version available: the 2025 supplement' if _a['slug'] == 'constitution' else 'Same'))
README = README.replace('TABLE_HERE', chr(10).join(_rows))
L.write_repo(HERE, README, LICENSE, {
    'path': 'us-ga', 'code': 'GA', 'name': 'Georgia', 'level': 'state',
    'repo': 'https://github.com/lexifina/united-states-georgia-law',
    'build': 'built: Constitution and all 53 O.C.G.A. titles, statute text only, one version (2025 supplement, dated 2025-12-31)',
    'register_date': '2026-10-30'})
