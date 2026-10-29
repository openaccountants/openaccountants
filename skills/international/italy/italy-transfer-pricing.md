---
name: italy-transfer-pricing
description: Use this skill whenever asked about Italy transfer pricing rules, documentation requirements, or prezzi di trasferimento compliance. Trigger on phrases like "transfer pricing Italy", "Italian TP documentation", "prezzi di trasferimento", "master file Italy", "local file Italy", "penalty protection Italy", "CbCR Italy", "APA Italy", "Agenzia delle Entrate TP", or any question about intercompany pricing for Italian entities.
version: 1.1
jurisdiction: IT
tax_year: 2026
last_updated: 2026-10-29
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
drafted_by: OpenAccountants
approved_by: pending
depends_on:
  - transfer-pricing-workflow-base
category: transfer-pricing
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Transfer pricing in Italy (prezzi di trasferimento) v1.1

Tax year **2026**. This Guide covers cross-border related-company pricing, optional documentation and penalty protection, country-by-country reporting (CbCR), low-value services and advance pricing agreements (APAs). It produces working papers for a qualified Italian tax adviser. It has no accountant attestation.

## Who this applies to

Italian businesses transacting with non-resident companies that control them, are controlled by them or share a controlling company. Article 110(7) TUIR substitutes the conditions and prices independent parties would agree in comparable circumstances where this increases income. Downward adjustments require the conditions of article 31-quater DPR 600/1973. The documentation rules also address Italian permanent establishments and resident companies' foreign establishments; profit attribution and downward relief need specialist review. See [TUIR art. 110(7)](https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1986-12-22;917~art110!vig=2026-10-29) and [Provvedimento 23 November 2020, points 1 and 3](https://www.agenziaentrate.gov.it/portale/documents/20143/2794495/Provv_prot_0360494_del_23112020.pdf/87a55907-b275-a3b5-1bc7-a6e316b70fef).

The definition of participation includes **more than 50%** of capital, voting rights or profits, or dominant management influence through shareholding or contractual links. Do not infer independence from shareholding alone. Documentation is an optional burden to obtain penalty protection, not a filing obligation for every taxpayer ([DM 14 May 2018, art. 2](https://www.gazzettaufficiale.it/eli/id/2018/05/23/18A03544/sg); [Risposta 174/2024](https://www.agenziaentrate.gov.it/portale/documents/20143/6314639/Risposta+n.+174_2024.pdf/f2013dc1-acb4-2459-77e9-bac69cc74e74)).

Tax year 2026 is distinct from **Redditi SC 2026**, which reports 2025 income. The form references below identify the published form actually read; the 2027 edition must be checked before filing 2026 income. This Guide does not calculate Pillar Two, hybrid mismatches, treaty relief or specialist financial/IP/restructuring benchmarks.

## Rates, bands and thresholds

| Item | Amount or condition | Period | Official source |
| --- | --- | --- | --- |
| Related-enterprise participation test | More than 50% of capital, votes or profits, **or** dominant influence | 2026 | [DM 14 May 2018, art. 2(b)](https://www.gazzettaufficiale.it/eli/id/2018/05/23/18A03544/sg) |
| SME documentation definition | Turnover/revenue **not above EUR 50 million**; excludes entities controlling or controlled by a non-SME | 2026 | [Provvedimento points 1.1(a), 4.1](https://www.agenziaentrate.gov.it/portale/documents/20143/2794495/Provv_prot_0360494_del_23112020.pdf/87a55907-b275-a3b5-1bc7-a6e316b70fef) |
| SME comparability update relief | Two following tax periods, only with public-source analysis and no significant changes to point 2.1.2 factors | 2026 | [Point 4.1](https://www.agenziaentrate.gov.it/portale/documents/20143/2794495/Provv_prot_0360494_del_23112020.pdf/87a55907-b275-a3b5-1bc7-a6e316b70fef) |
| Low-value service simplified margin | **5%** of all relevant direct and indirect costs, only if eligible and specially documented | 2026 | [DM art. 7](https://www.gazzettaufficiale.it/eli/id/2018/05/23/18A03544/sg) |
| Non-marginal transaction/category | **More than 5%** of total absolute positive and negative TP income components | 2026 documentation | [Circolare 15/E, section 4.2, pp. 20–21](https://www.agenziaentrate.gov.it/portale/documents/20143/3930122/Circolare+oneri+documentali+TP+26+11+21+h.+13.20+-+REV.pdf/5f23fab7-0853-68c6-cb5d-868fdfed9490) |
| CbCR prior-period consolidated revenue | **At least EUR 750 million**, or approximately equivalent local currency | 2026 reporting | [AdE CbCR guidance](https://www.agenziaentrate.gov.it/portale/web/guest/schede/comunicazioni/rendicontazione-dati-nazionali-paese-per-paese/scheda-informativa-rendicontazione-dati-nazionali) |
| Bilateral/multilateral APA application fee | Group turnover **below EUR 100m: EUR 10,000; EUR 100m through EUR 750m: EUR 30,000; above EUR 750m: EUR 50,000** | 2026 requests | [DPR 600/1973 art. 31-ter(3-bis)](https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1973-09-29;600~art31ter!vig=2026-10-29) |
| Renewal of bilateral/multilateral APA | Half the applicable application fee | 2026 requests | [Art. 31-ter(3-ter)](https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1973-09-29;600~art31ter!vig=2026-10-29) |
| Ordinary unfaithful-return penalty, before special adjustments | **70%**, minimum **EUR 150** | Violations from 1 September 2024 under legislation applicable through 2026 | [D.Lgs. 471/1997 art. 1(2)](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:1997-12-18;471~art1!vig=2026-10-29); [D.Lgs. 87/2024 art. 5(1)](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2024-06-14;87~art5!vig=2026-10-29) |

## The base

### Arm's-length analysis and method selection

Accurately delineate the transaction using contracts and actual conduct. Identify contractual terms, functions/assets/risks, goods or services, economic circumstances and business strategies. Transactions are comparable if no material difference affects the indicator, or reliable adjustments remove or substantially reduce the effect ([DM arts. 2–3](https://www.gazzettaufficiale.it/eli/id/2018/05/23/18A03544/sg)).

**Accepted Methods**

| Method | Accepted |
| --- | --- |
| Comparable Uncontrolled Price (CUP) | Yes |
| Resale Price Method (RPM) | Yes |
| Cost Plus Method (CPM) | Yes |
| Transactional Net Margin Method (TNMM) | Yes |
| Profit Split Method (PSM) | Yes |

Choose the most appropriate method for the case, considering its strengths and weaknesses, suitability, available reliable information and comparability. **At equal reliability**, prefer a traditional transaction method (CUP, resale price or cost plus) over TNMM or profit split; prefer **CUP over any other method** at equal reliability. One method is sufficient. Another method requires proof that none of the five works reliably and that the alternative gives an independent-party result. A compliant taxpayer-selected method is also the basis of the authority's verification ([DM art. 4(1)–(6)](https://www.gazzettaufficiale.it/eli/id/2018/05/23/18A03544/sg)).

Apply the analysis transaction by transaction; aggregate closely linked/unitary transactions when they cannot reliably be evaluated separately (DM art. 5). A comparable arm's-length range is acceptable; an indicator outside the range can be adjusted into it, subject to the taxpayer's contrary evidence and the authority's reasoned evaluation (DM art. 6).

### Low-value intra-group services

The optional simplification prices eligible services at the total relevant direct and indirect costs plus **5%**. All four conditions must hold: support services, outside the group's core activities, no use/creation of unique valuable intangibles, and no assumption/control/creation of significant provider risk. **Services the multinational group also supplies to independent customers are excluded**, even if the other conditions hold ([DM art. 7(1)–(3)](https://www.gazzettaufficiale.it/eli/id/2018/05/23/18A03544/sg)).

Keep the specific point-7 documentation: services and beneficiaries, why the services qualify, benefits and allocation keys with reasons, written agreements, detailed direct/indirect cost and margin calculations, and calculations applying allocation keys. The ordinary handover deadlines apply ([Provvedimento points 7.1–7.5](https://www.agenziaentrate.gov.it/portale/documents/20143/2794495/Provv_prot_0360494_del_23112020.pdf/87a55907-b275-a3b5-1bc7-a6e316b70fef)).

Documentation can cover only selected transactions; protection then covers only the adequately described transactions. An omitted marginal transaction receives no protection on adjustment, although that omission alone does not invalidate the rest of the documentation. The **more-than-5%** marginality test is a documentation threshold, not a pricing exemption or the low-value service margin ([Point 5.3.7](https://www.agenziaentrate.gov.it/portale/documents/20143/2794495/Provv_prot_0360494_del_23112020.pdf/87a55907-b275-a3b5-1bc7-a6e316b70fef); [Circolare 15/E, pp. 20–21](https://www.agenziaentrate.gov.it/portale/documents/20143/3930122/Circolare+oneri+documentali+TP+26+11+21+h.+13.20+-+REV.pdf/5f23fab7-0853-68c6-cb5d-868fdfed9490)).

## Deadlines and filing

The provvedimento of 23 November 2020 sets the content of the two documents. It says the Masterfile and the Documentazione Nazionale must be written in Italian, but the Masterfile may be presented in English (point 5.1.1). Both must be signed by the legal representative, or a delegate, with an electronic signature and time stamp applied by the date the income tax return is filed (point 5.1.2). The whole set is kept in electronic form. Source: https://www.agenziaentrate.gov.it/portale/documents/20143/2794495/Provv_prot_0360494_del_23112020.pdf/87a55907-b275-a3b5-1bc7-a6e316b70fef

### Master File (Documentazione di Gruppo)

**Master File (Documentazione di Gruppo)**

| Item | Detail |
| --- | --- |
| Required? | Optional, but needed for the penalty protection regime |
| Format | Prescribed Masterfile structure in Provvedimento point 2.2 |
| Language | Italian or English (point 5.1.1) |
| Deadline | Electronic signature with time stamp by the date the tax return is filed (point 5.1.2). For a return filed within ninety days of the deadline, see Claiming penalty protection below |

### Local File (Documentazione Nazionale)

**Local File (Documentazione Nazionale)**

| Item | Detail |
| --- | --- |
| Required? | Optional, but needed for the penalty protection regime |
| Format | Prescribed Documentazione Nazionale structure in Provvedimento point 2.3 |
| Language | Italian only. Risposta 174/2024 refused a request to present it in English. Circolare 15/E (point 8.1) allows annexes in another language, with an Italian/English translation on request if not already in either language |
| Deadline | Electronic signature with time stamp by the date the tax return is filed |
| Submission on request | Within 20 days of the request; additional information within 7 working days, or a longer period for complex transactions (Provvedimento points 5.2.1–5.2.2; Circolare 15/E section 8.2 clarifies working days) |
| Small and medium companies | A company with turnover (volume d'affari or ricavi) not above fifty million euro ("cinquanta milioni di euro"), and not controlling or controlled by a larger company, may skip updating the comparability data (points 2.1.1 to 2.1.5 of the Documentazione Nazionale) for the two following tax years, if the comparability analysis uses public sources and the items in point 2.1.2 do not change significantly (points 1.1(a) and 4.1) |

Sources for 2.1 and 2.2: the provvedimento linked above; Risposta 174/2024: https://www.agenziaentrate.gov.it/portale/documents/20143/6314639/Risposta+n.+174_2024.pdf/f2013dc1-acb4-2459-77e9-bac69cc74e74

### Claiming penalty protection

Art. 1(6) D.Lgs. 471/1997 says the penalty for an unfaithful return does not apply to a transfer pricing adjustment if, during the audit, the company hands over the documentation set out in the provvedimento. A company that holds the documentation must tell the Agenzia; without that notice the penalty applies. Source: https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:1997-12-18;471~art1!vig=2026-10-29

To benefit from penalty protection, ALL conditions must be met:

1. Masterfile and Documentazione Nazionale prepared as the provvedimento of 23 November 2020 requires, complete and truthful (points 5.3.2 and 5.3.3).
2. Electronic signature with time stamp by the date the tax return is filed. The statutory return deadline is the last day of the tenth month after period end, subject to applicable non-working-day extensions (DPR 322/1998 art. 2(2), (9)). Circolare 15/E says that for a return filed within ninety days of the deadline (late, or supplementary or replacing), the signature and time stamp must be applied by the date that return is actually filed.
3. The documentation-possession notice given in the annual return. In the published Redditi SC 2026 form (2025 income), this is the "Possesso documentazione" box in row RS106; check its successor in the return for 2026 income. That tick is the notice the law requires. After the ninety days, Circolare 15/E allows a late notice through remissione in bonis only if the taxpayer has the substantive eligibility requirements; the documentation was complete, signed and time stamped within ninety days of the ordinary deadline; the breach has not already been established; and no access, inspection, audit or other administrative assessment activity of which the taxpayer has formal knowledge has begun. The notice must be given in a supplementary return by the deadline for the next year's return, with simultaneous payment of the minimum penalty in art. 11(1) D.Lgs. 471/1997. Apply Circolare 15/E section 9's conditions in full; ordinary information/document requests in cooperative compliance are not the disqualifying assessment activity described there.
4. The documentation handed over during the audit, within 20 days of the request.

Incomplete/untruthful content, signature defects, a missing notice not cured under the stated rules, or missed handover deadlines put protection at risk. Partial omissions or inaccuracies that do not compromise the authority's analysis do not alone invalidate the documentation (Provvedimento points 5.3.2–5.3.4). Circolare 15/E: https://www.agenziaentrate.gov.it/portale/documents/20143/3930122/Circolare+oneri+documentali+TP+26+11+21+h.+13.20+-+REV.pdf/5f23fab7-0853-68c6-cb5d-868fdfed9490

The documentation is annual, effective for its tax period, retained until the assessment limitation expires, and kept electronically (Provvedimento points 5.1.3, 5.3.1). It is kept for request rather than submitted routinely with the return. The initial handover deadline is **20 days**; supplementary ordinary Masterfile/Local File information is due within **seven working days**, with a longer period for complex cases compatible with the audit timetable ([Circolare 15/E, section 8.2, pp. 35–36](https://www.agenziaentrate.gov.it/portale/documents/20143/3930122/Circolare+oneri+documentali+TP+26+11+21+h.+13.20+-+REV.pdf/5f23fab7-0853-68c6-cb5d-868fdfed9490)).

### Return fields and CbCR

In **Redditi SC 2026, section 17.17**, RS106 identifies A (controlled by a foreign company), B (controls a foreign company) or C (common control); the documentation-possession box supplies the notice; columns 5 and 6 report cumulative positive and negative TP income components. These are **2025-income form coordinates**, not confirmed 2027 coordinates ([AdE Redditi SC 2026 instructions](https://www.agenziaentrate.gov.it/portale/documents/20143/9764103/SC_istr_2026.pdf/51e462b7-2907-b093-4028-198631cbabdd?t=1772181405366)).

File CbCR **electronically with the Agenzia delle Entrate**, as a separate annual report within **12 months** of the reporting period's last day. The Agency's [CbCR electronic-file/control guidance](https://www.agenziaentrate.gov.it/portale/schede/comunicazioni/rendicontazione-dati-nazionali-paese-per-paese/swcontrollo-cbcr-dati-nazionali) identifies the telematic document route; this Guide does not prescribe an unsupported alternative channel. The resident ultimate parent files when the previous-period consolidated-revenue threshold is met. If the ultimate parent is foreign, an Italian constituent/designated entity files only in the situations and with the surrogate/EU-filer exemptions described by the authority. Verify the responsible filer rather than requiring every Italian group member to file ([AdE CbCR guidance, updated 6 May 2026](https://www.agenziaentrate.gov.it/portale/web/guest/schede/comunicazioni/rendicontazione-dati-nazionali-paese-per-paese/scheda-informativa-rendicontazione-dati-nazionali)).

## Penalties and interest

Without valid protection, a TP adjustment falls under the ordinary unfaithful-return penalty: **70%** of additional tax or excess credit used, minimum **EUR 150**, for violations from **1 September 2024** under the legislation applicable through 2026. This is the ordinary starting rule, not a computation of fraud aggravations, statutory reductions, voluntary corrections or settlements ([D.Lgs. 471/1997 art. 1(2)–(6)](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:1997-12-18;471~art1!vig=2026-10-29); [D.Lgs. 87/2024 art. 5(1)](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2024-06-14;87~art5!vig=2026-10-29)).

With suitable documentation delivered and the required notice, article 1(6) removes the article 1(2) penalty on the covered adjustment. It does not remove the tax or create an interest exemption. There is no standalone failure-to-create-documentation penalty in that paragraph: documentation is optional, but an adjustment without protection faces the ordinary rule. A missing notice can be cured only under the conditions above; do not promise protection from a tick-box alone.

**Timing boundary:** D.Lgs. 173/2024, annex article 102, applies its consolidated penalty code from **1 January 2027**. A return for 2026 income is filed in 2027. Check the applicable successor provision and violation date before applying the old article citation to that filing. Historical Circolare 15/E describes the former **90%–180%** range; it is not the current starting rate. No current interest rate or CbCR penalty is supplied here ([D.Lgs. 173/2024, annex art. 102](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2024-11-05;173:1~art102!vig=2026-10-29)).

## Cross-border points

### Advance pricing agreements

**Advance Pricing Agreements (APA)**

| Item | Detail | Note |
| --- | --- | --- |
| Source | all figures below | https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1973-09-29;600~art31ter!vig=2026-10-29 |
| Availability | Yes, for companies with international activity | Art. 31-ter(1): transfer pricing methods, permanent establishments, dividends, interest and royalties |
| Types | Unilateral (comma 2); bilateral or multilateral, after a mutual agreement with foreign authorities (comma 3) | |
| Governing legislation | Article 31-ter D.P.R. 600/1973 | Not art. 31-bis, which covers exchange of information |
| Application | To the competent office of the Agenzia, as set by a Director's provvedimento (comma 6) | |
| Duration, unilateral | The tax period in which it is signed and the four following periods | "per i quattro periodi d'imposta successivi" |
| Rollback, unilateral | To earlier open years with the same facts **and law**, if no formally known audit activity has started | Through ravvedimento or a supplementary return, without penalties |
| Duration, bilateral | As agreed with foreign authorities; ordinary effect can reach the request year. Earlier open years require the same facts and law, a request in the application, foreign-authority consent and no formally known audit activity (comma 3) | |
| Fee, bilateral or multilateral, group turnover below EUR 100 million | EUR 10,000 | "10.000 euro nel caso in cui il fatturato complessivo del gruppo" |
| Fee, group turnover from EUR 100 million to EUR 750 million | EUR 30,000 | "30.000 euro nel caso in cui il fatturato complessivo" |
| Fee, group turnover above EUR 750 million | EUR 50,000 | "50.000 euro nel caso in cui il fatturato complessivo" |
| Fee on renewal | Halved (comma 3-ter) | "le commissioni sono ridotte alla metà" |
| Fee, unilateral | The quoted statutory fee schedule concerns bilateral/multilateral requests | Do not apply that schedule to unilateral requests |

An APA is governed by **article 31-ter**, not article 31-bis (exchange of information). During its validity, audit powers address matters outside the agreement; material changes to facts or law affect its continued operation (paragraphs 2 and 5). The competent office, checking procedures and changed-circumstance monitoring are governed by the director's implementation provision (paragraph 6). An APA/MAP, downward relief under article 31-quater, PE attribution, exit tax and specialist financing/IP/restructuring analysis require a tax adviser.

Reconcile TP support to the books and the corporate return. Related bookkeeping and financial-statement work is in `italy-bookkeeping` and `italy-financial-statements`; IRES and IRAP computations are in `it-ires-corporate-tax` and `it-irap`. This Guide does not derive VAT/customs adjustments from an income-tax adjustment; review those separately with `italy-vat-return`. CbCR supplies tax authorities with information for cross-border risk assessment (AdE CbCR guidance).

## Two worked examples that recompute

### Example 1: qualifying low-value service

Assume an eligible support service meets **all** DM article 7 conditions, is not also provided by the group to independent customers, and has the required point-7 documentation. Relevant direct costs are **EUR 50,000** and indirect costs **EUR 20,000**. The base is EUR 70,000; the 5% margin is EUR 3,500; the service value is **EUR 73,500**. The costs are example inputs, not statutory allowances. This is not a general 5% margin for all group services.

```oa-check
name: Italy qualifying low-value service, 2026
inputs:
  direct_cost: 50000
  indirect_cost: 20000
steps:
  cost_base: direct_cost + indirect_cost
  margin: cost_base * 0.05
  service_value: cost_base + margin
expected:
  cost_base: 70000
  margin: 3500
  service_value: 73500
```

### Example 2: APA fee boundary at EUR 100 million

Assume a **bilateral** APA application under article 31-ter(3), with group turnover exactly **EUR 100 million**. The application fee is **EUR 30,000**, and a renewal fee is half, **EUR 15,000**. A group below that turnover boundary would instead pay EUR 10,000 and EUR 5,000. This example tests the included lower boundary of the middle band; the fee is not calculated as a percentage of turnover.

```oa-check
name: Italy bilateral APA fee at included EUR 100 million boundary
inputs:
  middle_band_application_fee: 30000
  below_band_application_fee: 10000
steps:
  middle_band_renewal_fee: middle_band_application_fee / 2
  below_band_renewal_fee: below_band_application_fee / 2
expected:
  middle_band_renewal_fee: 15000
  below_band_renewal_fee: 5000
```

## Ask the client first

- Which foreign companies do you trade with, and what is the control link (you control them, they control you, or a common parent)?
- Do you want penalty protection for this year, and is the return already filed? If filed, was it within the last ninety days?
- Is the Masterfile only in English, and is the Documentazione Nazionale in Italian?
- What is your turnover, and does a company that controls you, or that you control, exceed fifty million euro? This decides the small-company relief.
- Do you provide or receive support services (IT, HR, accounting) that meet all low-value conditions, and does the group also supply those services to independent customers?
- What is the group's prior-period consolidated revenue for CbCR, and its total turnover for the APA fee schedule?

Refer an ongoing audit or adjustment notice to a tax adviser/litigator. APA/MAP applications, downward adjustments, PE attribution, exit taxes, financial transactions, IP transfers, business restructurings, Pillar Two and hybrid-mismatch documentation are outside this computation. Check successor provisions for filings or requests in 2027 and later.

## Sources

| Source and provision | Official URL | Read on |
| --- | --- | --- |
| DPR 917/1986, TUIR art. 110(7) | https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1986-12-22;917~art110!vig=2026-10-29 | 2026-10-29 |
| DM 14 May 2018, arts. 1–9 | https://www.gazzettaufficiale.it/eli/id/2018/05/23/18A03544/sg | 2026-10-29 |
| AdE Provvedimento 360494/2020, points 1–8 | https://www.agenziaentrate.gov.it/portale/documents/20143/2794495/Provv_prot_0360494_del_23112020.pdf/87a55907-b275-a3b5-1bc7-a6e316b70fef | 2026-10-29 |
| AdE Circolare 15/E, 26 November 2021, sections 4, 6, 8–10 | https://www.agenziaentrate.gov.it/portale/documents/20143/3930122/Circolare+oneri+documentali+TP+26+11+21+h.+13.20+-+REV.pdf/5f23fab7-0853-68c6-cb5d-868fdfed9490 | 2026-10-29 |
| AdE Risposta 174/2024, documentation language/optional burden | https://www.agenziaentrate.gov.it/portale/documents/20143/6314639/Risposta+n.+174_2024.pdf/f2013dc1-acb4-2459-77e9-bac69cc74e74 | 2026-10-29 |
| AdE CbCR guidance, 6 May 2026 update | https://www.agenziaentrate.gov.it/portale/web/guest/schede/comunicazioni/rendicontazione-dati-nazionali-paese-per-paese/scheda-informativa-rendicontazione-dati-nazionali | 2026-10-29 |
| DPR 600/1973 art. 31-ter | https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1973-09-29;600~art31ter!vig=2026-10-29 | 2026-10-29 |
| DPR 322/1998 art. 2 | https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1998-07-22;322~art2!vig=2026-10-29 | 2026-10-29 |
| D.Lgs. 471/1997 art. 1 | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:1997-12-18;471~art1!vig=2026-10-29 | 2026-10-29 |
| D.Lgs. 87/2024 art. 5(1) | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2024-06-14;87~art5!vig=2026-10-29 | 2026-10-29 |
| D.Lgs. 173/2024, annex art. 102 | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2024-11-05;173:1~art102!vig=2026-10-29 | 2026-10-29 |
| AdE Redditi SC 2026 instructions, section 17.17 (2025 income) | https://www.agenziaentrate.gov.it/portale/documents/20143/9764103/SC_istr_2026.pdf/51e462b7-2907-b093-4028-198631cbabdd?t=1772181405366 | 2026-10-29 |
| AdE CbCR electronic-file/control guidance | https://www.agenziaentrate.gov.it/portale/schede/comunicazioni/rendicontazione-dati-nazionali-paese-per-paese/swcontrollo-cbcr-dati-nazionali | 2026-10-29 |

**Not yet confirmed:** the return coordinates and successor statutory cross-references for 2026 income filed in 2027; the precise violation-date treatment for that filing; current tax-interest rates; CbCR penalties; a general or interest-rate safe harbour (the legacy claims of absence are not asserted); APA processing time (the old 12–24-month estimate is unverified), unilateral application fees beyond the quoted statutory schedule, and annual APA compliance-report requirements under the implementation provision; TP-specific VAT/customs valuation effects and financial-statement related-party disclosure rules; operational Pillar Two dates and hybrid-mismatch requirements; detailed downward-adjustment/MAP/PE/exit-tax procedures; successor TUIR article numbers and 2027 application. These topics are retained as explicit boundaries, not computation rules. No old executable example was removed: the prior Guide had none.

## Disclaimer

This Guide and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this Guide. All outputs must be reviewed and signed off by a qualified professional before filing or acting upon.

> Contributed by OpenAccountants.

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
