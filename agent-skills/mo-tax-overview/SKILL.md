---
name: mo-tax-overview
description: "Macau tax overview for 2026: source-cited conditions, computation and filing boundaries. Not yet approved by an accountant."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/mo-tax-overview"
  jurisdiction: "MO"
  tax_year: "2026"
  last_updated: "2026-11-15"
---

# Macau Tax Overview v0.1

> **General reference only.** These instructions support working papers. Obtain qualified local review before filing, paying or adopting a position for particular facts.


## The method, step by step

1. Confirm Macau/Macao SAR, not mainland China or Hong Kong, the income year versus filing year, entity/occupation, residence/actual management and source of each receipt. The fiscal year runs January-December and the reporting currency is Macau pataca (MOP); DSF is the tax administrator. Residence and the foreign passive-income exception mean the old blanket foreign-source-outside shorthand cannot decide every 2026 case. [current official taxonomy, income and indirect tax headings](https://www.ipim.gov.mo/en/invest-here/taxation); [article 2](https://bo.dsaj.gov.mo/bo/i/78/36/lei21.asp?printer=1); [article 24](https://bo.dsaj.gov.mo/bo/i/2024/53/lei24.asp?printer=1).

2. For an ordinary company or sole proprietor’s commercial/industrial profits, load [corporate income tax](mo-corporate-income-tax.md). That skill owns Group A/B criteria, permanent bands, the latest annual exemption and normal payment cycle. It distinguishes 2025 income in the 2025-2026 filing cycle from unconfirmed final 2026 profits relief. It corrects Group A’s old June end-date to the amended July window. Do not copy its rates into a second card. [article 3](https://bo.dsaj.gov.mo/bo/i/78/36/lei21.asp?printer=1); [article 4](https://bo.dsaj.gov.mo/bo/i/78/36/lei21.asp?printer=1); [article 10](https://bo.dsaj.gov.mo/bo/i/78/36/lei21.asp?printer=1); [2026 Budget Law 13/2025 article 22](https://bo.dsaj.gov.mo/bo/i/2025/52/lei13.asp?printer=1).

3. For formation/entity choice, load [company formation](mo-company-formation.md), including capital/payment timing, local address, registry, DSF opening and work-permit boundaries. The form does not itself establish favourable tax treatment or labour-market access. [article 174](https://bo.dsaj.gov.mo/bo/i/99/31/codcompt/codcom0001.asp?printer=1); [article 179](https://bo.dsaj.gov.mo/bo/i/99/31/codcompt/codcom0001.asp?printer=1); [article 361](https://bo.dsaj.gov.mo/bo/i/99/31/codcompt/codcom0001.asp?printer=1); [Q19 work authorization separate from ownership](https://www.ipim.gov.mo/en/investment-promotion/business-information/q-a).

4. For employed work, load [payroll/social](mo-payroll-social.md). It owns ordinary professional-tax bands, the distinct income allowance and tax-liability rebate, FSS contribution classes and the non-resident employment fee. The old approximate 6.3% is only a conditional derived upper marginal gross-wage share; it is not an average or universal personal rate. Listed self-employed professions have their own professional-tax classification and filing obligations: the complete individual-tax skill is still missing. Single-payer employee filing relief is not a universal no-return rule. [article 5](https://bo.dsaj.gov.mo/bo/i/78/08/lei02.asp?printer=1); [article 10](https://bo.dsaj.gov.mo/bo/i/78/08/lei02.asp?printer=1); [article 11](https://bo.dsaj.gov.mo/bo/i/78/08/lei02.asp?printer=1); [article 4(o), income allowance](https://bo.dsaj.gov.mo/bo/i/78/08/lei02.asp?printer=1); [article 7](https://bo.dsaj.gov.mo/bo/i/78/08/lei02.asp?printer=1); [2026 Budget Law 13/2025 article 18](https://bo.dsaj.gov.mo/bo/i/2025/52/lei13.asp?printer=1).

5. For a general VAT question, import or stamp/lease/property transaction, load [VAT/GST boundaries](mo-vat-gst.md). Macau’s checked framework has no general VAT/GST/sales tax, but property tax, stamp duty, narrow tobacco/spirits consumption tax, tourism/motor-vehicle taxes and casino gaming taxation are separate. The no-VAT direct source is dated and its corroboration/limits are stated there. This pack does not supply the detailed gaming/property/vehicle return. [2020 Trade Policy Review paragraph 3.49](https://www.wto.org/english/tratop_e/tpr_e/s402_e.pdf); [current official taxonomy, income and indirect tax headings](https://www.ipim.gov.mo/en/invest-here/taxation); [article 2](https://bo.dsaj.gov.mo/bo/i/99/50/lei04.asp?printer=1); [article 1](https://bo.dsaj.gov.mo/bo/i/88/26/lei17.asp?printer=1).

6. Resolve the actual year’s measure, registration, DSF/FSS notices and tax-domicile record before a filing instruction. Do not assume every dividend, interest or royalty is untaxed just because the old overview said no general withholding: company source/inclusion, distribution and recipient rules and special non-resident professional withholding need separate analysis. Transfer-pricing and full cross-border skills remain missing; refer rather than inventing a rate or relief. [2026 tax-domicile declaration and channels](https://nhp.dsf.gov.mo/topic/declare_tax_domicile/en/home); [article 2](https://bo.dsaj.gov.mo/bo/i/78/36/lei21.asp?printer=1); [article 3](https://bo.dsaj.gov.mo/bo/i/78/36/lei21.asp?printer=1); [article 20](https://bo.dsaj.gov.mo/bo/i/78/36/lei21.asp?printer=1); [article 36](https://bo.dsaj.gov.mo/bo/i/78/08/lei02.asp?printer=1).

The owner skills supply all rates, deadlines and taxpayer exceptions. This router supplies intake and handoff, not a duplicate tax computation.


## Worked cases

### Route company receipts to an agreed profit working paper

Assume a Macau ordinary company presents MOP 1,200,000 assessable 2025 trading receipts and MOP 200,000 established allowable costs, with no other adjustments, owner distributions or foreign income. Hand MOP 1,000,000 net profit, derived, to corporate tax together with the actual Group A/B evidence and income year. Do not treat receipts as taxable profit or apply the latest annual exemption to a different year. [article 3](https://bo.dsaj.gov.mo/bo/i/78/36/lei21.asp?printer=1); [article 19](https://bo.dsaj.gov.mo/bo/i/78/36/lei21.asp?printer=1); [2026 Budget Law 13/2025 article 22](https://bo.dsaj.gov.mo/bo/i/2025/52/lei13.asp?printer=1).

```oa-check
name: Route company receipts to an agreed profit working paper
inputs:
  assessable_receipts: 1200000
  allowed_costs: 200000
steps:
  - profit_for_owner_skill: assessable_receipts - allowed_costs
expected:
  profit_for_owner_skill: 1000000
```

### Keep an outbound royalty separate from trading profit intake

Assume a company presents MOP 900,000 assessable trading receipts and MOP 300,000 already established allowable costs, plus a distinct MOP 80,000 outbound royalty requiring source/recipient/treaty analysis. Hand the derived MOP 600,000 trading subtotal and the separate MOP 80,000 gross payment to corporate/cross-border review. Do not automatically subtract the royalty again or assume a gross withholding amount. This is an intake reconciliation; full cross-border clearance is absent. [article 19](https://bo.dsaj.gov.mo/bo/i/78/36/lei21.asp?printer=1); [article 20](https://bo.dsaj.gov.mo/bo/i/78/36/lei21.asp?printer=1); [article 2](https://bo.dsaj.gov.mo/bo/i/78/36/lei21.asp?printer=1).

```oa-check
name: Keep an outbound royalty separate from trading profit intake
inputs:
  trading_receipts: 900000
  established_costs: 300000
  royalty_gross: 80000
steps:
  - trading_subtotal: trading_receipts - established_costs
  - payment_for_separate_review: royalty_gross
expected:
  trading_subtotal: 600000
  payment_for_separate_review: 80000
```


## When to refuse or refer

Stop if the jurisdiction, year, income class, residence/source or Group A/B facts are unknown, or a request needs final 2026 annual profits relief or an unmapped return field. Refer full self-employed/multi-payer income tax, treaty/foreign credits, transfer pricing, complicated property/excise/sector taxes and special withholding. Passing structural checks on five skills does not mean full Macau coverage or professional approval.


## Ask the client first

- Which jurisdiction, income year and filing cycle, entity/occupation and residence/management?
- What commercial income, work income, foreign receipts/payments, property, imports and staff?
- Which capital, ownership/MNE status, accounting classification and tax notices?
- Is the request a reference estimate, reconciled working paper or actual filing, and which form is accepted?


## Sources

Read on **2026-11-15** for the expressly listed sections. Gazette pages are current amended texts, read in Portuguese; older English company-code translations were not substituted for later amendments. The original-language operative text and exact quotes are retained in the external ledger.

| Source and scope actually read | URL | Read on |
|---|---|---|
| Read for 2026 Budget Law 13/2025 article 18; 2026 Budget Law 13/2025 article 22 | https://bo.dsaj.gov.mo/bo/i/2025/52/lei13.asp?printer=1 | 2026-11-15 |
| Read for article 174; article 179; article 361 | https://bo.dsaj.gov.mo/bo/i/99/31/codcompt/codcom0001.asp?printer=1 | 2026-11-15 |
| Read for current official taxonomy, income and indirect tax headings | https://www.ipim.gov.mo/en/invest-here/taxation | 2026-11-15 |
| Read for 2026 tax-domicile declaration and channels | https://nhp.dsf.gov.mo/topic/declare_tax_domicile/en/home | 2026-11-15 |
| Read for article 2 | https://bo.dsaj.gov.mo/bo/i/99/50/lei04.asp?printer=1 | 2026-11-15 |
| Read for Q19 work authorization separate from ownership | https://www.ipim.gov.mo/en/investment-promotion/business-information/q-a | 2026-11-15 |
| Read for article 10; article 19; article 2; article 20; article 3; article 4 | https://bo.dsaj.gov.mo/bo/i/78/36/lei21.asp?printer=1 | 2026-11-15 |
| Read for article 1 | https://bo.dsaj.gov.mo/bo/i/88/26/lei17.asp?printer=1 | 2026-11-15 |
| Read for article 24 | https://bo.dsaj.gov.mo/bo/i/2024/53/lei24.asp?printer=1 | 2026-11-15 |
| Read for article 10; article 11; article 36; article 4(o), income allowance; article 5; article 7 | https://bo.dsaj.gov.mo/bo/i/78/08/lei02.asp?printer=1 | 2026-11-15 |
| Read for 2020 Trade Policy Review paragraph 3.49 | https://www.wto.org/english/tratop_e/tpr_e/s402_e.pdf | 2026-11-15 |
Not yet confirmed: Full individual-tax, transfer-pricing and cross-border coverage; final 2026 profits relief/live forms; blanket no-withholding claims and the subject-specific unresolved boundaries in each owner skill. Old overview figures and deadlines have explicit owner destinations or unconfirmed boundaries; they are not duplicated as a second rate source.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-15. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `mo-tax-overview` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/mo-tax-overview. If neither is available, confirm every figure against the official source pages cited above before relying on it.
