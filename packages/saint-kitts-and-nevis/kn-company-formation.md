---
name: kn-company-formation
description: >
  Forming a company or other entity in Saint Kitts and Nevis in 2026. Covers the
  federal company under the Companies Act, Cap. 21.03 (memorandum, certificate, annual
  return before the end of the month after the anniversary month, directors' accounts,
  the 2024 agent amendments), and the Nevis routes: domestic company (Companies
  Ordinance 1999, Forms 26, 1 or 2, 4 and 9), business corporation and LLC through a
  licensed registered agent with the Financial Services Regulatory Commission, and the
  new limited partnership (Ordinance 3 of 2025, from 1 February 2026), plus the October
  2026 amendment bills and the tax registrations that follow. Trigger phrases include
  St Kitts company formation, Nevis LLC, Nevis IBC, Nevis limited partnership, register
  a company in St Kitts.
version: 1.0
jurisdiction: KN
tax_year: 2026
last_updated: 2026-11-14
category: formation
type: filing-howto
domain: formation
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
---

# Saint Kitts and Nevis: forming a company

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope and who this is for

People setting up an entity in Saint Kitts and Nevis in 2026: a federal company under the Companies Act, Cap. 21.03 (2020 revision, amended by Act 21 of 2024), or a Nevis domestic company, business corporation, limited liability company or limited partnership. Identify the legal form and registry before choosing documents. Tax obligations after formation: [kn-corporate-income-tax](kn-corporate-income-tax.md), [kn-vat-and-import-charges](kn-vat-and-import-charges.md). Nevis entity record rules and the end of the old offshore exemptions: [kn-special-regimes](kn-special-regimes.md).

## Ask the client first

1. Which island and which form: federal company, Nevis domestic company, Nevis business corporation (IBC), Nevis LLC, Nevis limited partnership?
2. Will the entity trade locally (VAT, corporation tax, business licence) or only abroad?
3. Who is the registered agent (licensed, with a physical office in Nevis for Nevis routes)?
4. Proposed directors, members or partners (a limited partnership needs at least two distinct partners).
5. Beneficial owners and where the records will be kept.

## The method, step by step

### Rates, bands and thresholds

| Item | 2026 figure | Conditions | Source |
|---|---|---|---|
| Federal company annual return, s.72 | Before the end of the month following the anniversary month of incorporation or registration | Signed by a director or the secretary, with the prescribed fee | [Companies Act, 2020 revision, ss.4, 72 and 106](https://lawcommission.gov.kn/wp-content/documents/Revised-Acts-of-St-Kitts-and-Nevis/Revised-Acts-of-St-Kitts-and-Nevis-2020/Ch-21_03-Companies-Act.pdf) |
| Nevis limited partnership | Ordinance 3 of 2025, commencement 1 February 2026 | At least 2 distinct partners; licensed agent with a physical place of business in Nevis; annual application and fee through the agent | [Ordinance 3 of 2025, ss.1, 7 and 11](https://www.nevisfsrc.com/wp-content/uploads/2026/01/No.-3-of-2025-Nevis-Limited-Partnership-Ordinance-2025.pdf) |

### Steps in order

1. **Federal company.** Subscribe a memorandum; meet the registration requirements; the Registrar issues the certificate (s.4). The 2024 amendment adds agent-related filing and maintenance provisions and changes member and director record requirements. Directors prepare accounts (s.106).
2. **Nevis domestic company** (Companies Ordinance 4 of 1999): Form 26 name search and reservation; articles on Form 1 (commercial) or Form 2 (non-profit); Form 4 registered office; Form 9 directors. Confirm foreign-director rules, current forms, fees and approvals ([Companies Registry brochure](https://nia.gov.kn/cdl_document/brochure-incorporating-a-domestic-company/)).
3. **Nevis business corporation:** engage a licensed registered agent with an office in Nevis, reserve the name, file Articles of Incorporation with the Registrar of Corporations; keep corporate and accounting records accessible and keep the agent's ownership and officer records up to date ([FSRC IBC page](https://www.nevisfsrc.com/services/ibcs/)).
4. **Nevis LLC:** appoint and keep a registered agent in Nevis; file Articles of Organisation with the Registrar of Companies; settle member or manager arrangements ([FSRC LLC page](https://www.nevisfsrc.com/services/llcs/)).
5. **Nevis limited partnership:** Articles of Formation with the Registrar through a licensed agent ([FSRC LP page](https://www.nevisfsrc.com/services/lps/)).
6. **Tax:** register with IRD; a locally incorporated business files a return even when inactive or on a holiday; international companies, Nevis IBCs and LLCs file CIT-101.

### What happens after

- Annual return each year (federal: s.72 timing above); registry renewals for Nevis entities.
- The Nevis Island Administration recorded Assembly passage on 6 October 2026 of amendment bills for domestic companies, business corporations, LLCs and limited partnerships: confirm the assented text, commencement and transitional rules before filing.
- Check beneficial ownership, accounting records, annual accounts, audit, business licences and economic substance separately from the federal tax return.

## Worked cases

### Federal company incorporated on 10 March 2025

The anniversary month is March, so the 2026 annual return is due before the end of April 2026 (month 4, derived). A company incorporated in December files before the end of the following January.

```oa-check
name: St Kitts annual return month for March and December incorporations
inputs:
  march: 3
  december: 12
steps:
  - due_month_march: march + 1
  - due_month_december: december + 1 - 12 * floor(december / 12)
expected:
  due_month_march: 4
  due_month_december: 1
```

## When to refuse or refer

- Nevis amendments passed in October 2026 until commenced.
- Legal forms beyond those above; licensing of regulated activities.
- Economic substance and beneficial ownership filings.

## Sources

| Source | URL | Read on |
|---|---|---|
| Companies Act Cap. 21.03 (2020 revision): read for ss.4, 72 (annual return timing) and 106 | https://lawcommission.gov.kn/wp-content/documents/Revised-Acts-of-St-Kitts-and-Nevis/Revised-Acts-of-St-Kitts-and-Nevis-2020/Ch-21_03-Companies-Act.pdf | 2026-11-14 |
| Companies (Amendment) Act 21 of 2024: read for the agent and record changes | https://lawcommission.gov.kn/wp-content/documents/Annual-Laws/2024/ACTs/Act-21-of-2024-Companies-Amendment-Act.pdf | 2026-11-11 |
| Nevis Companies Registry brochure, incorporating a domestic company: read for Forms 26, 1, 2, 4 and 9 | https://nia.gov.kn/cdl_document/brochure-incorporating-a-domestic-company/ | 2026-11-11 |
| Nevis FSRC pages for IBCs, LLCs and LPs: read for the agent and filing steps | https://www.nevisfsrc.com/services/ibcs/ | 2026-11-11 |
| Nevis Limited Partnership Ordinance 3 of 2025: read for ss.1, 7 and 11 (1 February 2026, two partners, agent) | https://www.nevisfsrc.com/wp-content/uploads/2026/01/No.-3-of-2025-Nevis-Limited-Partnership-Ordinance-2025.pdf | 2026-11-11 |
| NIA report on the four amendment bills, 6 October 2026 | https://nia.gov.kn/nevis-strengthens-financial-services-regulatory-regime-with-passage-of-four-bills/ | 2026-11-11 |

Not yet confirmed: registry fees and current forms; the 2024 federal amendment detail; the October 2026 Nevis amendments; sources dated 2026-11-11 were read by Ryan Duguid and not re-opened here.
