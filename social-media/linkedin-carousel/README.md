# LinkedIn Carousel System

This package contains a reusable LaTeX theme and the first completed LinkedIn document carousel for the `engineering-latex-templates` repository.

## Output format

- page ratio: 4:5
- physical page size: 216 mm x 270 mm
- pages in the repository showcase: 8
- output: vector, multi-page PDF
- intended platform: LinkedIn document post

## Structure

```text
template/
  carousel-theme.sty
  main-template.tex

engineering-latex-templates-carousel/
  carousel-theme.sty
  main.tex
  engineering-latex-templates-carousel.pdf
```

The reusable starter lives in `template/`. The completed repository showcase lives in `engineering-latex-templates-carousel/`.

## Compilation

From the completed-carousel directory:

```bash
pdflatex main.tex
pdflatex main.tex
```

The source imports curated previews from:

```text
../../../report-template/preview/engineering-report-template-preview.pdf
../../../presentation-template/preview/technical-presentation-template-preview.pdf
../../../ieee-paper-template/preview/ieee-paper-template-preview.pdf
```

The committed publication artifact is:

```text
engineering-latex-templates-carousel.pdf
```

The generic theme is reusable for future RF, antenna, CST, radar, MIMO, and engineering-documentation carousels.
