# Engineering LaTeX Templates

Reusable LaTeX templates for engineering reports, public portfolio reports, technical presentations, research papers, and project documentation.

This repository is a stable, version-controlled documentation system for recurring academic, research, industrial, consulting, and professional-portfolio work. Each top-level template is maintained as an independent product with its own purpose, metadata model, documentation, and rendered-preview policy.

## Repository contents

```text
engineering-latex-templates/
├── README.md
├── LICENSE
├── CHANGELOG.md
├── .gitignore
├── docs/
│   ├── WORKFLOW.md
│   ├── HANDOFF_INDEX.md
│   ├── HANDOFF_TEMPLATE.md
│   └── handoffs/
├── report-template/
│   ├── README.md
│   ├── main.tex
│   ├── setup/
│   ├── frontmatter/
│   ├── content/
│   ├── appendices/
│   ├── figures/
│   ├── codes/
│   ├── preview/
│   └── references.bib
├── portfolio-report-template/
│   ├── README.md
│   ├── main.tex
│   ├── setup/
│   ├── frontmatter/
│   ├── content/
│   ├── appendices/
│   ├── codes/
│   ├── figures/
│   ├── simulation_records/
│   ├── verification_records/
│   ├── preview/
│   └── references.bib
├── presentation-template/
│   ├── README.md
│   ├── main.tex
│   ├── sections/
│   ├── figures/
│   ├── speaker-notes/
│   └── preview/
├── ieee-paper-template/
│   ├── README.md
│   ├── main.tex
│   ├── figures/
│   ├── preview/
│   └── references.bib
├── social-media/
│   └── linkedin-carousel/
└── examples/
```

## Available templates

### Standard engineering report

`report-template/`

A modular report system for academic, institutional, industrial, and consulting reports, with:

- centralized user-editable metadata in `setup/00_metadata.tex`
- optional cover logo and optional identity rows
- standardized title-page typography
- configurable headers on non-cover pages
- separate objective and abstract files
- a single body menu in `content/00_report_body.tex`
- a single appendix menu in `appendices/00_appendices.tex`
- reusable theorem, definition, example, problem, code, matrix, and engineering environments
- bibliography support through `biblatex` and Biber

See [`report-template/README.md`](report-template/README.md).

### Public engineering portfolio report

`portfolio-report-template/`

A standalone public-report system for GitHub, LinkedIn, personal websites, recruiter-facing project repositories, and professional evidence packages, with:

- centralized public metadata in `setup/00_metadata.tex`
- a public cover without course, student-ID, grading, or institutional fields
- a Portfolio Context and Evidence page
- analytical, simulated, and measured evidence classification
- numerical-reliability and limitation guidance
- a multipage Engineering Verification Matrix
- reproducible calculation, simulation-record, and verification-record directories
- `biblatex` with a BibTeX backend for the validated Windows/MiKTeX workflow

See [`portfolio-report-template/README.md`](portfolio-report-template/README.md).

### Technical presentation

`presentation-template/`

A reusable Beamer template with section-based organization and speaker-note support.

See [`presentation-template/README.md`](presentation-template/README.md).

### IEEE paper starter

`ieee-paper-template/`

A complete illustrative IEEE-style starting point for conference or journal manuscripts. The official template and author instructions of the target venue always take precedence.

See [`ieee-paper-template/README.md`](ieee-paper-template/README.md).

### LinkedIn carousel system

`social-media/linkedin-carousel/`

A reusable 4:5 portrait LaTeX system for LinkedIn document posts, including the completed repository-showcase carousel and its curated multi-page PDF.

See [`social-media/linkedin-carousel/README.md`](social-media/linkedin-carousel/README.md).

## Rendered PDF previews

Curated PDFs show the reviewed appearance of each publication product:

- [Engineering report template preview](report-template/preview/engineering-report-template-preview.pdf)
- [Portfolio report template preview](portfolio-report-template/preview/portfolio-report-template-preview.pdf)
- [Technical presentation template preview](presentation-template/preview/technical-presentation-template-preview.pdf)
- [IEEE paper template preview](ieee-paper-template/preview/ieee-paper-template-preview.pdf)
- [LinkedIn repository-showcase carousel](social-media/linkedin-carousel/engineering-latex-templates-carousel/engineering-latex-templates-carousel.pdf)

Generated PDFs remain ignored by default. Explicitly named, reviewed publication artifacts are version-controlled and should be refreshed whenever a material source change affects rendered output.

## Recommended usage

1. Copy only the required top-level template folder or create a new repository from this repository.
2. Edit the selected template's `setup/00_metadata.tex` when that file exists.
3. Replace illustrative content with verified project-specific material.
4. Keep shared setup modules stable unless a formatting change is intentional.
5. Compile locally or upload the complete template folder to Overleaf.
6. Inspect every page before submission or public release.

Standard report example:

```bash
git clone https://github.com/hmolhem/engineering-latex-templates.git
cd engineering-latex-templates/report-template
latexmk -pdf main.tex
```

Portfolio report example for Windows/MiKTeX:

```powershell
cd engineering-latex-templates/portfolio-report-template
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

## Development workflow

Direct development on `main` is not allowed by project convention. Every meaningful change must be made on a dedicated branch and merged through a pull request.

Typical branch names:

```text
feature/<short-description>
fix/<short-description>
docs/<short-description>
refactor/<short-description>
release/<version>
```

Full workflow instructions are maintained in [`docs/WORKFLOW.md`](docs/WORKFLOW.md).

## Handoff documentation policy

Every meaningful change must include a Markdown handoff under `docs/handoffs/` recording:

- purpose and scope
- affected files
- design decisions
- implementation summary
- validation performed
- known limitations
- follow-up work
- related branch, commit, and pull request

Every new handoff must also be registered in [`docs/HANDOFF_INDEX.md`](docs/HANDOFF_INDEX.md). Use [`docs/HANDOFF_TEMPLATE.md`](docs/HANDOFF_TEMPLATE.md) as the starting structure.

## Compilation

The standard report template uses `biblatex` with Biber:

```bash
latexmk -pdf main.tex
```

The portfolio report template uses `biblatex` with BibTeX in the validated local workflow:

```powershell
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

Consult each template's README before compiling.

## Versioning

Repository changes are summarized in [`CHANGELOG.md`](CHANGELOG.md). Stable milestones should be tagged using semantic versioning:

```text
vMAJOR.MINOR.PATCH
```

## License

This repository is released under the [MIT License](LICENSE). You may use, copy, modify, merge, publish, distribute, sublicense, and sell copies of the repository materials, provided that the copyright notice and license text are retained in copies or substantial portions.

The MIT License applies to the original repository source and documentation. Third-party packages, fonts, trademarks, institutional logos, example references, and venue-specific assets remain subject to their own terms.

## Publication and reuse note

Included report content is illustrative and demonstrates template capabilities. Replace all sample text, figures, results, names, logos, evidence claims, and references before academic or professional publication. Public use of a template does not imply endorsement by an employer, university, client, software vendor, or other institution.
