# OpenAccountants Intelligence Roadmap

What separates a billion-dollar tax intelligence system from a collection of markdown files.

---

## Where we are

We have **345 skills**, **8 end-to-end jurisdictions**, and a **manifest-based routing system**. The skills compute tax correctly for a given set of facts in a single jurisdiction. This is table stakes — it's what any tax software does.

## Where we need to be

The system should be **smarter than any individual accountant** at the things accountants do poorly: cross-border interactions, deadline tracking, optimization opportunities, pattern recognition, and keeping up with law changes. No single accountant knows 134 jurisdictions. This system does.

---

## Level 1: Cross-Border Intelligence (nobody else has this)

### The problem

A freelance developer in Malta sells software to a German client. The Malta VAT skill says "EU B2B service = reverse charge, Box 3/6 output, no Malta VAT charged." The Germany VAT skill says "reverse charge from EU supplier = Vorsteuer and Umsatzsteuer self-assessment." But today, these skills don't talk to each other.

The same developer also has a US client. Different rules again — non-EU, no reverse charge framework, just zero-rated export of services.

And if that developer exceeds the €10,000 OSS threshold selling digital products to EU consumers? Now they need to register in the consumer's country or use One-Stop-Shop.

### What to build

A **cross-border skills layer** that sits between content skills and triggers when transactions cross jurisdictions:

```
skills/cross-border/
├── eu-reverse-charge.md           ← B2B services between EU states
├── eu-oss-digital.md              ← OSS for digital B2C sales to EU consumers
├── eu-intra-community-goods.md    ← Physical goods between EU states
├── non-eu-export-services.md      ← Services to non-EU clients
├── non-eu-import-services.md      ← Services received from non-EU suppliers
├── withholding-tax-matrix.md      ← Which countries withhold on what payments
├── tax-treaty-lookup.md           ← Double taxation relief by country pair
├── permanent-establishment.md     ← When cross-border activity creates PE risk
└── transfer-pricing-risk.md       ← When intra-group pricing triggers scrutiny
```

**The withholding tax matrix** is especially valuable — a simple lookup:

```
FROM → TO:    US    UK    DE    MT    IN    SG    ...
Royalties:    0%    20%   15%   0%    10%   10%
Services:     0%    0%    0%    0%    10%   0%
Interest:     0%    20%   0%    0%    10%   15%
Dividends:    15%   0%    15%   0%    10%   0%
```

Every freelancer with international clients needs this. No consumer tax product handles it well.

---

## Level 2: Tax Optimisation Engine

### The problem

Today, skills compute what you owe. They don't tell you what you COULD owe if you made different choices. A good accountant spots opportunities: "You're close to the QBI cliff — a Solo 401(k) contribution would drop you below the threshold and save $4,200."

### What to build

An **optimisation layer** that runs AFTER the base computation and identifies savings:

```
skills/optimisation/
├── retirement-contribution-optimiser.md    ← "Contributing €X to [vehicle] saves €Y"
├── entity-structure-analyser.md            ← "S-corp election would save $X at your income level"
├── deduction-maximiser.md                  ← "You have €X of unclaimed deductions"
├── timing-optimiser.md                     ← "Deferring this invoice to next month saves €X in VAT"
├── threshold-proximity-alerts.md           ← "You're €X from the [VAT registration / QBI cliff / etc.] threshold"
├── jurisdiction-comparison.md              ← "If you operated from [country B], your total tax would be €X less"
├── loss-harvesting.md                      ← "Realising this loss now creates €X of future relief"
└── election-advisor.md                     ← "You can elect [simplified expenses / cash basis / presumptive] — here's the comparison"
```

**How it works:** After the return assembly runs, the optimisation layer does a second pass:

```
For each optimisation skill:
  1. Read the computed return figures
  2. Model the alternative scenario
  3. Calculate the delta
  4. If delta > materiality threshold → add to reviewer brief as "Optimisation opportunity"
```

The reviewer sees: "3 optimisation opportunities identified. Total potential savings: €4,200. See Section F of reviewer brief."

This is what separates an AI tax system from tax software. Software computes. Intelligence advises.

---

## Level 3: Temporal Intelligence

### The problem

Tax law changes mid-year. India's GST rates changed in September 2025. Canada's lowest bracket changed July 2025. Spain's food VAT reductions expired January 2025. A transaction dated March 2025 has different rules than one dated October 2025.

Today, skills have ONE set of rates. They don't handle mid-year transitions.

### What to build

**Temporal versioning** in every skill:

```yaml
# In skill frontmatter
rates_timeline:
  - effective: 2025-01-01
    expires: 2025-06-30
    standard_rate: 15%
    note: "Pre-reform rate"
  - effective: 2025-07-01
    expires: null
    standard_rate: 14%
    note: "Post-reform rate (Bill C-59)"
```

**In the classification logic:**

```
When classifying a transaction:
  1. Read transaction date
  2. Look up rates_timeline for the period containing that date
  3. Apply the rate effective at that date
  4. If transaction spans a rate change boundary → split and apply both rates
```

**This also enables:**
- Automatic transition period handling (e.g., "invoiced December at 15%, paid January at 14% — which rate applies?")
- Historical return preparation (not just current year)
- Proactive alerts ("rates are changing on [date] — here's what changes for you")

---

## Level 4: Transaction Pattern Intelligence

### The problem

After processing thousands of bank statements, we see the same patterns: Stripe payouts, AWS charges, WeWork payments, Uber receipts, Adobe subscriptions. Today, each transaction is classified from scratch. The system doesn't learn.

### What to build

A **transaction pattern library** — a shared knowledge base of common counterparties and their tax treatment:

```
skills/patterns/
├── global-saas-vendors.md       ← Stripe, AWS, Google, Adobe, Microsoft, Slack, Notion...
├── global-payment-processors.md ← PayPal, Wise, Revolut, Square...
├── global-travel.md             ← Uber, Booking.com, Airbnb, airlines...
├── global-coworking.md          ← WeWork, Regus, Impact Hub...
├── global-professional.md       ← Accountants, lawyers, insurance providers...
└── [country]-common-vendors.md  ← Country-specific common counterparties
```

Each entry:

```
| Counterparty | Variations in bank statements | Default classification | VAT/GST treatment | Notes |
|---|---|---|---|---|
| Stripe | "STRIPE PAYMENTS", "STRIPE CONNECT", "STRIPE ATLAS" | Revenue (payment processor, not the sale) | No VAT on fees (financial service) | Net amount = gross revenue minus fees |
| Amazon Web Services | "AWS EMEA", "AMAZON WEB SERVICES" | IT infrastructure (hosting) | Reverse charge if cross-border B2B | Monthly billing, USD conversion |
| WeWork | "WEWORK", "THE WE COMPANY" | Office rent / coworking | Standard rate (commercial property) | Check if member or daily pass |
```

**Why this matters:** Instead of the user answering "what is this transaction?" for every AWS charge, the system recognises it instantly. Classification time drops from 30 minutes to 5 minutes for a typical bank statement.

---

## Level 5: Proactive Deadline Intelligence

### The problem

A freelancer in Spain has: IVA quarterly (Modelo 303) due Apr 20 / Jul 20 / Oct 20 / Jan 30. IRPF quarterly (Modelo 130) due same dates. RETA monthly due last business day. Annual IRPF (Modelo 100) due Jun 30. Modelo 390 (annual IVA summary) due Jan 30.

Missing any deadline = penalties. Most freelancers miss at least one per year.

### What to build

A **deadline engine** that reads the manifest + skill metadata and generates a personalised filing calendar:

```
skills/intelligence/
├── deadline-engine.md           ← Generates filing calendar from jurisdiction + obligations
├── penalty-calculator.md        ← "You're 3 days late — here's the penalty"
└── reminder-scheduler.md        ← "Your Q2 Modelo 303 is due in 14 days"
```

**How it works:**

```
1. Read user's jurisdiction + obligations from their profile
2. For each obligation, look up filing frequency and deadlines from the content skill
3. Generate a personalised calendar:

   Your filing calendar (2025):

   Jan 20  — Modelo 303 (Q4 2024 IVA) + Modelo 130 (Q4 2024 IRPF)
   Jan 30  — Modelo 390 (Annual IVA summary)
   Jan 31  — RETA cuota (January)
   Feb 28  — RETA cuota (February)
   Mar 31  — RETA cuota (March)
   Apr 20  — Modelo 303 (Q1 IVA) + Modelo 130 (Q1 IRPF)
   ...
   Jun 30  — Modelo 100 (Annual IRPF)

4. Send reminders via the platform 14 days and 3 days before each deadline
```

**Revenue opportunity:** This is a SaaS feature — users pay for the reminder service even if they don't use the full return preparation.

---

## Level 6: Feedback Loop Intelligence

### The problem

When a practitioner reviews a return and corrects something, that correction is lost. The skill doesn't learn. The same error appears for the next user.

### What to build

A **correction feedback system:**

```
1. Practitioner reviews output via checklist
2. Practitioner marks item as "Disagree" with correction
3. Correction is logged:
   {
     "skill": "germany-vat-return",
     "item": "reverse charge on EU services",
     "original_position": "Box 9a input",
     "correction": "Should be Box 9 (goods, not services)",
     "practitioner": "name",
     "credential": "StB",
     "date": "2026-05-15"
   }
4. After N corrections on the same item → skill is flagged for update
5. Correction pattern analysis → identifies systematic errors across skills
```

**This creates a flywheel:**
- More users → more reviews → more corrections → better skills → more trust → more users

**This is the moat.** Open-source skills can be copied. A correction feedback loop that makes the skills better over time cannot.

---

## Level 7: Multi-Entity Intelligence

### The problem

Today: one person, one jurisdiction, one business. But real life:
- A developer with an SMLLC in the US AND a sole proprietorship in Malta
- A consultant who operates through a holding company in Cyprus and a trading company in the UK
- A freelancer who incorporates to optimize tax and needs the S-corp vs sole prop comparison

### What to build (future — not now)

A **multi-entity orchestrator** that handles:
- Multiple entities for one person
- Entity comparison / optimization
- Consolidated view across entities
- Inter-entity transaction elimination

This is Phase 3+ material. Mention it in the roadmap but don't build it yet.

---

## Implementation priority

| Level | Impact | Effort | When |
|-------|--------|--------|------|
| **Level 1: Cross-border** | Very high — unique differentiator | Medium — 8-10 skills | Next session |
| **Level 2: Optimisation** | Very high — this is what users pay for | Medium — 8 skills | Next session |
| **Level 4: Transaction patterns** | High — massive UX improvement | Low — 5-6 reference files | Next session |
| **Level 5: Deadline engine** | High — SaaS revenue opportunity | Low — 3 skills | Next session |
| **Level 3: Temporal versioning** | Medium — correctness improvement | Medium — schema change across all skills | Month 2 |
| **Level 6: Feedback loops** | Very high long-term — creates the moat | High — requires platform integration | Month 2-3 |
| **Level 7: Multi-entity** | Medium — advanced users only | High | Month 4+ |

---

## What this makes us

| | Tax software (TurboTax, Xero Tax) | Human accountant | OpenAccountants (with intelligence) |
|---|---|---|---|
| **Jurisdictions** | 1-3 | 1-2 | 134+ |
| **Cross-border** | No | Some (if specialised) | Yes — systematic |
| **Optimisation** | Basic | Yes (if good) | Systematic, never misses |
| **Deadline tracking** | Yes (for their jurisdictions) | Manual | Automatic, all jurisdictions |
| **Pattern recognition** | Yes (for their integrations) | Yes (from experience) | Yes (from shared library) |
| **Learning from corrections** | No | Yes (individual) | Yes (collective — every correction improves it for everyone) |
| **Cost** | $50-200/year | $500-5,000/year | $X/year (you decide) |

**The positioning:** Not "cheaper than an accountant" — "smarter than any individual accountant because it knows 134 jurisdictions, never forgets a deadline, and learns from every practitioner who uses it."
