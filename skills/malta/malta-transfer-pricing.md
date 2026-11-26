---
name: malta-transfer-pricing
description: 'Use this skill whenever asked about Malta transfer pricing rules, documentation requirements, or arm''s length pricing for cross-border related-party transactions. Trigger on phrases like "transfer pricing Malta", "TP documentation", "master file Malta", "local file Malta", "arm''s length Malta", "related party transactions Malta", "CbCR Malta", "country-by-country report Malta", "BEPS Malta", "intercompany pricing Malta", or any question about transfer pricing compliance for Maltese entities within multinational groups. Covers basis year 2026, the Transfer Pricing Rules (S.L. 123.207) and the MTCA guidelines, the EUR 6,000,000 revenue and EUR 20,000,000 capital exceptions, grandfathering of pre-2024 arrangements, master file and local file on request, the TRA 135 company return attachment, unilateral rulings and APAs.'
version: 2.1
jurisdiction: MT
tax_year: 2026
last_updated: 2026-11-26
depends_on:
  - transfer-pricing-workflow-base
category: transfer-pricing
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: transfer-pricing
type: situation-rules
---

# Malta transfer pricing, 2026

## Scope and who this is for

Basis year 2026, year of assessment 2027. Apply the Transfer Pricing Rules, [S.L. 123.207](https://legislation.mt/eli/sl/123.207/eng/pdf), with the [MTCA guidelines](https://mtca.gov.mt/docs/default-source/documents/business-tax/international-affairs/international-direct-taxation/transfer-pricing/useful-links/guidelines---transfer-pricing-rules.pdf). Company tax computation is in **mt-corporate-tax**; a TP adjustment does not automatically settle VAT or financial-reporting treatment. Built from the law; not yet approved by an accountant.

## Ask the client first

- Legal entities, tax residence, permanent establishments, source of income/gains and which company’s total income is affected.
- Direct and indirect voting/ordinary-capital percentages, constitutional control powers and whether the entities are constituents of an MNE group as defined for CbCR.
- Full group structure and the data needed for the Annex I SME test, not only the Maltese company’s size.
- Arrangement dates, binding/execution dates, material changes in substance, rights, risks, pricing or duration, including changed conduct.
- Aggregate arm’s length revenue and capital income/expenditure items for the basis year; dividends paid, distributions in kind and any securitisation transaction.
- Existing master/local files, benchmark study, ruling/APA, material changes and any proposed foreign primary adjustment.

## The method, step by step

1. **Identify the company and associated enterprises.** Rule 2 excludes micro, small and medium-sized enterprises under Annex I of Regulation (EU) 651/2014. The ordinary relationship test includes direct/indirect participation of **more than 75%** in voting rights or ordinary capital, or control through powers in articles or another governing document, including common control. The percentage is **more than 50%** where the bodies are constituent entities of the CbCR-defined MNE group. Apply the definition at the relevant time: the earlier of the arrangement becoming binding or execution starting, subject to the rule’s guidance qualification.
2. **Apply every cross-border limb.** Rule 2 covers: (a) a non-resident party and a Malta-resident company whose total income is affected; (b) a party’s foreign PE effectively connected with the arrangement and a Malta-resident company whose total income is affected; or (c) a non-resident party and another non-resident company with a connected Malta PE **or otherwise Malta-source income or gains**, whose total income is affected. Do not decide this from the parties’ residence alone. Rule 10 separately applies to company/PE notional dealings; for PE attribution: Check this point with one of our partner accountants.
3. **Fix timing.** The Rules apply to basis years starting on or after **1 January 2024** for arrangements entered into then or materially altered then or later. An arrangement entered into before then and not materially altered comes within the Rules for basis years starting on or after **1 January 2027** (rule 1(2)). MTCA tests substance/functions/assets/risks and actual conduct, not merely document form. Minor administration, internal operational support, mere redomiciliation or a merger inheriting the same rights/obligations are not automatically material; consideration/method, risk-changing rights/obligations and duration changes can be. External change with parties still contractually bound by the old pricing is specifically qualified in the guidance. For a doubtful material change: Check this point with one of our partner accountants.
4. **Apply exceptions.** Rule 9(a) excludes an arrangement comprising a securitisation transaction under S.L. 123.128. Rule 9(b) excludes the period only when **both** aggregate arm’s length income/expenditure of a revenue nature do not exceed **EUR 6,000,000** and those of a capital nature do not exceed **EUR 20,000,000**. Equality qualifies; either excess defeats this threshold exception. Classify by nature, not simply P&L versus balance-sheet location. MTCA excludes dividends **paid** to an associate from the revenue aggregate; distributions in kind may need consideration. A written request does not itself opt in: the Commissioner must issue the determination under the proviso.
5. **Determine the arm’s length amount.** Under rules 3–5, substitute the amount independent parties would agree in comparable circumstances for the differing actual incurred/due or accrued/derived amount, including no-consideration transactions. The effect is confined to the parties’ total income under the Income Tax Acts; rule 7 addresses another party liable to Malta tax. For corresponding/downward adjustments in the actual case: Check this point with one of our partner accountants.
6. **Document on a timely basis.** Rule 6 expressly requires timely preparation and retention; MTCA requires the master and local file and can ask for further information within a reasonable timeframe. An absence of a fixed preparation date is not permission to wait until asked.
7. **File the applicable return information.** MTCA’s [7 May 2026 notice](https://mtca.gov.mt/news-results-page/2026/05/07/year-of-assessment-2026-tax-return-for-companies) introduced TRA 135 for **YA 2026**. For the applicable **YA 2027** attachment, its questions, portal fields and submission requirements: Check this point with one of our partner accountants. Assess CbCR separately; the revenue threshold alone does not mean every group company files a report.
8. **Seek certainty where needed.** Rule 11 permits a unilateral ruling; rule 12 permits bilateral or multilateral APAs. They can cover the specified earlier transactions under the statutory provisions below; neither route is confined absolutely to an arrangement that has not started.

### SME exclusion: a full Annex I test

[Regulation (EU) 651/2014 Annex I, arts. 1–6](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:02014R0651-20230701), read 26 November 2026. The SME ceiling is **fewer than 250 persons** and annual turnover **not exceeding EUR 50 million and/or** annual balance-sheet total **not exceeding EUR 43 million**. These are not standalone-company tests where partner or linked enterprises exist.

Use the latest approved period on an annual basis, turnover excluding VAT/other indirect taxes; changes generally require two consecutive accounting periods, while a new enterprise without approved accounts uses a bona fide estimate. Headcount is annual work units including owner-managers and regularly active partners, with part-year/part-time/seasonal fractions; qualifying vocational apprentices/students and maternity/parental leave duration are excluded. Add partner data proportionately using the greater capital/voting percentage and linked data at 100%, avoiding double counting. Apply the article 3 control, natural-person same/adjacent-market, public-body and investor exceptions and article 6 upstream/downstream rules. For a group structure, investor exception, ownership change or uncertain status: Check this point with one of our partner accountants. Do not conclude “SME” merely because the Malta subsidiary is small.

### Arm’s length standard and methods

MTCA’s rule 5 guidance prefers Chapter II of the **2022 OECD Transfer Pricing Guidelines** and permits other methods under paragraph 2.9: the price must satisfy arm’s length, a more appropriate OECD method must not be displaced, and the choice needs an explanation and documentation. The five method names are retained as a vocabulary, not a benchmark result: CUP, resale price and cost plus are traditional transaction methods; TNMM and transactional profit split are transactional profit methods ([OECD paragraphs 2.1–2.2](https://www.oecd.org/content/dam/oecd/en/publications/reports/2022/01/oecd-transfer-pricing-guidelines-for-multinational-enterprises-and-tax-administrations-2022_57104b3a/0e655865-en.pdf)). Select the most appropriate method for the circumstances, functional analysis, reliable information and comparability; no method suits every case. One method is generally appropriate; complex cases can use evidence from several under MTCA’s guidance. For actual benchmarking, comparables or profit splits: Check this point with one of our partner accountants.

**Low-value-adding intra-group services.** MTCA permits the charge to be determined under the OECD and EU Joint Transfer Pricing Forum guidance; a taxpayer opting for the simplified approach keeps Chapter VII information for request. For eligibility, the claimed 5% markup, cost pool, benefits and allocation keys: Check this point with one of our partner accountants. No automatic 5% price is supplied here. For any asserted interest or routine-service safe harbour, or Pillar One Amount B adoption: Check this point with one of our partner accountants.

**Notional interest deduction.** TP applies before NID. MTCA’s example determines that nominally interest-free debt should bear 3%; that debt then ceases to be NID risk capital. The example’s percentage is not a market-rate safe harbour. For mixed-debt characterisation and actual NID eligibility: Check this point with one of our partner accountants. Amounts brought forward from arrangements outside scope are not retrospectively restated merely because the arrangement later comes within these Rules; MTCA’s rule 3 guidance also addresses the expected continuation of an established arm’s length amount in subsequent/intervening out-of-scope periods, subject to relevant economic changes.

### Documentation requirements

| Document | Requirement and conditions | Source |
|---|---|---|
| Master file | In-scope arrangements: OECD Annex I to Chapter V; English or Maltese when requested; make available within a reasonable timeframe | MTCA guidelines, rule 6: https://mtca.gov.mt/docs/default-source/documents/business-tax/international-affairs/international-direct-taxation/transfer-pricing/useful-links/guidelines---transfer-pricing-rules.pdf |
| Local file | OECD Annex II to Chapter V; same request/language conditions | Same |
| Low-value service file | An opted simplified approach requires Chapter VII information, made available on request | Same |
| Period first exceeding Rule 9 limits | MTCA Example 4 requires documentation including the agreement from that year | Same |

TP documentation forms part of ITMA article 19(1) records. MTCA says the article 19(5) retention clock starts at the later of the end of the period the arrangement concerns or its date. Article 19(5) sets a nine-year minimum with named Companies Act exceptions; article 163(5) requires a company’s accounting records for ten years, with bound/unified records timed from the last entry. Apply the provisions to the actual record; do not merge all clocks into one universal rule. For the TP file’s classification or a multi-period retention question: Check this point with one of our partner accountants. [ITMA art. 19(5)](https://legislation.mt/eli/cap/372/eng/pdf); [Companies Act art. 163(5)](https://legislation.mt/eli/cap/386/eng/pdf).

## Rates, bands and thresholds

| Item | Figure and operative condition | Source |
|---|---|---|
| Scope starts | Basis years starting 1 January 2024 for new or materially altered arrangements | S.L. 123.207 rule 1: https://legislation.mt/eli/sl/123.207/eng/pdf |
| Older unaltered arrangements | Basis years starting 1 January 2027 | Same |
| Relationship participation | More than 75%; more than 50% for CbCR-defined MNE constituents; constitutional control is an alternative | Same, rule 2 |
| Rule 9(b) exception | Revenue nature ≤ EUR 6m **and** capital nature ≤ EUR 20m; apply all scope and exception conditions first | Same, rule 9 |
| Unilateral ruling fee | EUR 3,000 non-refundable; renewal EUR 1,000 non-refundable | Same, rule 11(7), (13) |
| Unilateral duration | Five years from effect, or shorter stated period; truth, notification and material-change conditions below | Same, rule 11(8)–(11) |
| Unilateral earlier transactions | Non-series arrangement: transactions in the year preceding the YA of request; otherwise preceding three basis years forming part of the arrangement | Same, rule 11(3), (8) |
| APA fees | EUR 5,000 non-refundable; renewal EUR 2,000 non-refundable | Same, rule 12(4), (10) |
| APA period | Up to five years from effect; on request also up to three basis years preceding the request | Same, rule 12(2), (5)–(6) |
| Renewal window | Written request during six months before expiry, no relevant material change; APA also needs other competent authorities’ agreement | Same, rules 11(13), 12(10) |
| Material-change notice | Unilateral: 30 days from later occurrence/awareness; APA: 30 days from occurrence or awareness under rule 12(7) | Same, rules 11(9), 12(7) |
| CbCR group exclusion boundary | Preceding-FY consolidated revenue below EUR 750m is an Excluded MNE Group; reporters/notifications need their separate statutory tests | S.L. 123.127 Annex III I(3)–(6): https://legislation.mt/eli/sl/123.127/eng/pdf |
| CbCR report deadline | For the Maltese reporting obligation under reg. 13(4)/Annex III: within twelve months of the MNE fiscal year’s last day | Same, reg. 13(6) |
| Company statutory return date | For article 11(2) ITA persons, ninth-month last day after the accounting date or 31 March of YA, whichever later; 31 Dec 2026 gives 30 Sept 2027, before any separately applicable extension | S.L. 372.16 rule 2(c)(i): https://legislation.mt/eli/sl/372.16/eng/pdf |

### Rulings, APAs and dispute resolution

A fee is not a promise of a ruling. A written request must identify the specific arrangement, relevant parties/beneficial owners, refer to the Rules and provide required information; all necessary information and applicable fees must be supplied. A ruling can be declined where existing law gives sufficient certainty, and withheld for outstanding return obligations (rule 11(2), (4), (6)). An APA applies the cross-referenced request conditions and the relevant MAP provision (rule 12(3)).

A unilateral ruling loses effect on the Commissioner’s material-change notification and is null where the required notice was not made or facts were misrepresented/withheld (rule 11(10)–(11)). For an APA, the competent authority obtains other authorities’ agreement before notifying loss of effect; nullity for omitted notice/misrepresentation also requires the foreign authorities’ agreement (rule 12(8)–(9)). These conditions qualify every duration quoted above. For modification, challenges/tribunal time limits, renewals or actual APA/MAP procedure: Check this point with one of our partner accountants.

A downward unilateral ruling without a foreign primary adjustment is considered only if arm’s length in principle and amount, otherwise double taxation would arise, and the ruling is spontaneously exchanged with the relevant foreign administration with the necessary facts and law (MTCA rule 11 guidance). For a taxpayer’s proposed downward adjustment: Check this point with one of our partner accountants. No blanket “MAP has no fee” or treaty-specific completion time is supplied.

## Worked cases
### Example 1 -- Does a company fall inside the Rules in 2026?

A Malta company that is not an SME (it is part of a large group) has cross-border arrangements with associated enterprises in its 2026 financial period, all entered into on or after 1 January 2024. No arrangement in this example qualifies for pre-2024 grandfathering. Revenue items (sales, services, interest, excluding dividends paid) total EUR 4,500,000 at arm's length. Capital items (loans and asset transfers) total EUR 25,000,000. Revenue stays under EUR 6,000,000, but capital goes over EUR 20,000,000. Rule 9 only takes a period out of scope when both stay within their limits, so the Rules apply for 2026. Assume the full Annex I SME test has established the given non-SME status and the securitisation exception does not apply. The company prepares the required documentation on a timely basis and makes the master and local files available on request. For the actual YA 2027 attachment and its contents: Check this point with one of our partner accountants; the source notice proves TRA 135 for YA 2026 only.

```oa-check
name: Rule 9 exception test, revenue EUR 4.5m and capital EUR 25m
inputs:
  revenue_items: 4500000
  capital_items: 25000000
  revenue_limit: 6000000
  capital_limit: 20000000
steps:
  - revenue_excess: max(0, revenue_items - revenue_limit)
  - capital_excess: max(0, capital_items - capital_limit)
  - total_excess: revenue_excess + capital_excess
expected:
  revenue_excess: 0
  capital_excess: 5000000
  total_excess: 5000000
```

A positive total_excess defeats the Rule 9(b) threshold exception in this example, after the other scope, timing and exception assumptions above have been satisfied. It does not alone establish that every company is in scope.

### Example 2 -- Interest-free loan to a foreign associate

A Malta company that is in scope lends EUR 2,000,000 interest-free to its parent abroad on 1 January 2026, a new arrangement after 1 January 2024, so no grandfathering applies. The benchmarking study sets an arm's length rate of 3% (the rate used in the MTCA guidelines' own example). The company adds the arm's length interest to its chargeable income for basis year 2026. The tax on it follows [mt-corporate-tax](mt-corporate-tax.md).

```oa-check
name: Interest-free loan priced at 3% for a full year
inputs:
  principal: 2000000
  rate_pct: 3
  months: 12
steps:
  - arm_length_interest: pct(principal, rate_pct) * months / 12
expected:
  arm_length_interest: 60000.00
```

## When to refuse or refer

- **TRA 135 and YA 2027:** Check this point with one of our partner accountants. The historical YA 2026 notice does not prove the future form’s contents.
- **CbCR:** For who files, surrogate/local-filing exceptions, Malta notifications, actual electronic submission and every trigger-specific penalty: Check this point with one of our partner accountants. The EUR 750m boundary is not itself a filing obligation for each constituent.
- **Benchmarking, comparables, profit splits, low-value services, PE attribution, SME structures, NID and downward adjustments:** Check this point with one of our partner accountants where the operative conditions cannot be settled from the evidence.
- **VAT and accounts:** TP adjustments apply only to Income Tax Acts under rule 8. Obtain the separate VAT-law or financial-reporting analysis; for IAS 24 disclosures: Check this point with one of our partner accountants.
- **Pillar Two deferral/information duties and Pillar One Amount B:** Check this point with one of our partner accountants; corporate minimum-tax analysis belongs in **mt-corporate-tax**.
- **Penalties and estimated assessments:** Check this point with one of our partner accountants. No unsupported generic penalty, exemption or estimated-assessment power is supplied.
- Outputs must be professionally reviewed before filing or acting.

## Filing and payment

Prepare and retain records on a timely basis; respond within the reasonable timeframe requested. Confirm the actual year’s corporate return/attachment and any CbCR filing/notification duties separately. The company statutory date above does not establish a future electronic extension or defer payment. For an actual filing, notification, payment or penalty computation not resolved here: Check this point with one of our partner accountants.

## Sources

| Source and actual read scope | URL | Read on |
|---|---|---|
| Read for S.L. 123.207 rules 1–12, provisions reflected here: scope, dates, amounts, documentary timing, exceptions, ruling/APA fees and validity/renewal conditions | https://legislation.mt/eli/sl/123.207/eng/pdf | 2026-11-26 |
| Read for MTCA guidelines all six pages, including material changes, methods, NID, record clocks and exceptions | https://mtca.gov.mt/docs/default-source/documents/business-tax/international-affairs/international-direct-taxation/transfer-pricing/useful-links/guidelines---transfer-pricing-rules.pdf | 2026-11-26 |
| Read for Annex I arts. 1–6: SME thresholds, aggregation, headcount and timing | https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:02014R0651-20230701 | 2026-11-26 |
| Read for OECD 2022 paragraphs 2.1–2.2, 2.9–2.10: method names and selection; detailed benchmarking is referred | https://www.oecd.org/content/dam/oecd/en/publications/reports/2022/01/oecd-transfer-pricing-guidelines-for-multinational-enterprises-and-tax-administrations-2022_57104b3a/0e655865-en.pdf | 2026-11-26 |
| Read for the YA 2026 notice naming TRA 135, not YA 2027 contents | https://mtca.gov.mt/news-results-page/2026/05/07/year-of-assessment-2026-tax-return-for-companies | 2026-11-26 |
| Read for S.L. 123.127 reg. 13(6), 48, Annex III I and II: CbCR boundary and report/notification distinctions; actual case filings/penalties referred | https://legislation.mt/eli/sl/123.127/eng/pdf | 2026-11-26 |
| Read for statutory return rule 2(c)(i) | https://legislation.mt/eli/sl/372.16/eng/pdf | 2026-11-26 |
| Read for ITMA art. 19(5), same-day completed financial-statements evidence reused unchanged | https://legislation.mt/eli/cap/372/eng/pdf | 2026-11-26 |
| Read for Companies Act art. 163(5), same-day completed financial-statements evidence reused unchanged | https://legislation.mt/eli/cap/386/eng/pdf | 2026-11-26 |

Not yet confirmed: none in usable guidance; the explicit referred topics above supply no operative conclusion.
