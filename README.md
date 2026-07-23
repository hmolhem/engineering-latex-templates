# Engineering LaTeX Templates

Reusable LaTeX templates for engineering reports, technical presentations, research papers, and
project documentation.

## Templates

- **`report-template/`** — standardized modular engineering report derived from the latest 5G
  phased-array report structure; fully populated with fictional examples demonstrating the
  available environments, figures, tables, code styles, appendices, and references.
- **`presentation-template/`** — reusable Beamer starting point.
- **`ieee-paper-template/`** — compact IEEE-style paper starting point.

## Recommended workflow

1. Create a new repository from this template repository.
2. Keep the setup files stable unless a formatting change is intentional.
3. Edit project metadata in `main.tex`.
4. Manage report sections through `content/00_report_body.tex`.
5. Compile locally with `latexmk -pdf main.tex` or upload the folder to Overleaf.

The report example uses invented technical content and placeholder branding. Replace all examples
with verified project-specific material before publication or submission.
