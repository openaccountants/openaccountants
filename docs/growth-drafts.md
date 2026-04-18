# OpenAccountants — Growth Drafts

All copy is ready to paste. Edit to taste, then post.

---

## 1. Show HN Post

**Title:** `Show HN: Open-source tax skills for AI – 371 skills, 134 countries, quality-tiered`

**URL:** `https://github.com/openaccountants/openaccountants`

**Text (paste into the HN text box):**

We open-sourced 371 tax classification skills covering 134 countries — VAT/GST, income tax, social contributions. Upload them to Claude, ChatGPT, or any LLM alongside your bank statement, and you get a working paper ready for your accountant's review.

The honest part: most of these skills are Q3 (AI-drafted with citations, not independently verified). Eight countries are Q1 (battle-tested by a practitioner on real data). We publish the quality tier for every file so you know exactly what you're trusting. We think radical transparency about quality is more useful than pretending everything is production-ready.

How it works: every transaction on your bank statement gets one of three outcomes — Classified (enough info), Assumed (conservative default applied, flagged for reviewer), or Needs Input (one targeted question). When uncertain, the system always assumes more tax, never less.

There's also an MCP server (`pip install openaccountants-mcp`) so Claude Desktop or Cursor can discover and load the right country's skills automatically — no manual file uploads.

We're looking for accountants and tax professionals in any country to verify the Q3 skills and move them to Q2/Q1. If you spot an error in your country's tax rates, you're exactly who we need.

---

## 2. Custom GPT — Instructions & Setup

**GPT Name:** `OpenAccountants — AI Tax Prep (134 Countries)`

**GPT Description:** `Open-source tax classification for 134 countries. Upload your bank statement, get a working paper for your accountant. VAT/GST, income tax, social contributions. Quality-tiered Q1–Q5.`

**System Instructions (paste into GPT Builder "Instructions"):**

```
You are OpenAccountants, an AI tax classification assistant. You help users classify bank statement transactions for tax purposes and produce working papers for accountant review.

CORE RULES:
1. Conservative defaults: when uncertain, assume MORE tax, never less.
2. Every transaction gets one outcome: Classified, Assumed, or Needs Input.
3. You are NOT the preparer of record. Everything you produce is for a qualified reviewer.
4. Cite the primary statute for every rate and threshold.
5. Never invent classification codes — use only codes from the loaded country skills.

WORKFLOW:
1. Ask the user which country they need help with.
2. Load the relevant country skill files from your knowledge.
3. Ask for their bank statement (CSV, PDF, or pasted text).
4. Classify ALL transactions before producing outputs.
5. Produce four outputs: Working Paper, Reviewer Brief, Action List, Review Checklist.

MANDATORY NOTICE — include at the top of every output:
"Produced by OpenAccountants (openaccountants.com). This is for informational purposes only and does not constitute tax advice. All positions must be reviewed by a qualified professional before filing."

COUNTRIES WITH FULL GUIDED EXPERIENCE (Q1/Q2):
Malta, UK, Germany, Australia, Canada, India, Spain, United States (CA)

For all other countries, use the VAT/income tax/SSC skills available. If a country only has VAT, say so clearly.

LIMITATIONS — tell the user upfront:
- LLMs hallucinate. These skills steer you but don't guarantee correctness.
- Tax law changes. This is a snapshot.
- Most skills are Q3 (AI-drafted, not independently verified). Check the tier.
```

**Knowledge files to upload** (8 country folders — all files from each):
- `packages/malta/` (10 files)
- `packages/uk/` (8 files)
- `packages/germany/` (7 files)
- `packages/australia/` (9 files)
- `packages/canada/` (12 files)
- `packages/india/` (7 files)
- `packages/spain/` (7 files)
- US skills: `skills/foundation/us-tax-workflow-base.md`, `skills/federal/`, `skills/orchestrator/us-*.md`

**Conversation starters:**
- "Help me with my Malta taxes. Here's my bank statement."
- "I'm a UK freelancer — classify my expenses for self-assessment."
- "What countries do you support?"
- "Explain the quality tiers."

---

## 3. Reddit Posts

### r/tax

**Title:** `I open-sourced 371 tax classification skills for AI across 134 countries`

We built OpenAccountants — an open-source set of tax skills that you upload to Claude, ChatGPT, or any LLM. Give it your bank statement and it classifies every transaction (VAT/GST, income tax, social contributions) and produces a working paper ready for your accountant.

134 countries covered. 8 have the full guided experience (Malta, UK, Germany, Australia, Canada, India, Spain, US-CA). The rest have varying levels of coverage.

We're transparent about quality: every skill has a tier from Q1 (battle-tested on real data by a practitioner) to Q5 (stub). Most are Q3 — AI-drafted with citations but not independently verified. We publish the tier so you know what you're trusting.

The idea: your accountant charges by the hour. Most of that time is classifying transactions. These skills do that work before the meeting. Your accountant reviews in 20 minutes instead of 3 hours.

Free, open-source, AGPL-3.0: https://github.com/openaccountants/openaccountants

Looking for accountants to verify country skills — if you spot an error in your country's tax rates, that's exactly the kind of PR we want.

---

### r/smallbusiness

**Title:** `Cut your accounting bill by 80% — open-source AI tax prep for 134 countries`

I'm an accountant who built an open-source project that does the grunt work of tax prep before your accountant meeting.

Upload your bank statement to Claude or ChatGPT along with your country's skill files, and it classifies every transaction, applies the right tax treatment, and produces a working paper your accountant can review and sign off on.

Instead of paying for 3 hours of transaction classification, your accountant reviews a pre-made working paper in 20 minutes.

It's free. 134 countries. Honest about limitations — most skills are AI-drafted (Q3), not fully verified. Eight countries (Malta, UK, Germany, Australia, Canada, India, Spain, US) have practitioner-tested skills.

GitHub: https://github.com/openaccountants/openaccountants

---

### r/accounting

**Title:** `Open-source project generating working papers from bank statements — looking for practitioners to verify`

Built an open-source set of tax skills for AI that produces working papers, reviewer briefs, and action lists from raw bank statements. 134 countries, covering VAT/GST, income tax, and social contributions.

The system uses conservative defaults (always assumes more tax when uncertain), cites statutes, and flags every assumption for the reviewer. It's designed to make YOUR review faster, not to replace you.

Most country skills are Q3 (AI-drafted with citations, not independently verified). We need practitioners to verify their country's rates and move skills to Q2/Q1. If you find an error — and you will — submit a PR. Your name goes on the skill publicly.

Every country we've verified so far has had errors in the AI draft. Yours probably does too.

https://github.com/openaccountants/openaccountants

---

### r/selfhosted / r/LocalLLaMA

**Title:** `MCP server for AI tax prep — 134 countries, works with Claude Desktop and Cursor`

Built an MCP (Model Context Protocol) server that gives your AI client access to 371 tax classification skills across 134 countries.

`pip install openaccountants-mcp`

Three tools: `list_jurisdictions`, `list_files(country)`, `get_file(country, filename)`. Your AI discovers what's available and loads the right skills automatically.

Works with Claude Desktop, Cursor, or any MCP-compatible client. Stdio transport. The skills themselves cover VAT/GST, income tax, and social contributions — upload a bank statement and get a classified working paper.

Quality is tiered Q1–Q5 (Q1 = practitioner-tested, Q3 = AI-drafted). We're honest about where the gaps are.

GitHub: https://github.com/openaccountants/openaccountants
PyPI: https://pypi.org/project/openaccountants-mcp/

---

## 4. Twitter/X Thread

**Thread (post each as a separate tweet):**

**1/**
I open-sourced 371 tax skills for AI across 134 countries.

Upload your bank statement to any LLM → get a classified working paper for your accountant.

Your accountant reviews in 20 min instead of 3 hours.

Free. Here's how it works 🧵

**2/**
The problem: accountants charge by the hour. Most of that time is classifying transactions — is this VAT-exempt? Business or personal? Which form line?

These skills teach the AI your country's rules. It does the classification. Your accountant just reviews.

**3/**
134 countries. 8 have the full guided experience:
- Malta
- UK
- Germany
- Australia
- Canada
- India
- Spain
- US (California)

The rest have varying coverage — many are VAT/GST only.

**4/**
We're radically honest about quality.

Every skill has a tier:
- Q1: Battle-tested on real data by a practitioner
- Q2: Research-verified against tax authority sites
- Q3: AI-drafted with citations, not independently verified

Most are Q3. We say this loudly.

**5/**
How to use it:

Option A — Manual: download your country's folder, upload to Claude/ChatGPT with your bank statement.

Option B — MCP: `pip install openaccountants-mcp` and your AI loads the right skills automatically.

**6/**
The system uses conservative defaults. When uncertain → assumes MORE tax, never less.

Every assumption is flagged. Every rate cites the statute. Your accountant can override — but they start from a defensible position.

**7/**
We need accountants and tax pros to verify country skills.

Every country we've checked has had errors in the AI draft. Yours probably does too.

Find an error → submit a PR → your name goes on the skill.

github.com/openaccountants/openaccountants

**8/**
If you're a developer: the MCP server is on PyPI and the MCP Registry.

If you're a business owner: upload the files and try it on last quarter's bank statement.

If you're an accountant: we need you to verify your country.

@AnthropicAI @OpenAI @cursor_ai

---

## 5. Twenty Tweet Ideas

Post 1-2 a day. Mix the categories. Don't post them all at once.

### Building in public (your journey)

**1.** I'm an accountant. I open-sourced 371 tax skills for AI across 134 countries.

People think accountants are boring. We're not — we're just expensive. So I'm trying to make us cheaper.

github.com/openaccountants/openaccountants

**2.** Day 1 of building in public as a solo accountant-turned-developer.

I have 20 GitHub stars, 0 contributors, and tax skills for 134 countries that nobody knows exist yet.

Let's see where this goes.

**3.** I built an MCP server that teaches Claude how to do your taxes.

Submitted it to the MCP Registry, 4 awesome lists, and 2 directories this week.

Rejection count so far: 1 (they said "verified by real accountants at times" wasn't enough QA).

They were right.

**4.** The hardest part of open-sourcing accounting isn't the code.

It's admitting that most of your AI-generated tax skills haven't been verified by a human yet.

So we publish the quality tier for every file. Q1 = battle-tested. Q3 = AI-drafted. Most are Q3.

Honesty is the product.

**5.** Got my first GitHub issue from someone in Poland who found 3 wrong tax rates.

This is the whole point. I can't verify 134 countries alone. The internet can.

### Tax insights (makes people follow you)

**6.** Your accountant charges $200/hr.

80% of that time is classifying transactions: "Is this VAT-exempt? Business or personal? Which form line?"

An LLM does that in 3 minutes.

Your accountant should review in 20 min instead of billing 3 hours. That's the future.

**7.** Fun tax fact: Malta has a 35% headline income tax rate.

But freelancers using the remittance basis effectively pay ~15%.

Most AI tax tools don't know this. Ours does (it's in the skill file, with the statute cited).

**8.** Every country we've verified has had errors in the AI-drafted tax rates.

Every. Single. One.

This is why "AI will replace accountants" is wrong. AI will draft. Humans will verify. The combo is 10x faster than either alone.

**9.** The difference between a $500 accounting bill and a $100 one:

$500 = accountant classifies 200 transactions from scratch
$100 = accountant reviews a pre-classified working paper

Same quality. Same sign-off. Different starting point.

**10.** There are 134 countries with VAT/GST systems.

I've now got AI skill files for all of them.

How many have been verified by a human? Eight.

That's the gap. That's the opportunity. That's why this is open-source.

### AI / developer audience

**11.** MCP is the most underrated distribution channel for AI tools right now.

I built a 3-tool MCP server in a day:
- list_jurisdictions
- list_files
- get_file

Now Claude automatically loads the right tax skills for any country. No uploads. No prompts.

pip install openaccountants-mcp

**12.** Hot take: the best AI use cases aren't chatbots.

They're boring domain-specific classification engines that save professionals 2 hours of grunt work.

Tax classification. Medical coding. Legal document review. The money is in the boring stuff.

**13.** I spent 3 years as an accountant before I started coding.

The thing nobody tells developers building fintech:

Tax rules aren't complex because governments are stupid. They're complex because every rule is a political compromise with a 50-year history. You can't simplify them — you have to encode them.

**14.** What happens when you give Claude 10 markdown files about Malta's tax system and a bank statement:

- 200 transactions classified in 90 seconds
- Each one cited to the relevant statute
- Conservative defaults when uncertain (more tax, never less)
- A working paper ready for accountant review

The future of accounting is already here. It's just not evenly distributed.

**15.** Everyone's building AI wrappers for APIs.

I'm building AI wrappers for tax law.

Same pattern. Wildly different stakes. If your API wrapper hallucinates, you get a 500 error. If mine hallucinates, someone underpays their taxes.

That's why we publish quality tiers.

### Engagement bait (conversation starters)

**16.** Accountants of Twitter: what's the most common mistake you see in freelancer tax returns?

Building open-source tax skills and I want to make sure we catch the real-world gotchas, not just the textbook ones.

**17.** If you could automate ONE part of your accounting workflow, what would it be?

For me it was transaction classification. 80% of the time, 20% of the brain.

**18.** Unpopular opinion: most "AI accounting" startups will fail because they don't have accountants on the team.

You can't build tax software by reading the tax code. You build it by doing 500 returns and learning where the edge cases actually are.

**19.** What's the going rate for a basic freelancer tax return in your country?

Genuinely curious. I'm seeing:
- Malta: €200-400
- UK: £300-600
- US: $400-800
- Germany: €400-1000

Reply with yours. Building a dataset.

**20.** The open-source community verified more tax rules in one week than I could verify in a year.

Turns out "your country needs you" is a surprisingly effective call to action when someone's tax rates are wrong on the internet.
