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
- Replaced the minimal IEEE starter with a complete illustrative beamforming paper containing equations, figures, tables, citations, BibTeX references, cross-references, and quantitative synthetic results.
- Expanded the IEEE template documentation and added Handoff `H003` for the enhancement workflow.
- Added a reusable LaTeX LinkedIn-carousel system using a 4:5 portrait page format.
- Added an eight-page repository showcase carousel with real rendered previews from the report, presentation, and IEEE paper templates.
- Added a narrow `.gitignore` exception for the curated LinkedIn carousel PDF.
- Added Handoff `H004` documenting the carousel implementation, validation, and maintenance workflow.
- Added the MIT License and documented repository reuse terms.
- Added Handoff `H005` documenting the licensing decision and scope.
- Rebuilt the committed LinkedIn carousel PDF from the approved final source after detecting a stale publication artifact.
- Added Handoff `H006` documenting artifact synchronization, validation, and the approved PDF checksum.
- Added `report-template/setup/00_metadata.tex` as the single user-editable source for report identity, author, institution, headers, optional title-page rows, logo controls, and PDF properties.
- Simplified `report-template/main.tex` into a stable, documented document-assembly controller.
- Synchronized `report-template/frontmatter/titlepage.tex` with the centralized metadata interface and added explicit visibility switches.
- Added Handoff `H007` documenting the report-template metadata refactor and Overleaf validation plan.

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
