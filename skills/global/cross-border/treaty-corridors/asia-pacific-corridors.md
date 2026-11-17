---
name: asia-pacific-corridors
description: >
  Compare source-country withholding tax and permanent-establishment exposure for
  payments between Singapore, Australia, India, Japan, Hong Kong, New Zealand,
  the UAE, South Korea and Malaysia in the eleven corridors listed below.
  Use for 2026 cross-border dividends, interest, royalties, technical services,
  holding-company distributions and treaty-versus-domestic comparisons.
  Determine direction, residence, beneficial ownership, payment character,
  ownership history, anti-abuse eligibility and local relief procedure before
  computing. This is a treaty-selection method for ordinary payments, with
  explicit holds where current domestic computation is not established.
version: 1.1
jurisdiction: GLOBAL
tax_year: 2026
last_updated: 2026-11-17
category: cross-border
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: cross-border
type: cross-country-method
---

# Asia Pacific Corridors v1.1

> **General reference only.** This Guide has not been reviewed for any particular person's facts, documents, elections, deadlines, residence, filing status or local procedures. Obtain qualified professional review before filing, paying or taking a tax position.

## Quick reference

Coverage: 2026 payments in these eleven corridors. The pair name identifies both jurisdictions; an arrow below means **source/payer jurisdiction → recipient's treaty residence**. Treaty percentages are maximum source taxes on an eligible payment, not automatic withholding instructions. A domestic exemption or lower charge can give a lower result. Read the corridor conditions and the domestic comparison before computing.

| Corridor | Dividend selector | Interest selector | Royalty selector | Services selector and official text |
|---|---|---|---|---|

| Singapore–Australia | AU→SG: 15%; SG→AU: no additional dividend tax under Article 8(2) while its domestic condition holds | 10% | 10% only within the treaty definition | Enterprise business profits: Article 5, subject to PE and separate income articles; individuals differ. [Articles 2, 5, 8–12](https://www.iras.gov.sg/docs/default-source/dtas/singapore-australia-dta%28ratified%29%28mli%29%2819-jul-2021%29.pdf) |

| Singapore–India | 10% for company holding at least 25% of shares; otherwise 15%; SG-source Article 10(3) exemption | 10% bona fide bank/similar financial institution loan, including insurance; otherwise 15%; government exception below | 10% | 10% only for Article 12 FTS; other services need classification. [Articles 10–12, 22; 2005 Protocol Article 4](https://www.iras.gov.sg/media/docs/default-source/dtas/protocol-amending-singapore-india-dta-%28ratified%29%28mli%29%281-oct-2019%29.pdf) |

| Singapore–Japan | 5% corporate 25% voting-share/six-month test described below; otherwise 15%; SG-source exemption | 10%, with government/debt exceptions below | 10% | Article 7 business profits only after classifying the payment. [Articles 5, 7, 10–12](https://www.mof.go.jp/tax_policy/summary/international/press_release/SynthesizedTextforJapan-SingaporeEN.pdf) |

| Singapore–Hong Kong | No comprehensive-treaty dividend rate | No comprehensive-treaty interest rate | No comprehensive-treaty royalty rate | Domestic law governs ordinary services; the limited transport agreement supplies no general no-PE exemption. [IRD agreement register](https://www.ird.gov.hk/eng/tax/dta_singapore.htm), [comprehensive list](https://www.ird.gov.hk/eng/tax/dta_inc.htm) |

| Japan–Australia | 5% corporate direct 10% voting; otherwise 10%; 0% corporate 80%/twelve-month plus Article 23 eligibility below; special vehicles differ | 10%; government/qualifying independent-finance exemption subject to exceptions | 5% | Article 7 requires no PE **and Article 23 entitlement**, after separate-article classification. [Articles 7, 10–12, 23](https://www.mof.go.jp/tax_policy/summary/international/tax_convention/SynthesizedTextforJapan_Australia_EN.pdf) |

| Japan–India | 10% | 10%, with government/debt exceptions | 10% | 10% Article 12 FTS; no Singapore-style make-available restriction. [Articles 10–12](https://www.mof.go.jp/english/policy/tax_policy/tax_conventions/india.text.rev.en.pdf.pdf) |

| Australia–New Zealand | 5% corporate direct 10% voting throughout 365 days including payment; otherwise 15%; 0% corporate 80% plus further conditions below | 10%; government/independent-finance exemptions subject to exceptions | 5% | Article 7 business profits after PE and separate-article checks. [Articles 5, 7, 10–12; MLI 8](https://www.ato.gov.au/law/view/pdf/mli/newzealand_c2.pdf) |

| India–UAE | 10% | 5% bona fide banking/similar financial institution; otherwise 12.5%; 0% qualifying government/central bank | 10% | No separate FTS article: classify under Articles 7, 12, 14 or 22; no automatic domestic-only charge. [Articles 7, 10–12, 14, 22](https://www.incometaxindia.gov.in/documents/20117/6715095/Synthesized-text-India-UAE-DTAA.pdf/25244922-8e6a-1569-81f3-04f9fcc29015?download=true&t=1762943463017&version=1.0) |

| South Korea–Japan | 5% corporate 25% voting-share/six-month test below; otherwise 15% | 10%, with government/debt exceptions | 10% | Article 7 business profits after PE and separate-article checks. [Articles 5, 7, 10–12](https://www.mof.go.jp/tax_policy/summary/international/tax_convention/SynthesizedTextforJapan_Korea_EN.pdf) |

| Hong Kong–UK | 0% generally; 15% qualifying property-investment-vehicle distributions except pension-scheme beneficial owners | 0% **only** if Article 11(3) recipient or payer condition holds; otherwise no automatic treaty exemption | 3% | Article 7 business profits after PE and separate-article checks. [Articles 5, 7, 10–12](https://www.ird.gov.hk/eng/pdf/Synthesised_Text_HKSAR_UK.pdf) |

| Malaysia–Singapore | Article 10(3) exemption while no additional dividend tax; fallback 5% corporate direct 25% capital, otherwise 10% | 10%; approved-loan/government exemptions below | 8% across the treaty definition | **5% Article 13 technical fees**, with performance/source conditions below; not a blanket Article 7 exemption. [Articles 10–13](https://www.iras.gov.sg/media/docs/default-source/uploadedfiles/pdf/singapore-malaysia-dta-%28mli%29%281-jun-2021%29.pdf) |


## Ask the client first

Obtain these six sets of facts before selecting a rate:

1. Payment/accrual date, currency, gross amount, any tax gross-up and the source jurisdiction, including which PE or fixed base bears the cost.
2. Actual recipient, entity type, treaty residence for the relevant period, residence certificate and any transparent-entity or dual-residence issue.
3. Beneficial owner, related parties, onward-payment obligations, lender status, government status and any applicable treaty entitlement or principal-purpose concern.
4. Contract and actual work: dividend, debt, copyright/software/know-how, equipment, ancillary assistance, technical fee or independent personal service; where each service is performed.
5. Capital/voting percentage, direct/indirect ownership chain, acquisition and distribution dates, accounting period, listing and any competent-authority determination.
6. Source-country premises, staff and agents, project and travel-day logs, connected projects/enterprises, effective connection to a PE/fixed base, remittance basis and available local relief documents.

## The method, step by step

### 1. Establish the applicable instrument and direction

Use the treaty and operative protocols/MLI together. A synthesised text helps identify modifications; its own disclaimer gives priority to the authentic instruments. Do not take a signed agreement as effective before its commencement provisions. For Japanese pairs, the current MOF index lists the operative agreements/protocols and links the syntheses used here. [MOF treaty index](https://www.mof.go.jp/english/policy/tax_policy/tax_conventions/tax_convetion_list_en.html); [AU–NZ synthesis introduction](https://www.ato.gov.au/law/view/pdf/mli/newzealand_c2.pdf).

Determine residence under the specific resident article, rather than incorporation alone. For dual-resident entities, stop an automatic rate selection and resolve the applicable competent-authority or other treaty rule. Australia–New Zealand also has a published administrative approach for eligible entities; a foreign residence certificate alone does not settle dual residence. [Article 4 and MLI 4](https://www.ato.gov.au/law/view/pdf/mli/newzealand_c2.pdf), [IRD procedure](https://www.taxpolicy.ird.govt.nz/tax-treaties/australia).


### 2. Classify first, then apply the source rule

Classify the actual rights and work, including mixed payments. Equipment rent is not automatically a royalty in every treaty; nor is every consultancy fee business profit exempt without a PE. Apply the specific dividend, interest, royalty, FTS or personal-service article before the residual business-profit rule. A treaty source rule can follow a PE/fixed base bearing the payment rather than the payer's registered office; apply that corridor's exact rule, including a third-state PE where specified. See the corridor articles below.

For interest/royalties, the stated ceiling ordinarily protects only the arm's-length amount where the special-relationship paragraph applies. A connected debt, shareholding, right or property can move taxation to the PE/fixed-base article. Apply the particular article's beneficial-owner and residence requirements, not merely a certificate held by a conduit. [SG–IN Articles 10–12](https://www.iras.gov.sg/media/docs/default-source/dtas/protocol-amending-singapore-india-dta-%28ratified%29%28mli%29%281-oct-2019%29.pdf), [JP–AU Articles 10–12](https://www.mof.go.jp/tax_policy/summary/international/tax_convention/SynthesizedTextforJapan_Australia_EN.pdf), [MY–SG Articles 10–13](https://www.iras.gov.sg/media/docs/default-source/uploadedfiles/pdf/singapore-malaysia-dta-%28mli%29%281-jun-2021%29.pdf).


### 3. Check entitlement before computing

The MLI principal purposes test can deny a benefit where obtaining it was one of the principal purposes of an arrangement/transaction, unless granting it accords with the relevant provisions' object and purpose. A holding percentage or no-PE finding alone does not clear that test. The syntheses/annexes below identify the applicable modifications. Japan–Australia additionally has Article 23 limitations; Singapore–India Article 24A's capital-gains LOB must not be turned into a universal passive-income test. [SG–AU Annex A Article 20H](https://www.iras.gov.sg/docs/default-source/dtas/singapore-australia-dta%28ratified%29%28mli%29%2819-jul-2021%29.pdf), [SG–IN Annex A/Article 24A](https://www.iras.gov.sg/media/docs/default-source/dtas/protocol-amending-singapore-india-dta-%28ratified%29%28mli%29%281-oct-2019%29.pdf), [JP–AU Article 23/MLI 7](https://www.mof.go.jp/tax_policy/summary/international/tax_convention/SynthesizedTextforJapan_Australia_EN.pdf), [AU–NZ MLI 7](https://www.ato.gov.au/law/view/pdf/mli/newzealand_c2.pdf).

Where a treaty's remittance limitation applies, establish the amount actually remitted/received before granting the source exemption or reduction. SG–AU Article 2(3) and SG–IN Article 24 contain such limits; SG–IN Article 24(2) exempts the specified government/approved-person income from that limitation. Do not assume all residence-state exemptions are remittance taxation. [SG–AU Article 2(3)](https://www.iras.gov.sg/docs/default-source/dtas/singapore-australia-dta%28ratified%29%28mli%29%2819-jul-2021%29.pdf); [SG–IN Article 24](https://www.iras.gov.sg/media/docs/default-source/dtas/protocol-amending-singapore-india-dta-%28ratified%29%28mli%29%281-oct-2019%29.pdf).


### 4. Apply the corridor's operative conditions

In the following sections, ordinary passive-income ceilings assume a treaty-resident beneficial owner, entitlement including anti-abuse rules, arm's-length amounts and no relevant effective connection to a PE/fixed base. Where a condition fails, reclassify or compute under the applicable law; do not reuse the ceiling on the failed category. Government and specialised-vehicle concessions require their own facts.

#### Singapore–Australia

- **Dividends:** Article 8(1) caps Australian source tax at 15% for a Singapore-resident beneficial owner. Article 8(2) exempts Singapore dividends from additional tax, subject to its domestic-law condition. It does not impose a 15% Singapore charge. [Article 8](https://www.iras.gov.sg/docs/default-source/dtas/singapore-australia-dta%28ratified%29%28mli%29%2819-jul-2021%29.pdf).
- **Interest:** 10% under Article 9; test the source, effective-connection and special-relationship paragraphs. No general financial-institution exemption is supplied here. [Article 9](https://www.iras.gov.sg/docs/default-source/dtas/singapore-australia-dta%28ratified%29%28mli%29%2819-jul-2021%29.pdf).
- **Royalties:** 10% under Article 10 only within its definition. Article 2(1)(k)/10(3) excludes the listed literary, dramatic, musical and artistic copyright and film/tape categories from that royalty route. Determine the applicable separate category and domestic charge; do not label every licence 10%. [Articles 2, 10](https://www.iras.gov.sg/docs/default-source/dtas/singapore-australia-dta%28ratified%29%28mli%29%2819-jul-2021%29.pdf).
- **Services:** non-individual enterprise services use the Article 4 PE/Article 5 profits analysis under the published mutual interpretation of 1 May 2018. Individuals' personal/professional services can be taxed where performed under Article 11, and employment follows Article 12. No universal services 0% rule applies. [Article 2(1)(k) interpretation; Articles 4, 5, 11, 12](https://www.iras.gov.sg/docs/default-source/dtas/singapore-australia-dta%28ratified%29%28mli%29%2819-jul-2021%29.pdf).


#### Singapore–India

- **Dividends:** 10% where the beneficial owner is a company holding at least 25% of the paying company's shares; 15% otherwise. Singapore-source dividends have Article 10(3)'s additional-tax exemption while that domestic condition holds. [Article 10](https://www.iras.gov.sg/media/docs/default-source/dtas/protocol-amending-singapore-india-dta-%28ratified%29%28mli%29%281-oct-2019%29.pdf).
- **Interest:** 10% for loans granted by a bank carrying on bona fide banking business or a similar financial institution, including an insurance company; 15% otherwise. Article 22 separately exempts government income: apply its definition, including non-commercial restrictions on the specified bodies. [Articles 11, 22](https://www.iras.gov.sg/media/docs/default-source/dtas/protocol-amending-singapore-india-dta-%28ratified%29%28mli%29%281-oct-2019%29.pdf).
- **Royalty/FTS ceiling:** 10%. The 2005 Protocol Article 4 replaced Article 12(2); the old 15%/10% wording still printed in the main IRAS text must not override it. Later protocol deletions do not delete that Article 4 replacement. [2005 Protocol Article 4; 2011 Protocol Article 1; 2016 Protocol Article 4](https://www.iras.gov.sg/media/docs/default-source/dtas/protocol-amending-singapore-india-dta-%28ratified%29%28mli%29%281-oct-2019%29.pdf).
- **FTS scope:** Article 12(4) covers managerial, technical or consultancy services only within its specified limbs: ancillary/subsidiary to royalty rights, make available technical knowledge/experience/skill/know-how/processes, or qualifying development/transfer of a technical plan/design enabling application. Read Article 12(5)'s exclusions, including ancillary property-sale services, ships/aircraft, educational teaching, personal-use services, employment/Article 14 and specified construction/natural-resource activities. A label on an invoice does not satisfy the test. [Article 12(3)–(5)](https://www.iras.gov.sg/media/docs/default-source/dtas/protocol-amending-singapore-india-dta-%28ratified%29%28mli%29%281-oct-2019%29.pdf).
- **Other services and remittances:** classify separately; independent personal services have Article 14 fixed-base/presence rules, not an automatic company-services exemption. Article 23 preserves domestic taxation of income not expressly mentioned; Article 24 can limit relief to remitted/received amounts. The capital-gains Article 24A LOB has its stated scope. [Articles 14, 23, 24, 24A](https://www.iras.gov.sg/media/docs/default-source/dtas/protocol-amending-singapore-india-dta-%28ratified%29%28mli%29%281-oct-2019%29.pdf).


#### Singapore–Japan

- **Dividends:** 5% where the beneficial owner is a company owning at least 25% of the paying company's voting shares throughout the six months immediately before the end of the accounting period for which the profits are distributed; 15% otherwise. The test is not simply six months before payment. Singapore-source additional tax is exempt under Article 10(4) while its domestic condition holds. [Article 10](https://www.mof.go.jp/tax_policy/summary/international/press_release/SynthesizedTextforJapan-SingaporeEN.pdf).
- **Interest:** 10%; Article 11(3) exempts the specified government, central-bank, wholly government-owned institution and qualifying government-guaranteed/insured/indirectly financed debt income. Use the Article 11(4) definitions and the effective-connection/source/related-party provisions. [Article 11](https://www.mof.go.jp/tax_policy/summary/international/press_release/SynthesizedTextforJapan-SingaporeEN.pdf).
- **Royalties:** 10%; the definition includes specified copyright/software, equipment, bareboat-charter income and certain alienation proceeds. Do not replace it with another corridor's definition. [Article 12](https://www.mof.go.jp/tax_policy/summary/international/press_release/SynthesizedTextforJapan-SingaporeEN.pdf).
- **Services:** use Articles 5/7 after testing royalties and other separate articles. The original Protocol's temporary industrial-interest/tax-sparing provisions ceased for the specified taxable years after 31 December 2000; they are not a current general exemption. [Articles 5, 7; Protocol paragraphs 3–5](https://www.mof.go.jp/tax_policy/summary/international/press_release/SynthesizedTextforJapan-SingaporeEN.pdf).


#### Singapore–Hong Kong

There is **no comprehensive DTA** for these ordinary dividend, interest, royalty and consultancy payments in the official comprehensive list read on 17 November 2026. The agreement identified for this pair is limited to income of enterprises operating ships or aircraft in international traffic. Its Article 3 exemption and Article 2 ancillary-income definition do not create general passive-income rates or an ordinary consultancy PE shield. [Comprehensive list](https://www.ird.gov.hk/eng/tax/dta_inc.htm), [pair register](https://www.ird.gov.hk/eng/tax/dta_singapore.htm), [limited agreement Articles 1–3](https://www.ird.gov.hk/chi/pdf/dt_singapore_air_sh.pdf).

Apply source domestic law and any independently established exemption. Singapore's ordinary interest/royalty rules and Hong Kong's royalty assessment are different; the absence of dividend/interest WHT in Hong Kong does not remove Singapore-source withholding or Hong Kong profits-tax exposure. The domestic comparison below applies; no invented capital/voting split or copyright royalty split may be used. [IRAS WHT rules](https://www.iras.gov.sg/taxes/withholding-tax/basics-of-withholding-tax/types-of-payment-and-withholding-tax-rates), [HK tax policy](https://www.fstb.gov.hk/en/treasury/general/prevailing-tax-policy.htm), [IRD DIPN 22](https://www.ird.gov.hk/eng/pdf/dipn22.pdf).


#### Japan–Australia

- **Ordinary dividends:** 5% for a company beneficial owner holding directly at least 10% of voting power; otherwise 10%. Article 10(2) does not add a six-month holding test. [Article 10(2)](https://www.mof.go.jp/tax_policy/summary/international/tax_convention/SynthesizedTextforJapan_Australia_EN.pdf).
- **Parent exemption:** 0% requires direct ownership of at least 80% of voting power throughout twelve months ending on the date entitlement to the dividend is determined, plus Article 10(3)(a), (b) or (c): qualifying listed-company status under Article 23(2)(c), at least 50% of aggregate vote and value owned directly or indirectly by five or fewer such listed companies, or competent-authority entitlement under Article 23(5). An 80% holding alone is insufficient. [Articles 10(3), 23](https://www.mof.go.jp/tax_policy/summary/international/tax_convention/SynthesizedTextforJapan_Australia_EN.pdf).
- **Special dividends/distributions:** Japan's deductible-dividend vehicle in Article 10(4) has a 15% cap where the specified real-property value exceeds 50%, otherwise 10%. Australia's property-trust distribution rule in Article 10(7) has a 15% cap only for a beneficial owner below the specified 10% capital-value threshold throughout its twelve-month test. Do not apply ordinary company-dividend rates automatically to these vehicles. [Article 10(4), (7)](https://www.mof.go.jp/tax_policy/summary/international/tax_convention/SynthesizedTextforJapan_Australia_EN.pdf).
- **Interest:** 10% ordinarily. Article 11(3)'s government/central-bank and qualifying unrelated independent financial-institution exemptions require their definitions and Article 23 entitlement; Article 11(4)'s back-to-back/equivalent financing restores the stated source-tax route. [Articles 11, 23](https://www.mof.go.jp/tax_policy/summary/international/tax_convention/SynthesizedTextforJapan_Australia_EN.pdf).
- **Royalties:** 5%; the definition includes qualifying ancillary technical assistance but not a general equipment-rental limb. Protocol paragraph 16 routes the specified spectrum-licence payments to Article 7. Check beneficial ownership, effective connection, source, excess amounts and the specific conduit clauses in Articles 10–12. [Article 12; Protocol 16](https://www.mof.go.jp/tax_policy/summary/international/tax_convention/SynthesizedTextforJapan_Australia_EN.pdf).
- **Business profits/LOB:** a no-PE Article 7 conclusion also requires Article 23 entitlement. Its routes include the defined qualified persons, qualifying active business/substantial related activity and competent-authority grant; evidence must satisfy the relevant ownership/holding conditions. Do not turn a no-PE fact into an unconditional services 0% rate. [Articles 7, 23](https://www.mof.go.jp/tax_policy/summary/international/tax_convention/SynthesizedTextforJapan_Australia_EN.pdf).


#### Japan–India

- **Dividends, interest, royalty and FTS:** the ordinary ceilings are each 10% under Articles 10–12. Interest has Article 11(3)/(4)'s government, specified institution and qualifying government-backed/financed-debt exceptions; test their precise definitions. [Articles 10–12](https://www.mof.go.jp/english/policy/tax_policy/tax_conventions/india.text.rev.en.pdf.pdf).
- **FTS:** Article 12(4) covers managerial, technical and consultancy services, including personnel, excluding the stated employment and Article 14 personal-service categories. It does not require the Singapore–India make-available test. [Article 12](https://www.mof.go.jp/english/policy/tax_policy/tax_conventions/india.text.rev.en.pdf.pdf).
- **Services/PE:** Article 7 applies only after separate-article classification; construction, supervisory and mineral-oil PE rules below are not a universal India ninety-day threshold. The MLI also modifies agency, activity exemptions and fragmentation. [Articles 5, 7; MLI 12, 13, 15](https://www.mof.go.jp/english/policy/tax_policy/tax_conventions/india.text.rev.en.pdf.pdf).


#### Australia–New Zealand

- **Dividends:** 5% for a company beneficial owner holding directly at least 10% of voting power; 15% otherwise. MLI Article 8 requires the ownership condition throughout a 365-day period including payment. The 0% route needs at least 80% voting ownership directly or through residents of either state, the same MLI holding test, **and** Article 10(3)'s qualifying listed, qualifying listed/equivalent-benefit ownership, or competent-authority route. Qualifying governments with direct voting ownership no more than 10% have Article 10(4)'s separate exemption. [Article 10 and MLI 8](https://www.ato.gov.au/law/view/pdf/mli/newzealand_c2.pdf).
- **Holding period incomplete at payment:** apply the ordinary 15% treaty withholding, then seek the over-withholding refund after the condition is actually met; intention to hold is insufficient. Reconcile any residence-state foreign credit when a refund changes the source tax. [IRD CS 20/03 paragraphs 15–20](https://www.taxtechnical.ird.govt.nz/-/media/project/ir/tt/pdfs/commissioner-s-statements/cs-20-03.pdf?modified=20211123023343#page=1).
- **Interest:** 10%; government/central-bank and qualifying unrelated independent financial institutions may be exempt. Back-to-back/equivalent arrangements can restore 10%. For NZ-source financial-institution interest, Article 11(4)(a) permits the 10% charge if the payer has not paid approved issuer levy, except where NZ has no such levy, the payer is ineligible to elect it, or its rate exceeds 2% of gross interest. Do not quote 0% without that check. [Article 11(3)–(4)](https://www.ato.gov.au/law/view/pdf/mli/newzealand_c2.pdf).
- **Royalties:** 5% within Article 12's rights/know-how/ancillary-assistance/film/broadcast/spectrum/forbearance definition. There is no general industrial-equipment-rental limb in that definition. Effective connection, third-state PE source and related-party excess paragraphs still apply. [Article 12](https://www.ato.gov.au/law/view/pdf/mli/newzealand_c2.pdf).
- **Services:** Article 7 can protect business profits without a PE, subject to specific articles; the service/equipment PE tests below remain relevant. MLI anti-fragmentation and PPT apply. The operative instrument is the 2009 convention, in force in 2010; the earlier convention/protocol are marked terminated in the official index. [Articles 5, 7/MLI 7, 13](https://www.ato.gov.au/law/view/pdf/mli/newzealand_c2.pdf), [IRD index](https://www.taxpolicy.ird.govt.nz/tax-treaties/australia).


#### India–UAE

- **Residence gate:** Article 4's UAE individual test requires at least 183 days in the calendar year; a UAE company must be incorporated there and managed/controlled wholly there. Do not substitute a visa, nationality or UAE incorporation alone. [Article 4](https://www.incometaxindia.gov.in/documents/20117/6715095/Synthesized-text-India-UAE-DTAA.pdf/25244922-8e6a-1569-81f3-04f9fcc29015?download=true&t=1762943463017&version=1.0).
- **Dividends:** 10% under Article 10(2), with the treaty's beneficial-owner condition. The operative text replaces the older split; do not use the old substantial/portfolio rates. [Article 10](https://www.incometaxindia.gov.in/documents/20117/6715095/Synthesized-text-India-UAE-DTAA.pdf/25244922-8e6a-1569-81f3-04f9fcc29015?download=true&t=1762943463017&version=1.0).
- **Interest:** 5% on a loan granted by a bank carrying on bona fide banking business or a similar financial institution; 12.5% otherwise. Article 11(3) exempts interest beneficially owned by the other government, political subdivision, local authority or central bank. [Article 11](https://www.incometaxindia.gov.in/documents/20117/6715095/Synthesized-text-India-UAE-DTAA.pdf/25244922-8e6a-1569-81f3-04f9fcc29015?download=true&t=1762943463017&version=1.0).
- **Royalties:** 10% within Article 12(3), including specified copyright, rights/equipment and know-how but excluding payments for working natural resources. Apply source, effective connection and special-relationship provisions. [Article 12](https://www.incometaxindia.gov.in/documents/20117/6715095/Synthesized-text-India-UAE-DTAA.pdf/25244922-8e6a-1569-81f3-04f9fcc29015?download=true&t=1762943463017&version=1.0).
- **Services/FTS:** there is no separate FTS article. Business profits may be protected by Article 7 without a PE, individual services can fall under Article 14, and Article 22 has a residence-only residual rule subject to its PE/fixed-base exception. Classify the actual item before choosing a route. The absence of an FTS article does not itself require an Indian domestic FTS charge. [Articles 7, 12, 14, 22](https://www.incometaxindia.gov.in/documents/20117/6715095/Synthesized-text-India-UAE-DTAA.pdf/25244922-8e6a-1569-81f3-04f9fcc29015?download=true&t=1762943463017&version=1.0).
- **UAE corporate tax:** withholding and corporate tax are different computations. The FTA describes zero withholding on the stated non-PE source income, while PE/property-nexus income has separate treatment. This Guide supplies no general corporate-tax exemption or automatic single corporate rate for all UAE recipients. [FTA nonresident basis](https://tax.gov.ae/en/taxes/corporate.tax/corporate.tax.topics/basis.of.taxation.nonresidents.aspx).


#### South Korea–Japan

- **Dividends:** 5% for a company beneficial owner owning at least 25% of the payer's voting shares throughout the six months immediately before the end of the accounting period for which profits are distributed; 15% otherwise. A bare 25% capital holding is not the stated test. [Article 10](https://www.mof.go.jp/tax_policy/summary/international/tax_convention/SynthesizedTextforJapan_Korea_EN.pdf).
- **Interest:** 10%, with Article 11's specified government/central-bank/wholly owned institution and government-backed/financed debt exemptions, definitions and effective-connection/source/related-party checks. [Article 11](https://www.mof.go.jp/tax_policy/summary/international/tax_convention/SynthesizedTextforJapan_Korea_EN.pdf).
- **Royalties:** 10%; Article 12 includes specified copyright/software, equipment, bareboat charters and certain alienation proceeds. [Article 12](https://www.mof.go.jp/tax_policy/summary/international/tax_convention/SynthesizedTextforJapan_Korea_EN.pdf).
- **Services:** Article 7 business profits require the PE analysis and separate-article classification. Political relations or trade volume are not treaty eligibility tests. [Articles 5, 7; MLI 7](https://www.mof.go.jp/tax_policy/summary/international/tax_convention/SynthesizedTextforJapan_Korea_EN.pdf).


#### Hong Kong–UK

- **Dividends:** 0% generally; 15% for distributions by the qualifying investment vehicle out of the stated exempt immovable-property income where it distributes most of that income annually. The property-vehicle charge does not apply where the beneficial owner is a pension scheme. Use the definition, not simply the label “UK REIT”. [Article 10](https://www.ird.gov.hk/eng/pdf/Synthesised_Text_HKSAR_UK.pdf).
- **Interest:** Article 11 exempts source tax only if a resident beneficial owner meets at least one paragraph 3 limb: specified government/HKMA, individual, listed company, pension scheme, unrelated wholly independent financial institution, or another company accepted by the competent authority under the stated purpose test; **or** the payer is the specified government/HKMA, a bank in its ordinary banking business, or the debt is a quoted Eurobond. Otherwise do not grant a blanket 0%; determine domestic charge and any other established relief. [Article 11(1)–(3)](https://www.ird.gov.hk/eng/pdf/Synthesised_Text_HKSAR_UK.pdf).
- **Royalties:** 3% for the resident beneficial owner within Article 12's definition, with effective-connection, source and special-relationship checks. The definition has no general industrial-equipment-rental limb. [Article 12](https://www.ird.gov.hk/eng/pdf/Synthesised_Text_HKSAR_UK.pdf).
- **Services:** Article 7 uses the PE test, including Article 5's connected construction/project service rule below. The MLI PPT replaces the old specified article purpose clauses; passing a percentage test alone does not establish entitlement. [Articles 5, 7; MLI 7](https://www.ird.gov.hk/eng/pdf/Synthesised_Text_HKSAR_UK.pdf).


#### Malaysia–Singapore

- **Dividends:** Article 10(3) exempts additional dividend tax while its domestic condition holds. Article 10(2)'s fallback is 5% for a company beneficial owner holding directly at least 25% of capital, 10% otherwise. Current Malaysian domestic dividend WHT is nil; Singapore one-tier dividends are also exempt as described below. [Article 10](https://www.iras.gov.sg/media/docs/default-source/uploadedfiles/pdf/singapore-malaysia-dta-%28mli%29%281-jun-2021%29.pdf), [HASiL current table](https://www.hasil.gov.my/antarabangsa/perjanjian-pengelakan-pencukaian-dua-kali-pppdk/kadar-cukai-pegangan/), [IRAS dividends](https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/what-is-taxable-what-is-not/dividends).
- **Interest:** 10%; Article 11(3) separately exempts Malaysian-source interest on an approved loan as defined by Article 2. Government exceptions in paragraphs 4–5 use the named/defined government institutions; they do not exempt every state-connected enterprise. Check effective connection, source and related-party excess. [Articles 2, 11](https://www.iras.gov.sg/media/docs/default-source/uploadedfiles/pdf/singapore-malaysia-dta-%28mli%29%281-jun-2021%29.pdf).
- **Royalties:** 8% throughout the Article 12 definition, including specified copyright, equipment and know-how. There is no 8%/10% copyright-versus-industrial split in this article. [Article 12](https://www.iras.gov.sg/media/docs/default-source/uploadedfiles/pdf/singapore-malaysia-dta-%28mli%29%281-jun-2021%29.pdf).
- **Technical fees:** Article 13 caps qualifying technical, managerial or consultancy fees at 5% of gross, excluding the employment category. Source is the payer's residence **and performance in that state**, or a PE/fixed base bearing the cost **and performance in its state**. For work partly outside the source state, establish the supported allocation before applying that article. An effectively connected PE/fixed base instead invokes Articles 7/14. Do not apply a universal no-PE 0% or charge 5% solely because the payer is resident. [Article 13](https://www.iras.gov.sg/media/docs/default-source/uploadedfiles/pdf/singapore-malaysia-dta-%28mli%29%281-jun-2021%29.pdf).
- **Other services:** classify Article 13 first; Article 7/14 treatment follows only for the applicable remainder. Use the current agreement, not the superseded agreement reproduced in Annex B. The MLI PPT is in Annex A. [Articles 7, 13, 14; Annex A](https://www.iras.gov.sg/media/docs/default-source/uploadedfiles/pdf/singapore-malaysia-dta-%28mli%29%281-jun-2021%29.pdf).


### 5. Check PE exposure independently of the withholding rate

These are duration triggers, not safe harbours from fixed-place or agency PE. “More than” does not mean “at least”. Count the specified fiscal/calendar/rolling period, project scope and associated-enterprise aggregation in the actual article. Premises or a dependent agent can create a PE before a duration trigger is met. Independence and preparatory/auxiliary exceptions have their own conditions.

| Corridor | Construction/project trigger | Services, equipment and other conditions | Official source |
|---|---|---|---|

| Singapore–Australia | Building/construction/installation/assembly or connected supervision: more than six months, aggregating within a twelve-month period | Substantial equipment is a separate trigger; also test fixed place and Article 4(5)'s contract/stock/order/processing agency limbs, ordinary independent agents and activity exceptions | [Article 4](https://www.iras.gov.sg/docs/default-source/dtas/singapore-australia-dta%28ratified%29%28mli%29%2819-jul-2021%29.pdf) |

| Singapore–India | Construction/installation/assembly and connected supervision: more than 183 days in a fiscal year | Personnel services other than Article 12 FTS: more than 90 days in a fiscal year, or more than 30 days for a related enterprise; mineral exploration services more than 183 days, relevant natural-resource installation/structure more than 120 days in the fiscal year; fixed place/agent still matter | [Article 5](https://www.iras.gov.sg/media/docs/default-source/dtas/protocol-amending-singapore-india-dta-%28ratified%29%28mli%29%281-oct-2019%29.pdf) |

| Singapore–Japan | Site/construction/installation or connected supervision: more than six months | No separate general personnel-services day threshold stated in Article 5; test fixed place, authority-to-conclude-contracts agent and the specified activity/independent-agent exceptions | [Article 5](https://www.mof.go.jp/tax_policy/summary/international/press_release/SynthesizedTextforJapan-SingaporeEN.pdf) |

| Singapore–Hong Kong | No comprehensive-treaty construction threshold | No general treaty service/fixed-place shield; determine domestic taxable presence and source. The transport-only agreement cannot supply the missing general PE article | [IRD register](https://www.ird.gov.hk/eng/tax/dta_singapore.htm), [limited agreement](https://www.ird.gov.hk/chi/pdf/dt_singapore_air_sh.pdf) |

| Japan–Australia | Construction/installation site more than twelve months; connected supervision/consultancy more than twelve months | Natural-resource activities including substantial equipment: more than 90 days in any twelve months; other substantial equipment more than 183 days. Aggregate connected associated-enterprise activities, count overlapping time once; MLI activity-exemption/anti-fragmentation rules and negotiation/conclusion/processing agency rules apply | [Article 5; MLI 13, 15](https://www.mof.go.jp/tax_policy/summary/international/tax_convention/SynthesizedTextforJapan_Australia_EN.pdf) |

| Japan–India | Construction/installation/assembly project, connected supervision and specified mineral-oil services/facilities: more than six months | No blanket ninety-day rule; fixed place plus MLI principal-role/contract agent, preparatory/auxiliary and anti-fragmentation provisions require their own tests; closely related is not confined to legal share ownership | [Article 5; MLI 12, 13, 15](https://www.mof.go.jp/english/policy/tax_policy/tax_conventions/india.text.rev.en.pdf.pdf) |

| Australia–New Zealand | Construction/installation/assembly site/project more than six months | Services more than 183 days in any twelve months under either individual-presence plus over 50% active-revenue limb, or same/connected-project limb. Apply Article 5(5)'s supervision/direction/control condition; under its same/connected-project limb disregard an individual's services not exceeding five days unless performed regularly or frequently; natural resources/standing timber more than 90 days, substantial equipment more than 183 days. For construction contract splitting, MLI 14 adds connected periods at the same site/project if the enterprise's own periods aggregate more than thirty days without exceeding six months and each closely related enterprise's period exceeds thirty days. For the other Article 5(4) triggers, Article 5(6)'s connected-associate aggregation and overlap-once rule continues; MLI anti-fragmentation and agency tests also apply | [Article 5; MLI 13–15](https://www.ato.gov.au/law/view/pdf/mli/newzealand_c2.pdf) |

| India–UAE | Construction/assembly or connected supervisory activities: more than nine months | Personnel services including consultancy on the same/connected project: more than nine months within any twelve-month period. Also test fixed place and habitual contract authority/independence; no “no service PE” assumption | [Article 5](https://www.incometaxindia.gov.in/documents/20117/6715095/Synthesized-text-India-UAE-DTAA.pdf/25244922-8e6a-1569-81f3-04f9fcc29015?download=true&t=1762943463017&version=1.0) |

| South Korea–Japan | Site/construction/installation or connected supervision: more than six months | No separate general services-day limb stated; fixed place, habitual contract authority, ordinary independent agents and activity exceptions still apply | [Article 5](https://www.mof.go.jp/tax_policy/summary/international/tax_convention/SynthesizedTextforJapan_Korea_EN.pdf) |

| Hong Kong–UK | Site/construction/assembly/installation or supervision: more than six months | Services including consultancy connected with an Article 5(3) site/project/supervision: aggregate more than 183 days in any twelve months under Article 5(4); this is not a general threshold for all services. Fixed-place/agency rules still apply | [Article 5](https://www.ird.gov.hk/eng/pdf/Synthesised_Text_HKSAR_UK.pdf) |

| Malaysia–Singapore | Construction/installation/assembly and connected supervision: more than six months | Article 13 technical-fee tax can apply without a PE. Test fixed place and authority/stock agency; an almost exclusively devoted agent loses independence where dealings are not at arm's length | [Articles 5, 13](https://www.iras.gov.sg/media/docs/default-source/uploadedfiles/pdf/singapore-malaysia-dta-%28mli%29%281-jun-2021%29.pdf) |

### 6. Compare domestic charge, then complete relief procedure

The following preserves the nine-jurisdiction domestic comparison for ordinary source payments to nonresidents. It is a starting comparison, not a complete country computation. Identify the actual instrument and taxpayer before applying it. A treaty cap does not create tax which domestic law does not impose. Do not use a held cell as a rate.

| Source jurisdiction | Dividends | Interest | Royalties | Conditions and official source |
|---|---|---|---|---|

| Singapore | Ordinary one-tier resident-company dividends exempt; do not treat co-operative/REIT distributions as the same category | 15% gross | 10% gross for the listed IP/know-how category; movable-property rent is a separate 15% category | These gross final rates require operations outside Singapore. Operations in Singapore, individual author/composer/choreographer royalties and services have different rules; do not use the ordinary columns for them. [IRAS WHT table/notes](https://www.iras.gov.sg/taxes/withholding-tax/basics-of-withholding-tax/types-of-payment-and-withholding-tax-rates), [dividends](https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/what-is-taxable-what-is-not/dividends) |

| Hong Kong | No dividend WHT | No interest WHT | Not generally tax-free: standard corporate effective amount 4.95% is **computed** as 30% deemed assessable receipts × 16.5%; 100% deemed receipts can instead apply to the specified associate/prior-HK-ownership case | Establish sections 15/21A charge, IP ownership history and the actual corporate profits-tax rate, including any two-tier entitlement, before withholding/assessment. 4.95% is not confined to connected nonresidents. This row does not decide recipient profits-tax liability on other income. [Tax policy](https://www.fstb.gov.hk/en/treasury/general/prevailing-tax-policy.htm), [DIPN 22 paragraphs 27–34](https://www.ird.gov.hk/eng/pdf/dipn22.pdf), [rates](https://www.ird.gov.hk/eng/tax/bus_pft.htm) |

| Japan | Listed-share category 15.315%; other dividends 20.42%, with the NTA's stated listed-share/holder exclusions | Specified interest category 15.315%; loan interest 20.42% | Listed industrial-property/copyright royalties 20.42% | Current NTA table includes the reconstruction surtax; classify under its items (5)–(8), not a rounded range. Treaty rates at/below domestic replace the applicable combined source rate as explained by NTA; do not add the domestic reconstruction surcharge to the treaty ceiling. [NTA No.2884, current 1 April 2026](https://www.nta.go.jp/taxes/shiraberu/taxanswer/gensen/2884.htm) |

| Australia | 30% unfranked amount; fully franked/conduit-foreign-income amounts have separate no-withholding treatment | 10% | 30% | Ordinary non-treaty rates; the unfranked portion of a partly franked dividend needs its own calculation. Obtain correct nonresident/address information and test any statutory exemption; treaty relief requires entitlement. [ATO withholding rates](https://www.ato.gov.au/businesses-and-organisations/hiring-and-paying-your-workers/payg-withholding/payments-you-need-to-withhold-from/withholding-from-investment-income/investment-income-and-royalties-paid-to-foreign-residents/withholding-rate), [payment categories/franking](https://www.ato.gov.au/businesses-and-organisations/hiring-and-paying-your-workers/payg-withholding/payments-you-need-to-withhold-from/withholding-from-investment-income/investment-income-and-royalties-paid-to-foreign-residents/interest-dividends-royalties-and-mit-payments) |

| New Zealand | 30% ordinary non-treaty maximum | 15% ordinary non-treaty maximum | 15% ordinary non-treaty maximum | Apply actual DTA, dividend/imputation/nonportfolio and approved-issuer-levy exceptions before using a maximum. This row does not compute a special dividend or AIL election. [IRD rate selection](https://www.ird.govt.nz/income-tax/withholding-taxes/non-resident-withholding-tax-nrwt/deduct-nrwt-at-the-right-rate) |

| India | **HOLD: no domestic computation supplied** | **HOLD: no domestic computation supplied** | **HOLD: no domestic computation supplied**, including FTS | The old generic rate table is not a current tax calculation. Establish the applicable Act/tax year, income class, taxpayer, special provision, surcharge/cess and withholding section before comparing with a treaty ceiling. The current form mapping confirms the Act transition, not the tax rate. [Department's Act/form transition guide](https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-06/Navigator%201.pdf) |

| South Korea | **HOLD: no domestic computation supplied** | **HOLD: no domestic computation supplied** | **HOLD: no domestic computation supplied** | The original unsupplemented national-rate row cannot establish the complete current national/local withholding result or bond exemptions. Determine those before a domestic-versus-treaty calculation. The treaty ceilings above remain conditional; their source is the [current Japan–Korea synthesis](https://www.mof.go.jp/tax_policy/summary/international/tax_convention/SynthesizedTextforJapan_Korea_EN.pdf), not evidence of domestic rates. |

| Malaysia | Nil dividend WHT | 15% | 10% | HASiL's current domestic row also lists technical fees at 10%; identify the domestic charging provision, performance/source and exemptions before using it. For SG treaty technical fees, apply Article 13's 5% conditions above. [HASiL current table and notes](https://www.hasil.gov.my/antarabangsa/perjanjian-pengelakan-pencukaian-dua-kali-pppdk/kadar-cukai-pegangan/), [treaty Article 13](https://www.iras.gov.sg/media/docs/default-source/uploadedfiles/pdf/singapore-malaysia-dta-%28mli%29%281-jun-2021%29.pdf) |

| UAE | Zero withholding on the FTA's stated non-PE state-source income | Same basis | Same basis | The FTA distinguishes PE income and property nexus from non-PE source income. Zero withholding does not establish no corporate tax, no PE or no residence-state tax. [FTA nonresident basis](https://tax.gov.ae/en/taxes/corporate.tax/corporate.tax.topics/basis.of.taxation.nonresidents.aspx) |


For an eligible category, compute the actual domestic charge and the treaty maximum on the correct base, then apply the allowable lower result. Do not compare percentages across different bases, include unverified surcharge/cess, or promise relief at source before its documents/procedure are established. Gross-up contracts require solving the actual gross payment first. Keep the domestic and treaty computations as separate working-paper lines.

**India procedure:** the current Act's treaty-information form is Form 41 under section 159/Rule 75, with the foreign residence certificate and TIN support; the official mapping pairs it with old Form 10F. Choose the applicable Act's portal tab and period, complete the particulars/residence/declaration panels, e-verify and retain the acknowledgement. A form submission supplies information; it does not itself establish beneficial ownership or treaty eligibility. Earlier-Act periods use the earlier form route. [Form 41 manual](https://www.incometax.gov.in/iec/foportal/newformpage/forms/form41-UM), [official mapping, pages 1–2](https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-06/Navigator%201.pdf).

**Japan procedure:** NTA requires the applicable treaty notification and supporting documents through the payer to the competent tax office by the day before payment for the stated reduction/exemption route. Do not describe entitlement as completed withholding relief until that step is satisfied. [No.2884 treaty-relief paragraph](https://www.nta.go.jp/taxes/shiraberu/taxanswer/gensen/2884.htm).

**Australia–New Zealand procedure:** retain proof of the ownership period and any additional exemption eligibility; where the MLI holding period is unfinished, follow the ordinary withholding/refund route above. For other local forms, payment deadlines and refund limitations, this Guide supplies no completed filing workflow; obtain the relevant source-country procedure before execution. [CS 20/03](https://www.taxtechnical.ird.govt.nz/-/media/project/ir/tt/pdfs/commissioner-s-statements/cs-20-03.pdf?modified=20211123023343#page=1).


## Worked cases

The inputs below are hypothetical. Each case assumes the stated treaty residence, beneficial ownership, documentation, anti-abuse clearance, arm's-length payment and absence of relevant effective connection. These examples compute treaty maximums, not a return or permission to withhold before local relief is completed.

### Case A: Singapore interest paid to Australia

A Singapore payer pays SGD 100,000 ordinary loan interest to an Australian-resident company beneficial owner. Assume the income is derived through operations outside Singapore, the loan is not within a domestic exemption and all Article 9/relief conditions are met. IRAS's ordinary domestic gross rate is 15%; the treaty ceiling is 10%. Domestic tax is SGD 15,000; treaty maximum SGD 10,000; difference SGD 5,000. Reverse the payment and the domestic comparison changes: do not reuse Singapore's rate for an Australian payer. [IRAS table note 1](https://www.iras.gov.sg/taxes/withholding-tax/basics-of-withholding-tax/types-of-payment-and-withholding-tax-rates), [SG–AU Article 9](https://www.iras.gov.sg/docs/default-source/dtas/singapore-australia-dta%28ratified%29%28mli%29%2819-jul-2021%29.pdf).

```oa-check
name: Singapore-source ordinary interest treaty comparison
inputs:
  gross_interest: 100000
  domestic_rate: 0.15
  treaty_rate: 0.10
steps:
  - domestic_tax: gross_interest * domestic_rate
  - treaty_maximum: gross_interest * treaty_rate
  - source_tax: min(domestic_tax, treaty_maximum)
  - difference: domestic_tax - source_tax
expected:
  domestic_tax: 15000
  treaty_maximum: 10000
  source_tax: 10000
  difference: 5000
```

### Case B: Malaysia technical fees performed partly outside Malaysia

A Malaysian-resident payer owes a Singapore-resident company beneficial owner MYR 100,000 for qualifying Article 13 technical consultancy. Contract, work and cost records support MYR 60,000 for services performed in Malaysia and MYR 40,000 performed elsewhere. Assume no relevant PE/fixed base and all entitlement conditions. The Article 13 source test covers the MYR 60,000 Malaysian performance, so its 5% treaty maximum is MYR 3,000. Applying 5% to the entire invoice would give MYR 5,000, overstating that maximum by MYR 2,000. This case does **not** declare the outside portion or every mixed invoice exempt: classify that portion and establish the actual domestic charge/relief before execution. [MY–SG Article 13(2)–(6)](https://www.iras.gov.sg/media/docs/default-source/uploadedfiles/pdf/singapore-malaysia-dta-%28mli%29%281-jun-2021%29.pdf).

```oa-check
name: Malaysia-source technical-fee allocation
inputs:
  invoice: 100000
  performed_in_malaysia: 60000
  treaty_rate: 0.05
steps:
  - outside_performance: invoice - performed_in_malaysia
  - treaty_maximum: performed_in_malaysia * treaty_rate
  - whole_invoice_comparison: invoice * treaty_rate
  - overstatement: whole_invoice_comparison - treaty_maximum
expected:
  outside_performance: 40000
  treaty_maximum: 3000
  whole_invoice_comparison: 5000
  overstatement: 2000
```


## When to refuse or refer

Stop a usable rate calculation where payment character, source, treaty residence, beneficial owner, ownership history or required documents are unestablished; where a domestic-comparison cell is held; or where no applicable comprehensive treaty exists. Report the missing legal/factual input and the affected amount, not a guessed zero.

Refer dual residence, transparent entities, conduit/back-to-back arrangements, principal-purpose concerns, related-party excess, special funds/REITs, effectively connected income, contested software/IP classification, gross-ups and domestic surcharge/local-tax issues for jurisdiction-specific analysis. A no-PE conclusion does not resolve a separate FTS/royalty charge.

## Self-checks

- [ ] Direction, payment period, treaty residence and recipient type match the selected instrument.
- [ ] Each reduced rate's beneficial-owner, ownership percentage, holding-period reference date and entitlement conditions are evidenced.
- [ ] Specific FTS/royalty/personal-service articles were tested before business profits.
- [ ] Fixed-place/agency and every applicable duration/aggregation rule were checked independently.
- [ ] Domestic charge and treaty ceiling use the same correctly established base; held domestic computations remain non-usable.
- [ ] Local relief procedure, acknowledgement and actual withholding/refund evidence support the result.
- [ ] Cases recompute, and any subsequent refund is reconciled with a residence-state foreign-tax credit.

## Sources

Read date is the date the operative provisions or specified official guidance were read, not an accountant approval. Synthesised texts are navigation aids alongside the authentic treaty, protocols and MLI. Source review for this Guide is confined to the stated subjects; it is not a full country tax-system review.

| Official source | Scope read for this Guide | Read on |
|---|---|---|

| [SGAU](https://www.iras.gov.sg/docs/default-source/dtas/singapore-australia-dta%28ratified%29%28mli%29%2819-jul-2021%29.pdf) | Read for: Definitions, mutual interpretation, residence, PE, profits, passive/personal-service articles, remittance and MLI PPT | 2026-11-17 |

| [SGIN](https://www.iras.gov.sg/media/docs/default-source/dtas/protocol-amending-singapore-india-dta-%28ratified%29%28mli%29%281-oct-2019%29.pdf) | Read for: Resident/PE/profits, passive/FTS/personal-service articles, government/remittance/residual, operative protocol replacement and PPT/LOB scope | 2026-11-17 |

| [SGJP](https://www.mof.go.jp/tax_policy/summary/international/press_release/SynthesizedTextforJapan-SingaporeEN.pdf) | Read for: Resident/PE/profits, passive definitions/exceptions, original Protocol expiry and MLI PPT | 2026-11-17 |

| [SGHK](https://www.ird.gov.hk/eng/tax/dta_singapore.htm) | Read for: Limited transport agreement status and nature | 2026-11-17 |

| [HKLIST](https://www.ird.gov.hk/eng/tax/dta_inc.htm) | Read for: Complete comprehensive-agreement country list; absence of SG | 2026-11-17 |

| [HKSHIP](https://www.ird.gov.hk/chi/pdf/dt_singapore_air_sh.pdf) | Read for: Limited transport agreement scope, definitions and exemption; not a general DTA | 2026-11-17 |

| [JPAU](https://www.mof.go.jp/tax_policy/summary/international/tax_convention/SynthesizedTextforJapan_Australia_EN.pdf) | Read for: Resident/PE/profits, passive/vehicle/financing exceptions, Article 23 and relevant Protocol/MLI conditions | 2026-11-17 |

| [JPIN](https://www.mof.go.jp/english/policy/tax_policy/tax_conventions/india.text.rev.en.pdf.pdf) | Read for: Resident/PE/profits, passive/FTS definitions and relevant MLI conditions | 2026-11-17 |

| [AUNZ](https://www.ato.gov.au/law/view/pdf/mli/newzealand_c2.pdf) | Read for: Operative PE/profits/passive articles, MLI residence/holding/anti-fragmentation/PPT changes | 2026-11-17 |

| [NZSTAT](https://www.legislation.govt.nz/secondary-legislation/pco-drafted/2010/13/en/2010-02-15.pdf) | Read for: Statutory treaty schedule PE/profits/passive provisions; reconciled with current official synthesis | 2026-11-17 |

| [NZPERIOD](https://www.taxtechnical.ird.govt.nz/-/media/project/ir/tt/pdfs/commissioner-s-statements/cs-20-03.pdf?modified=20211123023343#page=1) | Read for: CS20/03 operative holding-period, withholding/refund and foreign-credit explanation | 2026-11-17 |

| [NZINDEX](https://www.taxpolicy.ird.govt.nz/tax-treaties/australia) | Read for: Current instrument status, MLI effect and dual-residence procedure | 2026-11-17 |

| [INUAE](https://www.incometaxindia.gov.in/documents/20117/6715095/Synthesized-text-India-UAE-DTAA.pdf/25244922-8e6a-1569-81f3-04f9fcc29015?download=true&t=1762943463017&version=1.0) | Read for: Residence, PE/profits, passive/FTS classification, personal/residual articles and PPT | 2026-11-17 |

| [KRJP](https://www.mof.go.jp/tax_policy/summary/international/tax_convention/SynthesizedTextforJapan_Korea_EN.pdf) | Read for: Residence/PE/profits/passive definitions/exemptions and PPT | 2026-11-17 |

| [HKUK](https://www.ird.gov.hk/eng/pdf/Synthesised_Text_HKSAR_UK.pdf) | Read for: Residence/PE/profits/passive exceptions and MLI PPT | 2026-11-17 |

| [MYSG](https://www.iras.gov.sg/media/docs/default-source/uploadedfiles/pdf/singapore-malaysia-dta-%28mli%29%281-jun-2021%29.pdf) | Read for: Current agreement PE/profits/passive/technical-fee articles, source conditions and PPT; superseded annex not applied | 2026-11-17 |

| [SGDOM](https://www.iras.gov.sg/taxes/withholding-tax/basics-of-withholding-tax/types-of-payment-and-withholding-tax-rates) | Read for: Ordinary WHT table and conditions/notes; not all incentive exemptions | 2026-11-17 |

| [SGDIV](https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/what-is-taxable-what-is-not/dividends) | Read for: One-tier dividend treatment, co-operative/REIT distinctions | 2026-11-17 |

| [HKDOM](https://www.ird.gov.hk/eng/pdf/dipn22.pdf) | Read for: DIPN22 charge/deeming categories and paragraphs27–34; ownership/associate conditions | 2026-11-17 |

| [HKPOLICY](https://www.fstb.gov.hk/en/treasury/general/prevailing-tax-policy.htm) | Read for: No dividend/interest WHT; not a determination of all profits-tax liabilities | 2026-11-17 |

| [HKRATE](https://www.ird.gov.hk/eng/tax/bus_pft.htm) | Read for: Normal corporate profits-tax rate and existence of two-tier treatment | 2026-11-17 |

| [JPDOM](https://www.nta.go.jp/taxes/shiraberu/taxanswer/gensen/2884.htm) | Read for: Current2026 domestic categories/items5–8 and treaty notification/surtax paragraph | 2026-11-17 |

| [AUDOM](https://www.ato.gov.au/businesses-and-organisations/hiring-and-paying-your-workers/payg-withholding/payments-you-need-to-withhold-from/withholding-from-investment-income/investment-income-and-royalties-paid-to-foreign-residents/withholding-rate) | Read for: Official published ordinary non-treaty rates excerpt; open-body403 retained as a read limitation | 2026-11-17 |

| [AUFRANK](https://www.ato.gov.au/businesses-and-organisations/hiring-and-paying-your-workers/payg-withholding/payments-you-need-to-withhold-from/withholding-from-investment-income/investment-income-and-royalties-paid-to-foreign-residents/interest-dividends-royalties-and-mit-payments) | Read for: Official published payment/franking excerpt; open-body403 retained as a read limitation | 2026-11-17 |

| [NZDOM](https://www.ird.govt.nz/income-tax/withholding-taxes/non-resident-withholding-tax-nrwt/deduct-nrwt-at-the-right-rate) | Read for: Ordinary non-DTA maxima and need to select the applicable rate/exception | 2026-11-17 |

| [MYDOM](https://www.hasil.gov.my/antarabangsa/perjanjian-pengelakan-pencukaian-dua-kali-pppdk/kadar-cukai-pegangan/) | Read for: Current domestic and SG treaty rows, headers and notes; updated12July2026 | 2026-11-17 |

| [UAEDOM](https://tax.gov.ae/en/taxes/corporate.tax/corporate.tax.topics/basis.of.taxation.nonresidents.aspx) | Read for: Nonresident source WHT versus PE/property-nexus categories | 2026-11-17 |

| [INFORM](https://www.incometax.gov.in/iec/foportal/newformpage/forms/form41-UM) | Read for: Current Form41 purpose/prerequisites/filing panels and verification | 2026-11-17 |

| [INMAP](https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-06/Navigator%201.pdf) | Read for: Pages1–2 Act transition/tabs and41–10F mapping | 2026-11-17 |

| [MOFLIST](https://www.mof.go.jp/english/policy/tax_policy/tax_conventions/tax_convetion_list_en.html) | Read for: Assigned Japanese treaty-pair entries and operative protocol/synthesis links | 2026-11-17 |


Not yet confirmed: current Indian domestic category-specific rates, withholding bases and surcharge/cess across the 2026 Act transition; current Korean domestic national/local withholding computations and exemptions; complete source-country filing/payment/refund workflows other than the limited procedures above; special NZ dividend/imputation/nonportfolio and AIL computations; residual/excluded SG–AU copyright tax classification for a particular payment. These are explicit holds, not zero rates or permission to file. No holding-structure recommendation or claim about investment volume follows from this Guide.

## Disclaimer

This Guide and its outputs provide general reference and computational assistance, not tax, legal or financial advice. Treaty relief depends on the actual payment, operative law, documents and procedure. A qualified professional in the relevant jurisdiction must review the facts and output before filing, payment or reliance. The current version is maintained at [openaccountants.com](https://www.openaccountants.com).
