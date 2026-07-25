# Engineering LaTeX Templates

Reusable LaTeX templates for engineering reports, public portfolio reports, technical presentations, research papers, and project documentation.

This repository is a stable, version-controlled documentation system for recurring academic, research, industrial, consulting, and professional-portfolio work. Each top-level template is maintained as an independent product with its own purpose, metadata model, documentation, and rendered-artifact policy.

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
├── portfolio-report-template/
├── presentation-template/
├── ieee-paper-template/
├── social-media/
└── examples/
```

## Available templates

### Standard engineering report

`report-template/`

A modular report system for academic, institutional, industrial, and consulting reports. User-editable identity and title-page configuration are centralized in:

```text
report-template/setup/00_metadata.tex
```

The template includes optional identity rows and logo controls, standardized title-page typography, configurable headers, modular front matter and chapters, appendix support, reusable engineering environments, and `biblatex` with Biber.

See [`report-template/README.md`](report-template/README.md).

### Public engineering portfolio report

`portfolio-report-template/`

A standalone public-report system for GitHub, LinkedIn, personal websites, recruiter-facing project repositories, and professional evidence packages. It includes:

- centralized public metadata in `setup/00_metadata.tex`
- a public cover without course, student-ID, grading, or institutional fields
- a Portfolio Context and Evidence page
- analytical, simulated, and measured evidence classification
- numerical-reliability and limitation guidance
- a multipage Engineering Verification Matrix
- calculation, simulation-record, and verification-record directories
- `biblatex` with a BibTeX backend for the validated Windows/MiKTeX workflow

See [`portfolio-report-template/README.md`](portfolio-report-template/README.md).

### Technical presentation

`presentation-template/`

A reusable Beamer template with section-based organization and speaker-note support.

See [`presentation-template/README.md`](presentation-template/README.md).

### IEEE paper starter

`ieee-paper-template/`

A complete illustrative IEEE-style starting point for conference or journal manuscripts. Official venue templates and author instructions always take precedence.

See [`ieee-paper-template/README.md`](ieee-paper-template/README.md).

### LinkedIn carousel system

`social-media/linkedin-carousel/`

A reusable 4:5 portrait LaTeX system for LinkedIn document posts, including a completed repository-showcase carousel.

See [`social-media/linkedin-carousel/README.md`](social-media/linkedin-carousel/README.md).

## Rendered PDF previews

The following curated PDFs are intentionally version-controlled:

- [Engineering report template preview](report-template/preview/engineering-report-template-preview.pdf)
- [Technical presentation template preview](presentation-template/preview/technical-presentation-template-preview.pdf)
- [IEEE paper template preview](ieee-paper-template/preview/ieee-paper-template-preview.pdf)
- [LinkedIn repository-showcase carousel](social-media/linkedin-carousel/engineering-latex-templates-carousel/engineering-latex-templates-carousel.pdf)

The portfolio report was compiled and visually validated during H008. Its curated preview artifact is intentionally deferred until it is committed and independently reviewed as a repository artifact.

Generated PDFs remain ignored by default. Explicitly named, reviewed publication artifacts should be refreshed whenever a material source change affects rendered output.

## Recommended usage

1. Copy the required top-level template folder or create a new repository from this repository.
2. Edit the selected template's metadata file.
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

Full workflow instructions are maintained in [`docs/WORKFLOW.md`](docs/WORKFLOW.md).

## Handoff documentation policy

Every meaningful change must include a Markdown handoff under `docs/handoffs/` and a corresponding entry in [`docs/HANDOFF_INDEX.md`](docs/HANDOFF_INDEX.md). Use [`docs/HANDOFF_TEMPLATE.md`](docs/HANDOFF_TEMPLATE.md) as the starting structure.

## Compilation

The standard report template uses `biblatex` with Biber. The portfolio report template uses `biblatex` with BibTeX in the validated local workflow. Consult each template's README before compiling.

## Versioning

Repository changes are summarized in [`CHANGELOG.md`](CHANGELOG.md). Stable milestones should use semantic versioning.

## License

This repository is released under the [MIT License](LICENSE). Third-party packages, fonts, trademarks, institutional logos, example references, and venue-specific assets remain subject to their own terms.

## Publication and reuse note

Included report content is illustrative. Replace all sample text, figures, results, names, logos, evidence claims, and references before academic or professional publication. Public use does not imply endorsement by an employer, university, client, software vendor, or other institution.
