# Handoff: Template PDF Previews

## Metadata

| Field | Value |
|---|---|
| Date | `2026-07-22` |
| Author | `Hossein Molhem and ChatGPT` |
| Repository | `hmolhem/engineering-latex-templates` |
| Branch | `docs/add-template-pdf-previews` |
| Pull request | `Pending` |
| Related version | `Unreleased after v0.2.0` |
| Status | `Ready for review` |

## Purpose

Publish one curated PDF preview for each LaTeX template so users can inspect the rendered output before copying or compiling the source.

## Scope

Included:

- engineering report PDF preview
- technical presentation PDF preview
- IEEE paper PDF preview
- explicit `.gitignore` exceptions for curated preview PDFs
- README links to the published previews
- changelog and handoff-index updates

Excluded:

- changes to LaTeX source or rendering behavior
- regeneration of the preview PDFs inside GitHub Actions
- release tagging

## Affected files and directories

```text
.gitignore
README.md
CHANGELOG.md
docs/HANDOFF_INDEX.md
docs/handoffs/H002-template-pdf-previews.md
report-template/README.md
report-template/preview/engineering-report-template-preview.pdf
presentation-template/README.md
presentation-template/preview/technical-presentation-template-preview.pdf
ieee-paper-template/README.md
ieee-paper-template/preview/ieee-paper-template-preview.pdf
```

## Implementation summary

Each template now contains a dedicated `preview/` directory with one intentionally version-controlled PDF exported from the corresponding Overleaf project. The repository continues to ignore generated PDFs by default, while `.gitignore` contains narrow exceptions for the three curated preview files.

README documentation provides direct relative links to each preview so the files remain accessible in private and public repository views without requiring raw external URLs.

## Design decisions

### Curated previews remain close to their templates

Each PDF is stored inside the relevant template folder rather than in a central root-level preview directory. This keeps source, documentation, and rendered reference output together.

### Generated PDFs remain ignored by default

The general `*.pdf` rule remains active to prevent accidental commits of build outputs. Only the three explicitly named preview PDFs are exempted.

### Preview files are reference artifacts

The previews demonstrate current template appearance. They are not authoritative substitutes for compiling the source and should be refreshed whenever a future change materially affects rendered output.

## Validation

```text
Confirmed branch contains three PDF files.
Confirmed filenames and paths match README links.
Confirmed `.gitignore` exceptions are limited to curated previews.
Confirmed no LaTeX source files were modified in the user's PDF commit.
Visual PDF content was exported and reviewed by the repository owner from Overleaf.
```

## Known limitations

- Preview generation is currently manual.
- GitHub Actions does not yet compile or compare template output automatically.
- A preview can become stale if rendering changes are merged without refreshing the corresponding PDF.

## Follow-up work

- [ ] Add automated compilation checks for all templates.
- [ ] Define a review rule requiring preview refresh when rendered output changes.
- [ ] Consider release artifacts after the first stable `v1.0.0` milestone.

## Recovery and rollback

The change can be reverted by removing the three preview files, their README links, the `.gitignore` exceptions, and the related changelog/index entries. No LaTeX source behavior depends on the preview PDFs.

## Related references

- Root documentation: `README.md`
- Handoff index: `docs/HANDOFF_INDEX.md`
- Workflow: `docs/WORKFLOW.md`
- Changelog: `CHANGELOG.md`
