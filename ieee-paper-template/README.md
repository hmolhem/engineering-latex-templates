# Enhanced IEEE Paper Template

A reusable IEEE conference-paper starter built with `IEEEtran`. The included example is deliberately complete enough to demonstrate a realistic technical-paper workflow while remaining clearly identified as illustrative template content.

The official template, page limits, anonymity rules, reference requirements, copyright instructions, and PDF-compliance rules of the target venue always take precedence over this repository.

## Rendered preview

[Open the IEEE paper template preview](preview/ieee-paper-template-preview.pdf)

## Directory structure

```text
ieee-paper-template/
├── README.md
├── main.tex
├── references.bib
├── figures/
│   └── beam_patterns.pdf
└── preview/
    └── ieee-paper-template-preview.pdf
```

## Demonstrated capabilities

The sample paper demonstrates:

- IEEE conference metadata, author block, abstract, and keywords
- conventional and MVDR beamforming as fictional technical content
- numbered and cross-referenced equations
- citations in the body and an external BibTeX database
- one TikZ processing-flow diagram
- one external vector PDF figure
- two compact publication-style tables
- reproducible synthetic parameters and quantitative results
- discussion of assumptions, limitations, and evidence

The sample is not presented as an original research contribution. Replace its metadata, technical claims, numerical results, figures, and references before any real submission.

## Recommended workflow

1. Identify the exact IEEE conference or journal.
2. Download and review the current official author instructions.
3. Confirm whether the submission is single-blind, double-blind, or non-anonymous.
4. Replace the title, authors, affiliations, abstract, and keywords in `main.tex`.
5. Replace the illustrative beamforming example with verified project-specific work.
6. Add and verify all bibliographic records in `references.bib`.
7. Replace the sample figure under `figures/` with publication-ready evidence.
8. Compile and verify page count, margins, fonts, references, figure readability, and PDF compliance.

## Compilation

The `IEEEtran` class must be installed in the TeX distribution.

Preferred command:

```bash
latexmk -pdf main.tex
```

Manual sequence:

```bash
pdflatex main.tex
bibtex main
pdflatex main.tex
pdflatex main.tex
```

Clean generated files:

```bash
latexmk -c
```

Overleaf normally detects the BibTeX workflow from:

```latex
\bibliographystyle{IEEEtran}
\bibliography{references}
```

## Figures and tables

Use vector formats such as PDF when practical. Raster images should have sufficient resolution and readable labels at final column width. Keep captions concise but informative, and reference every figure and table in the body before or near its appearance.

## References

Verify author names, title capitalization, venue, volume, issue, pages, year, and DOI against authoritative publication records. A bibliography entry should support a specific statement or method in the text rather than appearing only in the reference list.

## Submission checklist

- [ ] The current official venue template is being used
- [ ] Author and affiliation rules are satisfied
- [ ] Anonymity requirements are satisfied
- [ ] The contribution is explicit and technically supported
- [ ] Every equation, figure, and table is referenced where appropriate
- [ ] Figures and tables are legible at final size
- [ ] Results are reproducible and supported by evidence
- [ ] References are complete, verified, and cited in the text
- [ ] Page limits and PDF-compliance requirements are satisfied
- [ ] No placeholder or illustrative content remains
- [ ] The final PDF has been inspected page by page

## Maintenance rule

Changes to this shared template must follow the branch, pull-request, changelog, preview-refresh, and handoff workflow documented in [`../docs/WORKFLOW.md`](../docs/WORKFLOW.md).
