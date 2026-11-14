---
name: ma-return-assembly
description: "Use this skill to assemble and sequence the complete Moroccan filing package for a self-employed person, tax year 2026, once the regime, income, social and VAT figures are known. Trigger on \"assemble my Morocco return\", \"what do I file in Morocco\", \"Morocco filing package\", \"declaration Maroc\". Picks the one income-tax declaration for the regime (auto-entrepreneur turnover return, CPU turnover return before 1 April, or the global income return before 1 May), the VAT return cadence and the 2026 dates from the CGI, and the submission steps. Consumes ma-auto-entrepreneur, ma-cpu, morocco-professional-income-tax, ma-social-contributions and morocco-vat. Computes no tax itself."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/ma-return-assembly"
  jurisdiction: "MA"
  tax_year: "2026"
  last_updated: "2026-11-14"
---

# Morocco return assembly, filing package, tax year 2026 (assemblage de la declaration marocaine)

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

This is the final orchestrator for a Morocco-resident self-employed person (travailleur independant, auto-entrepreneur). It assembles and sequences the filing package for 2026 income and computes nothing. Every figure comes from upstream; this file decides which declaration applies for the confirmed regime, what attaches, when each filing and payment is due, and how to submit.

The tax authority is the Direction Generale des Impots (DGI), which runs the SIMPL online service. Social cover runs through the Caisse Nationale de Securite Sociale (CNSS) and the Assurance Maladie Obligatoire (AMO). Auto-entrepreneur turnover is declared and paid to the body designated for the regime (the national auto-entrepreneur platform), not on SIMPL (Art. 82 bis).

Reply in the user's language (French, English or Darija), with the native French terms. This file assumes `ma-freelance-intake` has run and the regime is confirmed. If the regime is still open, route back to intake before assembling.

## Ask the client first

Collect these from the upstream skills; do not re-ask anything intake settled.

| Input | Source skill | Used for |
|---|---|---|
| Residency, activity type (commercial or craft against services), confirmed regime | `ma-freelance-intake` | Routing the declaration |
| Annual turnover in MAD | intake or regime skill | Band checks, ceiling-breach flag |
| ICE, RC number, identifiant fiscal (IF) | intake | All DGI filings |
| Auto-entrepreneur flat tax, and whether the option is monthly or quarterly | `ma-auto-entrepreneur` | Auto-entrepreneur declaration |
| CPU liability (IR plus droit complementaire) and annual or quarterly payment choice | `ma-cpu` | CPU turnover return |
| Net profit (resultat net) under RNR or RNS | `morocco-professional-income-tax` | Global income return |
| VAT position and cadence (monthly or quarterly) | `morocco-vat` | VAT returns, if liable |
| CNSS and AMO status and contribution figures | `ma-social-contributions` | CNSS filing |
| SIMPL and platform credentials | intake | Submission |

If a content skill did not run or returned no validated output, note the gap in the reviewer brief and continue with what is available rather than halting.

## The method, step by step

1. Confirm the regime and pick exactly one income-tax track. Never file two income-tax declarations for the same activity.
2. Add the VAT returns at the cadence `morocco-vat` set, if the person is liable.
3. Add the CNSS and AMO track from `ma-social-contributions`.
4. Map every deadline to a 2026 or 2027 date from the table below.
5. Attach the schedules, submit, pay, and keep the acknowledgment.

### Rates, bands and thresholds

| Item | Rule | Conditions | Year | Source URL |
|---|---|---|---|---|
| Auto-entrepreneur declaration and payment, monthly option | Before the end of the month after the month the turnover was collected | Art. 82 bis-II. To the designated body, not SIMPL | 2026 | https://www.tax.gov.ma/wps/wcm/connect/08712531-1e81-4e28-a38b-2bd9edf8e09e/CGI+2026+FR.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-08712531-1e81-4e28-a38b-2bd9edf8e09e-pM5DEs1 |
| Auto-entrepreneur declaration and payment, quarterly option | Before the end of the month after the quarter the turnover was collected | Art. 82 bis-II. A nil period is still declared | 2026 | same |
| Auto-entrepreneur IR | 0.5% (commercial, industrial, craft) or 1% (services) of turnover collected | Art. 73-III. Figure from `ma-auto-entrepreneur` | 2026 | same |
| CPU turnover return with payment | Before 1 April of the following year | Art. 82 quater-I. For 2026 turnover, before 1 April 2027 | 2026 | same |
| CPU quarterly payment option | Four instalments of 25%, before the end of the 3rd, 6th, 9th and 12th month of the following year | Art. 173-I | 2026 | same |
| Global income return, RNR or RNS professional income | Before 1 May of the following year | Art. 82-I. For 2026, before 1 May 2027 | 2026 | same |
| Global income return, other income only | Before 1 March of the following year | Art. 82-I | 2026 | same |
| VAT, monthly regime | Taxable turnover of the prior year of MAD 1,000,000 or more, or no establishment in Morocco | Art. 108-I | 2026 | same |
| VAT, quarterly regime | Taxable turnover of the prior year under MAD 1,000,000 | Art. 108-II | 2026 | same |
| VAT monthly return, filed electronically | Before the end of each month, for the month before | Art. 110. The paper deadline (before the 20th) does not apply to electronic filers | 2026 | same |
| VAT quarterly return, filed electronically | Before the end of the first month of each quarter, for the quarter before | Art. 111 | 2026 | same |
| Electronic filing | All businesses file electronically | Art. 155-I | 2026 | same |

### Which declaration by regime

**Auto-entrepreneur** (within MAD 500,000 commercial, industrial or craft, or MAD 200,000 services, Art. 42 ter):
- Declaration: the auto-entrepreneur turnover declaration, monthly or quarterly as opted, to the designated body (Art. 82 bis). Flat IR on turnover collected from `ma-auto-entrepreneur`.
- VAT: auto-entrepreneurs are outside Art. 145 and normally do not charge VAT on this turnover; if any VAT operation exists, route to `morocco-vat`.
- Social: CNSS and AMO via `ma-social-contributions`.
- A nil period is still declared: file zero, do not skip.

**CPU** (up to MAD 2,000,000 commercial or MAD 500,000 services, Art. 41-II):
- Declaration: the annual CPU turnover return (ADP150B), one line per activity, before 1 April of the following year, with payment (Art. 82 quater-I, 173-I). The CPU is IR at 10% on turnover times the trade coefficient plus the droit complementaire for AMO, both from `ma-cpu`.
- VAT: VAT returns via `morocco-vat` if liable (CPU does not by itself remove VAT duties).
- Social: CNSS and AMO via `ma-social-contributions`.

**RNR or RNS** (above the ceilings, or by election):
- Declaration: the global income return (declaration annuelle du revenu global) on SIMPL before 1 May, with the resultat net from `morocco-professional-income-tax` (Art. 82-I).
- VAT: via `morocco-vat`.
- Social: CNSS and AMO via `ma-social-contributions`.

**Ceiling breach.** Flag it prominently. The move between regimes follows each regime's own rule (for CPU, two consecutive years over the ceiling, Art. 41-II); the reviewer sets the effective date and which declaration covers which period. Do not silently apply one regime to the whole year.

### Submission

1. For the CPU and the global income return, log in to SIMPL with the identifiant fiscal (IF) and credentials. For the auto-entrepreneur declaration, use the auto-entrepreneur platform: these are separate systems.
2. Select the one income-tax form (auto-entrepreneur, or CPU, or global income return), plus the VAT return at the cadence `morocco-vat` set, if liable.
3. Attach the schedules: accounts or P&L (etats de synthese where required under RNR, see `ma-financial-statements`), VAT reconciliation, workpapers from the content skills.
4. Pay electronically (telepaiement) at filing.
5. Save the acknowledgment (accuse de reception). A return is not filed until acknowledged.

## Boundary and exception table

| Situation | Rule | What to do |
|---|---|---|
| Two income-tax declarations prepared for one activity | One track only | Keep the one for the confirmed regime |
| Auto-entrepreneur with nil turnover in a period | Still declares (Art. 82 bis) | File zero |
| CPU payer chose quarterly payment | Four 25% instalments in the following year (Art. 173-I) | Diarise the four dates |
| VAT filer using paper dates (the 20th) | Electronic filing is mandatory (Art. 155-I); the end-of-month date applies (Art. 110, 111) | Use the electronic deadline |
| Turnover crossed MAD 1,000,000 in 2026 | Monthly VAT from 2027 (Art. 108-I) | Tell `morocco-vat` |
| Upstream skill missing | Note the gap | Continue, flag in the brief |
| Mid-year ceiling breach | Reviewer sets the effective date | Flag; do not pick one regime for the year |

## Worked cases

**Case: CPU general food shop, 2026 CPU of MAD 4,530 (IR 2,250 plus droit complementaire 2,280, from `ma-cpu`), quarterly payment chosen.** The CPU turnover return is due before 1 April 2027. Quarterly payment splits the MAD 4,530 into four instalments of 25%: MAD 1,132.50 each, before the end of March, June, September and December 2027. The shop's VAT, if it is liable, runs on its own cadence: taxable turnover under MAD 1,000,000, so quarterly, each return before the end of the first month of the next quarter.

```oa-check
name: CPU 4530 paid quarterly
inputs:
  ir: 2250
  droit: 2280
steps:
  - cpu: ir + droit
  - instalment: cpu * 0.25
expected:
  cpu: 4530
  instalment: 1132.50
```

## When to refuse or refer

- The regime is not confirmed: route back to `ma-freelance-intake`.
- A company (IS), a non-resident, or a foreign establishment: refer to a Moroccan expert-comptable.
- Late returns, penalties already charged, a DGI letter or an audit: refer.
- This skill computes no tax. All amounts come from the content skills and must be reviewed and signed off by a qualified Moroccan expert-comptable before anything is filed with the DGI, CNSS or the auto-entrepreneur platform.

## Filing and payment

The dates are in the rates table above. In short, for 2026 income: auto-entrepreneur monthly or quarterly through 2026 and January 2027; CPU before 1 April 2027 (or four quarterly instalments in 2027); global income return before 1 May 2027; VAT monthly before the end of each month or quarterly before the end of the first month of each quarter; CNSS on its own schedule (see `ma-social-contributions` and `morocco-payroll`, where the CNSS dates are not yet confirmed).

## Completion checklist

- [ ] Intake complete; residency, activity type and regime confirmed.
- [ ] Exactly one income-tax declaration selected (auto-entrepreneur, CPU or global income return).
- [ ] Turnover checked against the band; any ceiling breach flagged with the effective date for the reviewer.
- [ ] VAT turnover reconciled with income-tax turnover or net (flag any mismatch).
- [ ] VAT returns at the right cadence, or confirmed not liable.
- [ ] CNSS and AMO registration current and contributions reconciled.
- [ ] Every deadline mapped to a date from the rates table.
- [ ] Right portal selected (SIMPL for CPU and the global income return; the auto-entrepreneur platform for its declaration); credentials working.
- [ ] Payment method ready; tax-due figure from the content skills.
- [ ] All open flags (deadlines, ceiling breach, data gaps, defaults) in the reviewer brief.
- [ ] Package routed for Moroccan expert-comptable sign-off before submission.

## Sources

| Source | URL | Read on |
|---|---|---|
| Code Général des Impôts 2026, DGI, French edition. Read for Art. 41-II and 42 ter limits, Art. 73-III auto-entrepreneur rates, Art. 82-I global return dates, Art. 82 bis auto-entrepreneur declaration dates, Art. 82 quater CPU return date, Art. 108 VAT cadence (MAD 1,000,000), Art. 110 and 111 VAT return dates, Art. 155 electronic filing, Art. 173-I CPU instalments | https://www.tax.gov.ma/wps/wcm/connect/08712531-1e81-4e28-a38b-2bd9edf8e09e/CGI+2026+FR.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-08712531-1e81-4e28-a38b-2bd9edf8e09e-pM5DEs1 | 2026-11-14 |

Not yet confirmed: the name and address of the auto-entrepreneur platform and its operator for 2026; CNSS filing cadence for self-employed people (see `ma-social-contributions`); SIMPL screen names and form numbers other than ADP150B.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-14. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `ma-return-assembly` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/ma-return-assembly. If neither is available, confirm every figure against the official source pages cited above before relying on it.
