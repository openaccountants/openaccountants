---
name: ne-corporate-income-tax
description: "Niger corporate income tax (impôt sur les sociétés, IS) for 2026: who is exempt, which charges are deductible, the minimum tax (impôt minimum forfaitaire, IMF) rates in force from 21 August 2026, the 2% withholding on insurance intermediaries, registration duties and fines, and the IRCM exemptions that touch companies. Built only from the two 2026 finance ordinances actually read (Ordonnance 2025-44 and its first rectification, Ordonnance 2026-45). The IS headline rate, the IMF base and floor, the annual return date, advance-payment rates and dividend, interest and non-resident withholding rates sit on visible holds because the consolidated 2026 Code was not readable. Use it to screen deductions and pick the right IMF category, not to compute a final IS liability. Two executable cases. Not yet approved by an accountant."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/ne-corporate-income-tax"
  jurisdiction: "NE"
  tax_year: "2026"
  last_updated: "2026-11-17"
---

# Niger corporate income tax v0.2

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

**Tax year 2026.** Two dates matter inside 2026. The 2026 finance ordinance (Ordonnance 2025-44 of 31 December 2025) amends the Code Général des Impôts (CGI) "A compter du 1er janvier 2026". Its first rectification (Ordonnance 2026-45, signed 21 August 2026) amends further articles "A compter de la signature". A rule below says which of the two it comes from.

## Who this applies to

Companies and other bodies liable to **impôt sur les sociétés (IS)** under Book I, Title I, Chapter 1 of the CGI. The headline IS rate and the general scope article were not in the texts read, so this Guide does not state them (see the hold under `## Sources`). Individuals in business pay the separate impôt sur les bénéfices d'affaires (IBA), which this Guide does not cover.

**Exempt from IS from 1 January 2026** (CGI art. 6 as replaced by Ordonnance 2025-44 art. 11): consumer cooperatives that only group members' orders and distribute the goods ordered; low-cost housing offices and companies; ciné-clubs and cultural centres; public awqaf and awqaf recognised as of public utility and entered in the Haute Autorité du Waqf register, within their object; mutual or cooperative savings and credit institutions; non-profit public establishments of the State or local authorities; local authorities, their syndicates and their non-profit public-service boards; chambers of commerce, industry, crafts, agriculture and trades when they do not carry on commercial activities.

**Non-profit associations from 21 August 2026** (CGI art. 7 as replaced by Ordonnance 2026-45 art. 2): a lawfully constituted non-profit association or body is exempt only while its management is **disinterested** (gestion désintéressée). It becomes liable to IS if its management is not disinterested. Management is disinterested when it is run on a voluntary basis by people with no direct or indirect interest in the results. Paying its officers does not break this if the statutes and practice ensure financial transparency, regular and periodic election of officers, effective member control and pay proportionate to the officers' actual duties.

**Investment companies with fixed capital (SICAF), from 1 January 2026** (CGI art. 72, created by Ordonnance 2025-44 art. 11): only venture-capital and private-equity financial establishments and companies holding an authorisation qualify, and they must hold at all times at least 50% of the net value of their total portfolio in shares of unlisted companies. Failing that condition loses the tax advantages. The advantages themselves were not in the text read.

## Rates, bands and thresholds

| Item | Rule and conditions | Official source |
|---|---|---|
| IMF, industrial enterprises | 0.75% of turnover (chiffre d'affaires), from 21 August 2026 | [Ordonnance 2026-45 art. 3, CGI art. 62(a), scan page 3](https://finances.gouv.ne/index.php/actualites/publications-du-ministere/file/1351-ordonnance-n-2026-45-premiere-rectification-de-la-loi-de-finances-2026) |
| IMF, other activities | 1.75% of turnover, from 21 August 2026 | same |
| IMF on gross margin | 3% of gross margin (marge brute) for enterprises whose IMF is computed on gross margin, other than independent hydrocarbon marketers and promoters, from 21 August 2026 | same |
| IMF, independent hydrocarbon marketers and promoters | 8% of gross margin, from 21 August 2026 | same |
| IMF, approved gold traders (legal persons) | 35% of the gross margin on goods actually exported and declared, from 21 August 2026. The sentence that follows item (e) makes this IMF discharge all profit tax on the same products | same |
| Cash-paid charge not deductible | A charge of XOF 2,000,000 or more for a transaction not paid by bank (procédé bancaire) is not deductible, from 1 January 2026 | [Ordonnance 2025-44 art. 11, CGI art. 23(4), PDF page 5](https://finances.gouv.ne/index.php/lois-de-finances/file/1303-ordonnance-n-2025-44) |
| SICAF portfolio condition | At least 50% of net portfolio value in unlisted shares, at all times | [Ordonnance 2025-44 art. 11, CGI art. 72, PDF page 6](https://finances.gouv.ne/index.php/lois-de-finances/file/1303-ordonnance-n-2025-44) |
| Withholding on insurance intermediaries | 2% of the amount excluding tax paid by insurance companies to intermediaries; deductible from the intermediary's IS or IBA profit, from 21 August 2026 | [Ordonnance 2026-45 art. 5, CGI art. 112 ter, scan page 4](https://finances.gouv.ne/index.php/actualites/publications-du-ministere/file/1351-ordonnance-n-2026-45-premiere-rectification-de-la-loi-de-finances-2026) |
| Late or missing declaration of existence | Fine XOF 100,000; XOF 200,000 if not regularised within 30 days of a formal notice, from 1 January 2026 | [Ordonnance 2025-44 art. 20, CGI art. 818(1)(c), PDF pages 31 to 32](https://finances.gouv.ne/index.php/lois-de-finances/file/1303-ordonnance-n-2025-44) |
| Fraudulent use of the tax identification number | Fine XOF 1,500,000, without prejudice to criminal penalties | same |

The IMF rates in force from 1 January to 20 August 2026 were set by the CGI text that Ordonnance 2026-45 replaced, which was not read. Do not apply the 21 August rates to that earlier period without the original text.

## The base

**Accounting.** Every enterprise operated in Niger must keep its accounts there, in the working language. The OHADA Uniform Act on accounting law and financial reporting applies within its scope. Under CGI art. 799(5), enterprises outside that accounting system's scope must use the particular accounting system prescribed for their professional sector or specific legal status; the text expressly includes banks, financial establishments and insurance companies. A non-resident operating in Niger keeps separate accounts for its Niger activity; a permanent establishment keeping accounts in another language must supply a translation by a State service or an approved translator. [CGI art. 799 as replaced by Ordonnance 2025-44 art. 19, PDF page 29](https://finances.gouv.ne/index.php/lois-de-finances/file/1303-ordonnance-n-2025-44).

**Deductible charges from 1 January 2026** (CGI art. 23 as replaced by Ordonnance 2025-44 art. 11, PDF pages 4 to 5). A charge is deductible only if it meets **all** of these conditions:

1. incurred in the direct interest of the business or part of its normal management;
2. an actual charge supported by sufficient evidence;
3. reduces the enterprise's net assets;
4. included in the charges of the year in which it was incurred;
5. contributes to income that is not exempt from IS;
6. not excluded by a specific tax provision.

Then apply the three overrides in the same article:

- The supporting invoices must carry the mandatory particulars of CGI art. 802, subject to that article's exceptions (art. 802 itself was not read).
- Purchases of raw local foodstuffs from an unregistered supplier are deductible when backed by a receipt from that supplier, kept by the buyer. Only unprocessed foodstuffs in the list annexed to the UEMOA VAT harmonisation directive qualify, excluding the products in point 1 of that list.
- Not deductible: any charge of XOF 2,000,000 or more for a transaction not paid by bank, and amounts paid for services under a contract that was not registered as required by CGI art. 435 point 15.

**Taxes and penalties from 1 January 2026** (CGI art. 45 as replaced, PDF page 5). Taxes borne by the enterprise and assessed or paid during the year are deductible, **except** IS itself, the IMF and the tax on certain general expenses. Settlements, fines, confiscations, penalties, surcharges and collection costs for breaches of price, supply, distribution or tax rules are not deductible.

**Minimum tax (IMF).** The rates are in the table. The definition of turnover or gross margin, how the IMF compares with IS, any floor amount and the payment schedule are in CGI articles not amended by the texts read, so they are held.

**IRCM exemptions that touch companies, from 1 January 2026** (CGI arts. 178 and 180 as replaced, PDF pages 7 to 9): among others, gains on sales of securities by enterprises under the reinvestment condition of CGI art. 20; income from SICAF and SICAV investments; income distributed by UCITS and other collective schemes approved by the regional market authority (CREPMF); and, under art. 180(c), interest and other income on business current accounts, but only where both parties are industrial, commercial, craft, agricultural or mining operators, the entries relate exclusively to both parties' activity, and the recipient's current-account income is taxed to IS or IBA in Niger. Art. 180 also exempts, among others, interest on savings-bank books and decentralised financial system accounts, and loan income of banks and financial establishments not represented by negotiable securities (not where funded from their own funds). Art. 20 and the IRCM rates were not read.

## Deadlines and filing

| Obligation | Rule | Source |
|---|---|---|
| Declaration of existence | File with the competent tax office within 30 days of starting activity, giving full identity and supporting documents for shareholders, partners, founders and beneficial owners; notify any later change within 15 days | [CGI art. 774 as replaced by Ordonnance 2025-44 art. 19, PDF page 28](https://finances.gouv.ne/index.php/lois-de-finances/file/1303-ordonnance-n-2025-44) |
| Insurance intermediary withholding | The insurer withholds on payment and pays it over without prior notice by the 15th of the following month to the competent tax receiver, on the administration's form | [CGI art. 112 quater, Ordonnance 2026-45 art. 5, scan page 5](https://finances.gouv.ne/index.php/actualites/publications-du-ministere/file/1351-ordonnance-n-2026-45-premiere-rectification-de-la-loi-de-finances-2026) |
| Annual IS return and balance | Held: the date, form and portal were not in the texts read | none read |

**Advance payments (précompte IS/IBA).** From 1 January 2026 the précompte is computed on customs value plus duties, excise and VAT (excluding the précompte itself) for imports, and on the total transaction amount including tax for domestic operations, except independent hydrocarbon marketers and promoters, who are charged on the gross margin fixed by the authorities [CGI art. 92 as replaced, PDF page 7](https://finances.gouv.ne/index.php/lois-de-finances/file/1303-ordonnance-n-2025-44). It is not charged on gifts in kind to the State and public bodies, personal imports by individuals, imports for diplomatic missions, international organisations, NGOs, development associations, qualifying awqaf and other exempt persons, samples, sales of phone top-ups to distributors and payment of public-body invoices [CGI art. 90 as replaced, PDF page 6](https://finances.gouv.ne/index.php/lois-de-finances/file/1303-ordonnance-n-2025-44). From 21 August 2026 art. 90 adds purchases and imports under public contracts for strategic military and security equipment for the defence forces (on application to the Minister), domestic purchases and sales of raw gold, exports of raw gold and imports of raw gold for re-export [Ordonnance 2026-45 art. 4, scan pages 3 to 4](https://finances.gouv.ne/index.php/actualites/publications-du-ministere/file/1351-ordonnance-n-2026-45-premiere-rectification-de-la-loi-de-finances-2026). The précompte rates and how it is credited against IS were not read.

## Penalties and interest

The registration fines are in the rates table (CGI art. 818). Late-filing, late-payment and under-declaration penalties and interest for IS were not in the texts read and are held. Do not quote a figure from memory.

## Cross-border points

- Treaties: the assessment, collection and control rules of the CGI apply subject to international conventions duly ratified by Niger [CGI preamble art. 1(2), Ordonnance 2025-44 art. 10, PDF page 3](https://finances.gouv.ne/index.php/lois-de-finances/file/1303-ordonnance-n-2025-44). No treaty was read.
- A non-resident operating in Niger keeps separate Niger accounts (art. 799 above).
- Bond income received by residents outside the UEMOA is exempt from IRCM from 1 January 2026 [CGI art. 178(a), PDF page 7](https://finances.gouv.ne/index.php/lois-de-finances/file/1303-ordonnance-n-2025-44).
- Withholding rates on dividends, interest, royalties and services paid to non-residents were not read and are held.

## Two worked examples that recompute

**1. Deduction screen with the XOF 2,000,000 boundary.** A company's 2026 accounting profit is XOF 10,000,000. The charges include: a supplier paid XOF 2,000,000 in cash; another supplier paid XOF 1,999,999 in cash; a tax penalty of XOF 300,000; and business licence tax (another tax, deductible) of XOF 400,000. All other conditions of art. 23 are met. The XOF 2,000,000 charge is "supérieur ou égal" to the limit and is added back; the XOF 1,999,999 charge stays deducted. The penalty is added back under art. 45(2); the other tax stays deducted under art. 45(1). The profit adjusted for these items is XOF 12,300,000. This Guide stops there: the IS rate is held.

```oa-check
name: Niger 2026 add-backs, cash charge at exactly XOF 2,000,000 and tax penalty
inputs:
  accounting_profit: 10000000
  cash_charge_at_limit: 2000000
  cash_charge_below_limit: 1999999
  tax_penalty: 300000
  other_deductible_tax: 400000
  limit: 2000000
steps:
  at_or_above_limit: cash_charge_at_limit - limit
  addback_at_limit: cash_charge_at_limit
  addback_below_limit: 0
  deducted_below_limit: cash_charge_below_limit
  addback_penalty: tax_penalty
  adjusted_profit: accounting_profit + addback_at_limit + addback_below_limit + addback_penalty
expected:
  at_or_above_limit: 0
  addback_at_limit: 2000000
  addback_below_limit: 0
  deducted_below_limit: 1999999
  adjusted_profit: 12300000
```

**2. Which IMF category: industrial or other activity.** A company's 2026 turnover after 21 August is XOF 400,000,000 (taken as the IMF base, whose definition is held). If it qualifies as an industrial enterprise, the IMF is 0.75%, XOF 3,000,000. If it is classed under other activities, the IMF is 1.75%, XOF 7,000,000. The classification decides XOF 4,000,000. Establish the industrial classification with evidence before using 0.75%. How the IMF compares with IS, any floor, and the treatment of turnover before 21 August are held.

```oa-check
name: Niger IMF from 21 August 2026, industrial versus other activities
inputs:
  turnover: 400000000
  rate_industrial: 0.0075
  rate_other: 0.0175
steps:
  imf_industrial: turnover * rate_industrial
  imf_other: turnover * rate_other
  difference: imf_other - imf_industrial
expected:
  imf_industrial: 3000000
  imf_other: 7000000
  difference: 4000000
```

## Ask the client first

- What is the entity (company, cooperative, association, SICAF, public body) and, for an association, is its management disinterested under the art. 7 tests?
- Is the business industrial, a gross-margin business, an independent hydrocarbon marketer or an approved gold trader?
- Which charges of XOF 2,000,000 or more were paid other than by bank, and were service contracts registered?
- Do the purchase invoices carry the mandatory particulars, and are there unregistered-supplier food purchases with receipts?
- Which part of the year's turnover falls before and after 21 August 2026?
- Is the company paid as an insurance intermediary, or paying non-residents?

## Sources

| Official source | What was read | Read on |
|---|---|---|
| [Ministry of Finance, Ordonnance 2025-44 of 31 December 2025, 2026 finance ordinance](https://finances.gouv.ne/index.php/lois-de-finances/file/1303-ordonnance-n-2025-44) | PDF downloaded through the page's public download form (SHA-256 a841c4fa...2f42e) and read: arts. 10 and 11 (CGI preamble art. 1, arts. 6, 23, 45, 72, 90, 92, 178, 180), PDF pages 3 to 9; arts. 19 and 20 (CGI arts. 774, 799, 801, 818), pages 28 to 32; arts. 43 and 44 and signature, page 47 | 2026-11-17 |
| [Ministry of Finance, Ordonnance 2026-45 of 21 August 2026, first rectification](https://finances.gouv.ne/index.php/actualites/publications-du-ministere/file/1351-ordonnance-n-2026-45-premiere-rectification-de-la-loi-de-finances-2026) | Scanned PDF downloaded through the public download form (SHA-256 5e8a3a25...8fae); scan pages 2 to 5 (arts. 1 to 6, including CGI arts. 7, 62, 90, 112 bis to quater) and page 48 (art. 25, signature 21 August 2026) read as page images | 2026-11-17 |

Not yet confirmed: the IS headline rate (the old Guide's 30%, from an unread CGI 2025 link, is not used); the general IS scope and territoriality article; the IMF base definitions, the comparison of IMF with IS, any IMF floor amount (the old Guide's "approximately 1% of turnover with a floor" is replaced by the 21 August 2026 rates above) and the IMF rates for 1 January to 20 August 2026; the annual return date (the old Guide's 30 April) and form; précompte rates and crediting (the old Guide's "instalments with a final balancing payment"); IRVM/IRCM rates on dividends (old Guide 10%) and interest (old Guide 13% to 25%); withholding on royalties and services paid to non-residents (old Guide about 16%); taxation of business capital gains (old Guide 20%) and the art. 20 reinvestment condition; the SICAF tax advantages; art. 802 invoice particulars; IS late-filing and late-payment penalties and interest; treaties. The consolidated CGI text in force for 2026 was not readable: the tax administration host impots.gouv.ne serves an expired certificate and the warning was not bypassed. Not yet approved by an accountant.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-17. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `ne-corporate-income-tax` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/ne-corporate-income-tax. If neither is available, confirm every figure against the official source pages cited above before relying on it.
