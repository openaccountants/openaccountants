---
name: mc-income-tax
description: "Monaco individual income tax and residence reference for 2026. Covers the official absence of resident personal income tax within its stated scope, French national treaty screening, fiscal residence certificate evidence and the alternative principal stay test. Use for Monaco resident tax, French citizens in Monaco, residence certificates and relocation questions. Separates personal receipts from business profits, VAT, social contributions and foreign taxation. Includes two arithmetic controls with stated factual assumptions and identifies unverified foreign procedures. Source cited partial draft awaiting review by a named Monaco professional."
jurisdiction: MC
category: international
tax_year: 2026
last_updated: 2026-10-24
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
version: 1.2
---

# Monaco individual income tax and residence

> **Source-cited draft; partial scope.** Checked 24 October 2026. No named Monaco professional has reviewed this Guide. It produces a working paper, not a filing or a final tax position. Read the [country gap register](README.md) before use.

## Who this applies to

Tax year 2026. The official Monaco government describes absence of personal income tax for Monegasque nationals and residents genuinely established in Monaco, subject to the France–Monaco convention. It expressly preserves other states' taxation. This is not a rule exempting every receipt earned by any person with a residence card. An individual carrying on an industrial or commercial business must separately test ISB: article 4 expressly provides for assessment in the proprietor's name. [Government, Tax in Monaco](https://monservicepublic.gouv.mc/en/themes/tax/information/general-information/tax-in-monaco); [Ordinance 3.152, arts. 1, 4](https://legimonaco.mc/tnc/ordonnance/1964/03-19-3.152).

French nationals require a separate treaty analysis. Article 7's historic test is five years of habitual Monaco residence at 13 October 1962, not merely arrival before that date. French official doctrine also addresses continuous residence since birth, sovereign/public service, marriage, children and historic dual-national cases. Do not treat all French nationals as identical or a modern residence certificate as treaty exemption evidence. [Convention, art. 7](https://legimonaco.mc/tai/convention/1963/05-18-tai1l000235/); [BOI-INT-CVB-MCO-10, I-A](https://bofip.impots.gouv.fr/bofip/12995-PGP.html/identifiant=BOI-INT-CVB-MCO-10-20210602).

## Rates, bands and thresholds

| Item | Amount or test | Period | Official source |
|---|---|---|---|
| Monaco personal income tax within the government-described scope | No personal income tax | Checked 2026 | [Fiscal paragraphs](https://monservicepublic.gouv.mc/en/themes/tax/information/general-information/tax-in-monaco) |
| Historic French-national residence test | Five years at 13 October 1962 | Treaty test, not a modern arrival cut-off | [Art. 7](https://legimonaco.mc/tai/convention/1963/05-18-tai1l000235/) |
| Principal-stay test for fiscal residence certificate | At least 183 days, or longer physical presence than in any other country | 2026 procedure | [Art. 3](https://legimonaco.mc/tnc/ordonnance/1986/03-28-8.566/) |
| Fiscal residence certificate validity | One year | 2026 procedure | [Art. 4](https://legimonaco.mc/tnc/ordonnance/1986/03-28-8.566/) |

## The base

There is no Monaco resident personal income tax computation within the scope above. Classify income before recording that result: personal receipts, an ISB business, VAT turnover and social contributions are different questions. The absence of personal income tax does not establish absence of inheritance, gift, registration or transaction taxes. This draft supplies no general wealth, property or capital-gains exemption and no foreign-tax calculation. [Government tax information](https://monservicepublic.gouv.mc/en/themes/tax/information/general-information/tax-in-monaco); [Arts. 1, 4](https://legimonaco.mc/tnc/ordonnance/1964/03-19-3.152).

A fiscal certificate applicant of foreign nationality needs a current residence card, evidence of accommodation, prior-year utilities and other requested residence evidence. Article 3 permits principal stay, the principal centre of activities, or the home test subject to its order: home is considered when principal stay cannot be defined. Principal activity centre concerns principal investments, business seat/effective management and asset administration. Bilateral arrangements remain relevant. Day counting is evidence for one test, not automatic exclusive worldwide tax residence. [Arts. 3–4](https://legimonaco.mc/tnc/ordonnance/1986/03-28-8.566/).

## Deadlines and filing

The government-described absence of Monaco personal income tax does not create a resident personal-income-tax return computation here. Establish and track any French or other foreign return separately; this Guide has not verified its deadlines or forms. For a Monaco fiscal residence certificate, apply to the Direction de la Sûreté Publique with article 3 evidence and renew against the one-year validity. The administrative certificate under articles 1–2 is different and expires after six months. A French treaty certificate of domicile is also a distinct document. [Arts. 1–4](https://legimonaco.mc/tnc/ordonnance/1986/03-28-8.566/); [I-A-1-b, residence evidence](https://bofip.impots.gouv.fr/bofip/12995-PGP.html/identifiant=BOI-INT-CVB-MCO-10-20210602).

## Penalties and interest

Do not invent a Monaco personal-income-tax late-return penalty where this Guide has no such return. Article 3 residence declarations are made under the penalties referenced to Penal Code article 98; the current penalty amounts and foreign personal-tax sanctions have not been verified here. Business ISB, VAT and social defaults have separate sourced rules in the companion Guides. [Art. 3](https://legimonaco.mc/tnc/ordonnance/1986/03-28-8.566/).

## Cross-border points

Resolve nationality, actual residence, French article 7 exceptions, foreign-source income and any foreign residence claim before a conclusion. The French doctrine treats residence interruptions and foreign economic/professional connections as material even for historic cases. Do not infer treaty benefits from no Monaco personal income tax. French and other-country tax, social-security affiliation and treaty entitlement remain separate working papers. [I-A-1 and I-A-2](https://bofip.impots.gouv.fr/bofip/12995-PGP.html/identifiant=BOI-INT-CVB-MCO-10-20210602); [Government fiscal scope](https://monservicepublic.gouv.mc/en/themes/tax/information/general-information/tax-in-monaco).

## Two worked examples that recompute

### Personal receipts within the stated scope

Assume a non-French person genuinely resident in Monaco, receiving EUR 60,000 salary and EUR 2,000 personal interest, with no separate ISB activity. Within the government-described personal-tax scope, Monaco personal income tax is zero. The EUR 62,000 tally is not a social-contribution base or proof of foreign exemption.

```oa-check
name: Personal receipts tally within established Monaco scope
inputs:
  salary: 60000
  interest: 2000
steps:
  - receipts: salary + interest
  - monaco_personal_tax: receipts * 0
expected:
  receipts: 62000
  monaco_personal_tax: 0
```

### Fewer than 183 days

An applicant records 170 days in Monaco, 160 in France and 35 in Italy. Monaco exceeds every other individual country, so the alternative principal-stay limb is met on those assumed complete records. The 13-day shortfall from 183 does not alone defeat it. Assume this applicant is French: the certificate test does not decide article 7 or calculate French tax. The checks below test counts, not a final residence determination.

```oa-check
name: Alternative principal stay count with French tax unresolved
inputs:
  monaco: 170
  france: 160
  italy: 35
steps:
  - days: monaco + france + italy
  - margin: monaco - max(france, italy)
  - shortfall: 183 - monaco
expected:
  days: 365
  margin: 10
  shortfall: 13
```

## Ask the client first

- What are all current and historic nationalities and dates of residence moves?
- What do travel records, home, family and activity evidence show?
- What income sources and business activities exist in each country?
- Is any French historic, birth, service, marriage or dual-national exception supported?
- What other countries claim residence or tax, and which certificates are held?

## Sources

| Official source and provisions read | URL | Read on |
|---|---|---|
| Government, personal tax fiscal paragraphs; successful preserved retrieval, later 403 | https://monservicepublic.gouv.mc/en/themes/tax/information/general-information/tax-in-monaco | 2026-10-24 |
| Ordinance 3.152, arts. 1 and 4 | https://legimonaco.mc/tnc/ordonnance/1964/03-19-3.152 | 2026-10-24 |
| France–Monaco convention, arts. 7 and 22 | https://legimonaco.mc/tai/convention/1963/05-18-tai1l000235/ | 2026-10-24 |
| BOI-INT-CVB-MCO-10, I-A-1 and I-A-2 | https://bofip.impots.gouv.fr/bofip/12995-PGP.html/identifiant=BOI-INT-CVB-MCO-10-20210602 | 2026-10-24 |
| Ordinance 8.566, arts. 1–4 | https://legimonaco.mc/tnc/ordonnance/1986/03-28-8.566/ | 2026-10-24 |

The government personal-tax page was read from the successful 15:18 UTC retrieval on this date. Its later recheck returned HTTP 403. That failure is recorded in the [source register](../../../docs/research/2026-10-24-monaco-sources.json); it is not a fresh successful retrieval.

**Not yet confirmed:** individual foreign returns, full treaty-exception applications, residence declaration sanctions and estate/transaction-tax computations. The alternative day-count example does not close those gaps.

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
