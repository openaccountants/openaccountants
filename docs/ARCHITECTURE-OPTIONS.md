# Repo Architecture — Design Options

Seven design patterns evaluated. Each one answers the same question: a developer clones this repo and says "I'm in Malta." What happens next?

---

## The constraints (non-negotiable)

1. Works with ANY LLM (Claude, ChatGPT, Gemini, local models)
2. User only needs files for ONE jurisdiction
3. Files have dependencies (Malta VAT needs EU directive, all skills need workflow base)
4. Contributors need to edit individual skills without breaking other jurisdictions
5. The repo is discoverable on GitHub (README must make sense immediately)
6. No build step required for basic usage (developer can use it right after cloning)

---

## Option 1: Per-Jurisdiction Folders (flat)

```
openaccountants/
├── README.md
├── malta/
│   ├── README.md
│   ├── foundation.md
│   ├── vat-return.md
│   ├── income-tax.md
│   ├── ssc.md
│   ├── estimated-tax.md
│   └── return-assembly.md
├── uk/
│   ├── README.md
│   ├── foundation.md
│   ├── vat-return.md
│   ├── ...
├── germany/
├── shared/
│   ├── cross-border/
│   ├── patterns/
│   └── intelligence/
└── docs/
```

**How a user uses it:** Open `malta/`, read the README, upload all .md files to LLM.

**Pros:**
- Dead simple to navigate — one folder per country
- Self-contained — no hunting across directories
- Each folder has its own README with specific instructions
- GitHub browsing is intuitive

**Cons:**
- `foundation.md` is duplicated in every folder (or symlinked, which GitHub renders poorly)
- EU VAT directive content duplicated across 27 EU country folders
- Contributing is confusing — do I edit `malta/vat-return.md` or some source file?
- Maintaining consistency across 134 duplicate foundation files is impossible

**Verdict:** Great for users, terrible for contributors and maintenance.

---

## Option 2: Source + Packages (generated)

```
openaccountants/
├── README.md
├── skills/                      ← Source of truth (what contributors edit)
│   ├── foundation/
│   ├── orchestrator/
│   ├── international/malta/
│   ├── international/uk/
│   └── ...
├── packages/                    ← Auto-generated (what users download)
│   ├── malta/
│   │   ├── README.md
│   │   ├── foundation.md
│   │   ├── vat-return.md
│   │   └── ...
│   ├── uk/
│   └── ...
└── scripts/
    └── build-packages.py        ← Resolves dependencies, copies files
```

**How a user uses it:** Open `packages/malta/`, read the README, upload files to LLM. Never touches `skills/`.

**How a contributor works:** Edit files in `skills/`. Run build script. Packages regenerate.

**Pros:**
- Clean separation of source vs distribution
- Contributors edit one place, changes propagate to packages
- Foundation.md is generated (not duplicated in source)
- Dependencies resolved by the build script

**Cons:**
- Requires a build step (even if automated via CI)
- Two copies of every file in the repo (source + package) — repo size doubles
- Packages can get out of sync with source if someone forgets to rebuild
- More complex for first-time contributors

**Verdict:** Clean architecture, but adds complexity.

---

## Option 3: Layered Loading (current structure, better docs)

```
openaccountants/
├── README.md                    ← "Step 1: Pick your country from the table below"
├── skills/
│   ├── foundation/
│   │   └── workflow-base.md     ← ALWAYS load this
│   ├── international/
│   │   ├── eu/
│   │   │   └── eu-vat-base.md   ← Load if EU country
│   │   ├── malta/
│   │   │   ├── malta-vat-return.md
│   │   │   ├── malta-income-tax.md
│   │   │   ├── malta-ssc.md
│   │   │   └── mt-estimated-tax.md
│   │   └── ...
│   ├── orchestrator/
│   │   ├── mt-freelance-intake.md
│   │   └── mt-return-assembly.md
│   └── ...
```

**How a user uses it:** README has a table:

| Country | Load these files | Dependencies |
|---------|-----------------|-------------|
| Malta | `international/malta/*` + `orchestrator/mt-*` | `foundation/workflow-base.md` + `international/eu/eu-vat-base.md` |
| UK | `international/uk/*` + `orchestrator/uk-*` | `foundation/workflow-base.md` |
| Germany | `international/germany/*` + `orchestrator/de-*` | `foundation/workflow-base.md` + `international/eu/eu-vat-base.md` |

User follows the table, downloads the listed files, uploads to LLM.

**Pros:**
- No restructuring needed — the repo already looks like this
- No duplication — each file exists once
- Contributors edit directly, no build step
- Adding a country = adding files + one row in the README table

**Cons:**
- User has to navigate multiple directories
- User has to understand the dependency table
- Easy to miss a file (forgot eu-vat-base.md → Malta VAT skill fails)
- The "orchestrator" directory name is not intuitive to end users

**Verdict:** Lowest effort to implement, but puts the burden on the user.

---

## Option 4: Single Entry Point per Jurisdiction

```
openaccountants/
├── README.md
├── malta.md                     ← ONE file. Everything Malta needs.
├── uk.md
├── germany.md
├── australia.md
├── ...
├── skills/                      ← Source files (for contributors)
│   └── ... (current structure)
└── scripts/
    └── bundle.py                ← Merges source → single files
```

**How a user uses it:** Download `malta.md`. Upload to LLM. Done.

**Pros:**
- Absolute simplest user experience — one file, one upload
- No dependency confusion
- Works with every LLM without exception
- Most shareable ("here's one file, try it")

**Cons:**
- Files are huge (Malta = ~1,500-2,000 lines merged)
- May exceed some LLMs' file upload limits or degrade performance
- Context gets diluted when everything is in one file
- We already tried this and you said we lost context
- Requires build step to regenerate from source
- Harder to update one part without regenerating the whole file

**Verdict:** Best UX, worst for LLM performance and maintenance.

---

## Option 5: Progressive Disclosure (skill packs)

```
openaccountants/
├── README.md
├── packs/
│   ├── malta-vat.md             ← Just Malta VAT (foundation included)
│   ├── malta-income-tax.md      ← Just Malta IT (foundation included)
│   ├── malta-ssc.md             ← Just Malta SSC (foundation included)
│   ├── malta-full.md            ← All Malta skills combined
│   ├── uk-vat.md
│   ├── uk-income-tax.md
│   ├── uk-full.md
│   └── ...
├── skills/                      ← Source (for contributors)
│   └── ...
```

**How a user uses it:**
- "I just need Malta VAT" → download `malta-vat.md` (one file, ~400 lines, includes foundation)
- "I need everything" → download `malta-full.md` (one file, ~1,500 lines)
- "I need VAT + income tax but not SSC" → download `malta-vat.md` + `malta-income-tax.md`

Each pack is self-contained — foundation rules are included in every file (compressed to ~50 lines at the top).

**Pros:**
- User chooses their level of complexity
- Each file is self-contained (no dependencies)
- Small files for simple needs, big file for full return
- Most flexible for different LLM context limits
- "Just try Malta VAT" is a ~400 line file — very low commitment

**Cons:**
- Foundation duplicated in every file (but only ~50 lines)
- Many files in packs/ (3-5 per jurisdiction × 30 jurisdictions = 90-150 files)
- Requires build step
- Testing burden — need to verify each pack works standalone

**Verdict:** Best balance of simplicity and flexibility. User starts small, adds more if needed.

---

## Option 6: LLM-Native Plugin Format

```
openaccountants/
├── README.md
├── plugins/
│   ├── malta/
│   │   ├── plugin.json          ← Metadata, dependencies, trigger descriptions
│   │   └── skills/
│   │       ├── vat/SKILL.md
│   │       ├── income-tax/SKILL.md
│   │       ├── ssc/SKILL.md
│   │       └── foundation/SKILL.md
│   ├── uk/
│   │   ├── plugin.json
│   │   └── skills/...
│   └── ...
```

**How a user uses it:**
- Claude Code: `claude plugin install ./plugins/malta` — loads only Malta skills
- Other LLMs: Upload the .md files from `plugins/malta/skills/`

**Pros:**
- Native Claude Code integration — one command installs one jurisdiction
- Skills are properly isolated — Malta plugin doesn't pollute UK context
- Plugin.json declares dependencies, trigger descriptions, metadata
- Follows Claude Code's actual plugin architecture

**Cons:**
- Only works natively with Claude Code — other LLMs just get the .md files
- Requires understanding the plugin format
- More complex directory structure
- Plugin format might change as Claude Code evolves

**Verdict:** Best for Claude Code users, but locks into one LLM's ecosystem.

---

## Option 7: Index-Driven (smart README)

```
openaccountants/
├── README.md                    ← The entire user interface
├── skills/                      ← Flat-ish structure
│   ├── _foundation.md
│   ├── _eu-vat-directive.md
│   ├── malta-vat.md
│   ├── malta-income-tax.md
│   ├── malta-ssc.md
│   ├── malta-estimated-tax.md
│   ├── malta-intake.md
│   ├── malta-assembly.md
│   ├── uk-vat.md
│   ├── uk-income-tax-sa103.md
│   └── ...
```

All skills in ONE directory. Named with jurisdiction prefix. Underscore prefix for shared files.

The README is the interface:

```markdown
## Quick Start

### Malta
Upload these files to your LLM:
1. `skills/_foundation.md` (required for all jurisdictions)
2. `skills/_eu-vat-directive.md` (required for EU countries)
3. `skills/malta-vat.md`
4. `skills/malta-income-tax.md`
5. `skills/malta-ssc.md`
6. `skills/malta-estimated-tax.md`
7. `skills/malta-intake.md`
8. `skills/malta-assembly.md`

Then attach your bank statement and say: "Help me with my 2025 Malta taxes."

### UK
Upload these files to your LLM:
1. `skills/_foundation.md`
2. `skills/uk-vat.md`
3. `skills/uk-income-tax-sa103.md`
...
```

**Pros:**
- All files in one place — no navigating subdirectories
- Jurisdiction prefix makes it obvious which files belong together
- README IS the routing table — user reads it and knows exactly what to do
- No build step, no duplication, no tooling
- Contributors edit directly
- Underscore prefix sorts shared files to the top

**Cons:**
- One directory with 200+ files is visually overwhelming on GitHub
- No self-contained packages — user must follow the README
- Naming conventions must be strict and enforced
- Doesn't scale well past 50 jurisdictions

**Verdict:** Simplest possible implementation, but doesn't scale and looks messy.

---

## Comparison Matrix

| Criteria | Opt 1 Folders | Opt 2 Src+Pkg | Opt 3 Layered | Opt 4 Single | Opt 5 Packs | Opt 6 Plugin | Opt 7 Index |
|----------|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| User simplicity | ★★★★★ | ★★★★ | ★★★ | ★★★★★ | ★★★★★ | ★★★★ | ★★★★ |
| No dependency confusion | ★★★★★ | ★★★★ | ★★ | ★★★★★ | ★★★★★ | ★★★★ | ★★★ |
| No build step needed | ★★ | ★ | ★★★★★ | ★ | ★ | ★★★ | ★★★★★ |
| Contributor simplicity | ★★ | ★★★ | ★★★★★ | ★★★ | ★★★ | ★★★ | ★★★★ |
| No duplication | ★ | ★★ | ★★★★★ | ★ | ★★ | ★★★★ | ★★★★★ |
| Works with all LLMs | ★★★★★ | ★★★★★ | ★★★★★ | ★★★★★ | ★★★★★ | ★★★ | ★★★★★ |
| GitHub browsability | ★★★★★ | ★★★ | ★★★ | ★★★★★ | ★★★★ | ★★★ | ★★ |
| Scales to 134 countries | ★★★★ | ★★★★★ | ★★★★ | ★★★★★ | ★★★★ | ★★★★★ | ★★ |
| LLM context efficiency | ★★★★ | ★★★★ | ★★★★ | ★★ | ★★★★★ | ★★★★ | ★★★★ |

---

## My recommendation: Option 5 (Progressive Disclosure)

**Why:**
1. A developer who "just wants to try it" downloads ONE file (malta-vat.md, ~400 lines) and uploads it. Zero commitment, zero confusion. That's how things go viral.
2. A serious user downloads the full pack (malta-full.md) for their complete return.
3. Each file is self-contained — no "you forgot to load the foundation" errors.
4. Works with every LLM — it's just a markdown file.
5. The foundation is compressed into ~50 lines at the top of each file — not the 700-line spec, just the essential execution rules.
6. Source files in `skills/` stay composable for contributors. A build script generates the packs.

**The viral path:**
```
Developer sees repo on HN/Twitter →
  clicks malta-vat.md (400 lines) →
    uploads to Claude with bank statement →
      sees transactions classified instantly →
        "holy shit this works" →
          shares it →
            downloads malta-full.md for their real return
```

That first step — one file, 400 lines, instant result — is what makes it spread.
