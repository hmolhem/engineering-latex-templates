# Public Engineering Portfolio Report Template

This template is a standalone system for turning an engineering project into a public, recruiter-readable, technically traceable portfolio report. It is intentionally separate from `report-template/`, which is designed for academic, industrial, and consulting reports that may retain course, institutional, client, or supervisor metadata.

## Portfolio-specific architecture

The template adds permanent support for:

- a public cover without student ID, course number, institution, or grading data
- `Portfolio Context and Evidence` before the abstract and objective
- explicit analytical, simulated, and measured evidence classification
- public-edition and non-endorsement statements
- a dedicated numerical-reliability and limitations discussion
- an engineering verification matrix linking claims to evidence
- reproducible calculation scripts and text-based verification records
- clear disclosure when native simulation files are excluded

## Normal front-matter order

```text
Public cover
Portfolio Context and Evidence
Abstract
Project Objective
Table of Contents
List of Figures
List of Tables
```

## Quick start

1. Edit `setup/00_metadata.tex`.
2. Replace `frontmatter/portfolio_context.tex` only when the default configurable language is insufficient.
3. Replace the abstract and objective.
4. Register chapters in `content/00_report_body.tex`.
5. Register appendices in `appendices/00_appendices.tex`.
6. Store public support files in `codes/` and `verification_records/`.
7. Compile and inspect every page before publication.

## Build

```bash
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

The template uses `biblatex` with Biber.

## Evidence rule

Every significant public claim should be classified as analytical, simulated, or measured and should identify its source location and limitations. Simulation must never be described as measurement.

## Relationship to the standard report template

`portfolio-report-template/` and `report-template/` share a general modular LaTeX philosophy, but they are maintained as separate products. Changes in one should not silently alter the publication behavior of the other.
