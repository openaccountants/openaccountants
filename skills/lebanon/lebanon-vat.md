---
name: lebanon-vat
description: "Use this skill for a Lebanon VAT return, TVA Lebanon or MOF Lebanon questions, tax year 2026. Return deadline changed by the 2026 Budget to one month. The rate needs checking: 12% was Cabinet-approved in Feb 2026 and no official page opened shows it enacted."
version: 2.1
jurisdiction: LB
tax_year: 2026
last_updated: 2026-11-01
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Lebanon VAT

Every figure here is unverified unless the table below links it: the Ministry of Finance text could not be opened. Do not treat 11% or 12% as settled without checking the Ministry.

## Who this applies to

Businesses registered or liable for VAT in Lebanon under Law 379 of 2001.

## Rates, bands and thresholds

| Item | Amount | Tax year | Official URL |
|---|---|---|---|
| Periodic VAT return deadline | one month instead of 20 days | 2026 | https://institutdesfinances.gov.lb/sites/default/files/2026-04/Pamphlet-Citizen%20Budget%202026-Apr26-En-final.pdf |
| VAT refund requests for 2024 | extra 2-month period for beneficiaries | 2026 | same |
| Advance at customs, no income tax or VAT declarations in previous 3 years | 1.5% of import value, credited | 2026 | same |
| Standard rate | 11% | 2026 | unverified: Ministry of Finance site showed a CAPTCHA, law text not opened |
| Registration threshold | LBP 100,000,000 | 2026 | unverified: Ministry of Finance site showed a CAPTCHA, law text not opened |

## The base

### Older quick reference (unverified)

**Quick reference table**

| Field | Value |
| --- | --- |
| Country | Lebanon |
| Standard rate | 11% (single rate; a 12% rate was Cabinet-approved Feb 2026; no official page opened shows it enacted) |
| Zero rate | 0% (exports, international transport) |
| Exempt | Financial/banking, insurance, medical, education, residential rental, public transport, unprocessed agricultural, books |
| Filing portal | https://www.finance.gov.lb |
| Authority | Ministry of Finance (MOF) |
| Currency | LBP (Lebanese Pound) |
| Filing frequency | Quarterly |
| Deadline | One month after the period (Budget 2026 art. 51), not 20 days |
| Registration threshold | LBP 100,000,000 (effectively negligible due to currency crisis) |
| Primary legislation | Law No. 379 of 2001; Decree 7336/2002 |
| CRITICAL WARNING | Economic crisis since 2019 -- exchange rates, enforcement, refunds all affected |
| Contributor | Open Accounting Skills Registry |
| Validated by | Pending |
| Last research update | 1 November 2026 |

#### 3.1 Lebanese banks (exempt -- exclude)

**Lebanese banks pattern table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| BANK AUDI, AUDI | EXCLUDE | Exempt financial service |
| BLOM BANK, BLOM | EXCLUDE | Same |
| BYBLOS BANK | EXCLUDE | Same |
| BANKMED, FRANSABANK | EXCLUDE | Same |
| INTEREST, LOAN | EXCLUDE | Out of scope |

#### 3.2 Government

**Government pattern table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| MOF, MINISTRY OF FINANCE | EXCLUDE | Tax payment |
| CUSTOMS, DOUANE | Check for import VAT | VAT recoverable |
| NSSF, CNSS | EXCLUDE | Social security |

#### 3.3 Utilities

**Utilities pattern table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| EDL, ELECTRICITE DU LIBAN | Domestic 11% | Electricity |
| OGERO, ALFA, TOUCH | Domestic 11% | Telecoms |

#### 3.4 SaaS

**SaaS pattern table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| GOOGLE, MICROSOFT, AWS | Reverse charge 11% | Non-resident; exchange rate critical |
| ZOOM, SLACK, NOTION | Reverse charge 11% | Same |

#### 5.1 Standard rate 11%

- **Standard rate** : 11% (Single rate. No reduced rates. If 12% enacted by Parliament, update accordingly.)

#### 5.2 Zero-rated

- **Zero-rated supplies** : Exports, international transport, duty-free zone supplies (conditions).

#### 5.3 Exempt

- **Exempt supplies** : Financial/banking, insurance, medical, education, residential rental, public transport, unprocessed agricultural, books/newspapers, gold (investment grade).

- **Blocked input items** : Blocked: entertainment/hospitality, personal-use items, passenger vehicles (unless transport/rental), purchases for exempt supplies, gifts (above thresholds), tobacco/alcohol (personal), club memberships.
- **Partial exemption** : Partial exemption: turnover-based apportionment. Annual adjustment required.

## Deadlines and filing

**VAT return form structure**

| Section | Description |
| --- | --- |
| A. Output VAT | 11% on domestic taxable supplies |
| B. Zero-rated | Exports |
| C. Exempt | Exempt revenue |
| D. Total supplies | A+B+C |
| E. Input VAT domestic | 11% on local purchases |
| F. Input VAT imports | Customs VAT |
| G. Total input | E+F |
| H. Net VAT | A minus G |
| Credit brought forward | Prior period |

Quarterly filing: unverified. The old table of 20 April, 20 July, 20 October and 20 January is superseded by art. 51: the return is due one month after the period end, so a calendar quarter falls due 30 April, 31 July, 31 October and 31 January, if the period is the calendar quarter. File through E-services ([IDAL](https://www.investinlebanon.gov.lb/en/doing_business/tax_system)): open E-services, send the required documents, receive the E-pin by email, open the form online. All taxpayers issuing invoices and receipts also pay the fixed fiscal stamp monthly with an electronic declaration within 15 days after month end, unless using a licensed stamping machine (art. 35).

## Penalties and interest

Old figures, unverified: late filing LBP 50,000 a day, late payment 1.5% a month, failure to register: backdated assessment plus penalties. Late declarations and incorrect information carry financial penalties, multiplied on repeat violations (Budget 2026 art. 18, [Citizen Budget](https://institutdesfinances.gov.lb/sites/default/files/2026-04/Pamphlet-Citizen%20Budget%202026-Apr26-En-final.pdf)). Amounts: unverified. An exceptional 85% reduction of penalties owed to public entities applied if paid within three months of the law's publication, with a reduced penalty of at least LBP 200,000 or USD 5; that window has passed unless extended (art. 43).

## Cross-border points

- **Reverse charge on services from non-resident** : Services from non-resident: self-assess at 11%. Claim input if taxable. Net zero. Exchange rate: must confirm with practitioner.
- **Import of goods VAT** : Import of goods: VAT at 11% on CIF plus customs plus excise. Collected by Lebanese Customs.

## Two worked examples that recompute

Rate 11% is unverified.

```oa-check
name: Standard sale
inputs:
  net: 10000000
steps:
  - vat: net * 0.11
  - total: net + vat
expected:
  vat: 1100000
  total: 11100000
```

Import: CIF LBP 100M plus duty LBP 5M. Decision: if 12% were enacted, the same import costs LBP 12.6M, LBP 1.05M more.

```oa-check
name: Import, 11% against 12%
inputs:
  base: 105000000
steps:
  - at11: base * 0.11
  - at12: base * 0.12
  - gap: at12 - at11
expected:
  at11: 11550000
  at12: 12600000
  gap: 1050000
```

#### Example 1 -- Standard sale

Company sells goods LBP 10,000,000 net. Output VAT = LBP 1,100,000 (11%). Total = LBP 11,100,000.

#### Example 2 -- Foreign currency reverse charge

UK law firm invoices USD 10,000. Reverse charge at 11% on LBP equivalent. Exchange rate: flag for practitioner -- conversion rate is critical during crisis.

#### Edge cases

Flag for practitioner. Multiple rates exist.

Cash refunds from MOF may not be obtainable. Carry forward.

Zero-rated only with customs declaration, bill of lading, proof of delivery.

Input VAT on purchases for exempt banking not recoverable.

Entertainment blocked for input recovery.

First sale may be taxable. Escalate.

#### Test suite

LBP 10M net. Expected: output LBP 1.1M (11%).

USD 5,000 to France. Expected: 0%. Input recoverable.

UK firm USD 10,000. Expected: 11% self-assessed. Exchange rate: flag.

Bank interest LBP 500M. Expected: no output. Input LBP 2.2M not recoverable.

Turkish goods CIF LBP 100M + duty LBP 5M. Expected: VAT base LBP 105M, VAT LBP 11.55M.

Dinner LBP 5M + VAT LBP 550K. Expected: input = 0.

#### Escalation protocol

```
REVIEWER FLAG / ESCALATION REQUIRED
[Standard format -- include note about economic crisis verification]
```

#### Out of scope -- direct tax

- Corporate income tax: 17%
- Personal income tax: progressive 2%-25%
- Social security (NSSF): employer and employee contributions

#### Prohibitions

- NEVER apply a rate without checking the Ministry for whether 12% is enacted
- NEVER allow input recovery on exempt supplies
- NEVER use exchange rate without practitioner confirmation
- NEVER assume pre-crisis rules apply unchanged
- NEVER assume MOF systems operational without confirming
- NEVER compute numbers -- engine handles arithmetic

## Ask the client first

**Minimum viable** -- bank statement. Acceptable from Bank Audi, Blom Bank, Byblos Bank, BankMed, Fransabank, or any Lebanese bank.

- **R-LB-1 -- Exchange rate determination** : Trigger: foreign currency transactions without confirmed MOF rate guidance. Message: "Multiple exchange rates exist. MOF guidance on applicable rate must be confirmed by practitioner before VAT calculations."  _(R-LB-1)_
- **R-LB-2 -- Crisis-era enforcement** : Trigger: questions about current MOF operational status. Message: "Verify current MOF enforcement position with local practitioner."  _(R-LB-2)_

## Sources

| Source | URL | Read on |
|---|---|---|
| Ministry of Finance Citizen Budget 2026, measures list, all pages (hosted by Institut des Finances, a Ministry body) | https://institutdesfinances.gov.lb/sites/default/files/2026-04/Pamphlet-Citizen%20Budget%202026-Apr26-En-final.pdf | 2026-11-01 |
| IDAL, Doing Business, Tax System (whole page) | https://www.investinlebanon.gov.lb/en/doing_business/tax_system | 2026-11-01 |
| Ministry of Finance, finance.gov.lb tax pages | unverified: CAPTCHA, not read | not read |

Not yet confirmed: every row marked unverified. finance.gov.lb returned a CAPTCHA during this refresh, which we did not solve; only archive indexes of it were read, and the text of 2026 Budget Law No. 40 of 10 Feb 2026 was not opened (the law number comes from a search summary, not an official page). Citizen Budget wording covers measures only, so anything else in that law is unread.

**Disclaimer.**

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
