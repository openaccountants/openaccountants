---
name: kz-company-formation
description: "Kazakhstan 2026 LLP formation: founder documents, registration workflow, capital minima, contribution deadlines and regulated-sector exceptions."
jurisdiction: KZ
tax_year: 2026
last_updated: 2026-11-14
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: tax

version: 0.1
type: filing-howto
category: international
---

# Kazakhstan LLP company formation v0.1

> **General reference only.** This skill produces draft working papers for review by a qualified Kazakhstan professional before filing, payment or taking a tax position. It is not approval of any particular taxpayer’s facts.

## Who this applies to

People incorporating an ordinary Kazakhstan ТОО/LLP and selecting the appropriate legal-entity registration path. ТОО is distinct from personal ИП, which is handled by `kz-formation`. АО/JSC, branches and representative offices remain alternative forms requiring their own current sector/registration analysis; this file does not invent their capital minima or commercial powers.

## Rates, bands and thresholds

| Item and conditions | Rule for 2026 | Official source |
|---|---|---|
| Ordinary LLP minimum capital | 100 МРП at the document-submission date; 100 in words on the page (LLP Law art. 23) | https://adilet.zan.kz/rus/docs/Z980000220_ |
| Small-business LLP exception | Minimum KZT 0; qualifying state Islamic special-finance company also has a zero minimum (art. 23) | https://adilet.zan.kz/rus/docs/Z980000220_ |
| Sector exceptions | Microfinance and payment organisations use sector-law capital minima; do not apply the ordinary 100-МРП/zero rule blindly (art. 23) | https://adilet.zan.kz/rus/docs/Z980000220_ |
| 2026 ordinary minimum, derived | KZT 432,500 = 100 × KZT 4,325, if the 2026 submission-date МРП applies | https://www.gov.kz/org/kgd-ulytau/documents/details/939202?lang=ru |
| Capital payment | Ordinary general-meeting deadline no more than 1 year after registration; special deferred usable-property case can be recognised under a notarised undertaking up to 3 years (art. 24; figures in words on the page) | https://adilet.zan.kz/rus/docs/Z980000220_ |

## The base

LLP Law art. 2 permits establishment by 1 or more persons and provides separate legal personality. Limited liability has statutory exceptions, including unpaid-contribution joint exposure; do not promise absolute immunity. Confirm small/other enterprise classification and regulated-activity status before the capital rule. Document contributions, participants’ shares and the meeting’s payment deadline. Money/non-money contributions and valuation requirements follow art. 23; refer complex property, microfinance/payment/financial entities and unpaid contributions.

Use the official government legal-entity/branch service. Check IIN availability for applicant, manager and founders. Select the actual registration type; enter address, name, manager and founder information in the current application. Prepare the charter/founding arrangements or valid standard-charter choice internally, distinguishing documents needed to create the entity from documents actually submitted to the registrar. The old statement that all charters/founding agreements must always be uploaded was too broad.

The government service requires a foreign legal founder’s legalised register extract or equivalent and notarised translations into Kazakh and Russian; a foreign individual founder supplies passport/identity documentation with the prescribed notarised translations into Kazakh and Russian. Check any applicable treaty/apostille substitution and founder/immigration restrictions; do not assume any nationality can incorporate on identical terms. Scan/attach the required documents to the actual relevant founder, sign by applicant and required founders with ЭЦП, then retain the service-history registration certificate/status and BIN. Do not submit duplicate applications during processing. Commercial LLP registration is through Government for Citizens under art. 19; it is not universally an act of the Ministry of Justice itself.

## Deadlines and filing

Check the actual official service category for its current completion time and charge; the old 1–3-business-day estimate is not a legal guarantee. A ТОО is formed at state registration under art. 19. Keep the registered capital/participants, charter/decisions, BIN and payment evidence. Choose the tax regime under art. 716 within its applicable legal-entity election window, then establish accounting, CIT/special-regime, VAT and payroll calendars through the owning skills. Capital contribution deadline and tax filing dates are distinct.

## Penalties and interest

Registration refusal and contribution default are separate matters. Art. 24 addresses unpaid contributions, loss compensation and possible capital reduction. Do not insert an unverified monetary penalty or use a capital shortfall as a presumed tax deduction.

## Cross-border points

Foreign founder documentation and rights, branch/representative-office powers, regulated industries, ownership restrictions and treaty/immigration issues require specialist confirmation. Annual CIT, registered VAT, payroll and statutory accounting obligations remain separate from incorporation; simplified taxation does not mean no company accounts.

## Two worked examples that recompute

Case 1: hypothetical ordinary non-small, non-regulated LLP submits in 2026. Minimum capital is KZT 432,500; founders commit KZT 500,000 and KZT 500,000, total KZT 1,000,000 and headroom KZT 567,500. This does not change the meeting’s contribution deadline.

```oa-check
name: Ordinary LLP capital reconciliation
inputs:
  mrp: 4325
  first: 500000
  second: 500000
steps:
  - minimum: 100 * mrp
  - capital: first + second
  - headroom: capital - minimum
expected:
  minimum: 432500
  capital: 1000000
  headroom: 567500
```

Case 2: a hypothetical qualifying small LLP chooses KZT 100,000 voluntary charter capital despite the zero statutory minimum. KZT 40,000 has been contributed; KZT 60,000 remains due under the adopted obligation. Zero minimum does not extinguish the chosen capital commitment.

```oa-check
name: Small LLP chosen capital remains payable
inputs:
  chosen_capital: 100000
  paid: 40000
steps:
  - unpaid: chosen_capital - paid
expected:
  unpaid: 60000
```

## Ask the client first

- Actual legal form, enterprise classification and regulated activity?
- Founders, residence/immigration entitlement, identity and ownership restrictions?
- Charter/standard charter, agreed capital, contribution form/valuation and deadline?
- Submission-date МРП, required translations/legalisation and signatures?
- Accepted certificate/BIN, regime election and post-registration accounting/payroll/VAT setup?

## Sources

| Source and operative sections actually read | URL | Read on |
|---|---|---|
| Read for current LLP Law arts. 2, 19 and 23–24, ordinary browser | https://adilet.zan.kz/rus/docs/Z980000220_ | 2026-11-14 |
| Read for government company/branch service: application, foreign founders, signing and result | https://www.gov.kz/services/3932?lang=ru | 2026-11-14 |
| Read for 2026 budget law art. 7 | https://www.gov.kz/org/kgd-ulytau/documents/details/939202?lang=ru | 2026-11-14 |
| Read for Tax Code art. 716 election rules | https://www.gov.kz/org/kgd-akmola/documents/details/1084149?lang=ru | 2026-11-14 |

Not yet confirmed: JSC capital/securities rules; branch versus representative-office commercial powers; current completion guarantees/charges by service category; foreign-founder/immigration entitlement and treaty/apostille substitutions; regulated capital regimes. The old KZT 393,200 calculation is a 2025 amount, not the 2026 minimum.
