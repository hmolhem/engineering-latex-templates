# Handoff: Rebuilt LinkedIn Carousel PDF

## Metadata

| Field | Value |
|---|---|
| Date | `2026-07-23` |
| Author | `Hossein Molhem and ChatGPT` |
| Repository | `hmolhem/engineering-latex-templates` |
| Branch | `fix/rebuild-linkedin-carousel-pdf` |
| Pull request | `Pending` |
| Related version | `Unreleased after v0.2.0` |
| Status | `Ready for review` |

## Purpose

Replace the committed LinkedIn carousel PDF after visual review showed that the publication artifact did not match the approved final carousel source and layout.

## Scope

Included:

- replacement of the committed eight-page LinkedIn carousel PDF
- verification of page count, page dimensions, PDF structure, embedded fonts, and rendered appearance
- changelog update
- correction of the Handoff `H005` index status after PR #5 merged
- addition of Handoff `H006`

Excluded:

- changes to `main.tex`
- changes to `carousel-theme.sty`
- redesign of carousel content
- changes to the three source preview PDFs
- automated PDF compilation or visual-regression CI

## Affected files

```text
social-media/linkedin-carousel/engineering-latex-templates-carousel/engineering-latex-templates-carousel.pdf
CHANGELOG.md
docs/HANDOFF_INDEX.md
docs/handoffs/H006-rebuilt-linkedin-carousel-pdf.md
```

## Problem statement

The repository-specific `main.tex` already contained the approved final eight-page carousel, including the final presentation-preview arrangement. However, the version-controlled PDF was visually identified as an older or incorrectly compiled artifact. The source and committed publication artifact were therefore out of synchronization.

## Implementation summary

The stale PDF was replaced with the approved final eight-page render. No LaTeX source changes were required because the existing source already represented the accepted design.

The replacement preserves the documented output path:

```text
social-media/linkedin-carousel/engineering-latex-templates-carousel/engineering-latex-templates-carousel.pdf
```

## Design decisions

### Treat the PDF as a derived publication artifact

The LaTeX source remains the authoritative editable representation. The committed PDF is retained because it is the curated file intended for direct LinkedIn upload and repository preview.

### Avoid unnecessary source changes

The defect was artifact synchronization, not a layout defect in `main.tex`. Editing the source would have obscured the actual root cause and introduced avoidable regression risk.

### Record the artifact checksum

The approved replacement PDF has the following SHA-256 checksum:

```text
2d2d15a9bb3f22fcb296a0b08cc1bfbea88848685b48824c724a6cbf9857b9e5
```

This checksum provides a precise reference for the publication-ready file.

## Validation

```text
Page count: 8
Page dimensions: 612 x 765 pt on all eight pages
Aspect ratio: 4:5 portrait
Encrypted: no
Form fields: 0
Attachments: 0
Annotations: 0
Fonts: embedded
Producer: pdfTeX-1.40.26
SHA-256: 2d2d15a9bb3f22fcb296a0b08cc1bfbea88848685b48824c724a6cbf9857b9e5
```

All eight pages were rendered to PNG at 120 dpi and reviewed together as a contact sheet. The review confirmed:

- the intended cover and closing-page designs
- the repository architecture page
- real report-template previews
- the approved three-slide presentation arrangement with equal 16:9 sizing
- both IEEE-paper preview pages
- the controlled-workflow page
- no visible clipping, overlap, broken glyphs, or unintended blank pages

The branch is ahead of `main` without divergence.

## Known limitations

- PDF compilation remains manual.
- The repository does not yet enforce that committed PDFs match current LaTeX source.
- The source depends on the relative locations and page numbers of the three curated preview PDFs.
- LinkedIn may apply its own document compression or thumbnail rendering.

## Follow-up work

- [ ] Merge the corrective pull request.
- [ ] Pull the merged correction to the local `main` branch.
- [ ] Confirm the local publication PDF checksum after merge.
- [ ] Upload the corrected PDF as the LinkedIn document post.
- [ ] Consider adding automated compilation and visual-regression checks.

## Recovery and rollback

Rollback can be performed by reverting the eventual merge commit. Because the LaTeX source is unchanged, rollback affects only the committed publication artifact and associated documentation.

## Related references

- Earlier carousel handoff: `docs/handoffs/H004-linkedin-carousel-system.md`
- Corrected PDF: `social-media/linkedin-carousel/engineering-latex-templates-carousel/engineering-latex-templates-carousel.pdf`
- Carousel source: `social-media/linkedin-carousel/engineering-latex-templates-carousel/main.tex`
- Handoff index: `docs/HANDOFF_INDEX.md`
- Changelog: `CHANGELOG.md`
