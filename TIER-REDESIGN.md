# Tier System Redesign

Based on audit of 7 key skills (Malta VAT, Germany VAT, Malta IT, Malta SSC, India GST, UK VAT, Australia GST).

---

## What we found

39% of all tier tags are noise (statutory facts tagged [T1]).
16% of T2 items could be resolved with one onboarding question.
Only 18% of T2 is genuinely unknowable.

## The new system

### 1. Facts don't get tags

Statutory rates, form numbers, deadlines, penalties — these are just facts. They don't need a confidence label. "VAT rate 18%" is not "T1 deterministic" — it's just 18%.

### 2. Tiers are about DATA, not rules

**Classified** — the source documents carry enough information to apply the rule. No flag needed.

**Assumed** — a fact is missing. We applied the conservative default. Disclosed in the reviewer brief. These items fall into two sub-categories:

- **Askable** — we can resolve it with one question at onboarding. "Are you in hospitality?" "Do you have a home office?" "Is this the first supply of this property?" These should be moved to the intake skill's question list. Once asked, they become Classified.

- **Unknowable** — we genuinely cannot determine this without investigation. "What was this cash withdrawal for?" "What % of your vehicle use is business?" "Is this SaaS billed from Ireland or the US?" These stay as Assumed with conservative default + reviewer flag.

**Out of scope** — the situation triggers a refusal. Too complex, too risky, or outside the skill's coverage. Stop, refuse, refer.

### 3. The intake feeds the classification

Every "Askable Assumed" item in a content skill should become a question in the intake skill. The content skill's Tier 2 catalogue IS the intake skill's question list. They're designed together.

The goal: **minimize Assumed items by maximizing what we ask at onboarding.**

### 4. What changes in each skill

**Remove:** [T1] tags on statutory facts (rates, form numbers, deadlines, penalties, thresholds)

**Keep:** Classification rules that are genuinely deterministic lookups (supplier pattern library, transaction classification matrices)

**Move to intake:** Every [T2] item where one question resolves it (industry, exempt supplies, home office, vehicle use, registration type)

**Keep as Assumed:** Items that are genuinely unknowable (cash withdrawals, SaaS billing entity, bad debt verification, mixed-use splits without documentation)

**Fix:** Items tagged [T2] because the skill author wasn't sure about a threshold — research it and make it a fact

### 5. The supplier pattern library replaces most T1 classification

Instead of tagging each rule [T1], build a lookup table:
- "If bank statement says X, classify as Y"
- The table IS the T1 system — no tags needed
- Anything NOT in the table falls through to Tier 2 logic

### 6. Per-country T2 catalogue

Each country has its own list of "things we can't determine from documents alone." This list is:
- Different per country (Malta entertainment rules ≠ Germany Bewirtungskosten rules)
- The basis for the country's intake questions
- The source of conservative defaults
- The driver of the review checklist

---

## Action plan

1. Start with Malta VAT v2.0 as the gold standard (already done — no inline tags, sections handle tiers)
2. Rewrite Germany VAT to match (agent running)
3. Convert remaining skills in batches — remove noise tags, build supplier pattern libraries, move askable items to intakes
4. Update workflow base to reflect new tier philosophy (done)
5. Update manifest to track which skills have been converted

---

## Metrics

After conversion, each skill should have:
- **Zero** [T1] tags on statutory facts
- **A supplier pattern library** with 20-60 country-specific vendor patterns
- **An "Askable" list** that maps to the intake skill's questions
- **An "Unknowable" list** of 5-15 genuinely ambiguous items with conservative defaults
- **A refusal catalogue** of out-of-scope situations
