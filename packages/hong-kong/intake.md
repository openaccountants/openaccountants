# Intake — Onboarding for Hong Kong

> This file guides the AI through the onboarding process.
> It runs BEFORE any classification begins.

## Step 1: Scope Check

Ask these questions as a batch. Do not explain the workflow. Just ask.

| # | Question |
|---|----------|
| 1 | Were you a full-year Hong Kong resident in 2025? |
| 2 | What is your business structure? (Sole trader / self-employed / LLC / partnership / limited company) |
| 3 | Are you registered for VAT/GST? If yes, what type? |
| 4 | Do you have employees? |
| 5 | What industry/sector are you in? |

## Refusals (STOP if any trigger)

| Trigger | Response |
|---------|----------|
| Not full-year resident | "I'm set up for full-year Hong Kong residents only. You need a qualified tax professional who handles non-resident returns." |
| Partnership | "Partnerships file separately. You need a qualified tax professional familiar with partnership returns." |
| Limited company / corporation | "I don't cover corporate returns. You need a qualified tax professional." |
| Has employees | "Payroll and employer obligations are outside my scope. You need a qualified tax professional." |

If all checks pass, continue.

## Step 2: Document Upload

Ask the user to upload everything they have:
- Bank statements (CSV or PDF) for the full year
- Sales invoices (especially for cross-border or zero-rated supplies)
- Purchase invoices for any significant claims
- Prior year return (if available)
- Any VAT/GST returns filed during the year

Say: **"Drop all your documents here — bank statements, invoices, prior returns. Everything you have for 2025."**

## Step 3: Inference

Read the documents and extract:
- Gross revenue / turnover
- Major expense categories
- VAT/GST collected and paid (if registered)
- Tax payments already made (estimated/provisional)
- Client breakdown (domestic vs international)
- Capital items purchased

Present a summary and ask: **"Does this look right? Anything missing or wrong?"**

## Step 4: Gap Filling

Ask ONLY about things the documents don't answer:
- Business use percentage (vehicle, phone, home office)
- Any elections made (simplified expenses, cash basis, etc.)
- First year in business?

Then proceed to classification using the loaded country skills.

---

*OpenAccountants — openaccountants.com*
*All outputs must be reviewed by a qualified tax professional before filing.*
