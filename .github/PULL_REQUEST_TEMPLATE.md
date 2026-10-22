## What this PR does

<!-- One sentence -->

## Country/jurisdiction affected

<!-- e.g., Malta, Germany, all EU -->

## Legal — Contributor License Agreement (CLA)

OpenAccountants is a mixed-licence project: code is AGPL-3.0-only, skills are under the OpenAccountants Guide License v1.0, and a commercial licence exists for both (see [LICENSING.md](https://github.com/openaccountants/openaccountants/blob/main/LICENSING.md)). We need a clear **yes** from you before we can merge your contribution.

- [ ] **I have read [CLA.md](https://github.com/openaccountants/openaccountants/blob/main/CLA.md) and agree to the Contributor License Agreement** for everything included in this pull request. *(Checking this box is your explicit opt-in.)*

If you cannot agree, do not open this PR — contact **info@openaccountants.com** to discuss alternatives (including a formal signed agreement).

## Checklist

### Repo & sync (required)

- [ ] File is in `skills/` (not only `packages/`)
- [ ] Jurisdiction is clear (folder path or `jurisdiction:` in frontmatter)
- [ ] I only edited files under `skills/**` (generated trees rebuild automatically)
- [ ] **Name for attribution** (as it should appear on the skill): ______
- [ ] My OpenAccountants profile GitHub username matches this account (optional — set it at openaccountants.com/profile for full credit)

### Content quality

- [ ] Rates and thresholds cite an official source (statute, tax authority website)
- [ ] `## Sources` section present, each URL with the date it was read
- [ ] Worked examples included, each in an `oa-check` block that recomputes
- [ ] Pack `README.md` updated if a domain was added (`applicable:` / `not_applicable:`)
- [ ] `tier` is `2` unless a named accountant reviewed it (then `1` with `reviewed_by` and `reviewed_on`)
- [ ] Disclaimer present at the end
- [ ] `python3 scripts/validate-guides.py --changed-only` passes
- [ ] `python3 scripts/check-examples.py --changed-only` passes
- [ ] If this closes a `[XX] Complete the pack` issue, the description says `Closes #N`
