# OpenAccountants AI skills (tax rules your AI follows)

Every tax skill in this repository, in the open [Agent Skills](https://agentskills.io) format: one folder, one `SKILL.md`, with a `name`, a `description` that tells the AI when to use it, and the method. Install a country and your AI knows how that country's income tax, VAT or GST, payroll, company formation and cross-border rules work, every time the topic comes up.

<!-- oa-skills-stats:start -->
**2,068 skills** across **273 jurisdictions**. 33 are accountant-reviewed (a named accountant in `metadata.reviewed_by`); the other 2,035 are source-cited drafts.
<!-- oa-skills-stats:end -->

> General reference only, not advice on your situation. Confirm with a qualified professional in the relevant jurisdiction before you file, pay or amend.

## Install

One line. Pick countries by code, a single skill by name, or `all`.

```bash
# Claude Code (installs into ~/.claude/skills)
curl -fsSL https://raw.githubusercontent.com/openaccountants/openaccountants/main/agent-skills/install.sh | sh -s -- MT NL DE IE GB

# any Agent Skills client: say where its skills folder is
curl -fsSL https://raw.githubusercontent.com/openaccountants/openaccountants/main/agent-skills/install.sh | sh -s -- GB --to ~/.hermes/skills
curl -fsSL https://raw.githubusercontent.com/openaccountants/openaccountants/main/agent-skills/install.sh | sh -s -- all --to ./.claude/skills
```

Re-run the same line to update. The script downloads the skill files you asked for and nothing else; no telemetry.

**Hermes Agent** ([NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)) reads skills from `~/.hermes/skills/`. Install with the `--to ~/.hermes/skills` form above, or copy a folder in by hand:

```bash
cp -r malta-vat-return ~/.hermes/skills/
```

Then `/skills` in Hermes lists what is installed and `/malta-vat-return` invokes one by name. Hermes loads only each skill's short description at startup and reads the full `SKILL.md` when a task matches, so the whole library costs little context. For live figures, add the connector too: `{"mcpServers": {"openaccountants": {"command": "uvx", "args": ["openaccountants-mcp"]}}}`, or point Hermes at the hosted server at openaccountants.com.

**Claude Code plugin** (Malta, Netherlands, Germany, Ireland, UK bundled, plus the connector):

```
/plugin marketplace add openaccountants/openaccountants
/plugin install openaccountants@openaccountants
```

## Skills and the connector are two halves

| | **Installed skills** (this folder) | **The connector** ([openaccountants.com/connect](https://www.openaccountants.com/connect)) |
|---|---|---|
| What | The method, read by your AI whenever the topic comes up | Today's figures, official sources and the named accountant, fetched live |
| Best for | Reach: it works offline and in any Agent Skills client | Currency: rates, thresholds and deadlines as of today; VAT number checks |

Every `SKILL.md` ends with where its current version lives, so an AI with both installed reads the method here and checks the figures there.

## What a skill is, and who stands behind it

A skill sets out the method for one tax task in one jurisdiction: scope, the order of operations, the figures with their official sources, the edge cases, the self-checks. `metadata` in each file carries the jurisdiction, tax year, last update, the author line and the review status. There are exactly two quality states (see [docs/QUALITY-TIERS.md](../docs/QUALITY-TIERS.md)):

- **Accountant-reviewed:** a named licensed accountant reviewed the whole skill; their name is in `metadata.reviewed_by`.
- **Source-cited draft:** written from official sources, every figure cited, not yet reviewed by an accountant. An `authored_by` line says who wrote it; it is not a review.

Nothing here is a sign-off on a figure. The official source cited next to each figure is the authority on the number.

## How this folder is built

Generated from `skills/**` by [`scripts/build-agent-skills.py`](../scripts/build-agent-skills.py) in the nightly sync from openaccountants.com, so it follows the library. Do not edit a `SKILL.md` here; change the source skill under `skills/`, or the live skill on openaccountants.com, and the next sync carries it through. `index.json` lists every skill with its jurisdiction and author line; `install.sh` reads it.

## License

- Tooling and code: AGPL-3.0-only
- Skill content (`SKILL.md` files): OpenAccountants Guide License v1.0 (skills were called Guides until October 2026; the licence keeps its name). See [LICENSE.md](LICENSE.md) and the repository's [LICENSING.md](../LICENSING.md).

## Links

- Site: [openaccountants.com](https://www.openaccountants.com)
- Add the connector: [openaccountants.com/connect](https://www.openaccountants.com/connect)
- The open standard: [agentskills.io](https://agentskills.io)
