# OpenAccountants — User Stories & Orchestration Plan

How real users will interact with the platform, and what we need to build to make it work.

---

## The core problem

Today: **California freelancers have a complete end-to-end flow.** Everyone else hits a wall.

We have 346 skill files covering 134 countries. But skills without orchestration are like ingredients without a recipe — a user can't cook with them.

---

## What a user actually needs

```
User says: "I'm a freelance developer in [country]. Help me with my taxes."
                                    │
                                    ▼
                        ┌─────────────────────┐
                        │  GLOBAL ROUTER       │
                        │  Detects jurisdiction │
                        │  + business type      │
                        └──────────┬──────────┘
                                   │
                    ┌──────────────┼──────────────┐
                    ▼              ▼              ▼
              ┌──────────┐  ┌──────────┐  ┌──────────┐
              │ US Intake │  │ UK Intake│  │ MT Intake│  ...
              └────┬─────┘  └────┬─────┘  └────┬─────┘
                   │             │             │
                   ▼             ▼             ▼
              ┌──────────┐  ┌──────────┐  ┌──────────┐
              │ US Return │  │ UK Return│  │ MT Return│
              │ Assembly  │  │ Assembly │  │ Assembly │
              └──────────┘  └──────────┘  └──────────┘
```

**Three layers needed for each jurisdiction:**
1. **Router** — one global skill that detects jurisdiction and hands off
2. **Intake** — jurisdiction-specific: refusal sweep, document upload, inference
3. **Return Assembly** — jurisdiction-specific: chains content skills in order

---

## User Stories

### Story 1: California freelance developer (WORKS TODAY)

> **Alex, 32, software contractor in San Francisco, SMLLC**
>
> "Help me prepare my 2025 tax return. I'm a freelance software developer, single-member LLC in California."
>
> **What happens:**
> 1. `us-ca-freelance-intake` fires automatically
> 2. 3-question refusal sweep (residency, structure, work type)
> 3. Alex uploads bank statements, 1099s, prior return
> 4. Claude infers: $185K gross, $12K expenses, Solo 401(k), Covered California
> 5. Alex confirms, answers 2 gap-fill questions (home office, business use %)
> 6. Federal assembly runs: bookkeeping → Schedule C/SE → retirement → QBI → 1040
> 7. CA assembly runs: Form 540 + Form 568 + 540-ES
> 8. Output: Excel working paper + reviewer brief + action list
> 9. Alex logs in to openaccountants.com → requests CPA review → files
>
> **Status: COMPLETE. Works end to end.**

---

### Story 2: UK freelance designer in London (BROKEN TODAY)

> **Sarah, 28, freelance graphic designer in London, sole trader**
>
> "I need help with my Self Assessment. I'm a freelance designer in London."
>
> **What happens today:** Nothing. No intake skill exists. Sarah is rejected.
>
> **What SHOULD happen:**
> 1. Global router detects "London" / "Self Assessment" → routes to `uk-freelance-intake`
> 2. Refusal sweep: UK residency? Sole trader? (not partnership/LLP/Ltd?) No crypto/rental/employment?
> 3. Sarah uploads bank statements + invoices
> 4. Claude infers: £65K turnover, £8K expenses, student loan Plan 2
> 5. Sarah confirms, answers gap-fill (simplified expenses election? use of home?)
> 6. UK assembly runs:
>    - `uk-self-employment-sa103` (trading income computation)
>    - `uk-income-tax-sa100` (personal allowance, tax bands, final calc)
>    - `uk-national-insurance` (Class 2 + Class 4)
>    - `uk-student-loan-repayment` (Plan 2 threshold check)
>    - `uk-payments-on-account` (Jan/Jul payment schedule)
>    - `uk-vat-return` (if VAT registered — £85K threshold check)
> 7. Output: Working paper + reviewer brief
> 8. Sarah logs in → requests chartered accountant review → files via HMRC
>
> **Skills needed:**
> - `uk-freelance-intake.md` (NEW)
> - `uk-return-assembly.md` (NEW)
> - Content skills exist but are Q4 stubs — need content

---

### Story 3: German freelance developer in Berlin (BROKEN TODAY)

> **Max, 35, freelance developer in Berlin, Freiberufler**
>
> "Ich brauche Hilfe mit meiner Steuererklärung. Freelance Softwareentwickler in Berlin."
>
> **What SHOULD happen:**
> 1. Global router detects "Berlin" / "Steuererklärung" / "Freelance" → `de-freelance-intake`
> 2. Refusal sweep: German resident? Freiberufler or Gewerbetreibender? No employees? No Kleinunternehmer?
> 3. Max uploads Kontoauszüge (bank statements) + Rechnungen (invoices)
> 4. Claude infers: €95K Umsatz, €12K Betriebsausgaben, Krankenversicherung privat
> 5. Max confirms
> 6. DE assembly runs:
>    - `germany-vat-return` (UStVA — already Q1!)
>    - `de-income-tax` (Einkommensteuererklärung)
>    - `de-trade-tax` (Gewerbesteuer — only if Gewerbetreibender)
>    - `de-social-contributions` (KV, RV if applicable)
>    - `de-estimated-tax` (Vorauszahlungen)
> 7. Output: Working paper + reviewer brief
> 8. Max logs in → requests Steuerberater review → files via ELSTER
>
> **Skills needed:**
> - `de-freelance-intake.md` (NEW)
> - `de-return-assembly.md` (NEW)
> - `de-income-tax.md` is Q4 stub — needs content
> - `germany-vat-return.md` is Q1 — ready

---

### Story 4: Maltese freelance accountant in Valletta (PARTIALLY WORKS)

> **Maria, 40, self-employed accountant in Valletta**
>
> "Help me with my TA24 and VAT return."
>
> **What happens today:** Malta content skills (income tax, SSC, VAT) are all Q1, but there's no intake or assembly to chain them.
>
> **What SHOULD happen:**
> 1. Global router → `mt-freelance-intake`
> 2. Refusal sweep: Malta resident? Self-employed (not TA22 part-time)? Article 10 or 11 VAT?
> 3. Maria uploads bank statements + invoices
> 4. MT assembly runs:
>    - `malta-vat-return` (Malta VAT return — Q1!)
>    - `malta-income-tax` (TA24 — Q1!)
>    - `malta-ssc` (Class 2 — Q1!)
>    - `mt-estimated-tax` (provisional tax — Q4 stub)
> 5. Output: Working paper + reviewer brief
> 6. Maria logs in → requests warranted accountant review → files via CFR
>
> **Skills needed:**
> - `mt-freelance-intake.md` (NEW)
> - `mt-return-assembly.md` (NEW)
> - Content skills are Q1 — READY
> - This is the lowest-hanging fruit after US-CA

---

### Story 5: Indian freelance developer in Bangalore (BROKEN TODAY)

> **Priya, 29, freelance developer in Bangalore**
>
> "Help me file my ITR and GST returns."
>
> **What SHOULD happen:**
> 1. Global router → `in-freelance-intake`
> 2. Refusal sweep: Indian resident? Presumptive taxation (44ADA) eligible? Old or new tax regime?
> 3. Priya uploads bank statements + GST portal data
> 4. IN assembly runs:
>    - `india-gst` (GSTR-3B + GSTR-1 — Q2!)
>    - `in-income-tax` (ITR-4 presumptive or ITR-3 — Q4 stub)
>    - `in-advance-tax` (quarterly instalments — Q4 stub)
>    - `in-tds-freelance` (TDS certificates — Q4 stub)
> 5. Output: Working paper + reviewer brief
> 6. Priya logs in → requests CA review → files via income tax portal
>
> **Skills needed:**
> - `in-freelance-intake.md` (NEW)
> - `in-return-assembly.md` (NEW)
> - Income tax skills are Q4 stubs — need content

---

### Story 6: Freelancer who moved mid-year (REFUSED — BY DESIGN)

> **Tom, 30, moved from New York to London in June 2025**
>
> "I need help filing taxes. I was in NYC for half the year and London for the second half."
>
> **What happens:** Global router detects multi-jurisdiction → HARD REFUSAL.
> "I handle single-jurisdiction, full-year residents only. You need a CPA/tax advisor who handles international tax and multi-jurisdiction filings. I can't help with split-year residency."
>
> **This is correct behaviour.** Cross-border is T3 — out of scope.

---

### Story 7: Small business owner with employees (REFUSED — BY DESIGN)

> **Lisa, 45, runs a 5-person design studio in Melbourne**
>
> "Help me with my business taxes and BAS."
>
> **What happens:** Intake detects employees → HARD REFUSAL.
> "I'm built for sole traders and single-person businesses. You have employees, which means PAYG withholding, super guarantee, and WorkCover — I don't cover those. You need a registered tax agent."
>
> **Correct. Payroll is out of scope.**

---

## What we need to build

### 1. Global Router (NEW — highest priority)

A single skill that acts as the universal entry point:

```
File: skills/orchestrator/global-freelance-router.md

Purpose:
- Detect jurisdiction from user's message (country, city, tax system mentions)
- Detect business type (freelancer, sole prop, contractor)
- Route to the correct jurisdiction-specific intake
- If no intake exists for that jurisdiction → helpful refusal with explanation
```

### 2. Jurisdiction Intake Template (NEW)

A template that every country's intake follows:

```
File: skills/orchestrator/intake-template.md

Standard sections:
- Step 0: Jurisdiction confirmation
- Step 1: Refusal sweep (3-5 gating questions)
- Step 2: Document upload prompt
- Step 3: Inference pass
- Step 4: Gap-fill questions
- Step 5: Handoff to return assembly
```

### 3. Priority intake + assembly skills to build

| Jurisdiction | Intake | Assembly | Content ready? |
|-------------|--------|----------|----------------|
| **Malta** | NEW | NEW | Q1 — all 3 content skills ready |
| **UK** | NEW | NEW | Q4 stubs — need content |
| **Germany** | NEW | NEW | Q1 VAT, Q4 stubs for rest |
| **Australia** | NEW | NEW | Q2 GST, Q4 stubs for rest |
| **India** | NEW | NEW | Q2 GST, Q4 stubs for rest |
| **Canada** | NEW | NEW | Q2 GST/HST, Q4 stubs for rest |
| **US-NY** | NEW | NEW | Q2 IT-201 + IT-204-LL ready |
| **Spain** | NEW | NEW | Q2 VAT, Q4 stubs for rest |
| **UAE** | NEW | NEW | Q2 VAT, Q4 stubs for rest |

### 4. Orchestration build order

```
Phase 1 (immediate — before launch):
  ✅ Global router
  ✅ Malta intake + assembly (all content Q1, fastest to complete)
  ✅ US-NY intake + assembly (content Q2, extends existing US flow)

Phase 2 (first month):
  ○ UK intake + assembly + fill content skill stubs
  ○ Germany intake + assembly + fill income tax stub
  ○ Australia intake + assembly + fill content stubs

Phase 3 (months 2-3):
  ○ India, Canada, Spain, UAE intake + assembly
  ○ Fill content stubs for these jurisdictions
```
