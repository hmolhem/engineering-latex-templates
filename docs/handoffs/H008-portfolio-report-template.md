# H008 — Standalone Engineering Portfolio Report Template

## Metadata

| Field | Value |
|---|---|
| Date | `2026-07-25` |
| Author | `Hossein Molhem and ChatGPT` |
| Repository | `hmolhem/engineering-latex-templates` |
| Branch | `feature/portfolio-report-template` |
| Pull request | `#9` |
| Related version | `Unreleased after v0.2.0` |
| Status | `Open in PR #9; curated preview artifact deferred` |

## Purpose

Add a standalone LaTeX template for public engineering portfolio reports on GitHub, LinkedIn, personal websites, recruiter-facing repositories, and professional application packages.

The new template is independent from `report-template/`:

- `report-template/` remains the standard product for academic, institutional, industrial, and consulting reports.
- `portfolio-report-template/` is designed for public engineering evidence and professional portfolio publication.

## Repository location

```text
engineering-latex-templates/
├── report-template/
├── portfolio-report-template/
├── presentation-template/
├── ieee-paper-template/
└── social-media/
```

## Main features

The template adds:

- centralized public-project metadata
- a public title page without student ID, course, grading, or institutional fields
- a Portfolio Context and Evidence page
- abstract and project-objective front matter
- modular engineering chapters and appendices
- analytical, simulated, and measured evidence classification
- numerical-reliability and limitation guidance
- calculation, simulation-record, and verification-record directories
- an Engineering Verification Matrix
- external bibliography support

## Engineering Verification Matrix

The matrix is maintained in:

```text
portfolio-report-template/content/07_engineering_verification_matrix.tex
```

It links each public claim to a verification ID, evidence class, evidence location, and limitation or qualification.

The final implementation uses `longtable`, repeated headers, `booktabs` horizontal rules, no vertical grid rules, whitespace between rows, left-aligned descriptive columns, and a centered verification-ID column.

The reusable row macro is defined in:

```text
portfolio-report-template/setup/05_environments.tex
```

## Bibliography backend

The template uses `biblatex` with:

```latex
backend=bibtex
```

Validated local build sequence:

```powershell
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

BibTeX was selected because it is available in the validated local MiKTeX installation and avoids the missing Perl dependency required by `latexmk`.

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

The title page, portfolio context, abstract, objective, contents, lists, report chapters, verification matrix, appendices, and bibliography were reviewed.

A second reconstruction and build from the prepared source package produced a 26-page document. The revised verification matrix rendered without vertical grid rules.

## Generated-file policy

Temporary outputs must not be committed, including `main.pdf`, `main.aux`, `main.bbl`, `main.blg`, `main-blx.bib`, `main.log`, `main.out`, `main.toc`, `main.lof`, and `main.lot`.

The repository now ignores generated `*-blx.bib` files. A generated `main-blx.bib` that entered the initial feature commit was removed before PR creation.

## Curated preview status

The portfolio PDF was generated and visually validated locally, but the binary preview was not included in the initial branch push.

The `.gitignore` contains a narrow future exception for:

```text
portfolio-report-template/preview/portfolio-report-template-preview.pdf
```

Committing the binary preview is intentionally deferred to a separately reviewed artifact update. The root README does not expose a broken portfolio-preview link in PR #9.

## Files added or modified

```text
portfolio-report-template/
.gitignore
README.md
CHANGELOG.md
docs/HANDOFF_INDEX.md
docs/handoffs/H008-portfolio-report-template.md
```

No unrelated source changes were made to the existing report, presentation, IEEE-paper, or social-media products.

## Known limitations

- Included engineering content is illustrative and must be replaced with verified project-specific material.
- Measured claims require traceable physical-test evidence.
- The local build uses a manual four-command sequence.
- BibTeX is less capable than Biber for advanced Unicode, multilingual, and custom-sorting workflows.
- Automated compilation and visual-regression CI are not implemented.
- The curated portfolio preview artifact is deferred.

## Remaining work

- review PR #9
- merge after repository-owner approval
- record the final head and merge commits
- mark H008 as merged in the handoff index
- add the curated portfolio preview through a separately reviewed artifact update

## Recovery and rollback

Before merge, close PR #9 and delete the feature branch to abandon H008 without changing `main`.

After merge, revert the H008 merge commit to remove the standalone portfolio template and related documentation without rewriting repository history.

## Related references

- Pull request: `#9`
- Branch: `feature/portfolio-report-template`
- Template controller: `portfolio-report-template/main.tex`
- Metadata: `portfolio-report-template/setup/00_metadata.tex`
- Package configuration: `portfolio-report-template/setup/01_packages.tex`
- Verification matrix: `portfolio-report-template/content/07_engineering_verification_matrix.tex`
- Template README: `portfolio-report-template/README.md`
- Handoff index: `docs/HANDOFF_INDEX.md`
- Changelog: `CHANGELOG.md`
- Root README: `README.md`
