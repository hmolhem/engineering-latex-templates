# IEEE Paper Starter

A lightweight LaTeX starting point for IEEE-style conference and journal manuscripts.

The official template, page limits, reference style, anonymity rules, copyright requirements, and author instructions of the target venue always take precedence over this repository.

## Directory structure

```text
ieee-paper-template/
├── README.md
├── main.tex
├── references.bib
└── figures/
```

## Recommended workflow

1. Identify the exact IEEE conference or journal.
2. Download and review the current official author instructions.
3. Confirm whether the submission is single-blind, double-blind, or non-anonymous.
4. Update title, authors, affiliations, abstract, and keywords in `main.tex`.
5. Organize sections around the contribution and validation evidence.
6. Add references to `references.bib`.
7. Add publication-ready figures under `figures/`.
8. Compile and verify page count, margins, fonts, references, and PDF compliance.

## Suggested manuscript structure

```text
Abstract
Index Terms
I. Introduction
II. Related Work or Background
III. Methodology
IV. Experimental or Simulation Setup
V. Results
VI. Discussion
VII. Conclusion
Acknowledgment
References
```

The exact structure should follow the technical contribution rather than being applied mechanically.

## Figures

Use vector formats such as PDF when practical. Raster images should have sufficient resolution for publication and readable labels at final column width.

Example:

```latex
\begin{figure}[t]
    \centering
    \includegraphics[width=\columnwidth]{figures/example.pdf}
    \caption{Concise caption that explains the evidence shown.}
    \label{fig:example}
\end{figure}
```

## References

Keep bibliographic entries in `references.bib`. Verify author names, title capitalization, venue, volume, issue, pages, year, and DOI against authoritative publication records.

## Compilation

The `IEEEtran` class must be installed in the TeX distribution.

```bash
latexmk -pdf main.tex
```

Clean generated files:

```bash
latexmk -c
```

## Submission checklist

- [ ] Correct official IEEE template is being used
- [ ] Author and affiliation rules are satisfied
- [ ] Anonymity requirements are satisfied
- [ ] Contribution is explicit in the introduction
- [ ] Figures and tables are legible at final size
- [ ] Results are reproducible and technically supported
- [ ] References are complete and verified
- [ ] Page limit is satisfied
- [ ] No placeholder text remains
- [ ] PDF compliance requirements are satisfied

## Maintenance rule

Changes to this shared starter must follow the branch, pull-request, changelog, and handoff workflow documented in [`../docs/WORKFLOW.md`](../docs/WORKFLOW.md).
