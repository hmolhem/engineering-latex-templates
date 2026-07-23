# Standard Engineering Report Template

This report template is derived from the modular structure used in Hossein Molhem's final 5G
phased-array report. It preserves the standardized cover typography, configurable page headers,
front matter, content-menu workflow, reusable environments, code styles, appendices, and
bibliography system.

## Quick start

1. Edit the metadata block at the top of `main.tex`.
2. Replace `frontmatter/objective.tex` and `frontmatter/abstract.tex`.
3. Add, remove, or reorder report sections in `content/00_report_body.tex`.
4. Add, remove, or reorder appendices in `appendices/00_appendices.tex`.
5. Replace the fictional sample material with project-specific analysis and evidence.

## Optional cover logo

The logo is controlled in `main.tex`:

```latex
% Comment the next line to remove the logo from the cover page.
\newcommand{\reportlogo}{figures/logo-placeholder.png}
```

Replace the placeholder file with an institutional or company logo that you are authorized to use.

## Headers

Every non-cover page uses values defined in `main.tex`:

```latex
\newcommand{\headerleft}{\courseshorttitle}
\newcommand{\headerright}{\reportshorttitle}
```

The `fancy` and `plain` page styles are both defined, so chapter openings, the table of contents,
lists, appendices, and references retain the same header.

## Compilation

Use `latexmk`:

```bash
latexmk -pdf main.tex
```

The template uses `biblatex` with the Biber backend. A manual sequence is:

```bash
pdflatex main.tex
biber main
pdflatex main.tex
pdflatex main.tex
```

## Content organization

```text
main.tex
├── frontmatter/
│   ├── titlepage.tex
│   ├── objective.tex
│   └── abstract.tex
├── content/
│   └── 00_report_body.tex      # single menu called by main.tex
├── appendices/
│   └── 00_appendices.tex       # appendix menu called by main.tex
├── setup/
├── codes/
├── figures/
└── references.bib
```
