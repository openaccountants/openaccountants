# User Journey Analysis — First Principles

No assumptions. No building. Just: what does a real user do, and where does it break?

---

## The user

Maria, 34, freelance software developer in Valletta, Malta. Self-employed, Article 10 VAT registered, invoices EU and non-EU clients. Has a BOV business bank account. Needs to file her 2025 TA24, VAT return, and SSC.

She's heard about OpenAccountants from a developer friend or a tweet.

---

## Step 0: Discovery

Maria finds openaccountants.com or the GitHub repo.

**Question she has:** "Can this help me with my Malta taxes?"

**What she sees on the website:** A list of skills, coverage for 134 countries, Malta is covered.

**What she needs to know:**
- What do I download?
- What do I do with it?
- Which LLM do I use?
- What documents do I need?

**Current state:** The README says `git clone` into Claude Code. That's for developers, not for Maria. She uses Claude.ai or ChatGPT.

**BLOCKER 1:** There's no clear "download the Malta skills" button or package. She'd have to navigate GitHub, find the right files across multiple directories, and figure out which ones she needs.

---

## Step 1: Getting the skills

Assuming she figures out what to download, what does she actually need?

**Files she needs:**
1. `malta-vat-return.md` — VAT classification + supplier patterns
2. `malta-income-tax.md` — TA24 computation
3. `malta-ssc.md` — Class 2 contributions
4. `mt-estimated-tax.md` — Provisional tax
5. `workflow-base.md` — How to produce outputs, conservative defaults
6. `eu-vat-base.md` — EU VAT directive (Malta VAT depends on this)
7. `mt-freelance-intake.md` — Onboarding questions
8. `mt-return-assembly.md` — Cross-checks

**Where these files are:**
- `skills/international/malta/` — 4 files
- `skills/foundation/` — 1 file
- `skills/international/eu/` — 1 file
- `skills/orchestrator/` — 2 files

**BLOCKER 2:** Files are spread across 4 directories. Maria doesn't know which ones she needs. The manifest.json lists them but she's not going to read a JSON file.

**Possible solutions:**
- A. One download per jurisdiction (the package approach)
- B. The website serves the right files based on jurisdiction selection
- C. A README section per jurisdiction: "If you're in Malta, download these 8 files"
- D. Keep all files, but the LLM's skill system only loads the right ones (Claude Code approach)

---

## Step 2: Loading the skills into an LLM

Maria has the files. Now what?

**Option A: Claude.ai (web)**
- Create a new Project called "Malta Taxes 2025"
- Add the .md files as Project Knowledge
- Start a conversation with her bank statement attached
- Claude reads the skills from project knowledge + the bank statement from the chat

**Option B: Claude Code (CLI)**
- Clone the repo or copy files to `~/.claude/skills/`
- Claude Code loads skill descriptions automatically
- She types in the terminal

**Option C: ChatGPT**
- Create a Custom GPT with the .md files as knowledge
- Or attach the files to a conversation

**Option D: Any other LLM**
- Paste the content or attach files

**BLOCKER 3:** If she uses Claude.ai Projects, she can add all 8 files as project knowledge and it works. But she has to know WHICH 8 files. If she adds all 371, the project knowledge gets diluted.

If she uses Claude Code and clones the whole repo, 371 skill descriptions compete for attention. Claude might load the wrong skill or get confused.

**The core tension:** We want the repo to contain everything (for contributors, for completeness). But we want users to load only their jurisdiction.

---

## Step 3: The conversation

Maria has loaded the Malta skills. She attaches her BOV bank statement and says:

> "Help me with my 2025 Malta taxes. Here's my bank statement."

**What should happen:**
1. The intake skill asks 5-6 onboarding questions
2. Claude reads the bank statement and classifies transactions using the supplier pattern library
3. Claude builds the Malta VAT return, TA24, SSC, and provisional tax outputs
4. Claude runs cross-checks
5. Claude produces the working paper + reviewer brief

**BLOCKER 4:** Does the LLM actually follow the skill instructions? This depends on:
- How well the skill is written (clear instructions vs vague guidelines)
- Whether the LLM has enough context (all 8 files + bank statement must fit)
- Whether the skill format works for the specific LLM (Claude vs GPT vs others)

**BLOCKER 5:** The bank statement. Maria's BOV statement might be a PDF (not machine-readable), or a CSV with Maltese column headers. The skill has a bank statement reading guide — but does the LLM actually use it?

---

## Step 4: The output

Claude produces the working papers. Maria gets:
- VAT return box values
- TA24 computation
- SSC calculation
- Provisional tax schedule
- Reviewer brief with flags

**BLOCKER 6:** The output format. The skill says "produce an Excel working paper" — but Claude.ai can't create Excel files. It can create a table in the chat, or a CSV. Is that good enough?

**BLOCKER 7:** The reviewer handoff. Maria needs to get this reviewed by a warranted accountant. The skill says "visit openaccountants.com" — but what does she actually upload there? The chat transcript? A downloaded file?

---

## Summary of blockers

| # | Blocker | Severity | Where it breaks |
|---|---------|----------|-----------------|
| 1 | No clear "download Malta skills" path | HIGH | Discovery |
| 2 | Files spread across 4 directories | MEDIUM | Getting skills |
| 3 | Loading the RIGHT files, not all 371 | HIGH | Loading into LLM |
| 4 | Does the LLM actually follow the skill? | MEDIUM | Conversation |
| 5 | Bank statement format compatibility | MEDIUM | Conversation |
| 6 | Output format (no Excel in web LLMs) | LOW | Output |
| 7 | Reviewer handoff unclear | LOW | After output |

---

## What we need to decide

### Q1: One file or many files per jurisdiction?

**One file:**
- Pro: Simple to download, simple to upload, no dependency confusion
- Con: Long file, potentially loses context depth, harder to maintain

**Many files:**
- Pro: Each skill is focused, easier to update, matches the repo structure
- Con: User has to know which files, dependencies between files

### Q2: How does the user find their jurisdiction's files?

- A. Website serves them (openaccountants.com/malta → download button)
- B. Repo has a `/packages/` directory with one file per jurisdiction
- C. README has a "Quick start by country" section
- D. A script/tool that bundles the right files

### Q3: What's the minimum viable skill set per jurisdiction?

For Malta, do we NEED all 8 files? What if we just had:
- `malta-vat-return.md` — the one skill that's Q1, battle-tested, has the supplier pattern library
- That's it. Just VAT. Not income tax, not SSC. Just the one thing that works perfectly.

And then income tax is a separate download. SSC is a separate download. Each one works standalone.

This avoids the "one giant file" problem AND the "which 8 files do I need" problem.

### Q4: What's the role of the repo vs the website?

- **Repo:** Source of truth. Contributors work here. Developers clone it.
- **Website:** User-facing. "I'm in Malta" → here are your skills, download them, upload to your LLM.

The repo doesn't need to optimize for end-user installation. The website does.

---

## Recommendation

Don't restructure the repo. The repo is fine for what it is — a source of truth with 371 skills organized by country and obligation type.

Build the **distribution layer** on the website:
1. User selects their country
2. Website bundles the right files
3. User downloads and uploads to their LLM

The repo stays a repo. The website does the packaging.

But we should validate: **does ONE skill file (e.g., just malta-vat-return.md) actually work when uploaded to Claude.ai?** If yes, that's the minimum viable product — one file per obligation, no bundling needed.
