# Handoff: Enhanced IEEE Paper Template

## Metadata

| Field | Value |
|---|---|
| Date | `2026-07-23` |
| Author | `Hossein Molhem and ChatGPT` |
| Repository | `hmolhem/engineering-latex-templates` |
| Branch | `feature/enhance-ieee-paper-template` |
| Pull request | `Pending` |
| Related version | `Unreleased after v0.2.0` |
| Status | `Ready for review` |

## Purpose

Replace the minimal IEEE paper starter with a complete, polished, and reusable IEEE-style technical-paper example suitable for demonstrating equations, figures, tables, citations, cross-references, and bibliography management.

## Scope

Included:

- complete `IEEEtran` conference example
- conventional and MVDR beamforming case study
- mathematical signal and beamformer models
- TikZ workflow diagram
- external vector beam-pattern figure
- two publication-style tables
- in-text citations and BibTeX references
- quantitative synthetic results
- expanded IEEE-template README
- refreshed curated preview PDF
- changelog and handoff-index updates

Excluded:

- claims of original research contribution
- automatic regeneration of the external figure
- GitHub Actions compilation
- venue-specific copyright or submission forms

## Affected files and directories

```text
CHANGELOG.md
docs/HANDOFF_INDEX.md
docs/handoffs/H003-enhanced-ieee-paper-template.md
ieee-paper-template/main.tex
ieee-paper-template/references.bib
ieee-paper-template/README.md
ieee-paper-template/figures/beam_patterns.pdf
ieee-paper-template/preview/ieee-paper-template-preview.pdf
```

## Implementation summary

The previous placeholder-only IEEE starter was replaced with a two-column technical paper titled `A Compact Reproducible Example of Conventional and MVDR Beamforming`. The sample includes a narrowband uniform-linear-array model, conventional beamforming, diagonally loaded MVDR beamforming, an output-SINR metric, a TikZ processing diagram, an external vector beam-pattern figure, two tables, and five bibliography records.

The technical content is explicitly presented as illustrative template material. Users are instructed to replace the metadata, numerical results, figures, and references before real submission.

## Design decisions

### Use a realistic but non-claiming engineering example

A beamforming case study gives the template enough technical depth to demonstrate IEEE layout behavior without presenting the repository example as a novel publication.

### Separate bibliography data from the paper source

References are maintained in `references.bib` and rendered through `IEEEtran.bst`. This is closer to normal conference and journal workflows than an inline placeholder bibliography.

### Demonstrate both internal and external graphics

The paper uses TikZ for the processing workflow and a vector PDF for the beam pattern. This demonstrates two common publication workflows and reinforces the repository's preference for scalable graphics.

### Preserve curated preview policy

The existing preview filename remains unchanged so the root README link remains stable. The PDF must be refreshed whenever the rendered IEEE template materially changes.

## Validation

```text
The candidate package compiled successfully in Overleaf.
The repository owner visually inspected and approved the rendered two-page PDF.
In-text citations and bibliography entries were confirmed present.
Equations, figures, tables, labels, and cross-references were confirmed present.
The external beam-pattern PDF is committed at the path referenced by main.tex.
The curated IEEE preview PDF was replaced with the approved rendered output.
The branch contains all source, bibliography, figure, README, changelog, handoff, and index changes required by this scope.
The branch is ahead of main without divergence.
```

## Known limitations

- The external beam-pattern figure is a generated reference artifact; its generation script is not yet included.
- Preview generation remains manual through Overleaf.
- The example does not guarantee compliance with every IEEE venue.
- The author email remains a placeholder.

## Follow-up work

- [ ] Add a reproducible Python or MATLAB script for the beam-pattern figure.
- [ ] Add GitHub Actions compilation checks.
- [ ] Consider a journal-mode variant after the conference template stabilizes.
- [ ] Define stable-release criteria for `v1.0.0`.

## Recovery and rollback

Rollback can be performed by reverting the branch or eventual merge commit. The prior minimal starter can be recovered from Git history. The enhanced example is isolated to the IEEE template and does not affect the report or presentation templates.

## Related references

- IEEE template documentation: `ieee-paper-template/README.md`
- Handoff index: `docs/HANDOFF_INDEX.md`
- Workflow: `docs/WORKFLOW.md`
- Changelog: `CHANGELOG.md`
