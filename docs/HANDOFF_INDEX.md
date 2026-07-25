# Handoff Index

This index provides a chronological entry point to the repository's implementation history. Add one row for every meaningful change and link it to the corresponding Markdown handoff file.

## Handoffs

| Date | ID | Title | Area | Branch | Status | Handoff |
|---|---|---|---|---|---|---|
| 2026-07-22 | `H001` | Repository documentation and controlled development workflow | Repository-wide | `docs/repository-documentation-and-handoffs` | Merged in PR #1 | [`H001-repository-documentation-and-workflow.md`](handoffs/H001-repository-documentation-and-workflow.md) |
| 2026-07-22 | `H002` | Template PDF previews | All templates | `docs/add-template-pdf-previews` | Merged in PR #2 | [`H002-template-pdf-previews.md`](handoffs/H002-template-pdf-previews.md) |
| 2026-07-23 | `H003` | Enhanced IEEE paper template | IEEE paper template | `feature/enhance-ieee-paper-template` | Merged in PR #3 | [`H003-enhanced-ieee-paper-template.md`](handoffs/H003-enhanced-ieee-paper-template.md) |
| 2026-07-23 | `H004` | LinkedIn carousel system | Social media / repository showcase | `feature/linkedin-carousel-system` | Merged in PR #4 | [`H004-linkedin-carousel-system.md`](handoffs/H004-linkedin-carousel-system.md) |
| 2026-07-23 | `H005` | MIT License | Repository-wide | `chore/add-mit-license` | Merged in PR #5 | [`H005-mit-license.md`](handoffs/H005-mit-license.md) |
| 2026-07-23 | `H006` | Rebuilt LinkedIn carousel PDF | Social media / publication artifact | `fix/rebuild-linkedin-carousel-pdf` | Merged in PR #6 | [`H006-rebuilt-linkedin-carousel-pdf.md`](handoffs/H006-rebuilt-linkedin-carousel-pdf.md) |
| 2026-07-25 | `H007` | Report template metadata refactor | Engineering report template | `refactor/report-template-metadata` | Merged in PR #7 | [`H007-report-template-metadata-refactor.md`](handoffs/H007-report-template-metadata-refactor.md) |

## Naming convention

Handoff filenames use this pattern:

```text
H###-short-descriptive-title.md
```

Examples:

```text
H001-repository-documentation-and-workflow.md
H002-template-pdf-previews.md
H003-enhanced-ieee-paper-template.md
H004-linkedin-carousel-system.md
H005-mit-license.md
H006-rebuilt-linkedin-carousel-pdf.md
H007-report-template-metadata-refactor.md
```

The numeric identifier must remain unique and sequential. A handoff is never deleted after merge; corrections should be recorded in a later handoff and cross-referenced.

## Retrieval guidance

Use this index first when reconstructing prior decisions. Each handoff should identify the related branch, pull request, files, validation steps, known limitations, and follow-up work.
