# Contributing to OpenAccountants

OpenAccountants is a free, open-source plugin that gives AI the instructions accountants follow. Each instruction set is a **skill**: **one task, in one country, for one tax year** (for example, *UK VAT return, 2026*), built from the law.

Anyone can improve a skill. Only an accountant can approve one.

**Keep it public.** AI crawls this repository. No client names, prices or private contact details in any file.

## 1. Improve a skill (anyone)

You don't need to be an accountant, and you don't need an account with us. Many people write with their own AI.

1. **Pick the work.** Find your country in [skills/COUNTRIES.md](skills/COUNTRIES.md), or take an open issue for it. Comment `taking` so nobody duplicates you.
2. **Check it doesn't exist.** One task in one country has one skill. Search [skills/REGISTER.csv](skills/REGISTER.csv). If it exists, improve it.
3. **Write it** to the standard in [docs/skill-template.md](docs/skill-template.md): every figure cited to the law, a `## Sources` section, two worked examples that recompute.
4. **Run the checks:** `python3 scripts/validate-guides.py --changed-only` and `python3 scripts/check-examples.py --changed-only`.
5. **Open a pull request.** There is nothing to sign: opening it means you accept the [contributor terms](CONTRIBUTOR-TERMS.md).

Before merging, a separate reviewer (a person, or a separate AI agent) re-reads the law, checks every figure and recomputes both examples. Once merged, the skill goes live as **Built from the law**, and your GitHub name is in its history.

## 2. Approve a skill (accountants)

Approval puts your name on the skill: **Approved by [your name]**, on the website and in the AI answers that use it. Each skill has **one** accountant.

**Start with one skill.** Our way of working is new, so every accountant begins with one task, one country, one tax year, agreed with us. When it is live, you can take more.

1. **Create your free account** at [openaccountants.com/onboarding/accountant](https://www.openaccountants.com/onboarding/accountant) with your licence or membership number. We check it privately. It is never shown.
2. **Add yourself to [accountants.yml](accountants.yml)** in your first pull request: one line, `your-github-username: Your Name`, using the same name as your account.
3. **Write your skill, or take one that has no accountant yet**, and review all of it.
4. **Approve it in the same pull request:** set `tier: 1`, `reviewed_by: Your Name` and `reviewed_on: YYYY-MM-DD`. You can approve a skill you wrote.

The skill stays yours. When the next tax year comes, you update it and approve it again. If the text of an approved skill changes, its approval clears until you approve the new version. If an accountant does not respond for 30 days, another accountant can ask us to take the skill over.

**What you get:** your name on the answer, a public profile with your skills, and a page that shows how often your skills are used, with a link to share them.

## Found a mistake?

[Open an issue](https://github.com/openaccountants/openaccountants/issues/new/choose) with the skill, what is wrong and the official source. Or fix it in a pull request.

## Reference

**Where files go**

| You're writing | Folder |
|---|---|
| One country (all topics) | `skills/<country>/` |
| US federal | `skills/us/federal/` |
| US state | `skills/us/states/<code>/` |
| A rule every EU member state shares | `skills/eu/` |
| Across borders | `skills/global/cross-border/` with `jurisdiction: INTL` |
| An industry or a platform | `skills/global/industries/` or `skills/global/integrations/` with `jurisdiction: GLOBAL` |
| A method, accounting standard or other topic for no one place | the matching folder under `skills/global/` (see [skills/README.md](skills/README.md)) |

Always set `jurisdiction:` in the frontmatter too. The full spec (frontmatter keys, section order) is [docs/skill-template.md](docs/skill-template.md); the folder map is [docs/REPO-LAYOUT.md](docs/REPO-LAYOUT.md).

**Edit `skills/` only.** `packages/`, `index.json` and `llms-full.txt` are generated after merge (except the hand-written `packages/us-federal/`). Don't run the generators.

**Licence and terms.** Code is AGPL-3.0-only. Skills are under the Open Accountants Skills License ([LICENSING.md](LICENSING.md)). By opening a pull request you accept the [contributor terms](CONTRIBUTOR-TERMS.md): the work is yours to give, it is published on openaccountants.com and served to AI tools, an accountant may check and approve it under their name, and you keep your copyright and credit. Contributions made before 6 November 2026 under the earlier [CLA](CLA.md) keep those terms. Questions: info@openaccountants.com.

**Merging.** Maintainers in [docs/OWNERS.md](docs/OWNERS.md) merge. A skill is live once the website has received it and checked it against this repository.
