---
name: iraq-tax
description: Use this skill whenever asked about Iraq taxation, sales tax, or the absence of VAT in Iraq. Iraq does NOT have a broad-based VAT or GST. It imposes specific sales taxes on enumerated products (up to 300% on alcohol/tobacco) and has an income tax system. ALWAYS read this skill before handling any Iraq tax work.
version: 2.0
---

# Iraq Tax Compliance Skill v2.0

## Section 1 -- Quick reference

| Field | Value |
|---|---|
| Country | Iraq |
| VAT/GST status | NOT IMPLEMENTED |
| Specific sales taxes | Alcohol 300%, tobacco 300%, mobile/internet 20%, travel 15%, cars 15%, hotels 10%, telecom 5% |
| Corporate income tax | 15% standard |
| Personal income tax | Progressive 3%-15% |
| Authority | General Commission for Taxes (GCT), Ministry of Finance |
| Filing portal | No centralized electronic portal (paper filing) |
| Currency | IQD (Iraqi Dinar) |
| Primary legislation | Income Tax Law No. 113 of 1982 (as amended) |
| Contributor | Open Accounting Skills Registry |
| Validated by | Pending |
| Last research update | April 2026 |

---

## Section 2 -- Required inputs and refusal catalogue

**Minimum viable** -- bank statement or transaction list. Acceptable from Rasheed Bank, Rafidain Bank, Trade Bank of Iraq, or any Iraqi bank.

**Refusal catalogue:**

**R-IQ-1 -- Oil sector.** Message: "Oil sector taxation is T3. Escalate."

**R-IQ-2 -- Kurdistan Region.** Message: "KRI has separate tax administration. Escalate for dual-filing obligations."

---

## Section 3 -- Supplier pattern library

### 3.1 Iraqi banks

| Pattern | Treatment | Notes |
|---|---|---|
| RASHEED BANK | EXCLUDE | Financial transaction |
| RAFIDAIN BANK | EXCLUDE | Same |
| TRADE BANK OF IRAQ, TBI | EXCLUDE | Same |
| INTEREST, LOAN | EXCLUDE | Out of scope |

### 3.2 Government

| Pattern | Treatment | Notes |
|---|---|---|
| GCT, GENERAL COMMISSION FOR TAXES | EXCLUDE | Tax payment |
| CUSTOMS | EXCLUDE | Customs duty |
| SOCIAL SECURITY | EXCLUDE | Social insurance |

---

## Section 4 -- Worked examples

### Example 1 -- Client asks about Iraq VAT

**Input:** "What is the VAT rate in Iraq?"

**Resolution:** Iraq does not have VAT. No broad-based consumption tax exists. Specific sales taxes apply to enumerated products only.

### Example 2 -- Alcohol import

Importer brings alcohol into Iraq. 300% sales tax at customs plus customs duties. No input credit mechanism. Tax is a direct cost.

---

## Section 5 -- Classification rules

### 5.1 No VAT system

Iraq has no VAT registration, filing, collection, or invoicing requirements.

### 5.2 Specific sales taxes

These are excise-type levies on enumerated goods only. No input credit. No staged collection. No registration system.

| Product | Rate |
|---|---|
| Alcohol | 300% |
| Tobacco | 300% |
| Mobile/internet | 20% |
| Travel tickets | 15% |
| Cars | 15% |
| Hotels/restaurants (deluxe) | 10% |
| Telecom services | 5% |

### 5.3 Corporate income tax

15% flat on net profits from Iraqi-source income. Oil/gas: 35%. Agricultural income: exempt.

---

## Section 6 -- Return form structure

No VAT return exists. CIT return filed annually by 31 May, paper-based at GCT offices. Financial statements in Arabic must accompany.

---

## Section 7 -- No reverse charge

No VAT system means no reverse charge mechanism exists.

---

## Section 8 -- No input deductibility

No input credit system for sales taxes. Tax on alcohol/tobacco is embedded cost.

---

## Section 9 -- Filing, deadlines, and penalties

| Obligation | Deadline |
|---|---|
| CIT return | 31 May following year-end |
| Books/records | Arabic language required |

Social security: employer 12% + employee 5% = 17%.

---

## Section 10 -- Edge cases, test suite, and escalation

### Edge cases

**EC1 -- VAT question.** Iraq has no VAT.

**EC2 -- Alcohol import.** 300% sales tax at customs. No credit.

**EC3 -- E-commerce/digital.** No VAT/sales tax on digital services. CIT if PE exists (escalate PE).

**EC4 -- Kurdistan Region.** Dual filing may be needed. Escalate.

**EC5 -- Agricultural income.** Exempt from income tax.

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

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com).
