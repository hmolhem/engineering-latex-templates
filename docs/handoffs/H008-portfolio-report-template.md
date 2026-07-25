# H008 — Standalone Engineering Portfolio Report Template

## Metadata

| Field | Value |
|---|---|
| Date | `2026-07-25` |
| Author | `Hossein Molhem and ChatGPT` |
| Repository | `hmolhem/engineering-latex-templates` |
| Implementation branch | `feature/portfolio-report-template` |
| Pull request | `#9` |
| Head commit | `86afcd410a2f4c2c0ed82bad078cb311ba639de7` |
| Merge commit | `8ac0d5089939087f39bd1de6b0b93dd5bc4ced21` |
| Preview-closeout branch | `docs/h008-preview-closeout` |
| Related version | `Unreleased after v0.2.0` |
| Status | `Merged in PR #9; curated preview publication in closeout review` |

## Purpose

Add an independent LaTeX template for public engineering portfolio reports on GitHub, LinkedIn, personal websites, recruiter-facing repositories, and professional application packages.

The new product is intentionally separate from `report-template/`:

- `report-template/` remains the standard template for academic, institutional, industrial, and consulting reports.
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

The merged template includes:

- centralized public-project metadata
- a professional public title page without student ID, course, grading, or institutional fields
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

A second reconstruction and build from the prepared source package produced a 26-page A4 document. The revised verification matrix rendered without vertical grid rules.

## Generated-file policy

Temporary outputs must not be committed, including `main.pdf`, `main.aux`, `main.bbl`, `main.blg`, `main-blx.bib`, `main.log`, `main.out`, `main.toc`, `main.lof`, and `main.lot`.

The repository ignores generated `*-blx.bib` files. A generated `main-blx.bib` that entered the initial feature commit was removed before PR creation.

## Curated preview closeout

The reviewed publication artifact is:

```text
portfolio-report-template/preview/portfolio-report-template-preview.pdf
```

Preview verification record:

```text
Pages: 26
Page size: A4, 595 x 842 pt on every page
Encrypted: no
Form fields: 0
Attachments: 0
Fonts: embedded
Rendered review: completed
SHA-256: a27dc05773637fecf1b3b79270e32a2ad3c1aab16caf0cd860c52afbe9763528
```

The root-level `main.pdf` remains temporary. Only the named preview artifact is intentionally version-controlled.

## Files added or modified by H008

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
- Curated previews must be refreshed and inspected manually after material source changes.

## Lifecycle closeout

- [x] Dedicated feature branch used
- [x] Standalone root-level template added
- [x] Local compilation completed
- [x] Rendered PDF reviewed
- [x] PR #9 opened and reviewed
- [x] PR #9 merged
- [x] Feature branch deleted
- [x] Local `main` synchronized with `origin/main`
- [x] Head and merge commits recorded
- [x] Curated preview regenerated after the final table correction
- [x] Preview metadata, page count, fonts, and checksum verified
- [ ] Preview-closeout pull request merged

## Recovery and rollback

Revert merge commit `8ac0d5089939087f39bd1de6b0b93dd5bc4ced21` to remove the standalone portfolio template and its H008 documentation without rewriting repository history.

If only the curated preview must be removed, revert the preview-closeout merge commit rather than reverting the H008 implementation.

## Related references

- Pull request: `#9`
- Implementation branch: `feature/portfolio-report-template`
- Head commit: `86afcd410a2f4c2c0ed82bad078cb311ba639de7`
- Merge commit: `8ac0d5089939087f39bd1de6b0b93dd5bc4ced21`
- Template controller: `portfolio-report-template/main.tex`
- Metadata: `portfolio-report-template/setup/00_metadata.tex`
- Package configuration: `portfolio-report-template/setup/01_packages.tex`
- Verification matrix: `portfolio-report-template/content/07_engineering_verification_matrix.tex`
- Preview: `portfolio-report-template/preview/portfolio-report-template-preview.pdf`
- Template README: `portfolio-report-template/README.md`
- Handoff index: `docs/HANDOFF_INDEX.md`
- Changelog: `CHANGELOG.md`
- Root README: `README.md`
