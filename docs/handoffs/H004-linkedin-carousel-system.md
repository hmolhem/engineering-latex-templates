# Handoff: LinkedIn Carousel System

## Metadata

| Field | Value |
|---|---|
| Date | `2026-07-23` |
| Author | `Hossein Molhem and ChatGPT` |
| Repository | `hmolhem/engineering-latex-templates` |
| Branch | `feature/linkedin-carousel-system` |
| Pull request | `Pending` |
| Related version | `Unreleased after v0.2.0` |
| Status | `Ready for review` |

## Purpose

Add a reusable LaTeX system for producing LinkedIn document carousels and use it to create an eight-page public showcase for the `engineering-latex-templates` repository.

## Scope

Included:

- reusable 4:5 portrait carousel theme
- minimal reusable starter document
- completed eight-page repository showcase
- real rendered previews from the report, presentation, and IEEE paper templates
- curated multi-page PDF for LinkedIn publication
- narrow `.gitignore` exception for the curated carousel PDF
- carousel README, changelog entry, and handoff-index update

Excluded:

- automated LinkedIn publishing
- analytics collection after publication
- alternate social-media aspect ratios
- automated preview extraction or cropping
- GitHub Actions compilation

## Affected files and directories

```text
.gitignore
CHANGELOG.md
docs/HANDOFF_INDEX.md
docs/handoffs/H004-linkedin-carousel-system.md
social-media/linkedin-carousel/README.md
social-media/linkedin-carousel/template/carousel-theme.sty
social-media/linkedin-carousel/template/main-template.tex
social-media/linkedin-carousel/engineering-latex-templates-carousel/carousel-theme.sty
social-media/linkedin-carousel/engineering-latex-templates-carousel/main.tex
social-media/linkedin-carousel/engineering-latex-templates-carousel/engineering-latex-templates-carousel.pdf
```

## Implementation summary

The implementation introduces a fixed-layout LaTeX carousel system with a 216 mm by 270 mm page size, equivalent to a 4:5 portrait ratio suitable for LinkedIn document posts. The generic template provides shared colors, typography, cards, pills, headings, footers, and slide numbering.

The completed repository showcase contains eight pages covering the documentation problem, repository architecture, real report previews, real presentation previews, the enhanced IEEE paper preview, the controlled Git workflow, and a repository call to action.

## Design decisions

### Preserve a reusable system and a completed example

The generic starter is separated from the repository-specific carousel so future technical projects can reuse the same visual language without copying the full promotional content.

### Import existing curated previews

The carousel source references the three existing template-preview PDFs instead of duplicating them. This preserves a single source of truth for rendered template examples.

### Keep all presentation previews at the same scale

The three presentation images use identical 16:9 dimensions. The title slide is centered in the first row, while the system-model and results slides share the second row. This avoids misleading visual rescaling between examples.

### Commit only the publication artifact

Ordinary LaTeX build files remain ignored. A narrow `.gitignore` exception allows only the named final carousel PDF to be version-controlled.

## Validation

```text
The repository owner reviewed and approved the eight-page rendered carousel.
The final page ratio is 4:5 and all pages use the same dimensions.
The report page displays real cover, technical-content, and code previews.
The presentation page displays three real 16:9 slides at equal scale.
The IEEE page displays both real rendered paper pages.
No intentional clipping, stretching, or overlapping was observed in the approved PDF.
The final curated PDF is present at the documented repository path.
The LaTeX source references existing preview PDFs at valid relative paths.
The branch is ahead of main without divergence.
```

## Known limitations

- PDF compilation is manual.
- The source depends on the current relative locations and page counts of the three curated template previews.
- LinkedIn rendering may apply its own compression or thumbnail treatment.
- The carousel has not yet been tested with post-publication analytics.
- Only the 4:5 LinkedIn document-post format is currently supported.

## Follow-up work

- [ ] Publish the carousel as a LinkedIn document post.
- [ ] Write and review the accompanying LinkedIn caption.
- [ ] Record baseline impressions, document views, profile views, and inbound engagement.
- [ ] Reuse the system for wearable-antenna, patch-antenna, array, radar, and MIMO project carousels.
- [ ] Consider automated PDF compilation and visual regression checks.

## Recovery and rollback

Rollback can be performed by reverting the eventual merge commit. The carousel system is isolated under `social-media/linkedin-carousel/`; reverting it does not modify the report, presentation, or IEEE template sources. The three existing curated preview PDFs remain independent source artifacts.

## Related references

- Carousel documentation: `social-media/linkedin-carousel/README.md`
- Handoff index: `docs/HANDOFF_INDEX.md`
- Workflow: `docs/WORKFLOW.md`
- Changelog: `CHANGELOG.md`
