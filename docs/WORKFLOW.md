# Repository Development Workflow

This document defines the required workflow for maintaining the engineering LaTeX templates repository.

## Core rule

Do not develop directly on `main`.

Every change must follow this sequence:

```text
Issue or change request
→ dedicated branch
→ implementation
→ validation
→ handoff update
→ commit and push
→ pull request
→ review
→ merge into main
```

## 1. Synchronize local main

Before starting new work:

```bash
git switch main
git pull origin main
```

Confirm that the working tree is clean:

```bash
git status
```

Expected result:

```text
nothing to commit, working tree clean
```

## 2. Create a dedicated branch

Use a descriptive branch name:

```bash
git switch -c docs/improve-report-documentation
```

Recommended prefixes:

| Prefix | Purpose |
|---|---|
| `feature/` | New capability or template feature |
| `fix/` | Defect correction |
| `docs/` | Documentation-only change |
| `refactor/` | Structural improvement without intended behavior change |
| `release/` | Release preparation |
| `chore/` | Maintenance or tooling |

## 3. Make focused changes

Each branch should address one coherent objective. Avoid mixing unrelated report, presentation, and IEEE-template modifications in the same pull request unless they are part of a common repository-wide change.

## 4. Update documentation

A meaningful change must update the relevant documentation:

- root `README.md` for repository-wide behavior
- template-specific `README.md` for local behavior
- `CHANGELOG.md` for user-visible changes
- a new file in `docs/handoffs/`
- `docs/HANDOFF_INDEX.md`

Use `docs/HANDOFF_TEMPLATE.md` for each handoff.

## 5. Validate before commit

For LaTeX changes, compile every affected template.

Standard report:

```bash
cd report-template
latexmk -pdf main.tex
```

Presentation:

```bash
cd presentation-template
latexmk -pdf main.tex
```

IEEE paper:

```bash
cd ieee-paper-template
latexmk -pdf main.tex
```

Also inspect:

- title page
- headers and footers
- table of contents
- figures and tables
- code listings
- references
- appendices
- warnings and unresolved references

Remove generated files before committing unless intentionally tracked.

## 6. Review staged changes

```bash
git status
git diff
git add <files>
git diff --staged
```

Do not stage unrelated local files.

## 7. Commit

Use an imperative, specific commit message:

```bash
git commit -m "Document repository workflow and handoff policy"
```

Examples:

```text
Add optional logo fallback to report cover
Fix header spacing on plain pages
Document presentation speaker-note workflow
Refactor report content menu structure
```

## 8. Push the branch

```bash
git push -u origin docs/improve-report-documentation
```

## 9. Open a pull request

The pull request must include:

- problem or objective
- summary of changes
- affected areas
- validation performed
- known limitations
- linked handoff file
- screenshots or generated PDF when layout changes are involved

## 10. Review and merge

Review the changed files and generated output before merging. Prefer squash merge for a focused branch unless preserving multiple commits has clear historical value.

After merge:

```bash
git switch main
git pull origin main
git branch -d docs/improve-report-documentation
```

The remote branch may also be deleted after merge.

## Pull request checklist

- [ ] Work was performed on a dedicated branch
- [ ] Scope is focused
- [ ] Relevant templates compile
- [ ] No generated artifacts were accidentally committed
- [ ] Root or template README was updated when needed
- [ ] `CHANGELOG.md` was updated when needed
- [ ] A handoff file was added
- [ ] `HANDOFF_INDEX.md` was updated
- [ ] No confidential, proprietary, or copyrighted material was added without authorization
