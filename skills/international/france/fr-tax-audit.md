---
name: fr-tax-audit
description: French tax audit procedures, penalties, and taxpayer rights (contrôle fiscal). Trigger on phrases like "contrôle fiscal", "vérification de comptabilité", "redressement fiscal", "DGFIP contrôle", "proposition de rectification", "pénalités fiscales", "majoration 40%", "manquement délibéré", "intérêts de retard", "abus de droit", "commission départementale", "recours hiérarchique", "charte du contribuable vérifié", "FEC contrôle", "rejet de comptabilité", "acte anormal de gestion", "tax audit France", "tax penalties France", "objection tax France", "délai de reprise", "prescription fiscale", "régularisation spontanée". Covers the 8 verification axes (FEC, IS, charge deductibility, CCA 455, revenue, TVA, fixed assets, international), penalty schedules, audit procedures, and taxpayer rights.
version: 1.0
jurisdiction: FR
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# FR Tax Audit

## France — Tax Audit Procedures & Penalties (Contrôle Fiscal) v1.0

> **Based on work by [Romain Simon (@romainsimon)](https://github.com/romainsimon/paperasse)**, licensed under MIT. Adapted for the OpenAccountants format.

> **Disclaimer:** This skill is for informational purposes only and does not constitute tax advice. All positions must be reviewed and signed off by a qualified expert-comptable or avocat fiscaliste before filing. Get this reviewed at **openaccountants.com**.

## Section 1 — Quick Reference

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | France |
| Authority | Direction Générale des Finances Publiques (DGFiP) |
| Scope | Vérification de comptabilité of IS/IR entities |
| Key legislation | Livre des Procédures Fiscales (LPF), CGI |
| FEC obligation | art. L. 47 A-I LPF |

## Section 2 — Audit Procedure (Phases)

**Audit Procedure Phases**  _(art. L. 47 LPF; art. L. 47 A-I LPF; art. L. 13 LPF; art. L. 57 LPF)_

| Phase | Legal basis | Description |
| --- | --- | --- |
| 1. Avis de vérification | art. L. 47 LPF | Minimum 2 business days advance notice |
| 2. FEC examination | art. L. 47 A-I LPF | Mandatory delivery within 15 days |
| 3. On-site verification | art. L. 13 LPF | At registered office |
| 4. Proposition de rectification | art. L. 57 LPF | Formal notification of adjustments |
| 5. Taxpayer response | — | 30 days (extendable by 30 days) |
| 6. Inspector's response | — | Confirmation or abandonment of each item |
| 7. Commission départementale | — | In case of persistent disagreement |
| 8. Mise en recouvrement | — | Issuance of amended tax notice |

### Taxpayer guarantees

**Taxpayer guarantees**  _(art. L. 47 LPF; LPF; art. L. 52 LPF)_

| Right | Source |
| --- | --- |
| Oral and adversarial debate | art. L. 47 LPF |
| Charte du contribuable vérifié | LPF |
| Hierarchical appeal (interlocuteur départemental) | LPF |
| Departmental tax commission | LPF |
| Maximum audit duration: 3 months for SMEs | art. L. 52 LPF |

## Section 3 — The 8 Verification Axes

### Axis 1: FEC Examination (art. L. 47 A-I LPF)

**Mandatory checks on the FEC file**  _(art. L. 47 A-I LPF)_

| Check | Consequence of failure |
| --- | --- |
| Format conformity (18 columns, pipe `\ | ` separator) |
| Global balance: total debits = total credits | Comptabilité non probante |
| Per-entry balance: each EcritureNum is balanced | Presumption of concealment |
| Sequential numbering (no gaps) | Presumption of concealment |
| Dates within the financial year | Fictitious entries |
| No negative amounts | Format violation |
| PieceRef populated for every entry | Missing supporting documents |
| CompteNum consistent with PCG roots | Irregular accounts |

- **Non-compliant FEC → comptabilité non probante** — Non-compliant FEC → comptabilité non probante: burden of proof shifts to the taxpayer.  _(art. L. 192 LPF)_

### Axis 2: Corporate Tax (IS) Control (art. 38–39 CGI)

**IS control checkpoints**  _(art. 38–39 CGI)_

| Checkpoint | Legal basis | Detail |
| --- | --- | --- |
| IS add-back (account 695) | art. 39-1-4° CGI | IS is not deductible — verify it is added back |
| PME reduced rate eligibility | art. 219-I-b CGI | CA < EUR 10M, capital paid up, ≥75% held by individuals |
| Short year proration | art. 219-I-b CGI | EUR 42,500 × (days / 365) |
| Non-deductible charges | art. 39 CGI | Fines, luxury expenses, personal expenses |
| Acte anormal de gestion | Case law (CE) | Charges unrelated to business interest |

### Axis 3: Charge Deductibility (art. 39-1 CGI)

**Four cumulative conditions:**
1. Incurred in the interest of the business
2. Reflects normal management
3. Supported by invoices/documentation
4. Results in a decrease of net assets

**Systematic examination grid**  _(art. 39-1 CGI)_

| Account | Typical audit question |
| --- | --- |
| 604 (Subcontracting, APIs) | Exclusively professional use? Invoices in company name? |
| 6132 (Home office) | Justified proportion? Conforming to BOFiP? Convention exists? |
| 6135 (SaaS / hosting) | 100% professional? No personal consumption? |
| 6181 (Documentation) | Link with business activity? |
| 622 (Intermediaries) | Nature and supporting documents? |
| 6231 (Advertising) | Gifts = gratuities? Directories = advertising? |
| 627/6278 (Banking) | Consistent with bank statements? |
| 651 (Domain names) | All related to business activity? |
| 654 (Chargebacks) | Documented irrecoverability? |

### Axis 4: Shareholder Current Account 455 (art. 39-1-3° and 212 CGI)

**High fiscal risk**, especially SASU/EURL.

**CCA 455 checks**  _(art. 39-1-3° and 212 CGI)_

| Check | Detail |
| --- | --- |
| Pre-incorporation expenses | Assumed within 6 months? Annexed to statuts/PV? Professional character? |
| Home office | Justified surface proportion? Plan available? Non-deductible: mortgage principal |
| Interest on current account | No interest = OK. If interest paid: capped at TMPV BCE rate |
| Currency conversion | BCE rate acceptable; inspector may demand per-transaction rate |

### Axis 5: Revenue (art. 38-2 CGI)

**Revenue checks**  _(art. 38-2 CGI)_

| Check | Detail |
| --- | --- |
| Revenue completeness | Cross-check payment platforms (Stripe, PayPal) vs. accounting |
| Period cut-off | Revenue booked only for the financial year |
| Credit balance on 411 (Clients) | Abnormal — advance? Omitted revenue? |
| Asset disposals | Proper classification (account 775)? |
| Commissions / ancillary revenue | Nature? Foreign withholding tax? |

### Axis 6: TVA

**If franchise en base (art. 293 B CGI):**

**Franchise en base checks**  _(art. 293 B CGI)_

| Check | Detail |
| --- | --- |
| Threshold monitoring | Services: EUR 36,800 (tolerance EUR 39,100). Annualise if short year |
| Invoice mention | "TVA non applicable, art. 293 B du CGI" |
| Asset disposals | Subject to TVA or exempt? |
| Intra-EU / extra-EU services | Autoliquidation (art. 283-2 CGI)? |

**If TVA collected:**

**TVA collected checks**

| Check | Detail |
| --- | --- |
| CA3/CA12 vs accounting concordance |  |
| Deductible TVA documentation |  |
| Pro-rata deduction if mixed activity |  |

### Axis 7: Fixed Assets and Depreciation (art. 39-1-2° CGI)

**Fixed assets checks**  _(art. 39-1-2° CGI)_

| Check | Detail |
| --- | --- |
| Capitalisation threshold | EUR 500 HT (SME tolerance). If franchise TVA: TTC amounts |
| Depreciation method | Linear 3 years for IT equipment (standard). Pro-rata temporis from date of commissioning |
| Mixed use | Phone and computer: 100% professional justified? If mixed: only professional portion deductible |

### Axis 8: International Operations

**International operations checks**  _(art. 182 B CGI)_

| Check | Detail |
| --- | --- |
| Transfer pricing | Applicable if foreign subsidiary or intra-group transactions |
| Withholding tax (art. 182 B CGI) | Payments to foreign providers: 25% withholding? Check applicable tax treaty |
| DES (Déclaration Européenne de Services) | Required for intra-EU service purchases |

## Section 4 — Penalty Schedule

### Interest on late payment (intérêts de retard — art. 1727 CGI)

**Interest parameters**  _(art. 1727 CGI)_

| Parameter | Value |
| --- | --- |
| Monthly rate | 0.20% |
| Annual rate | 2.40% |
| Start date | 1st day of month following due date |
| End date | Last day of month of payment |

### Surcharges (majorations — art. 1729 CGI)

**Surcharge schedule**  _(art. 1729 CGI)_

| Situation | Rate | Condition |
| --- | --- | --- |
| Good faith | 0% | Material error, first offence |
| Insufficient declaration (bonne foi) | 10% | art. 1758 A CGI |
| Deliberate omission (manquement délibéré) | **40%** | Proven intent to evade |
| Fraudulent schemes (manoeuvres frauduleuses) | **80%** | Artifice, false documents |
| Abuse of law (abus de droit) | **80%** | Artificial arrangements |

### Computation example — deliberate omission

```
Disallowed charges:                      EUR 10,000
Additional IS (at 25%):                  EUR  2,500
Late interest (12 months × 0.20%):       EUR     60
Surcharge (40%):                         EUR  1,000
────────────────────────────────────────────────────
Total assessment:                        EUR  3,560
```

## Section 5 — Risk Assessment Grid

### Aggravating factors

**Aggravating factors**

| Factor | Impact |
| --- | --- |
| SASU/EURL without auditor | Heightened scrutiny on personal charges |
| First financial year | Limited history, frequent errors |
| Revenue in foreign currency | Conversion rate risk |
| High 455 current account balance | Suspicion of patrimony confusion |
| Internet/SaaS activity | Territorial allocation difficulties |

### Mitigating factors

**Mitigating factors**

| Factor | Impact |
| --- | --- |
| Small size (CA < EUR 50k) | Lighter verification |
| Regular bookkeeping | Compliant FEC, balanced entries |
| First year in good faith | Tolerance for formal errors |
| No employees | No social risk |
| Franchise en base TVA | No collected-TVA risk |

## Section 6 — Common Adjustment Scenarios

### Scenario 1: Personal expenses in account 455

**Assessment:** Reintegration of personal portion. Possible requalification as "disguised remuneration" → social contributions. If significant amounts: acte anormal de gestion.

### Scenario 2: Overstated home office

**Assessment:** Reintegration of excess (declared % − actual %) × charges. Surcharge 10% (good faith) or 40% (if recurring).

### Scenario 3: Pre-incorporation expenses without état des actes

**Assessment:** Full reintegration of pre-incorporation charges. Additional IS on the amount.

### Scenario 4: Omitted revenue (credit balance on 411)

**Assessment:** If inspector considers it undeclared revenue → added to fiscal result + IS + 40% surcharge if intentional.

### Scenario 5: Incorrect currency conversion

**Assessment:** Recalculation of all foreign-currency charges at correct BCE rate. IS on the difference.

## Section 7 — Statute of Limitations (Droit de Reprise)

**Statute of limitations**

| Tax | Standard period |
| --- | --- |
| IS / IR | 3 years (until 31 Dec of the 3rd year following the tax year) |
| TVA | 3 years |
| IFI | 6 years |
| All taxes (undisclosed activity / fraud) | **10 years** |

- **Document retention recommendation** — minimum 6 years (recommended: 10 years to cover all scenarios)

## Section 8 — Voluntary Regularisation

If the taxpayer corrects before an audit:
- Late interest: 0.20%/month (still applies)
- **No surcharge** if regularisation is spontaneous and in good faith
- For significant cases (crypto, foreign income, unreported gains): consult an avocat fiscaliste for structured regularisation

## Section 9 — Audit Report Format

For each anomaly, the adjustment is formalised as a **chef de redressement** containing:

1. **Tax concerned** (IS / TVA / Other)
2. **Financial year**
3. **Legal basis** (CGI article / BOFiP reference)
4. **Nature** of the adjustment
5. **Factual finding**
6. **Legal foundation and case law**
7. **Amount** (base, additional tax, interest, surcharge, total)
8. **Risk level** (high / medium / low)
9. **Corrective recommendation**

## Section 10 — Conservative Defaults

**Conservative defaults**

| Ambiguity | Default |
| --- | --- |
| Charge deductibility doubtful | Flag as potentially non-deductible |
| Surcharge rate unclear | Assume 10% (good faith) |
| FEC gap found | Flag as potential concealment |
| Revenue source unclear | Include in taxable revenue |

## Section 11 — Key Legal References

**Key legal references**

| Rule | Article |
| --- | --- |
| Taxable profit | art. 38-1 CGI |
| Net asset variation | art. 38-2 CGI |
| Deductible charges (4 conditions) | art. 39-1 CGI |
| IS non-deductible | art. 39-1-4° CGI |
| CCA interest cap | art. 39-1-3° and 212 CGI |
| IS rates | art. 219-I CGI |
| PME reduced rate | art. 219-I-b CGI |
| Franchise en base | art. 293 B CGI |
| Autoliquidation | art. 283-2 CGI |
| Late interest | art. 1727 CGI |
| Surcharges | art. 1729 CGI |
| Good-faith insufficient declaration | art. 1758 A CGI |
| FEC obligation | art. L. 47 A-I LPF |
| Audit notice | art. L. 47 LPF |
| On-site verification | art. L. 13 LPF |
| Rectification notice | art. L. 57 LPF |
| SME audit duration | art. L. 52 LPF |
| Non-probante burden shift | art. L. 192 LPF |
| Standard statute of limitations | art. L. 169 LPF |
| Home office (BOFiP) | BOI-BIC-CHG-40-20-10 |
| Pre-incorporation expenses (BOFiP) | BOI-IS-BASE-30-10 |

## Footer

*OpenAccountants — open-source accounting skills for AI*
*This output must be reviewed by a qualified professional before filing or acting upon.*
*Latest verified skills: **openaccountants.com** | Report errors: **github.com/openaccountants/openaccountants***

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network — accountants who put
their name behind the tax answers AI gives people. The live, always-current
version (and the professional behind it) is at
[openaccountants.com](https://www.openaccountants.com).

- Use it in your AI: https://www.openaccountants.com/connect
- Meet the accountants: https://www.openaccountants.com/network

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.
