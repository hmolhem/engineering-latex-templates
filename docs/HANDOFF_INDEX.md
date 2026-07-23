# Handoff Index

This index provides a chronological entry point to the repository's implementation history. Add one row for every meaningful change and link it to the corresponding Markdown handoff file.

## Handoffs

| Date | ID | Title | Area | Branch | Status | Handoff |
|---|---|---|---|---|---|---|
| 2026-07-22 | `H001` | Repository documentation and controlled development workflow | Repository-wide | `docs/repository-documentation-and-handoffs` | Merged in PR #1 | [`H001-repository-documentation-and-workflow.md`](handoffs/H001-repository-documentation-and-workflow.md) |
| 2026-07-22 | `H002` | Template PDF previews | All templates | `docs/add-template-pdf-previews` | Ready for review | [`H002-template-pdf-previews.md`](handoffs/H002-template-pdf-previews.md) |

## Naming convention

Handoff filenames use this pattern:

```text
H###-short-descriptive-title.md
```

Examples:

```text
H001-repository-documentation-and-workflow.md
H002-template-pdf-previews.md
H003-presentation-notes-layout.md
```

The numeric identifier must remain unique and sequential. A handoff is never deleted after merge; corrections should be recorded in a later handoff and cross-referenced.

## Retrieval guidance

Use this index first when reconstructing prior decisions. Each handoff should identify the related branch, pull request, files, validation steps, known limitations, and follow-up work.
