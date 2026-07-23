# Standard Engineering Report Template

This modular report template is derived from the structure used in Hossein Molhem's final 5G phased-array report. It preserves the preferred cover typography, configurable headers, separate front matter, centralized content menus, reusable engineering environments, code styles, appendices, and bibliography system.

## Directory structure

```text
report-template/
├── README.md
├── main.tex
├── references.bib
├── setup/
│   ├── 01_packages.tex
│   ├── 02_layout.tex
│   ├── 03_math_macros.tex
│   ├── 04_code_styles.tex
│   ├── 05_environments.tex
│   ├── 06_advanced_math.tex
│   ├── 07_DSP_Radar_macros.tex
│   └── 08_theme.tex
├── frontmatter/
│   ├── titlepage.tex
│   ├── objective.tex
│   └── abstract.tex
├── content/
│   ├── 00_report_body.tex
│   └── section files
├── appendices/
│   ├── 00_appendices.tex
│   └── appendix files
├── figures/
├── codes/
└── generated build files ignored by Git
```

## Architecture

`main.tex` is the project control file. It defines metadata, loads setup modules, includes front matter, and calls only the centralized body and appendix menus.

```text
main.tex
├── setup/*.tex
├── frontmatter/titlepage.tex
├── frontmatter/objective.tex
├── frontmatter/abstract.tex
├── content/00_report_body.tex
├── appendices/00_appendices.tex
└── references.bib
```

This design keeps the main file stable while allowing sections and appendices to be added, removed, or reordered through dedicated menu files.

## Quick start

1. Edit the metadata block at the top of `main.tex`.
2. Replace the content of `frontmatter/objective.tex`.
3. Replace the content of `frontmatter/abstract.tex`.
4. Add, remove, or reorder sections in `content/00_report_body.tex`.
5. Add, remove, or reorder appendices in `appendices/00_appendices.tex`.
6. Replace fictional figures, code, tables, citations, and engineering results.
7. Compile and inspect the complete PDF.

## Metadata and headers

The report title, author, institution, course, supervisor, date, and page headers are controlled from `main.tex`.

Typical header configuration:

```latex
\newcommand{\headerleft}{\courseshorttitle}
\newcommand{\headerright}{\reportshorttitle}
```

Every non-cover page uses these values. Both `fancy` and `plain` page styles are configured so that chapter openings, the table of contents, lists, appendices, and references retain consistent headers.

## Optional cover logo

The cover logo is controlled from `main.tex`:

```latex
% Comment the next line to remove the logo from the cover page.
\newcommand{\reportlogo}{figures/logo-placeholder.png}
```

To use a logo:

1. Place the authorized image in `figures/`.
2. Update the path assigned to `\reportlogo`.
3. Compile and verify its size and alignment.

To remove the logo, comment out the command. Do not publish institutional or corporate logos without authorization.

## Front matter

The `frontmatter/` directory contains independent components:

- `titlepage.tex` — cover layout and typography
- `objective.tex` — project objective
- `abstract.tex` — technical abstract

The objective is intentionally separate from the abstract because the two serve different functions in engineering project reports.

## Content menu

The report body is controlled from:

```text
content/00_report_body.tex
```

Example:

```latex
\input{content/01_introduction}
\input{content/02_theory}
\input{content/03_methodology}
\input{content/04_results}
\input{content/05_discussion}
\input{content/06_conclusion}
```

Commenting or reordering these lines changes the report structure without modifying `main.tex`.

## Appendices

Appendices are controlled from:

```text
appendices/00_appendices.tex
```

Example:

```latex
\input{appendices/appendix_a_source_code}
\input{appendices/appendix_b_console_output}
```

Appendix support may be disabled by commenting the corresponding appendix call in `main.tex` or the menu entries, depending on the project structure.

## Demonstrated capabilities

The fictional sample report is designed to exercise the template rather than provide authoritative engineering results. It demonstrates:

- objective and abstract pages
- equations, aligned derivations, vectors, and matrices
- theorem, lemma, definition, example, and problem environments
- custom objective and engineering callout environments
- figures and subfigures
- standard tables and long tables
- TikZ diagrams
- Python, MATLAB, Vitis HLS, PowerShell, and console listings
- missing-figure placeholders
- appendices
- IEEE-style citations and bibliography

## Adding a new section

Create a file such as:

```text
content/08_validation.tex
```

Then register it in `content/00_report_body.tex`:

```latex
\input{content/08_validation}
```

## Adding code

Place source files under `codes/` and include them using the appropriate listing style defined in `setup/04_code_styles.tex`. Keep reusable style definitions in `setup/`; keep project-specific source code in `codes/`.

## Compilation

Preferred command:

```bash
latexmk -pdf main.tex
```

The template uses `biblatex` with Biber. Manual sequence:

```bash
pdflatex main.tex
biber main
pdflatex main.tex
pdflatex main.tex
```

Clean generated files:

```bash
latexmk -c
```

## Validation checklist

- [ ] Cover title and metadata are correct
- [ ] Logo is present only when authorized and needed
- [ ] Objective and abstract are project-specific
- [ ] Headers display the intended short titles
- [ ] Table of contents and lists are current
- [ ] All figures and tables are referenced
- [ ] All citations resolve
- [ ] No placeholder content remains
- [ ] Appendix menu matches included files
- [ ] No confidential or proprietary material is present
- [ ] Final PDF has been visually inspected page by page

## Maintenance rule

Changes to the template itself must follow the repository branch, pull-request, changelog, and handoff workflow documented in [`../docs/WORKFLOW.md`](../docs/WORKFLOW.md).
