# LinkedIn Carousel System

This package contains a reusable LaTeX theme and the first completed carousel for the `engineering-latex-templates` repository.

## Output format

- page ratio: 4:5
- physical page size: 216 mm x 270 mm
- pages: 8
- output: vector, multi-page PDF
- intended platform: LinkedIn document post

## Structure

```text
template/
  carousel-theme.sty
engineering-latex-templates/
  main.tex
  carousel-theme.sty
  engineering-latex-templates-carousel.pdf
```

Compile with:

```bash
pdflatex main.tex
pdflatex main.tex
```

The theme is reusable for future RF, antenna, CST, radar, MIMO, and engineering-documentation carousels.
