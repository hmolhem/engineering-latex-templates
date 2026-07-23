# Engineering LaTeX Templates

Reusable LaTeX templates for engineering reports, technical presentations, research papers, and project documentation.

This repository is intended to serve as a stable, version-controlled documentation system for recurring academic, research, industrial, and consulting work. The report template is based on the standardized architecture used in the latest 5G phased-array project report.

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

A modular report system with:

- configurable metadata in `main.tex`
- optional cover logo
- standardized title-page typography
- configurable headers on all non-cover pages
- separate objective and abstract files
- a single content menu in `content/00_report_body.tex`
- a single appendix menu in `appendices/00_appendices.tex`
- reusable theorem, definition, example, problem, code, matrix, and engineering environments
- bibliography support through `biblatex` and Biber

See [`report-template/README.md`](report-template/README.md).

### Technical presentation

`presentation-template/`

A reusable Beamer template with section-based organization and speaker-note support.

See [`presentation-template/README.md`](presentation-template/README.md).

### IEEE paper starter

`ieee-paper-template/`

A lightweight IEEE-style starting point for conference or journal manuscripts. The official template and author instructions of the target venue always take precedence.

See [`ieee-paper-template/README.md`](ieee-paper-template/README.md).

### LinkedIn carousel system

`social-media/linkedin-carousel/`

A reusable 4:5 portrait LaTeX system for LinkedIn document posts, including the completed repository-showcase carousel and its curated multi-page PDF.

See [`social-media/linkedin-carousel/README.md`](social-media/linkedin-carousel/README.md).

## Rendered PDF previews

The following curated PDFs show the current rendered appearance of each template:

- [Engineering report template preview](report-template/preview/engineering-report-template-preview.pdf)
- [Technical presentation template preview](presentation-template/preview/technical-presentation-template-preview.pdf)
- [IEEE paper template preview](ieee-paper-template/preview/ieee-paper-template-preview.pdf)
- [LinkedIn repository-showcase carousel](social-media/linkedin-carousel/engineering-latex-templates-carousel/engineering-latex-templates-carousel.pdf)

Generated PDFs remain ignored by default. These explicitly named publication artifacts are intentionally version-controlled and should be refreshed whenever a future source change materially affects rendered output.

## Recommended usage

1. Create a new repository from this template repository, or copy only the required template folder.
2. Edit project metadata in `main.tex`.
3. Replace fictional example content with verified project-specific material.
4. Keep shared setup files stable unless a formatting change is intentional.
5. Compile locally with `latexmk` or upload the project folder to Overleaf.

Example:

```bash
git clone https://github.com/hmolhem/engineering-latex-templates.git
cd engineering-latex-templates/report-template
latexmk -pdf main.tex
```

## Development workflow

Direct development on `main` is not allowed by project convention. Every change must be made on a dedicated branch and merged through a pull request.

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

Every meaningful change must include a Markdown handoff file under:

```text
docs/handoffs/
```

The handoff must record:

- purpose and scope
- affected files
- design decisions
- implementation summary
- validation performed
- known limitations
- follow-up work
- related branch, commit, and pull request

Every new handoff must also be registered in [`docs/HANDOFF_INDEX.md`](docs/HANDOFF_INDEX.md). Use [`docs/HANDOFF_TEMPLATE.md`](docs/HANDOFF_TEMPLATE.md) as the required starting structure.

## Compilation

The standard report template uses `biblatex` with Biber:

```bash
latexmk -pdf main.tex
```

Manual sequence:

```bash
pdflatex main.tex
biber main
pdflatex main.tex
pdflatex main.tex
```

## Versioning

Repository changes are summarized in [`CHANGELOG.md`](CHANGELOG.md). Stable milestones should be tagged using semantic versioning:

```text
vMAJOR.MINOR.PATCH
```

Examples:

```text
v0.2.0
v1.0.0
v1.1.0
```

## License

This repository is released under the [MIT License](LICENSE). You may use, copy, modify, merge, publish, distribute, sublicense, and sell copies of the repository materials, provided that the copyright notice and license text are retained in copies or substantial portions.

The MIT License applies to the original repository source and documentation. Third-party packages, fonts, trademarks, institutional logos, example references, and venue-specific assets remain subject to their own terms.

## Publication and reuse note

The included report content is fictional and demonstrates template capabilities only. Replace all example text, figures, results, institutional names, logos, and references before academic or professional submission.
