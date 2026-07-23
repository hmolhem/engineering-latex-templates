# Technical Presentation Template

A reusable Beamer template for technical lectures, engineering project presentations, research talks, and design reviews.

## Directory structure

```text
presentation-template/
├── README.md
├── main.tex
├── sections/
├── figures/
└── speaker-notes/
```

## Recommended organization

Keep presentation metadata and global Beamer settings in `main.tex`. Place substantial slide groups in independent files under `sections/` and include them from the main file.

Example:

```latex
\input{sections/01_introduction}
\input{sections/02_methodology}
\input{sections/03_results}
\input{sections/04_conclusion}
```

Store reusable images and diagrams under `figures/`. Keep extended speaking scripts or preparation notes under `speaker-notes/` when they should not be embedded directly in the slide source.

## Speaker notes

Speaker notes may be added inside frames using:

```latex
\note{
Explain the engineering motivation before introducing the equation.
}
```

For a normal audience copy:

```latex
\setbeameroption{hide notes}
```

For a notes copy, use the desired Beamer notes mode supported by the project configuration, such as:

```latex
\setbeameroption{show notes}
```

Always compile and inspect both the audience and presenter versions when notes are required.

## Adding a new section

Create a section file:

```text
sections/05_future_work.tex
```

Then include it from `main.tex`:

```latex
\input{sections/05_future_work}
```

## Compilation

```bash
latexmk -pdf main.tex
```

Clean generated files with:

```bash
latexmk -c
```

## Presentation checklist

- [ ] Title, author, institution, and date are correct
- [ ] Slide sequence matches the talk narrative
- [ ] Figures remain readable when projected
- [ ] Equations use consistent notation
- [ ] Each slide has one clear purpose
- [ ] Citations and image attributions are present where required
- [ ] Speaker notes are hidden in the audience copy
- [ ] Final PDF has been visually inspected

## Maintenance rule

Changes to the shared presentation template must follow the branch, pull-request, changelog, and handoff workflow documented in [`../docs/WORKFLOW.md`](../docs/WORKFLOW.md).
