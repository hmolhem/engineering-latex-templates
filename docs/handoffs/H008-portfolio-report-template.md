# H008 — Standalone Engineering Portfolio Report Template

## Metadata

| Field | Value |
|---|---|
| Date | `2026-07-25` |
| Author | `Hossein Molhem and ChatGPT` |
| Repository | `hmolhem/engineering-latex-templates` |
| Branch | `feature/portfolio-report-template` |
| Pull request | `Pending` |
| Related version | `Unreleased after v0.2.0` |
| Status | `Local validation complete; ready for repository review` |

## Purpose

Add a standalone LaTeX template for publishing professional engineering
portfolio reports on GitHub, LinkedIn, personal websites, and technical
application packages.

The new template is intentionally independent from `report-template/`.

- `report-template/` remains the standard template for academic, institutional,
  industrial, and consulting reports.
- `portfolio-report-template/` is intended for public engineering projects,
  recruiter-facing documentation, and technical portfolio publication.

## Repository location

```text
engineering-latex-templates/
├── report-template/
├── portfolio-report-template/
├── presentation-template/
├── ieee-paper-template/
└── social-media/
```

## Main architecture

```text
portfolio-report-template/
├── README.md
├── main.tex
├── references.bib
├── setup/
├── frontmatter/
├── content/
├── appendices/
├── codes/
├── figures/
├── verification_records/
└── preview/
```

## Main features

The template includes:

- centralized public-project metadata
- a professional public title page
- a Portfolio Context and Evidence page
- abstract and project-objective pages
- modular engineering-report chapters
- analytical, simulated, and measured evidence classification
- numerical-reliability and limitation guidance
- an Engineering Verification Matrix
- appendix and bibliography support
- reusable code and verification-record directories
- a curated rendered PDF preview

## Public-document design

The portfolio template excludes academic and administrative information by
default, including:

- student ID
- grades
- assignment numbers
- course numbers
- instructor information
- institutional approval or endorsement

The public report should clearly distinguish analytical, simulated, and measured
results.

Simulation results must not be represented as hardware measurements.

## Engineering Verification Matrix

The verification matrix is maintained in:

```text
portfolio-report-template/content/07_engineering_verification_matrix.tex
```

It connects each public engineering claim to:

- a verification ID
- evidence class
- evidence location
- limitation or qualification

The matrix uses `longtable` so it can continue across multiple pages.

The final design uses:

- no vertical borders
- no internal vertical rules
- `booktabs` horizontal rules
- repeated headers on continuation pages
- whitespace between rows
- left-aligned descriptive columns
- a centered verification-ID column

The reusable row macro is defined in:

```text
portfolio-report-template/setup/05_environments.tex
```

## Bibliography backend

The template uses `biblatex` with the BibTeX backend:

```latex
backend=bibtex
```

The validated local build sequence is:

```powershell
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

BibTeX was selected because it is available in the validated local MiKTeX
installation and avoids the missing Perl dependency required by `latexmk`.

## Validation performed

```text
Operating system: Windows
Shell: PowerShell
TeX distribution: MiKTeX
LaTeX engine: pdfLaTeX
Bibliography backend: BibTeX
Compilation: successful
Rendered PDF inspection: completed
Fatal LaTeX errors: none
```

The following areas were reviewed:

- title page
- Portfolio Context and Evidence
- abstract and project objective
- table of contents
- list of figures
- list of tables
- report chapters
- Engineering Verification Matrix
- appendices
- bibliography

## Artifact policy

The root build output is temporary and must not be committed:

```text
portfolio-report-template/main.pdf
```

The reviewed preview is intentionally retained:

```text
portfolio-report-template/preview/portfolio-report-template-preview.pdf
```

The repository `.gitignore` contains a narrow exception for this curated
preview.

Generated LaTeX files such as `.aux`, `.bbl`, `.blg`, `.log`, `.out`, `.toc`,
`.lof`, and `.lot` remain ignored and should be removed after local validation.

## Files added or modified

Expected H008 scope:

```text
portfolio-report-template/
.gitignore
README.md
CHANGELOG.md
docs/HANDOFF_INDEX.md
docs/handoffs/H008-portfolio-report-template.md
```

The implementation should not introduce unrelated changes to the existing
report, presentation, IEEE-paper, or social-media templates.

## Known limitations

- The included engineering content is illustrative and must be replaced with
  verified project-specific material.
- Measured claims require traceable physical-test evidence.
- The local build currently uses a manual four-command sequence.
- Preview generation and inspection remain manual.
- Automated LaTeX compilation and visual-regression testing are not yet
  implemented.
- BibTeX is less capable than Biber for advanced Unicode, multilingual, or
  custom sorting workflows.

## Remaining work

- update the root `README.md`
- update `CHANGELOG.md`
- confirm the H008 row in `docs/HANDOFF_INDEX.md`
- review the complete Git diff
- commit and push the feature branch
- open and review the pull request
- merge after approval
- record the pull-request, head-commit, and merge-commit identifiers
- mark H008 as merged in the handoff index

## Recovery and rollback

Before merge, the feature branch may be deleted without affecting `main`.

After merge, revert the H008 merge commit to remove the portfolio template and
its related documentation without rewriting repository history.

## Related files

- `portfolio-report-template/main.tex`
- `portfolio-report-template/setup/00_metadata.tex`
- `portfolio-report-template/setup/01_packages.tex`
- `portfolio-report-template/setup/05_environments.tex`
- `portfolio-report-template/frontmatter/portfolio_context.tex`
- `portfolio-report-template/content/07_engineering_verification_matrix.tex`
- `portfolio-report-template/README.md`
- `portfolio-report-template/preview/portfolio-report-template-preview.pdf`
- `docs/HANDOFF_INDEX.md`
- `CHANGELOG.md`
- `README.md`
