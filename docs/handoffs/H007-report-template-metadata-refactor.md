# Handoff: Report Template Metadata Refactor

## Metadata

| Field | Value |
|---|---|
| Date | `2026-07-25` |
| Author | `Hossein Molhem and ChatGPT` |
| Repository | `hmolhem/engineering-latex-templates` |
| Branch | `refactor/report-template-metadata` |
| Pull request | `Pending` |
| Related version | `Unreleased after v0.2.0` |
| Status | `Ready for Overleaf validation` |

## Purpose

Make the standard engineering report template easier and safer to reuse by separating user-editable report metadata from document assembly and title-page layout.

## Scope

Included:

- creation of `report-template/setup/00_metadata.tex`
- migration of course, project, author, institution, header, logo, and PDF-property fields out of `main.tex`
- conversion of `main.tex` into a stable, well-commented document controller
- synchronization of `frontmatter/titlepage.tex` with the centralized metadata interface
- explicit visibility switches for the logo, student ID, supervisor, and semester
- documentation updates for the revised workflow
- handoff, index, and changelog updates
- preparation of an Overleaf-ready ZIP for owner validation

Excluded:

- redesign of the report body or sample engineering content
- changes to mathematical macros, code styles, reusable environments, or bibliography style
- replacement of the existing authorized/example logo asset
- refresh of the committed preview PDF before owner approval
- automated compilation or visual-regression CI

## Affected files and directories

```text
report-template/setup/00_metadata.tex
report-template/main.tex
report-template/frontmatter/titlepage.tex
report-template/README.md
CHANGELOG.md
docs/HANDOFF_INDEX.md
docs/handoffs/H007-report-template-metadata-refactor.md
```

## Implementation summary

A dedicated metadata module now serves as the primary report configuration surface. It contains:

- course or project context
- institution and department
- assignment and project titles
- formatted and plain report titles
- author, student ID, supervisor, semester, and submission date
- running-header text
- optional-logo path and width
- PDF subject and keyword fields
- Boolean visibility switches for optional title-page elements

`main.tex` now loads `setup/00_metadata.tex` before the shared setup modules and focuses only on package assembly, PDF metadata, front matter, body menus, appendices, and bibliography.

`frontmatter/titlepage.tex` now consumes the centralized metadata without duplicating user-editable values. Its comments direct users to the metadata file and explain title-page behavior.

## Design decisions

### Centralize user-editable values

The metadata file is numbered `00` so it appears first in the setup directory and is loaded before all other setup modules. This makes the intended editing sequence visible in both the filesystem and `main.tex`.

### Keep formatted and plain titles separate

`\reporttitle` supports deliberate cover-page line breaks and typography. `\reporttitleplain` remains free of layout commands so it can be used safely in PDF document properties.

### Use explicit visibility switches

The template uses readable Boolean switches:

```latex
\showreportlogotrue
\showstudentidtrue
\showsupervisortrue
\showsemestertrue
```

Changing `true` to `false` suppresses an optional element without deleting metadata or commenting structural code.

### Keep a visible missing-logo warning

When the logo is enabled but the configured file is absent, the cover shows a diagnostic box. This prevents a user from unknowingly submitting a report with a missing required logo.

### Preserve title-page layout separation

The metadata file defines content, while `frontmatter/titlepage.tex` defines presentation. This reduces duplication and makes future layout revisions less likely to overwrite project-specific information.

## User-facing behavior

For a new report, the normal workflow is now:

1. Open `setup/00_metadata.tex`.
2. Replace the fictional project, institution, author, and submission fields.
3. Set optional title-page switches to `true` or `false`.
4. Replace `frontmatter/objective.tex` and `frontmatter/abstract.tex`.
5. Register body sections and appendices through their menu files.
6. Compile `main.tex`.

Most users should not need to edit `main.tex` or `frontmatter/titlepage.tex`.

## Validation

```text
Repository branch: refactor/report-template-metadata
Structural review: completed
Metadata duplication review: completed
Title-page variable trace: completed
Logo path retained: report-template/figures/logo-placeholder.png
Handoff/index/changelog consistency: completed
Overleaf compilation: pending repository-owner validation
Preview PDF refresh: intentionally deferred until approval
```

The branch preserves the existing document class, setup-module order after metadata, front-matter sequence, body and appendix menus, bibliography database, and logo asset path.

## Known limitations

- Final compilation and rendered-page inspection must be completed in Overleaf by the repository owner.
- PDF strings can still produce warnings if users place complex LaTeX commands in plain metadata fields.
- The title page currently assumes the course, institution, and department rows are present.
- The committed preview PDF remains unchanged until the source revision is approved.

## Follow-up work

- [ ] Upload the provided ZIP to Overleaf.
- [ ] Compile with pdfLaTeX and Biber.
- [ ] Inspect the cover, headers, PDF properties, objective, abstract, lists, body, appendices, and references.
- [ ] Test optional switches in both `true` and `false` states.
- [ ] Refresh the curated report preview PDF after approval.
- [ ] Commit final validation corrections, if any.
- [ ] Open and merge the pull request.
- [ ] Close H007 with the pull-request number and merge commit.

## Recovery and rollback

Revert the eventual H007 merge commit to restore metadata definitions inside `main.tex` and the earlier title-page behavior without rewriting repository history.

## Related references

- Root documentation: `README.md`
- Template documentation: `report-template/README.md`
- Metadata file: `report-template/setup/00_metadata.tex`
- Main controller: `report-template/main.tex`
- Title page: `report-template/frontmatter/titlepage.tex`
- Changelog entry: `CHANGELOG.md`
- Related commit: `Pending final validation commit`
