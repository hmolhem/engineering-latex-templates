# Changelog

## Unreleased

- Expanded the root README with the complete repository structure, template summaries, compilation instructions, versioning guidance, and publication notes.
- Added a mandatory branch-and-pull-request development workflow.
- Added a reusable Markdown handoff template.
- Added a chronological handoff index and the first repository handoff record.
- Expanded the README files for the report, presentation, and IEEE paper templates.
- Added a pull-request checklist template for consistent reviews.
- Added curated PDF previews for the report, presentation, and IEEE paper templates.
- Added narrow `.gitignore` exceptions so only the named preview PDFs are version-controlled.
- Added Handoff `H002` documenting preview placement, maintenance, and rollback.

## v0.2.0 — Standardized 5G-report architecture

- Rebuilt the report template from the latest standardized 5G project report.
- Restored `frontmatter/objective.tex`.
- Restored consistent configurable headers on all non-cover pages.
- Preserved the preferred cover typography and spacing.
- Added an optional cover-logo mechanism controlled from `main.tex`.
- Restored appendix support through `appendices/00_appendices.tex`.
- Restored the single report-body menu at `content/00_report_body.tex`.
- Added a fully populated fictional report demonstrating custom environments, equations, figures,
  subfigures, tables, code listings, missing-figure placeholders, appendices, and references.

## v0.1.0 — Initial repository structure

- Added report, presentation, and IEEE paper template folders.
