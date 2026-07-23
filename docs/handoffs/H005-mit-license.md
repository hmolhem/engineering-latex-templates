# Handoff: MIT License

## Metadata

| Field | Value |
|---|---|
| Date | `2026-07-23` |
| Author | `Hossein Molhem and ChatGPT` |
| Repository | `hmolhem/engineering-latex-templates` |
| Branch | `chore/add-mit-license` |
| Pull request | `Pending` |
| Related version | `Unreleased after v0.2.0` |
| Status | `Ready for review` |

## Purpose

Add an explicit open-source license so the repository's public reuse terms are clear and consistent with the open-source language used in the repository showcase.

## Scope

Included:

- standard MIT License text
- copyright attribution to Hossein Molhem
- root README license section
- repository-tree update for `LICENSE`
- README clarification regarding third-party assets
- changelog and handoff-index updates

Excluded:

- dual licensing
- contributor license agreements
- trademark permissions
- relicensing of third-party packages, fonts, logos, references, or venue-specific assets
- legal advice regarding a particular commercial or academic use

## Affected files

```text
LICENSE
README.md
CHANGELOG.md
docs/HANDOFF_INDEX.md
docs/handoffs/H005-mit-license.md
```

## Implementation summary

The repository now contains the standard MIT License. The license permits use, copying, modification, merging, publication, distribution, sublicensing, and sale of copies, subject to retention of the copyright notice and license text.

The README now identifies the MIT License, links to the license file, and distinguishes original repository materials from third-party assets that remain governed by their own terms.

## Design decisions

### Use MIT rather than a restrictive documentation license

The repository is intended to be copied, adapted, and reused for academic, engineering, research, and consulting documentation. MIT provides a familiar, permissive framework with minimal reuse friction.

### Preserve explicit attribution and disclaimer text

The standard license text was used without custom restrictions. This keeps the license recognizable and preserves the standard warranty disclaimer.

### Clarify third-party boundaries

The repository contains or references packages, fonts, trademarks, institutional names, logos, bibliography records, and venue-specific conventions that are not automatically relicensed by this repository. The README records that boundary explicitly.

## Validation

```text
The standard MIT License text is present at the repository root.
The copyright year is 2026.
The copyright holder is Hossein Molhem.
The README links to LICENSE and summarizes the permitted reuse terms.
The README clarifies that third-party assets retain their own terms.
The changelog includes the licensing change.
H005 is registered in the handoff index.
The branch is isolated from main and is ready for review.
```

## Known limitations

- The MIT License is not a substitute for venue-specific publication requirements.
- The license does not grant rights to third-party trademarks, logos, fonts, packages, or copyrighted source material.
- Users remain responsible for checking the terms of assets they add to derived projects.
- This handoff records an engineering repository decision and is not legal advice.

## Follow-up work

- [ ] Merge the licensing pull request before promoting the repository as open source.
- [ ] Confirm GitHub detects the repository license as MIT after merge.
- [ ] Keep third-party asset notices accurate as new examples are added.
- [ ] Consider adding contribution guidelines before accepting external contributions.

## Recovery and rollback

Rollback can be performed by reverting the eventual merge commit. Removing the license would return the repository to default copyright status, so any rollback should also remove or revise open-source claims in the README and social-media materials.

## Related references

- License file: `LICENSE`
- Root documentation: `README.md`
- Handoff index: `docs/HANDOFF_INDEX.md`
- Workflow: `docs/WORKFLOW.md`
- Changelog: `CHANGELOG.md`
