---
name: iraq-tax
description: "Use whenever asked about Iraq taxation, sales tax or the absence of VAT in Iraq, tax year 2026. Iraq has no VAT or GST."
version: 2.1
jurisdiction: IQ
tax_year: 2026
last_updated: 2026-11-01
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Iraq Tax

## Section 1 -- Quick reference

**Quick reference**

| Field | Value |
| --- | --- |
| Country | Iraq |
| VAT/GST status | NOT IMPLEMENTED |
| Specific sales taxes | See [VAT or GST](iq-vat-gst.md) |
| Corporate income tax | 15% standard |
| Personal income tax | Progressive 3%-15% |
| Authority | General Commission for Taxes (GCT), Ministry of Finance |
| Filing | At GCT branches |
| Currency | IQD (Iraqi Dinar) |
| Primary legislation | Income Tax Law No. 113 of 1982 (as amended) |
| Contributor | Open Accounting Skills Registry |
| Validated by | Pending |
| Last research update | 1 November 2026 |

## Section 2 -- Required inputs and refusal catalogue

**Minimum viable** -- bank statement or transaction list. Acceptable from Rasheed Bank, Rafidain Bank, Trade Bank of Iraq, or any Iraqi bank.

**Refusal catalogue:**

- **R-IQ-1 -- Oil sector** — Oil sector taxation is T3. Escalate.  _(R-IQ-1 -- Oil sector.)_
- **R-IQ-2 -- Kurdistan Region** — KRI has separate tax administration. Escalate for dual-filing obligations.  _(R-IQ-2 -- Kurdistan Region.)_

### 3.1 Iraqi banks

**Iraqi banks pattern library**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| RASHEED BANK | EXCLUDE | Financial transaction |
| RAFIDAIN BANK | EXCLUDE | Same |
| TRADE BANK OF IRAQ, TBI | EXCLUDE | Same |
| INTEREST, LOAN | EXCLUDE | Out of scope |

### 3.2 Government

**Government pattern library**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| GCT, GENERAL COMMISSION FOR TAXES | EXCLUDE | Tax payment |
| CUSTOMS | EXCLUDE | Customs duty |
| SOCIAL SECURITY | EXCLUDE | Social insurance |

### Example 1 -- Client asks about Iraq VAT

**Input:** "What is the VAT rate in Iraq?"

**Resolution:** Iraq does not have VAT. No broad-based consumption tax exists. Specific sales taxes apply to enumerated products only.

### Example 2 -- Alcohol import

Importer brings alcohol into Iraq. 300% sales tax at customs plus customs duties. No input credit mechanism. Tax is a direct cost.

### 5.1 No VAT system

- **No VAT system** — Iraq has no VAT registration, filing, collection, or invoicing requirements.  _(Section 5.1 No VAT system)_

### 5.2 Specific sales taxes

See [VAT or GST](iq-vat-gst.md) for rates.

- **Nature of specific sales taxes** — These are excise-type levies on enumerated goods only. No input credit. No staged collection. No registration system.  _(Section 5.2 Specific sales taxes)_

### 5.3 Corporate income tax

- **Corporate income tax - standard** — 15% percent (flat on net profits from Iraqi-source income)  _(Section 5.3 Corporate income tax)_
- **Oil & gas sector corporate tax rate** — 35% for activities under Law 19 of 2010  _(GCT return guide)_
- **Agricultural income** — Agricultural income: exempt.  _(Section 5.3 Corporate income tax)_

## Section 6 -- Return form structure

- **Return form structure** — No VAT return exists. CIT return filed annually by 31 May, paper-based at GCT offices. Financial statements in Arabic must accompany.  _(Section 6 -- Return form structure)_

## Section 7 -- No reverse charge

- **No reverse charge** — No VAT system means no reverse charge mechanism exists.  _(Section 7 -- No reverse charge)_

## Section 8 -- No input deductibility

- **No input deductibility** — No input credit system for sales taxes. Tax on alcohol/tobacco is embedded cost.  _(Section 8 -- No input deductibility)_

## Section 9 -- Filing, deadlines, and penalties

**Filing, deadlines, and penalties**

| Obligation | Deadline |
| --- | --- |
| CIT return | 31 May following year-end |
| Books/records | Arabic language required |


### Edge cases

**EC1 -- VAT question.** Iraq has no VAT.

**EC2 -- Alcohol import.** 300% sales tax at customs. No credit.

**EC3 -- E-commerce/digital.** No VAT. Telecom sales tax status is unverified; see [VAT or GST](iq-vat-gst.md). CIT if PE exists (escalate PE).

**EC4 -- Kurdistan Region.** Dual filing may be needed. Escalate.

**EC5 -- Agricultural income.** Exempt from income tax (art. 7(1)).

### Test suite

**Test 1 -- VAT question.** Expected: "Iraq does not have VAT."

**Test 2 -- CIT.** IQD 100M profit. Expected: CIT IQD 15M (15%). File by 31 May.

**Test 3 -- Alcohol.** IQD 1M cost. Expected: 300% sales tax embedded. No credit.

**Test 4 -- Agriculture.** IQD 50M farming income. Expected: exempt.

**Test 5 -- Foreign contractor.** IQD 500M government contract. Expected: CIT 15%. WHT at source.

### Escalation protocol

```
REVIEWER FLAG / ESCALATION REQUIRED
[Standard format]
```

### Prohibitions

- NEVER state Iraq has VAT -- it does not
- NEVER apply VAT calculations to Iraq
- NEVER apply input credits to specific sales taxes
- NEVER assume federal rules apply in Kurdistan Region
- NEVER file without Arabic documentation
- NEVER compute numbers -- engine handles arithmetic

## Sources

| Source | URL | Read on |
|---|---|---|
| Income Tax Law 113 of 1982, GCT consolidated text: arts. 11, 12, 13, 15, 17, 19, 27, 45, 46, penalties | https://tax.mof.gov.iq/uploads/Najwan/law/Income-Tax-Law-No.-113-of-1982-Ar.pdf | 2026-11-01 |
| GCT guide to the company income tax return (scan, read in full by OCR) | https://tax.mof.gov.iq/uploads/Najwan/%D8%AF%D9%84%D9%8A%D9%84%20%D9%85%D9%84%D8%A6%20%D8%AA%D8%B5%D8%B1%D9%8A%D8%AD%20%D8%B6%D8%B1%D9%8A%D8%A8%D8%A9%20%D8%A7%D9%84%D8%B4%D8%B1%D9%83%D8%A7%D8%AA.pdf | 2026-11-01 |
| Sales Tax Instructions 5 of 2015 (scan, read in full by OCR) | https://tax.mof.gov.iq/uploads/Najwan/law/%D8%AA%D8%B9%D9%84%D9%8A%D9%85%D8%A7%D8%AA%20%D9%81%D8%B1%D8%B6%20%D9%88%20%D8%AC%D8%A8%D8%A7%D9%8A%D8%A9%20%D8%B6%D8%B1%D9%8A%D8%A8%D8%A9%20%D8%A7%D9%84%D9%85%D8%A8%D9%8A%D8%B9%D8%A7%D8%AA%20-%20Copy%202.pdf | 2026-11-01 |

Not yet confirmed: Arabic books rule beyond correspondence, social security (see payroll skill).

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com).

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
