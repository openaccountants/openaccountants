## What this PR does

<!-- One sentence -->

## Country/jurisdiction affected

<!-- e.g., Malta, Germany, all EU -->

## Contributor terms

By opening this pull request you accept the [contributor terms](https://github.com/openaccountants/openaccountants/blob/main/CONTRIBUTOR-TERMS.md): the work is yours to give and is shared under this repository's licences. Your skill will be published, served to AI tools through the OpenAccountants plugin, and may be checked, improved and approved by a licensed accountant. You keep your authorship. There is nothing to sign.

## Checklist

### Repo & sync (required)

- [ ] File is in `skills/` (not only `packages/`)
- [ ] Jurisdiction is clear (folder path or `jurisdiction:` in frontmatter)
- [ ] I only edited files under `skills/**` (generated trees rebuild automatically)
- [ ] **Name for attribution** (as it should appear on the skill): ______
- [ ] If I am an accountant and want my name on this skill, I followed [CONTRIBUTING.md, "Approve a skill (accountants)"](https://github.com/openaccountants/openaccountants/blob/main/CONTRIBUTING.md#2-approve-a-skill-accountants)

### Content quality

- [ ] Rates and thresholds cite an official source (statute, tax authority website)
- [ ] `## Sources` section present, each URL with the date it was read
- [ ] Worked examples included, each in an `oa-check` block that recomputes
- [ ] Pack `README.md` updated if a domain was added (`applicable:` / `not_applicable:`)
- [ ] If I am publishing this as my own professional work as an approved accountant, my own approval is recorded in this PR (`tier: 1`, my name in `reviewed_by`, the actual date in `reviewed_on`). Otherwise `tier: 2` carries no approval claim
- [ ] Disclaimer present at the end
- [ ] `python3 scripts/validate-guides.py --changed-only` passes
- [ ] `python3 scripts/check-examples.py --changed-only` passes
- [ ] If this closes a `[XX] Complete the pack` issue, the description says `Closes #N`
