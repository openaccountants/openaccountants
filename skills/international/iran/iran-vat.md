---
name: iran-vat
description: Use this skill whenever asked to prepare, review, or classify transactions for an Iran VAT return. Trigger on phrases like "Iran VAT", "INTA tax", "Iran value added tax". Iran imposes VAT at 10% (9% VAT + 1% municipal) under the VAT Law of 2008 as amended. Iran uses the Solar Hijri calendar for all tax purposes. ALWAYS read this skill before handling any Iran VAT work.
version: 2.0
---

# Iran VAT Return Skill v2.0

## Section 1 -- Quick reference

| Field | Value |
|---|---|
| Country | Iran (Islamic Republic) |
| Combined rate | 10% (9% VAT + 1% municipal tax) |
| Zero rate | 0% (exports) |
| Exempt | Unprocessed agricultural, bread/flour, books, medical, education, banking/insurance, public transport, handmade carpets |
| Filing portal | https://tax.gov.ir |
| Authority | Iranian National Tax Administration (INTA) |
| Currency | IRR (Iranian Rial) |
| Filing frequency | Quarterly (seasonal, Solar Hijri calendar) |
| Primary legislation | VAT Law of 2008; 2025 Budget Act |
| Contributor | Open Accounting Skills Registry |
| Validated by | Pending |
| Last research update | April 2026 |

**Conservative defaults:**

| Ambiguity | Default |
|---|---|
| Unknown rate | 10% (9% + 1%) |
| Unknown purchase status | Not deductible |
| Unknown counterparty | Domestic Iran |

---

## Section 2 -- Required inputs and refusal catalogue

**Minimum viable** -- bank statement. Acceptable from Bank Melli, Bank Mellat, Bank Saderat, Bank Tejarat, Parsian Bank, or any Iranian bank.

**Refusal catalogue:**

**R-IR-1 -- Free Trade Zone.** Trigger: operations in Kish, Qeshm, Chabahar, Arvand, Aras zones. Message: "Free zone VAT rules vary by zone. Escalate to specialist."

**R-IR-2 -- Oil/gas sector.** Message: "Escalate to specialist."

---

## Section 3 -- Supplier pattern library

### 3.1 Iranian banks (exempt -- exclude)

| Pattern | Treatment | Notes |
|---|---|---|
| BANK MELLI, MELLI IRAN | EXCLUDE | Exempt financial service |
| BANK MELLAT | EXCLUDE | Same |
| BANK SADERAT, BANK TEJARAT | EXCLUDE | Same |
| PARSIAN BANK, PASARGAD BANK | EXCLUDE | Same |
| INTEREST, LOAN | EXCLUDE | Out of scope |

### 3.2 Government

| Pattern | Treatment | Notes |
|---|---|---|
| INTA, SAZMAN MALIYATI | EXCLUDE | Tax payment |
| CUSTOMS, IRICA | Check for import VAT | Duty exclude; VAT recoverable |
| TAMIN EJTEMAEI, SOCIAL SECURITY | EXCLUDE | Social insurance |

### 3.3 Utilities

| Pattern | Treatment | Notes |
|---|---|---|
| TAVANIR, BARGH | Domestic 10% | Electricity |
| MOKHABERAT, MCI, IRANCELL, RIGHTEL | Domestic 10% | Telecoms |

### 3.4 SaaS and digital

| Pattern | Treatment | Notes |
|---|---|---|
| Non-resident digital services | Reverse charge 10% | Subject to payment restrictions |

---

## Section 4 -- Worked examples

### Example 1 -- Standard domestic sale

**Input:** Company sells goods IRR 100,000,000 net. Standard-rated.

VAT (9%) = IRR 9,000,000. Municipal (1%) = IRR 1,000,000. Total tax = IRR 10,000,000. Gross = IRR 110,000,000.

### Example 2 -- Free zone to mainland

Goods from Kish Free Zone to Tehran. Treated as import. VAT at 10% at customs checkpoint.

---

## Section 5 -- Classification rules

### 5.1 Standard rate 10% (9% VAT + 1% municipal)

Single combined rate for all taxable supplies. Both components reported separately on return.

### 5.2 Zero-rated (0%, input recoverable)

Exports of goods/services outside Iran. Goods to Free Trade Zones (conditions).

### 5.3 Exempt (no VAT, no recovery)

Unprocessed agricultural, livestock, bread/flour, books/newspapers, medical/pharmaceutical, education, banking/insurance, public transport, handmade carpets, gold bullion.

---

## Section 6 -- VAT return form structure

### Output

| Section | Description |
|---|---|
| Taxable sales | Sales at 10% combined |
| Zero-rated | Exports |
| Exempt | Exempt supplies |
| VAT component | 9% portion |
| Municipal tax | 1% portion |
| Reverse charge output | Self-assessed on imported services |

### Input

| Section | Description |
|---|---|
| Input VAT on purchases | 9% component recoverable |
| Input municipal on purchases | 1% component recoverable |
| Customs VAT | Import VAT |
| Reverse charge input | Self-assessed input |

### Net

Output minus input. Credit brought forward from prior season.

---

## Section 7 -- Reverse charge and imports

Services from non-resident: self-assess at 10% (9% + 1%). Claim input if taxable. Net zero.

Import of goods: VAT on CIF plus customs duties plus commercial profit tax. Collected by IRICA.

---

## Section 8 -- Deductibility and blocked input

Blocked: personal-use items, purchases for exempt supplies, entertainment (above limits), passenger vehicles for personal use, gifts/donations (above limits).

---

## Section 9 -- Filing, deadlines, and penalties

Filing is quarterly aligned to Solar Hijri seasons:

| Season | Months | Deadline (approx. Gregorian) |
|---|---|---|
| Spring | Farvardin-Khordad | ~July 6 |
| Summer | Tir-Shahrivar | ~October 7 |
| Autumn | Mehr-Azar | ~January 5 |
| Winter | Dey-Esfand | ~April 4 |

| Violation | Penalty |
|---|---|
| Late filing | 10% of tax due |
| Late payment | 2.5% per month |
| Failure to register | Backdated assessment + penalties |

---

## Section 10 -- Edge cases, test suite, and escalation

### Edge cases

**EC1 -- VAT/municipal split.** Always report 9% and 1% separately.

**EC2 -- Free zone to mainland.** Treated as import. VAT at customs.

**EC3 -- Agricultural exemption.** Unprocessed wheat exempt. No output, no input recovery.

**EC4 -- Foreign SaaS.** Reverse charge at 10%. Payment restrictions do not change VAT treatment.

**EC5 -- Export with docs.** Zero-rated if export documentation exists.

### Test suite

**Test 1 -- Standard sale.** IRR 100M net. Expected: VAT IRR 9M, municipal IRR 1M, total IRR 10M.

**Test 2 -- Export.** IRR equivalent of USD 10,000. Expected: 0%. Input recoverable.

**Test 3 -- Reverse charge.** Indian consulting USD 5,000. Expected: 10% self-assessed. Net zero.

**Test 4 -- Exempt medical.** Medicines IRR 500M. Expected: no output. Input IRR 20M not recoverable.

**Test 5 -- Import.** CIF IRR 1B + duty IRR 100M. Expected: VAT IRR 99M (9%), municipal IRR 11M.

### Escalation protocol

```
REVIEWER FLAG / ESCALATION REQUIRED
[Standard format]
```

### Out of scope -- direct tax

- Corporate income tax: 25%
- Personal income tax: progressive
- Social security: employer 23%, employee 7%

### Prohibitions

- NEVER apply rate other than 10% to standard taxable supplies
- NEVER allow input recovery on exempt supplies
- NEVER ignore municipal tax (1%) -- always collected with VAT
- NEVER issue invoices without Farsi text
- NEVER use Gregorian dates on official filings
- NEVER compute numbers -- engine handles arithmetic

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com).
