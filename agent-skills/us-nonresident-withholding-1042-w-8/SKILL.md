---
name: us-nonresident-withholding-1042-w-8
description: "How a US payer withholds and reports tax on payments to foreign persons in 2026 under chapter 3. Covers collecting Forms W-8BEN, W-8BEN-E, W-8ECI, W-8IMY and W-8EXP (and W-9 for US persons), their 3-year validity, the 30% rate on US-source fixed or determinable income (dividends, rents, royalties, services performed in the US), treaty rates claimed on the W-8, the exemptions for portfolio interest and bank deposit interest, deposits (USD 2,000 and USD 200 rules), and Forms 1042 and 1042-S due 15 March 2027, e-filed through IRIS. Points to chapter 4 (FATCA) withholding. Trigger on \"Form 1042\", \"Form 1042-S\", \"W-8BEN\", \"W-8BEN-E\", \"withholding on foreign contractors\", \"paying a foreign person\", \"30% withholding\", \"NRA withholding\", \"treaty rate withholding\", \"chapter 3 withholding\". Federal only."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/us-nonresident-withholding-1042-w-8"
  jurisdiction: "US"
  tax_year: "2026"
  last_updated: "2026-11-13"
---

# US withholding on payments to foreign persons: W-8 forms, Forms 1042 and 1042-S, 2026

> **Source-cited draft.** Built from IRS Pub. 515 (2026), the 2025 Instructions for Form 1042, the 2026 Instructions for Form 1042-S, the Instructions for Form W-8BEN and 26 U.S.C. 1441 and 1471, read on 2026-11-13. No accountant has reviewed it. All outputs must be reviewed by a qualified tax professional before filing.

**Answer first.** A US payer (the withholding agent) must withhold **30%** of the gross amount of US-source fixed or determinable income paid to a foreign person, such as dividends, rents, royalties and fees for services performed in the US, unless a valid Form W-8 supports a lower treaty rate or an exemption. Fees for services performed entirely outside the US are not US-source, so no withholding. Portfolio interest and bank deposit interest are exempt. The agent deposits the tax under the USD 2,000 and USD 200 rules, then files **Form 1042** and **Forms 1042-S** by **15 March 2027** for 2026 payments, and gives each payee a Form 1042-S. For 2026 Forms 1042-S, e-filing must use IRIS.

## Scope and who this is for

In scope: a US business, partnership, trust or individual paying US-source income to a foreign person in 2026; documentation; the chapter 3 rate; deposits; Forms 1042, 1042-S and 1042-T.

Out of scope, and where it goes:

| Topic | Skill |
| --- | --- |
| Buying US real property from a foreign seller (FIRPTA, Form 8288) | `us-firpta-withholding-8288` |
| The foreign person's own US return | `us-form-1040-nr-nonresident-return` |
| A foreign-owned US company's Form 5472 | `us-form-5472-foreign-owned-us` |
| Paying US contractors (Form W-9 and Form 1099-NEC) | `us-1099-nec-issuance` |
| Wages paid to nonresident employees (Form W-2, Form 941) | `us-form-941-940-payroll` |
| Whether a person is a US resident for tax | `us-tax-residency` |
| Chapter 4 (FATCA) withholding on payments to foreign financial institutions and entities | refer (see the refusal table) |
| Partnership withholding on effectively connected income (section 1446) | refer |

## Ask the client first

1. **Who is the payee** (individual or entity, country), and do you hold a signed Form W-8 or W-9? When was it signed?
2. **What is the payment for** (dividend, interest, rent, royalty, service fee, prize, scholarship), and **where were any services performed**? Days in the US and days outside, if a person worked in both.
3. **Amounts and dates** of every 2026 payment to each foreign payee.
4. **Does the W-8 claim a treaty rate?** Which article and rate is on Part II of Form W-8BEN (line 10) or Part III of Form W-8BEN-E?
5. **Is the income connected with a US business of the payee?** If yes, the payee should give Form W-8ECI instead.
6. **Does the payer have an EIN and an EFTPS enrolment** for deposits?

## The method, step by step

### Rates, bands and thresholds

| Item | Amount, 2026 | Source |
| --- | --- | --- |
| Statutory withholding rate on US-source FDAP income paid to a foreign person | 30% | [26 U.S.C. 1441(a)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap3-subchapA-sec1441.htm); [IRS Pub. 515 (2026)](https://www.irs.gov/pub/irs-pdf/p515.pdf) |
| Chapter 4 (FATCA) withholding rate on withholdable payments to non-compliant foreign entities | 30% | [26 U.S.C. 1471(a)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap4-sec1471.htm); [IRS Pub. 515 (2026)](https://www.irs.gov/pub/irs-pdf/p515.pdf) |
| Deposit within 3 business days after a quarter-monthly period ends, if undeposited tax is at least | USD 2,000 | [Instructions for Form 1042 (2025)](https://www.irs.gov/pub/irs-pdf/i1042.pdf) |
| Deposit within 15 days after month end, if undeposited tax at month end is at least (and under USD 2,000) | USD 200 | [Instructions for Form 1042 (2025)](https://www.irs.gov/pub/irs-pdf/i1042.pdf) |
| Forms 1042 and 1042-S for 2026 payments due | 15 March 2027 | [IRS Pub. 515 (2026)](https://www.irs.gov/pub/irs-pdf/p515.pdf); [Instructions for Form 1042-S (2026)](https://www.irs.gov/pub/irs-pdf/i1042s.pdf) |
| Forms 1042-S must be e-filed if the filer has this many information returns in the year | 10 or more | [Instructions for Form 1042-S (2026)](https://www.irs.gov/pub/irs-pdf/i1042s.pdf) |
| Form W-8BEN validity | signing date to the last day of the third following calendar year | [Instructions for Form W-8BEN](https://www.irs.gov/pub/irs-pdf/iw8ben.pdf) |

Treaty rates are not listed here: they differ by country and income type. Take the rate from the article the payee cites, checked against the IRS tax treaty tables and the treaty text, and refuse a rate that is not on a valid form.

### Steps

1. **Is the payee foreign?** Collect Form W-9 from US persons and the right Form W-8 from foreign ones:
   - **W-8BEN**: foreign individual who is the beneficial owner;
   - **W-8BEN-E**: foreign entity that is the beneficial owner (it also states the chapter 4 status);
   - **W-8ECI**: income effectively connected with the payee's US trade or business (no chapter 3 withholding; the payee files a US return);
   - **W-8IMY**: intermediary, flow-through entity or a foreign branch, with the owners' forms behind it;
   - **W-8EXP**: foreign government, international organisation, foreign central bank, tax-exempt organisation.
2. **No valid form?** Apply the presumption rules in Pub. 515: an undocumented payee is often presumed foreign, so withhold at 30%. A form is invalid if unsigned, expired, or the payer knows it is wrong.
3. **Is the income US-source and FDAP?** Dividends from US corporations, interest paid by US persons, rents from US property, royalties for use in the US, and pay for services performed in the US are US-source. Services performed outside the US are foreign-source: no chapter 3 withholding and no Form 1042-S. Split a fee by days worked in and out of the US where needed.
4. **Exemptions.** Portfolio interest (on registered obligations, not paid to a 10% shareholder, a bank on an ordinary loan, or a related controlled foreign corporation) and bank deposit interest not connected with a US business are not subject to chapter 3 withholding, though portfolio interest is still reported on Form 1042-S. Effectively connected income documented on Form W-8ECI is not withheld under chapter 3.
5. **Rate.** 30%, or the treaty rate claimed on a valid W-8BEN or W-8BEN-E (with a US or foreign TIN where the form requires one, and the limitation on benefits box on W-8BEN-E).
6. **Withhold from the gross amount** when paid (credited, or made available). If the payer agrees to bear the tax instead, the tax is computed on the grossed-up amount (refer if this arises).
7. **Chapter 4 check.** For payments to foreign entities, read the chapter 4 status on Form W-8BEN-E. A non-participating foreign financial institution, or a passive entity that does not identify its US owners, is withheld at 30% under chapter 4. Credit chapter 4 withholding against chapter 3, so the total does not exceed 30% (refer for the detail).
8. **Deposit** the tax by EFTPS: USD 2,000 or more undeposited at the end of a quarter-monthly period (the 7th, 15th, 22nd and last day of the month) within 3 business days; USD 200 to USD 1,999 at month end within 15 days after the month; under USD 200 at year end, with Form 1042 or by 15 March.
9. **Report.** One Form 1042-S per payee per type of income (including exempt amounts). File with the IRS and give to the payee by 15 March 2027. File Form 1042 (the annual return) by the same date, reconciling the tax withheld with the deposits. Paper Forms 1042-S go with Form 1042-T. Form 7004 extends filing of Form 1042, not payment.

## Boundary and exception table

| Situation | Treatment |
| --- | --- |
| Foreign freelancer works entirely abroad | Foreign-source: no withholding, no Form 1042-S; keep a W-8BEN on file to show foreign status (no Form 1099 needed) |
| Foreign freelancer worked some days in the US | Withhold on the US-source share (days in the US over total days), unless a treaty or Form 8233 exempts it |
| Payee gives Form W-9 | US person: no chapter 3 withholding; Form 1099 rules apply |
| W-8BEN signed 10 June 2023 | Valid to 31 December 2026; get a new one for 2027 payments |
| Dividends to a foreign corporation through a US broker | The broker is usually the withholding agent; the issuer does not withhold twice |
| Interest on a loan from a foreign parent to its US subsidiary | Not portfolio interest (10% shareholder); 30% or treaty rate; check the US subsidiary's Form 5472 too |
| Payee claims treaty benefits for services (independent personal services) | Individuals use Form 8233, not Form W-8BEN, for compensation for personal services |

### Defaults when a fact is missing

| Missing fact | Default, and flag it |
| --- | --- |
| No W-8 or W-9 | Presume foreign under Pub. 515 and withhold 30%; get a form before the next payment |
| Treaty rate not stated on the form | 30% |
| Where services were performed | Ask; do not assume all abroad |
| Chapter 4 status on a W-8BEN-E | Refer before paying |

### Red flags to raise with the client

| Flag | Why it matters |
| --- | --- |
| Foreign payees paid for years with no forms and no withholding | The withholding agent is liable for the tax not withheld, plus penalties and interest |
| A treaty rate claimed by a payee in a country with no treaty, or by an entity with no limitation on benefits box ticked | The claim fails: withhold 30% |
| Royalties or rents paid to a foreign person with no W-8 | 30% due on the gross amount |
| Forms 1042-S not matched to Form 1042 | IRS notices; reconcile before filing |

## Worked cases

**Case 1, a decision: does a foreign consultant's fee need withholding?** A US company pays a consultant resident abroad a USD 40,000 fee for a project. The consultant gives a valid Form W-8BEN and claims no treaty benefit. She worked 30 of the 120 project days in the US. If all work had been done abroad, nothing is withheld. Here 30 of 120 days, a quarter, were in the US: USD 10,000 is US-source and USD 3,000 must be withheld at 30%, with a Form 1042-S for USD 10,000. Recommend either withholding USD 3,000 or getting a valid treaty claim on Form 8233 before payment.

```oa-check
name: Foreign consultant, fee split by days worked in the US (2026)
inputs:
  fee: 40000
  us_days: 30
  total_days: 120
steps:
  - us_source: fee * us_days / total_days
  - withholding_if_split: us_source * 0.30
  - withholding_if_all_abroad: 0
expected:
  us_source: 10000.00
  withholding_if_split: 3000.00
  withholding_if_all_abroad: 0
```

**Case 2, dividends and portfolio interest to one foreign individual.** On 5 March 2026 a US company pays a foreign shareholder with a valid Form W-8BEN (no treaty rate claimed) USD 20,000 of dividends and USD 8,000 of interest on registered bonds that qualifies as portfolio interest. Withholding: 30% of USD 20,000 = USD 6,000; the interest is exempt. The USD 6,000 is undeposited at the end of the quarter-monthly period ending 7 March and is at least USD 2,000, so it must be deposited within 3 business days. Two Forms 1042-S: dividends USD 20,000 with USD 6,000 withheld, and interest USD 8,000 with an exemption code.

```oa-check
name: Dividends and portfolio interest to a foreign individual (2026)
inputs:
  dividends: 20000
  portfolio_interest: 8000
steps:
  - tax_on_dividends: dividends * 0.30
  - tax_on_interest: portfolio_interest * 0
  - total_withheld: tax_on_dividends + tax_on_interest
  - over_quarter_monthly_rule: total_withheld - 2000
expected:
  tax_on_dividends: 6000.00
  tax_on_interest: 0
  total_withheld: 6000.00
  over_quarter_monthly_rule: 4000.00
```

## When to refuse or refer

| Code | Situation | Action |
| --- | --- | --- |
| R-NRW-CH4 | Payment to a foreign financial institution or a foreign entity with an unclear chapter 4 status | Refer: chapter 4 (FATCA) rules |
| R-NRW-INTERMED | Payee is an intermediary, qualified intermediary or flow-through (Form W-8IMY) | Refer |
| R-NRW-GROSSUP | Payer agreed to bear the tax | Refer: grossed-up computation |
| R-NRW-1446 | Partnership with foreign partners and effectively connected income | Refer: section 1446 and Forms 8804 and 8805 |
| R-NRW-PAST | Several years of unwithheld payments | Refer: correction and penalty relief |

## Filing and payment

For 2026 payments: deposits by EFTPS through the year under the rules above; Forms 1042-S to the IRS and to each payee, and Form 1042, by **15 March 2027** (the next business day if it falls on a weekend or holiday). 2026 Forms 1042-S are e-filed through IRIS, which replaces the FIRE system for forms due in 2027. Form 1042 itself must be e-filed where the instructions require it. Keep every W-8 and W-9 for as long as it may be relevant to the tax.

## Completion checklist

- A valid, unexpired W-8 or W-9 on file for every payee before payment.
- Source of each payment decided, with days worked in and outside the US for services.
- 30% or a documented treaty rate applied to the gross amount; exemptions recorded.
- Deposits made on time under the USD 2,000 and USD 200 rules.
- Forms 1042-S (one per payee per income type) and Form 1042 filed and furnished by 15 March 2027, reconciled to deposits.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| IRS Pub. 515 (2026). Read for the 30% rate, the W-8 forms, presumption rules, portfolio and bank deposit interest exemptions, source rules, chapter 4 withholding, and IRIS for 2026 Forms 1042-S due 15 March 2027. | https://www.irs.gov/pub/irs-pdf/p515.pdf | 2026-11-13 |
| Instructions for Form 1042 (2025). Read for deposit rules (USD 2,000 within 3 business days after a quarter-monthly period; USD 200 within 15 days after month end), the 15 March due date and Form 7004. | https://www.irs.gov/pub/irs-pdf/i1042.pdf | 2026-11-13 |
| Instructions for Form 1042-S (2026). Read for filing and furnishing by 15 March, e-filing for 10 or more returns, Form 1042-T for paper filing. | https://www.irs.gov/pub/irs-pdf/i1042s.pdf | 2026-11-13 |
| Instructions for Form W-8BEN. Read for "Expiration of Form W-8BEN": valid to the last day of the third succeeding calendar year. | https://www.irs.gov/pub/irs-pdf/iw8ben.pdf | 2026-11-13 |
| 26 U.S.C. 1441 (govinfo, 2024 edition). Read for (a) withholding of 30%. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap3-subchapA-sec1441.htm | 2026-11-13 |
| 26 U.S.C. 1471 (govinfo, 2024 edition). Read for (a) the 30% chapter 4 withholding. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap4-sec1471.htm | 2026-11-13 |

Not yet confirmed: the 2026 Instructions for Form 1042 were not yet published when read; the deposit rules are from the 2025 instructions. Treaty rates are deliberately not stated.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-13. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `us-nonresident-withholding-1042-w-8` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/us-nonresident-withholding-1042-w-8. If neither is available, confirm every figure against the official source pages cited above before relying on it.
