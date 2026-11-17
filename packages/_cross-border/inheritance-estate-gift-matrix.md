---
name: inheritance-estate-gift-matrix
description: "Use when an executor, donor, donee or beneficiary asks about inheritance, estate, gift or generation-skipping transfer taxes across jurisdictions. Build the residence, relationship, asset-situs, allowance, relief, treaty and filing analysis before computing. Covers Erbschaftsteuer, Schenkungsteuer, droits de succession, successioni and Spanish ISD regional differences. Includes 2026 official-source rules and explicit nonusable legacy gaps. Excludes probate procedure, will drafting and trust administration beyond transfer-tax mechanics; inherited-asset income tax needs its own country analysis."
version: 0.2
jurisdiction: GLOBAL
tax_year: 2026
last_updated: 2026-11-17
type: cross-country-method
depends_on:
  - cross-border-workflow-base
category: cross-border
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: cross-border
---

# Inheritance, estate and gift tax matrix v0.2

**Built from the law. Not yet approved.** This is a source-cited 2026 preparation method. The Sources section distinguishes the provisions actually read from unresolved claims; a read date is not an accountant approval or proof of all-country completeness.

## Scope

This guide loads on top of `cross-border-workflow-base`. It covers inheritance tax (beneficiary model), estate tax (estate model), gift tax, US GST, asset situs and limited double-tax relief. It retains the original country topics while correcting stale figures and unsupported categorical rules. Event dates and the actual domestic/treaty scope control; current-year metadata does not make a held or historical statement usable.

This guide does NOT cover probate procedure and grant-of-representation mechanics, trust administration tax beyond a reference, will drafting and conflicts-of-law advice, or income tax on inherited assets after death. The civil-law EU regulation and basis interactions below are boundaries, not a probate or income-tax return service. The reviewer is the customer of the output: every affected local filing needs credentialed practitioner review.

## Ask the client first

- What is the death/gift date, and what citizenship, domicile, residence/LTR history and prior transfers apply to each decedent, donor and recipient?
- What are the legal ownership, location, value, debts and trust/retained-benefit terms for every asset, including pensions, insurance, shares and crypto?
- What is each beneficiary's exact relationship, age, disability, marriage/PACS/partnership/cohabitation history and dependency evidence?
- What earlier gifts, allowances, DSUE/GST allocations, elections, foreign taxes and spouse transfers have already been used or reported?
- What business/farm activities, ownership, employee/payroll records, commitment documents and future retention obligations support any relief?
- Which returns, payment references, authority notices, probate documents and deadlines are already outstanding, and which country facts remain unresolved?

## The method, step by step

### Prepare and sequence the computation

**Step 1: define the brief.** Use this matrix to prepare a reviewer brief for an executor, donor, donee or beneficiary. Inheritance tax is usually assessed on the recipient, estate tax on the estate; gift and US generation-skipping transfer (GST) tax need separate tests. It is a cross-country method, not a complete return manual or proof that an unlisted country has no tax.

**Step 2: test status and jurisdiction.** First fix the event date and each person's citizenship, residence history, domicile where relevant, UK long-term residence (LTR), relationship and prior transfers. Then identify every country with a plausible donor, decedent, beneficiary or asset connection. Income-tax residence does not automatically decide transfer-tax residence. US estate-tax residence turns on domicile. [Form 706 general instructions: resident](https://www.irs.gov/instructions/i706).

**Step 3: establish assets and bases.** Build an asset-by-asset inventory: legal owner, trust or retained benefit, gross value, debts, valuation evidence and each country's situs rule. Include real estate, tangible movables, incorporated/listed and private-company shares, bank accounts, government and other debt, cash, insurance, pensions and crypto-assets. Do not assign situs from the generic asset label alone. Separate the taxable acquisition from exempt property, permitted debts and allowances before applying the correct schedule.

**Step 4: compute and test relief.** Classify each beneficiary under the actual country rule. Apply prior-transfer aggregation, exemptions and reliefs in statutory order; check holding periods, payroll, ownership, active-business tests, retained benefits and clawback commitments before reducing the base. Compute each country separately, then test the actual treaty and unilateral credit. A treaty index is a route to the treaty, not permission to claim a credit.

**Step 5: confirm filing and unresolved items.** Identify the competent authority and current form, evidence, payment and filing deadline for each country. Obtain local filing instructions where this matrix records only a threshold or rate. Calculate income-tax basis and later-disposal consequences separately; a transfer-tax exemption does not establish an income-tax exemption. Stop the affected computation at any item listed under Not yet confirmed; do not issue a zero-tax conclusion from an unverified absence claim.


### United States

For 2026, the basic exclusion amount is USD 15,000,000 for the estate/gift unified system and the separate GST exemption is USD 15,000,000. The original USD 13,990,000 relates to 2025, not 2026. This is not the exclusion for a nonresident who is not a US citizen. [Rev. Proc. 2025-32 §2.14](https://www.irs.gov/irb/2025-45_IRB); [Form 706: exclusion by year](https://www.irs.gov/instructions/i706).

US citizens and estate-tax domiciliaries start with worldwide property. Form 706 is generally required when gross estate plus adjusted taxable gifts and the specific gift exemption exceed the applicable exclusion, even if deductions remove tax. File within 9 months of death; a filing extension and a payment extension are different requests, using Form 4768 where applicable. [Form 706 general instructions: filing](https://www.irs.gov/instructions/i706); [Form 706: gross estate](https://www.irs.gov/instructions/i706).

DSUE portability requires a timely, complete Form 706 election even when no return would otherwise be required. The surviving spouse uses the last deceased spouse's available DSUE, subject to the noncitizen/nonresident and QDOT rules. Simplified late portability relief under Rev. Proc. 2022-32 is limited to estates not otherwise required to file and its conditions, including the 5th-anniversary limit. Do not treat marriage as an automatic doubling of the exclusion or apply DSUE to GST. [Form 706: portability relief](https://www.irs.gov/instructions/i706); [Form 709: DSUE](https://www.irs.gov/instructions/i709).

The unified estate/gift schedule starts at 18% and reaches 40%; it is not a flat tax on every dollar transferred. The GST top rate is 40%. Prior taxable gifts, allowable credit and allocated GST exemption must be reconciled before tax is determined. [Form 706 Table A](https://www.irs.gov/instructions/i706); [Form 709: rates](https://www.irs.gov/instructions/i709).

The 2026 annual gift exclusion is USD 19,000 per donor per donee for present interests. The special exclusion for qualifying gifts to a spouse who is not a US citizen is USD 194,000; it is not the unlimited marital deduction. Gift splitting and gifts of future interests require their own return/election analysis. [Rev. Proc. 2025-32 §4.42](https://www.irs.gov/irb/2025-45_IRB).

The separate education exclusion requires direct payment of tuition to a qualifying educational organization; books, supplies, room and board do not qualify. Medical payments must go to the care provider or qualifying medical insurance, satisfy §213(d), and exclude amounts reimbursed by the donee's insurance. These exclusions do not depend on kinship. [Form 709: educational and medical exclusions](https://www.irs.gov/instructions/i709).

The estate marital deduction for property included in the gross estate is subject to terminable-interest/QTIP rules. A noncitizen spouse generally requires a qualifying domestic trust (QDOT) and election unless a treaty provides otherwise. Charitable deductibility requires the actual estate/gift charitable provision and eligible purpose/recipient; §501(c)(3) status by itself is not an unlimited deduction for every transfer. NRA estate charitable deductions generally require a domestic entity or US use, unless a treaty changes the result. [Form 706-NA Part IV line 7](https://www.irs.gov/instructions/i706na); [Form 706 Schedule M](https://www.irs.gov/instructions/i706).

For a nonresident noncitizen estate, US real estate and physically US tangible property are generally US situs; stock of a corporation organized under US law is US situs regardless of certificate location. Other corporate stock is generally outside the US. The original phrase including foreign corporations' US-business income is not a general share-situs rule; special expatriate look-through rules require a separate test. [Form 706-NA Part V: stock](https://www.irs.gov/instructions/i706na); [Form 706-NA Part V: expatriates](https://www.irs.gov/instructions/i706na).

Do not label all US bank accounts or US-government bonds US situs. The Form 706-NA rules exclude specified deposits not effectively connected with a US trade or business, qualifying portfolio debt and other specified obligations; contingent-interest and transfer-timing exceptions matter. Life-insurance proceeds on the nonresident decedent's life are outside the US under the stated rule. [Form 706-NA Part V: deposits](https://www.irs.gov/instructions/i706na); [Form 706-NA Part V: debt](https://www.irs.gov/instructions/i706na); [Form 706-NA Part V: insurance](https://www.irs.gov/instructions/i706na).

USD 60,000 is the nonindexed Form 706-NA filing threshold, counting the specified gifts as well as US-situated property. It is not a universal USD 60,000 deduction. The ordinary maximum unified credit is USD 13,000, with territory/treaty and prior-credit adjustments. The same rate schedule can reach 40%. Form 706-NA is generally due within 9 months of death; document worldwide estate amounts for proportionate deductions. [IRS NRA estate scope](https://www.irs.gov/businesses/small-businesses-self-employed/estate-tax-for-nonresidents-not-citizens-of-the-united-states); [Form 706-NA Part II line 7](https://www.irs.gov/instructions/i706na); [Form 706-NA Part IV](https://www.irs.gov/instructions/i706na).

Report gifts on the return for the year of the gift. Form 709 is generally due by 15 April of the following year, moved to the next business day for a weekend/legal holiday. If the donor dies, the earlier estate-return deadline, including its extensions, can control. Filing extensions do not automatically extend payment. Check the separate nonresident-noncitizen gift return route instead of assuming Form 709 fits every donor. [Form 709: when to file](https://www.irs.gov/instructions/i709).

Inherited-property income-tax basis is generally fair market value at death, or the valid alternate valuation, subject to exceptions and estate-value consistency. It may step down as well as up and is not restricted to US-citizen beneficiaries. Lifetime-gift basis is generally the donor's basis, with loss and other exceptions. The original modified-estate-regime carryover reference is historical and held below; it is not a 2026 election. [IRS gifts/inheritances basis FAQ](https://www.irs.gov/faqs/interest-dividends-other-types-of-income/gifts-inheritances/gifts-inheritances); [IRS gift FAQ: basis](https://www.irs.gov/businesses/small-businesses-self-employed/frequently-asked-questions-on-gift-taxes).


### United Kingdom

For transfers from 6 April 2025, LTR replaces domicile for the principal overseas-property scope test: normally UK residence in at least 10 of the preceding 20 tax years. On departure the tail is 3 to 10 tax years, not automatically 10: 10 to 13 resident years normally produce a 3-year tail, then the tail increases with resident years to 10. Apply the published 2025/26 transition and 10 consecutive nonresident-year reset rules. [HMRC: long-term UK residence](https://www.gov.uk/guidance/inheritance-tax-if-youre-a-long-term-uk-resident).

LTR can bring overseas property and relevant overseas trust property into scope. Trust treatment turns on settlor residence at chargeable events and the statutory transition, including the restricted protection for certain foreign property held on 30 October 2024 and death/end-of-interest charges. Do not claim that only trusts settled after 6 April 2025 lose excluded-property protection. Non-LTR UK-property scope also has specific excluded-asset rules; UK situs is not decided from a generic account label. [HMRC LTR: transition and trusts](https://www.gov.uk/guidance/inheritance-tax-if-youre-a-long-term-uk-resident); [HMRC outside-UK death scope](https://www.gov.uk/inheritance-tax/when-someone-living-outside-the-uk-dies).

The basic nil-rate band is GBP 325,000. HMRC's current table lists it through 5 April 2031. The residence nil-rate band is up to GBP 175,000 for a qualifying home closely inherited by direct descendants, limited by the home value and reduced by GBP 1 for every GBP 2 of estate value over GBP 2,000,000. The RNRB table lists through 5 April 2030; do not assume both future end dates are identical. Unused spouse/civil-partner bands require the relevant transfer conditions and claim. [HMRC threshold table](https://www.gov.uk/government/publications/rates-and-allowances-inheritance-tax-thresholds-and-interest-rates/inheritance-tax-thresholds-and-interest-rates); [HMRC RNRB threshold table](https://www.gov.uk/government/publications/rates-and-allowances-inheritance-tax-thresholds-and-interest-rates/inheritance-tax-thresholds-and-interest-rates); [HMRC RNRB: taper](https://www.gov.uk/guidance/inheritance-tax-residence-nil-rate-band).

The spouse/civil-partner exemption is limited to the nil-rate band when the transferor is LTR and the recipient is not LTR, counting earlier exempt spouse/civil-partner transfers cumulatively, including other marriages. It is not limited merely because the recipient is non-LTR: the restriction does not apply where both are non-LTR. Elections changing treatment need their own advice; do not assume an election without the record. [IHTM47030: spouse exemption](https://www.gov.uk/hmrc-internal-manuals/inheritance-tax-manual/ihtm47030).

The ordinary death rate is 40% above available bands/exemptions. A 36% rate can apply to the relevant estate component if at least 10% of its baseline amount passes to qualifying charity; this is not 10% of gross assets. Charity and spouse exemptions require the eligible recipient and property conditions, not a blanket label. [HMRC IHT overview](https://www.gov.uk/inheritance-tax).

Potentially exempt gifts can fall out after survival for 7 years; retained-benefit gifts and trusts need separate treatment. Taper reduces tax on chargeable gifts, not the gift value, and generally matters only after the available nil-rate band is used: 40% within 3 years, then 32%, 24%, 16%, 8% for the successive yearly bands, and 0% after 7 years. A lifetime chargeable trust transfer can attract 20%, with additional death charges subject to the actual trust, cumulation and grossing rules; do not apply that rate to every lifetime gift. [HMRC gifts: seven-year rule](https://www.gov.uk/inheritance-tax/gifts); [HMRC trusts and IHT](https://www.gov.uk/trusts-taxes/trusts-and-inheritance-tax).

APR is based on agricultural value of qualifying UK property, not all farm assets: livestock, machinery and specified other items are excluded. Ordinarily require 2 years' qualifying owner occupation or 7 years' ownership with qualifying occupation by another. Qualifying owner occupation, grazing arrangements and specified tenancies can receive 100%; other qualifying cases receive 50%. Tenanted land is not automatically restricted to 50%. From 6 April 2026 the combined APR/BPR allowance for property otherwise qualifying for 100% relief is GBP 2,500,000, not the original GBP 1,000,000; excess qualifying value receives 50%. [HMRC Agricultural Relief: 6-Apr-2026 rules](https://www.gov.uk/guidance/agricultural-relief-on-inheritance-tax).

BPR eligibility generally requires 2 years' ownership and an eligible business/interest or shares. Investment businesses, nonqualifying sale arrangements and nonbusiness assets are excluded or restricted. The 100% class is subject to the combined GBP 2,500,000 APR/BPR allowance from 6 April 2026; 50% applies to excess and the specified 50% classes, including listed controlling holdings and eligible shares on markets such as AIM. Unused spouse/civil-partner allowance can be transferred under the claim rules; prior qualifying gifts and trusts affect the allocation. Do not claim APR and BPR twice on the same value. [HMRC Business Relief: eligibility](https://www.gov.uk/business-relief-inheritance-tax/what-qualifies-for-business-relief); [HMRC Business Relief: allowance](https://www.gov.uk/business-relief-inheritance-tax/what-qualifies-for-business-relief); [HMRC Agricultural Relief: allocation and transfer](https://www.gov.uk/guidance/agricultural-relief-on-inheritance-tax).

Quick succession relief requires an earlier chargeable transfer within 5 years that increased this decedent's estate and on which tax was or becomes payable; it is not relief whenever two relatives die within that period. Obtain the relief calculation for the actual earlier transfer. [IHTM22042: quick succession relief](https://www.gov.uk/hmrc-internal-manuals/inheritance-tax-manual/ihtm22042).

Pay IHT by the end of the 6th month after the month of death; interest may accrue thereafter. Reporting and probate deadlines are distinct. Full IHT400 information can be needed even where no tax is payable, under the detailed estate/gift/foreign-property/trust conditions. The original IHT205/C5 small-estate shortcuts are held below, not current filing instructions. [HMRC paying IHT](https://www.gov.uk/paying-inheritance-tax); [HMRC: check type of estate](https://www.gov.uk/valuing-estate-of-someone-who-died/check-type-of-estate).


### Germany

ErbStG §2 determines unlimited/limited liability; German citizenship departure and deemed connections matter. Class I includes spouse/registered partner, children/stepchildren and descendants, and parents/grandparents on death. Class II includes parents/grandparents on lifetime gifts, siblings and their first-degree descendants, specified step/in-law relationships and divorced/former partners. Class III is the rest. Germany has 3 classes, not Classes I-IV. [ErbStG §§2,15](https://www.gesetze-im-internet.de/erbstg_1974/BJNR109330974.html).

Personal allowances under §16: spouse/registered partner EUR 500,000; children/stepchildren and children of a deceased child EUR 400,000; other grandchildren EUR 200,000; other Class I EUR 100,000; Classes II and III EUR 20,000. Limited liability can require proportionate reduction. Aggregate same-person acquisitions within 10 years under §14, with the statutory previous-tax credits and limits; do not treat the allowance as refreshing after every transfer. [ErbStG §§14,16](https://www.gesetze-im-internet.de/erbstg_1974/BJNR109330974.html).

Apply the §19 rate to the whole taxable acquisition, not marginal slices. These are the rates after the available allowance.

| Taxable acquisition up to / above | Class I | Class II | Class III | Official source |
|---|---|---|---|---|
| EUR 75,000 | 7% | 15% | 30% | [ErbStG §19](https://www.gesetze-im-internet.de/erbstg_1974/BJNR109330974.html) |
| EUR 300,000 | 11% | 20% | 30% | [ErbStG §19](https://www.gesetze-im-internet.de/erbstg_1974/BJNR109330974.html) |
| EUR 600,000 | 15% | 25% | 30% | [ErbStG §19](https://www.gesetze-im-internet.de/erbstg_1974/BJNR109330974.html) |
| EUR 6,000,000 | 19% | 30% | 30% | [ErbStG §19](https://www.gesetze-im-internet.de/erbstg_1974/BJNR109330974.html) |
| EUR 13,000,000 | 23% | 35% | 50% | [ErbStG §19](https://www.gesetze-im-internet.de/erbstg_1974/BJNR109330974.html) |
| EUR 26,000,000 | 27% | 40% | 50% | [ErbStG §19](https://www.gesetze-im-internet.de/erbstg_1974/BJNR109330974.html) |
| Above EUR 26,000,000 | 30% | 43% | 50% | [ErbStG §19](https://www.gesetze-im-internet.de/erbstg_1974/BJNR109330974.html) |

Section19(3) mitigates a bracket jump: the extra tax is limited by the specified 50% or 75% portion of the excess over the prior threshold. A computation must test that mitigation. [ErbStG §19(3)](https://www.gesetze-im-internet.de/erbstg_1974/BJNR109330974.html).

The standard business relief under §§13a/13b is 85% for qualifying property within the EUR 26,000,000 acquisition threshold, including the 10-year aggregation rule. Eligibility requires the qualifying business/shareholding and administrative-asset tests, including the 90% exclusion test; it is not simply any family company. The standard holding period is 5 years and the payroll sum normally 400%, with exemptions for no/at most 5 employees and reduced 250%/300% tests for 6-10/11-15 employees. Disposals and failures can claw back relief; record continuing obligations. [ErbStG §13a](https://www.gesetze-im-internet.de/erbstg_1974/BJNR109330974.html); [ErbStG §13b](https://www.gesetze-im-internet.de/erbstg_1974/BJNR109330974.html).

The irrevocable 100% option extends the holding/payroll period to 7 years; its normal payroll sum is 700%, with the stated smaller-employer modifications, and administrative assets must not exceed 20%. Confirm the detailed §13b asset/debt/young-asset rules and shareholding conditions before either relief. The original unlocated BFH ruling/transitional statement remains nonusable below. [ErbStG §13a(10)](https://www.gesetze-im-internet.de/erbstg_1974/BJNR109330974.html).

Section 30 generally requires written notification within 3 months of knowledge of the acquisition, from recipient and donor for gifts, subject to the precise court/notarial exceptions. That is not the return deadline. Under §31 the Finanzamt can require a return within a deadline it sets of at least 1 month. Do not use the original automatic three-month return deadlines or the unsourced usual 4-6-month request. [ErbStG §30](https://www.gesetze-im-internet.de/erbstg_1974/BJNR109330974.html); [ErbStG §31](https://www.gesetze-im-internet.de/erbstg_1974/BJNR109330974.html).


### France

A surviving spouse or PACS partner is exempt from death duties, not automatically from gift duty. A sibling can be fully exempt on death only under the unmarried/widowed/divorced/separated, age over 50 or incapacity, and 5-year cohabitation conditions. Otherwise siblings pay 35% on the first EUR 24,430 taxable portion and 45% above. Relatives through the 4th degree, including first cousins, generally pay 55%; more distant relatives and unrelated recipients 60%. [DGFiP: death calculation](https://www.impots.gouv.fr/particulier/questions/comment-dois-je-calculer-les-droits-de-succession); [DGFiP: death exemptions](https://www.impots.gouv.fr/particulier/questions/comment-dois-je-calculer-les-droits-de-succession).

Lineal death-duty marginal bands after allowances; do not apply the highest bracket to the whole share.

| Taxable portion, EUR | Marginal rate | Official source |
|---|---|---|
| Up to 8,072 | 5% | [CGI art.777 / DGFiP](https://www.impots.gouv.fr/particulier/questions/comment-dois-je-calculer-les-droits-de-succession) |
| 8,072 to 12,109 | 10% | [CGI art.777 / DGFiP](https://www.impots.gouv.fr/particulier/questions/comment-dois-je-calculer-les-droits-de-succession) |
| 12,109 to 15,932 | 15% | [CGI art.777 / DGFiP](https://www.impots.gouv.fr/particulier/questions/comment-dois-je-calculer-les-droits-de-succession) |
| 15,932 to 552,324 | 20% | [CGI art.777 / DGFiP](https://www.impots.gouv.fr/particulier/questions/comment-dois-je-calculer-les-droits-de-succession) |
| 552,324 to 902,838 | 30% | [CGI art.777 / DGFiP](https://www.impots.gouv.fr/particulier/questions/comment-dois-je-calculer-les-droits-de-succession) |
| 902,838 to 1,805,677 | 40% | [CGI art.777 / DGFiP](https://www.impots.gouv.fr/particulier/questions/comment-dois-je-calculer-les-droits-de-succession) |
| Above 1,805,677 | 45% | [CGI art.777 / DGFiP](https://www.impots.gouv.fr/particulier/questions/comment-dois-je-calculer-les-droits-de-succession) |


The ordinary child-or-parent death-duty allowance is EUR 100,000; sibling EUR 15,932; nephew/niece EUR 7,967. Where no other allowance applies, the death-duty fallback is EUR 1,594. The additional disabled allowance is EUR 159,325 subject to disability conditions. Previous gifts from the same person within 15 years can consume allowances and bands. EUR 31,865 for grandchildren is a lifetime-gift allowance, not an automatic grandchild death allowance; do not extend the ordinary child/parent allowance to every lineal descendant, and check representation separately. A spouse/PACS lifetime gift has an EUR 80,724 allowance and its own rate thresholds; death exemption is separate. [DGFiP gifts: allowances and aggregation](https://www.impots.gouv.fr/particulier/calcul-et-paiement-des-droits); [DGFiP gifts: grandchildren](https://www.impots.gouv.fr/particulier/calcul-et-paiement-des-droits); [DGFiP death: allowances and disability](https://www.impots.gouv.fr/particulier/questions/comment-dois-je-calculer-les-droits-de-succession).

Dutreil under CGI art.787 B can exempt 75% of qualifying business-share value. The ordinary collective/unilateral commitment lasts at least 2 years and must be in force at transmission; post-mortem and deemed-acquired routes have separate conditions. Financial/voting thresholds are 10%/20% for listed and 17%/34% for unlisted companies. Eligible activity must remain principally operational throughout the required periods; management of the company's own movable/immovable investments is excluded, with a separate active-holding analysis. [BOI-ENR-DMTG-10-20-40-10 §§1-60,70-210](https://bofip.impots.gouv.fr/bofip/6509-PGP.html/identifiant=BOI-ENR-DMTG-10-20-40-10-20260810).

The individual commitment after the collective period is 4 years for transmissions before 21 February 2026 and 6 years for transmissions from that date. An eligible signatory or recipient must perform the required main professional activity/management function during the collective period and the 3 years following transmission; a deemed-acquired pact requires a recipient, not merely the donor, to meet the post-transfer management condition. Indirect holdings and usufruct gifts have additional preservation/voting conditions. Do not translate 75% base relief into a 75% reduction of the final progressive tax. [BOI-ENR-DMTG-10-20-40-10 §§270-395](https://bofip.impots.gouv.fr/bofip/6509-PGP.html/identifiant=BOI-ENR-DMTG-10-20-40-10-20260810); [BOI-ENR-DMTG-10-20-40-10 §330](https://bofip.impots.gouv.fr/bofip/6509-PGP.html/identifiant=BOI-ENR-DMTG-10-20-40-10-20260810).

From 21 February 2026, the Dutreil exempt share value excludes the specified luxury/nonbusiness assets unless exclusively allocated to the qualifying activity for at least 3 years before transmission (or since acquisition) and through the individual commitment (or disposal). This includes the statutory hunting/fishing, vehicles/boats/aircraft, valuables/art, racehorses, wines/spirits and residences categories, subject to their stated exceptions and controlled-subsidiary look-through. Art qualifying under CGI art.238 bis AB is expressly outside the listed art exclusion; do not impose the ordinary exclusive-use test on that statutory exception. Obtain the actual asset allocation and compliance evidence before calculating relief. [BOI-ENR-DMTG-10-20-40-10 §§400-500](https://bofip.impots.gouv.fr/bofip/6509-PGP.html/identifiant=BOI-ENR-DMTG-10-20-40-10-20260810).

Death declarations are generally due within 6 months for a death in metropolitan France, or 12 months abroad. Overseas-department and untitled-immovable-property exceptions can give different periods. Filing/payment exemptions for small estates have their own relationship and undeclared-prior-gift conditions. File with the competent registration service, using the nonresident route where needed. Duty is normally payable on filing; qualifying business transmissions may obtain 5 years' deferral then 10 years' instalments only on application, guarantees and interest, not automatically. [DGFiP: death declaration deadlines](https://www.impots.gouv.fr/particulier/questions/quand-dois-je-deposer-les-declarations-de-revenu-et-de-succession-en-cas-de); [DGFiP: succession payment](https://www.impots.gouv.fr/particulier/questions/comment-puis-je-payer-les-droits-de-succession).


### Spain

Select the competent administration and applicable regional or state rules before calculating ISD; beneficiary/decedent residence, immovable location and nonresident rules matter. National Ley 29/1987 arts.20-22 provide a fallback, not an election to ignore the autonomous community. Inheritances, lifetime gifts and succession agreements need their own taxable-event analysis. [Ley 29/1987 arts.20-22](https://www.boe.es/buscar/act.php?id=BOE-A-1987-28141); [Ley 29/1987 art.24](https://www.boe.es/buscar/act.php?id=BOE-A-1987-28141).

For national death-duty reductions, Group I is descendants/adoptees under 21: EUR 15,956.87 plus EUR 3,990.72 per year under 21, capped at EUR 47,858.59. Group II is descendants/adoptees 21 or older, spouse and ascendants/adoptive parents: EUR 15,956.87. Group III is collateral relatives of the 2nd/3rd degrees and ascendants/descendants by affinity: EUR 7,993.46. Group IV, including 4th-degree collateral relatives and strangers, has no relationship reduction. Additional disability reduction is EUR 47,858.59 for at least 33% but under 65%, or EUR 150,253.03 for at least 65%. These are not automatically lifetime-gift allowances. [Ley 29/1987 art.20(2),(5)](https://www.boe.es/buscar/act.php?id=BOE-A-1987-28141).

The national marginal tariff ranges from 7.65% to 34%, with the fixed amounts in art.21. Multiply the resulting quota by the art.22 coefficient for relationship group and pre-existing wealth, then test the coefficient-jump mitigation. The highest coefficient is 2.4 for Group IV with wealth over EUR 4,020,770.98. The derived 81.6% is 34% × 2.4 at that top marginal combination, not a flat effective tax rate on every Group IV inheritance. [Ley 29/1987 art.21](https://www.boe.es/buscar/act.php?id=BOE-A-1987-28141); [Ley 29/1987 art.22](https://www.boe.es/buscar/act.php?id=BOE-A-1987-28141).

National business death relief is a 95% reduction for the qualifying business/professional activity/shares covered by the Wealth Tax exemption, passing to the specified spouse/descendant class (extended relatives where no descendants) and maintained for 10 years unless the acquirer dies first. Prohibited substantial value reductions and clawback apply. National lifetime business relief separately requires a donor at least 65 or with permanent incapacity in the statutory absolute or gran invalidez category, cessation of paid management where exercised, and recipient maintenance/Wealth Tax eligibility for 10 years unless the recipient dies first. [Ley 29/1987 art.20(2)(c),(6)](https://www.boe.es/buscar/act.php?id=BOE-A-1987-28141).

National habitual-home death relief is 95%, capped at EUR 122,606.47 per beneficiary and subject to the 10-year preservation condition and eligible spouse/ascendant/descendant class, or a collateral relative over 65 who lived with the deceased for the prior 2 years. Regional replacements can differ. The original generic favorable pacto sucesorio statement is held below; civil validity alone does not establish the tax result. [Ley 29/1987 art.20(2)(c)](https://www.boe.es/buscar/act.php?id=BOE-A-1987-28141).

Madrid death-tax relief includes a 99% quota rebate for the specified direct-family/spouse category; a registered qualifying partner can be assimilated. It leaves 1% of the pre-rebate quota, not zero tax and not a filing exemption. Gift documentation/fund-origin conditions are distinct; do not use the inheritance example to clear a gift. The regional page also records separate Group III and small-gift changes. [Madrid: beneficios fiscales, close-family rebate](https://www.comunidad.madrid/atencion-contribuyente/beneficios-fiscales).

Andalucía art.39 gives a 99% death-quota rebate for Groups I/II and statutory assimilations, including qualifying life-insurance receipts. This is not universal elimination. Its separate gift rebate has voluntary-declaration, documentation and fund-origin conditions in art.40; the current EUR 5,000 document threshold/aggregation conditions must be checked for a gift rather than importing death treatment. [Andalucía Ley 5/2021 arts.26,39-40](https://www.boe.es/eli/es-an/l/2021/10/20/5/con).

Murcia's inheritance guidance gives Groups I/II a 99% death-quota rebate after applicable state/regional deductions. It separately specifies business, partner and residence conditions. Cantabria's current art.8 gives Groups I/II a 100% death-quota rebate; the original 99% and under-22 formulation is not the current rule. Apply the legal group/assimilation definitions, not a similar-sounding family label. [Murcia: inheritance FAQ 21-24](https://agenciatributaria.carm.es/sucesiones?inheritRedirect=true); [Cantabria DL 62/2008 art.8](https://boe.es/buscar/act.php?id=BOCT-c-2008-90028&p=20260430&tn=0).

Catalonia gives spouses/qualifying stable partners a 99% death-quota rebate. From 27 June 2025 a separate 99% route can cover descendants/ascendants of a woman whose death resulted from the specified gender violence, with the statutory evidence required. Outside those special routes, Group I beneficiaries use a weighted schedule whose first EUR 100,000 band is 99%; Group II beneficiaries start at 60% for that band, not 99%, with lower marginal rebates at higher bases. The published election restrictions can disallow these schedules when specified business/other reductions are chosen; home and decennial double-tax reductions are compatible. Do not apply a flat first-band rate to the whole inheritance. [ATC: death-quota rebates, points 1-6](https://atc.gencat.cat/es/tributs/isd/herencies/bonificacio/).

Galicia's 2026 relationship reduction is EUR 1,000,000 plus EUR 100,000 per year under 21 for Group I, capped at EUR 1,500,000; Group II receives EUR 1,000,000. This is a base reduction, not the original claimed 99% quota rebate up to EUR 1 million. The same-person acquisition aggregation and remaining available reduction must be checked. [ATRIGA 2026, DL 1/2011 art.6(2),(5)](https://www.atriga.gal/documents/20632401/21043974/BeneficiosFiscales-Sucesiones-es-01-01-2026.pdf/1b2c418f-b912-4439-9698-41aa782a002c).

The national death presentation period is 6 months from death; a further equal period can be requested within the first 5 months, with interest and the prescribed request details. An extension is not automatic on a late request. Use the competent administration's actual declaration/self-assessment forms: Model 650 and any required estate inventory such as 660 are not a universal pair for every autonomous community. [RD 1629/1991 arts.67-68](https://www.boe.es/buscar/act.php?id=BOE-A-1991-27678).


### Italy

For successions opened and gifts made from 1 January 2025, D.Lgs.346/1990 as amended by D.Lgs.139/2024 provides the following ordinary rates on the net value over the per-beneficiary allowance. Gift rates/allowances are reproduced in TUS art.56.

| Relationship | Allowance, EUR | Rate above allowance | Official source |
|---|---|---|---|
| Spouse/direct line | 1,000,000 | 4% | [TUS arts.7,56 / AdE3/E §4](https://def.finanze.it/DocTribFrontend/getPrassiDetail.do?id=%7B94E7FE33-0385-403D-8228-BE658CC58749%7D&primoPiano=true) |
| Siblings | 100,000 | 6% | [TUS arts.7,56 / AdE3/E §4](https://def.finanze.it/DocTribFrontend/getPrassiDetail.do?id=%7B94E7FE33-0385-403D-8228-BE658CC58749%7D&primoPiano=true) |
| Other relatives through the 4th degree, direct-line affinity and collateral affinity through the 3rd degree | None ordinarily | 6% | [TUS arts.7,56 / AdE3/E §4](https://def.finanze.it/DocTribFrontend/getPrassiDetail.do?id=%7B94E7FE33-0385-403D-8228-BE658CC58749%7D&primoPiano=true) |
| Others | None ordinarily | 8% | [TUS arts.7,56 / AdE3/E §4](https://def.finanze.it/DocTribFrontend/getPrassiDetail.do?id=%7B94E7FE33-0385-403D-8228-BE658CC58749%7D&primoPiano=true) |

A beneficiary with the qualifying severe disability under Law104/1992 art.3(3) has the EUR 1,500,000 threshold. [AdE3/E §§4,9](https://def.finanze.it/DocTribFrontend/getPrassiDetail.do?id=%7B94E7FE33-0385-403D-8228-BE658CC58749%7D&primoPiano=true).

The ordinary death declaration is due within 12 months of opening of succession, subject to the specific later-start events for representatives/trustees, inventories, authorizations and other art.31 cases. The current regime is self-assessment; payment of succession duty is generally due within 90 days after the declaration deadline, not necessarily on the actual early filing date. Filing is generally electronic, with the specified nonresident postal route. Other real-estate duties and valuations must be checked separately. [TUS art.31, reproduced in AdE Circular 3/E](https://def.finanze.it/DocTribFrontend/getPrassiDetail.do?id=%7B94E7FE33-0385-403D-8228-BE658CC58749%7D&primoPiano=true); [TUS arts.27,33,37; AdE Circular 3/E §§2,5](https://def.finanze.it/DocTribFrontend/getPrassiDetail.do?id=%7B94E7FE33-0385-403D-8228-BE658CC58749%7D&primoPiano=true).

D.Lgs.123/2025 originally stated application from 1 January 2026, but its art.205 commencement was expressly postponed to 1 January 2027 by the 2026 conversion text. Do not use that future consolidated code as the controlling 2026 numbering. Parliamentary discussion alone does not enact higher rates; the original speculation and simplified cadastral/FMV valuation formula remain held below. [Converted DL200/2025, art.4(5), Gazette61 of 14-Mar-2026](https://www.gazzettaufficiale.it/do/gazzetta/downloadPdf?dataPubblicazioneGazzetta=20260314&edizione=0&estensione=pdf&numeroGazzetta=61&numeroSupplemento=0&progressivo=0&tipoSerie=SG&tipoSupplemento=GU).


### Belgium

Inheritance taxation is regional: establish Flanders, Wallonia or Brussels jurisdiction; do not extend the Flanders example to the other regions. Flanders direct-line/partner marginal bands are 3% to EUR 50,000, 9% on EUR 50,000.01-250,000, and 27% above EUR 250,000, calculated separately per heir and separately on movable and immovable property. Partner classification includes qualifying legal/factual cohabitants; factual cohabitation normally requires the uninterrupted prior year and shared household. [Flanders government: direct-line/partner tariff](https://www.vlaanderen.be/belastingen-en-begroting/vlaamse-belastingen/erfbelasting/tarieven-in-de-erfbelasting/algemeen-tarief-in-de-erfbelasting).

For Flanders deaths from 1 January 2026, the surviving partner's movable-property foot exemption is EUR 75,000, formerly EUR 50,000. It is unavailable for a direct-line relative or equivalent and cannot transfer unused relief to immovables; excess movable value uses the applicable higher bands. Family-home/business cohabitation tests can require a longer period than the ordinary partner tariff. [Flanders government: partnerabattement](https://www.vlaanderen.be/belastingen-en-begroting/vlaamse-belastingen/erfbelasting/partnerabattement-voor-de-roerende-goederen-in-de-erfbelasting).


### Netherlands

The 2026 inheritance allowance is up to EUR 828,035 for a qualifying partner and EUR 26,230 for a child, stepchild, foster child or grandchild. A disabled child may qualify for EUR 78,671 under the 3-year earnings-capacity and maintenance conditions. Partner status requires the authority's marriage/registered partnership or qualifying cohabitation conditions. Pension/annuity imputation can reduce the partner allowance; the published 2026 minimum is EUR 213,915, not the unreduced headline in every case. [Belastingdienst: 2026 inheritance allowances](https://www.belastingdienst.nl/wps/wcm/connect/nl/erfbelasting/content/vrijstelling-erfbelasting); [Belastingdienst: partner conditions](https://www.belastingdienst.nl/wps/wcm/connect/nl/erfbelasting/content/partners-voor-de-erfbelasting); [Belastingdienst: survivor pension reduction](https://www.belastingdienst.nl/wps/wcm/connect/nl/erfbelasting/content/geen-of-minder-erfbelasting-betalen).

After the available allowance, the 2026 marginal rates to EUR 158,669 and above are 10%/20% for partners and children, 18%/36% for grandchildren and further descendants, and 30%/40% for other recipients. The middle category is not all relatives through the second degree. Aggregate partners where required and establish Dutch jurisdiction before applying these domestic amounts. [Belastingdienst: 2026 inheritance tariffs](https://www.belastingdienst.nl/wps/wcm/connect/nl/erfbelasting/content/tarieven-erfbelasting).


### Japan

The basic deduction is JPY 30,000,000 plus JPY 6,000,000 per statutory heir, with the statutory adopted-heir counting limits. Deduct the applicable debts/funeral/exempt amounts and include required prior gifts before the basic deduction. The 2026 addback ordinarily still uses gifts within the prior 3 years; the extension toward 7 years has its own commencement/transition. Declaration and payment are generally due within 10 months from the day after knowledge of death. [NTA No15001: basic exemption, base and filing](https://www.nta.go.jp/english/taxes/others/02/15001.htm); [NTA No4155: statutory-heir count](https://www.nta.go.jp/taxes/shiraberu/taxanswer/sozoku/4155.htm).

The 10%-55% inheritance schedule is applied to hypothetical statutory shares of the taxable estate to establish total tax, before allocation/adjustments to actual recipients; it is not simply each beneficiary's actual share times a rate. The published 2026 quick table includes its specified deductions. Do not compute the final tax without the statutory-heir and recipient adjustments. [NTA No4155: 2026 rate calculation](https://www.nta.go.jp/taxes/shiraberu/taxanswer/sozoku/4155.htm).

Worldwide versus Japan-only scope depends on the full heir/decedent residence and nationality table. A Japan-address heir is generally unlimited, but a temporary resident receiving from a foreign/nonresident decedent has the stated exception. The temporary-resident definition includes an eligible visa and no more than 10 years of Japan address in the prior 15; it is not a standalone test making everyone with at least 10 of 15 years worldwide taxable. Overseas Japanese and non-Japanese heirs have different prior-10-year/decedent branches. Stop for an unresolved branch rather than using the original shortcut. [NTA No15001: full taxpayer classification table](https://www.nta.go.jp/english/taxes/others/02/15001.htm).


### Denmark

For a 2026 death, spouse/registered partner has no boafgift. The ordinary 15% estate duty for the specified close-family and qualifying cohabitant categories uses the estate allowance DKK 392,300 (2025: DKK 346,000), not one allowance per child. Most other beneficiaries face an additional 25% after the first duty, producing the derived combined 36.25% where both apply. Do not apply that combined rate to the gross estate without the allocation/allowance calculation. [Skattestyrelsen: boafgift table](https://skat.dk/borger/skatter-og-afgifter-ved-doedsfald).

For 2026 gifts in the ordinary covered close-family category, the annual threshold is DKK 80,600 (2025: DKK 76,900) per donor/recipient, with 15% on the excess. Grandparents/stepparents instead have 36.25%; qualifying children's spouses have DKK 28,200 and 15%. Spouse gifts are normally exempt unless separated/divorced; a gift outside the close-family regime can be recipient income, not tax-free simply because gift duty does not apply. Cohabitation and cross-border nexus conditions must be checked. [Skattestyrelsen: 2026 gift thresholds and relationship table](https://skat.dk/borger/gaver-gevinster-og-legater/gaver-saa-meget-maa-du-give).


### Switzerland

No federal inheritance tax applies. All cantons except Obwalden and Schwyz levy inheritance tax; who is exempt and the rates depend on the canton. Spouses/registered partners and descendants are normally exempt, not universally under one federal rule; step/foster children depend on local equivalence. Establish canton/commune, relationship and cross-border treaty position. Named-canton rates and comparative claims are not established by the inheritance page and are held below; the separate gift overview follows. [ch.ch: inheritance tax, scope and cantonal exceptions](https://www.ch.ch/en/family-and-partnership/inheritance/inheritance-tax).

No federal gift tax applies. Most cantons and some communes levy gift tax; the recipient is liable under the cantonal rules. Spouses/registered partners and descendants are normally exempt, with step/foster-child equivalence depending on the canton. Obtain the actual canton/commune deadline, exemption and rate; a general federal absence does not clear a local gift. [ch.ch: gift-tax scope and cantonal exceptions](https://www.ch.ch/de/familie-und-partnerschaft/erbschaft/schenkungssteuer/).


### Other countries

Sweden: the former inheritance/gift statute was repealed from 1 January 2005 by SFS2004:1341; the original phrase abolished 2004 describes the legislative year, not that stated effective date. Current Income Tax Act chapter8 §2 exempts acquisitions by inheritance, will, gift or property division, with the stated property-transfer exception. Later income/disposal rules remain separate. [Riksdagen: repealed Act1941:416 metadata](https://data.riksdagen.se/dokument/sfs-1941-416.html); [Income Tax Act1999:1229 ch.8 §2](https://data.riksdagen.se/dokument/sfs-1999-1229.html).

Norway: inheritance tax was abolished for deaths/gifts from 1 January 2014. Older deaths/gifts can retain the earlier liability even if distributed later. Abolition does not remove later gains taxation; continuity of basis is the general rule, with specified property exceptions. [Skatteetaten: inheritance tax abolition and continuity](https://www.skatteetaten.no/en/person/taxes/get-the-taxes-right/gift-and-inheritance/inheritance-tax-is-abolished/).

Austria: inheritance/gift tax ceased from 1 August 2008. Gratuitous real-estate transfers can still attract real-estate transfer tax; specified gifts require reporting. Do not interpret abolition as no tax or no filing on every transfer. [BMF2008 abolition information §1](https://findok.bmf.gv.at/findok/iwg/35/35732/35732.1.pdf); [BMF current gift-reporting guidance](https://www.bmf.gv.at/themen/steuern/steuern-von-a-bis-z/schenkungsmeldung.html).

Czech Republic: the tax authority identifies inheritance/legacy receipts as income-tax exempt generally, not only direct-line inheritance. Lifetime gifts have separate family, household and occasional-gift conditions. Exempt-income notification can still apply; do not infer that exempt receipt means no reporting. The original grouped abolition label is not a sufficient gift analysis. [Finanční správa: exempt income](https://financnisprava.gov.cz/cs/dane/dane/dan-z-prijmu/fyzicke-osoby/ostatni).

Slovakia: Income Tax Act §3(2)(a) excludes qualifying property acquired by inheritance/gift from the income-tax subject matter, but not income subsequently produced or gifts connected with employment/business and the specified health-provider gifts. This does not establish no tax or no fee in every property transaction. The original 2004 abolition date is historical and is not needed to substitute for the current receipt test. [Finančná správa: inheritance/gift receipts and exceptions](https://podpora.financnasprava.sk/327616-Predmetom-dane-z-pr%C3%ADjmov-fyzickej-osoby-FO-nie-je-).

Hungary has inheritance and gift duty; the original abolished-2010 statement is wrong. NAV's January2026 guidance gives general inheritance/gift duty of 18% and residential-property duty of 9%, with vehicle exceptions and the specified jurisdiction rules. Direct-line relatives (including adoption), spouses and siblings have the stated inheritance/gift exemptions. Establish eligibility instead of applying a country-wide zero. [NAV2026 amounts/rates, pp.3-4](https://nav.gov.hu/pfile/file?path=%2Fen%2Ftaxation%2Ftaxinfo%2Famounts-and-rates-of-duties); [NAV2026 family exemptions](https://nav.gov.hu/pfile/file?path=%2Fen%2Ftaxation%2Ftaxinfo%2Famounts-and-rates-of-duties).

Canada: inherited-property cost generally corresponds to the deceased's deemed proceeds, usually fair market value immediately before death. Spouse/common-law partner and farm/woodlot transfers can differ. Reconcile the deceased's final income-tax return and any deemed-disposition tax separately; the original broad no-estate/gift-tax statement is not established solely by this basis page and is held below. [CRA: special transactions, gifts and inheritances](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/tax-return/completing-a-tax-return/personal-income/line-12700-capital-gains/special-rules-other-transactions.html).

New Zealand: estate duty was repealed in 1992 and gift duty abolished for dispositions on or after 1 October 2011. Gifts can still have income-tax/GST, anti-avoidance and social-assistance consequences; absence of gift duty is not a clearance of those issues. [IRD7-Jan-2026 gifting overview](https://www.taxtechnical.ird.govt.nz/overviews/gifting).

Singapore: estate duty was removed for deaths on or after 15 February 2008. The source's remaining asset rules describe older estates; do not apply them as a current estate charge. Its estate page does not by itself establish the original separate gift-tax absence claim. [IRAS: estate duty commencement](https://www.iras.gov.sg/taxes/other-taxes/estate-duty/estate-duty).

Hong Kong: estate duty abolition applies to deaths on or after 11 February 2006; earlier transitional estates have different rules. Current absence of a separate gift tax is not established by this estate-duty source. Property stamp duties and later income/gains questions need their own analysis. [IRD: Revenue(Abolition of Estate Duty)Ordinance2005](https://www.ird.gov.hk/eng/tax/edu.htm).

China: the Beijing planning/natural-resources authority's retained property-inheritance answer says no inheritance tax is payable for the question described, and labels its validity permanent. This is a bounded property FAQ, not proof of every national gift/transfer-tax consequence or the original never-enacted-proposals assertion. Other transaction taxes require their own authority. [Beijing property-inheritance FAQ, main text dated24-Apr-2022](https://ghzrzyw.beijing.gov.cn/qaknowledge/202205/t20220505_2700412.html).

South Africa: estate duty covers worldwide property/deemed property of an ordinarily resident decedent and South African property of a nonresident, after allowed deductions and the ZAR 3,500,000 abatement. Duty is 20% on the first ZAR 30,000,000 dutiable value and 25% above. Donations duty applies to resident donors: 20% up to the cumulative ZAR 30,000,000 of nonexempt donations from 1 March 2018, and 25% above; exemptions must be deducted before that running threshold. The two bases are not interchangeable. [SARS: estate duty scope/base](https://www.sars.gov.za/types-of-tax/estate-duty/); [SARS: donations duty rate and aggregation](https://www.sars.gov.za/types-of-tax/donations-tax/).

Brazil: ITCMD is a state-level death/gift tax. Senate Resolution9/1992 art.1 establishes an 8% maximum, not a universal state rate or verified 1% minimum. Obtain the relevant state's operative schedule, exemption, progressive rules and situs provisions before computing; the original 1%-8% range cannot substitute for them. [Senate Resolution9/1992 arts.1-2](https://legis.senado.leg.br/norma/590017/publicacao?tipoDocumento=RSF&tipoTexto=PUB).

Mexico: the SAT reproduction of LISR art.93(XXII) exempts inheritance/legacy receipts. XXIII distinguishes gifts between spouses or down the direct line, gifts upward subject to the no-onward-transfer condition, and the separate annual limit for other gifts. It does not support the original 10%-of-UMA formula. Check current income-tax disclosure and property-transfer obligations separately; a federal receipt exemption is not a whole-transaction tax clearance. [LISR art.93(XXII)-(XXIII), SAT reproduction](https://wwwmat.sat.gob.mx/articulo/15199/articulo-93).

Argentina: Buenos Aires' 2026 law provides a provincial gratuitous-transfers tax, with relationship-based fixed-plus-marginal schedules. Article47 ranges from 1.603% in the lowest parent/child/spouse band to 9.513% in the highest distant-relative/stranger band, not the original 1.6%-6.4%. Article48 sets separate per-beneficiary minimum amounts; do not apply the percentage to gross property without the Fiscal Code nexus/base/aggregation tests. The claim that every other province has abolished such taxes remains unconfirmed. [Buenos Aires2026 tax law arts.47-48](https://www.arba.gov.ar/archivos/Publicaciones/leyimpositiva2026.pdf).

South Korea: the NTS ordinary inheritance schedule has five progressive rates from 10% to 50%, with fixed deductions, applied after taxable-base deductions rather than to gross property. The ordinary gift schedule also runs 10%-50%; special business/startup rates, generation-skipping surcharges, prior-gift aggregation and recipient deductions require their own eligibility computation. This matrix does not certify all special reliefs on the linked overview. [NTS: inheritance rate section](https://www.nts.go.kr/nts/cm/cntnts/cntntsView.do?cntntsId=7957&mi=6529); [NTS: gift rate section](https://www.nts.go.kr/nts/cm/cntnts/cntntsView.do?cntntsId=7960&mi=6533).

India: for tax years beginning before 1 April 2026, the old Act continues under the repeal/savings rule. Its official gift guidance distinguishes money without consideration whose annual aggregate exceeds INR 50,000 (the whole aggregate, not only the excess) from separate immovable/specified-movable-property tests. Qualifying relatives, marriage of the individual, will/inheritance and the other statutory exclusions must be tested. The relative definition is specific, not every cousin/niece/nephew. For tax years beginning from 1 April 2026, the new section92 and its FinanceAct2026 position must be confirmed before a computation; see the precise hold below. [Income-tax Act1961 s.56(2)(x), official gift guidance](https://www.incometaxindia.gov.in/en/deemed-income-including-gifts-); [Income Tax Department new-Act transition FAQ21](https://www.incometax.gov.in/iec/foportal/help/all-topics/e-filing-services/objective-and-scope-new-act-faq).


### Cross-border

Do not use worldwide residence/local situs as a universal two-line law. US citizenship/domicile, UK LTR/tails, German deemed connections, Japan's heir/decedent table and regional/cantonal rules differ. Real-estate location is an essential connection to test, not a promise that every country/treaty ALWAYS levies tax. For shares, bank accounts, government bonds, private equity, cash and crypto, record the result and statute separately for every taxing country; the US exceptions above illustrate why the former generic situs table cannot be a computation rule.

The current IRS estate/gift treaty index lists Australia, Austria, Canada, Denmark, Finland, France, Germany, Greece, Ireland, Italy, Japan, Netherlands, South Africa, Switzerland and the UK. Canada's estate provisions are in Income Tax Treaty art.XXIX B, not a section2056A protocol. Norway and Sweden are not on that current IRS list; do not claim a current US treaty from the old list. Read the actual treaty's covered taxes/persons, situs, credits and effective dates for the event before applying it. [IRS: estate/gift treaty index](https://www.irs.gov/businesses/small-businesses-self-employed/estate-gift-tax-treaties-international).

HMRC lists IHT treaties with Ireland, South Africa, USA, Netherlands, Sweden and Switzerland; older Estate Duty agreements with France, Italy, India and Pakistan have the stated different scope. Do not assume identical coverage. HMRC unilateral relief requires the same foreign-situated property/tax and is limited by UK tax; third-country/dual-situs cases need the published apportionment and actual evidence. [HMRC: IHT double taxation relief, treaty and unilateral branches](https://www.gov.uk/guidance/inheritance-tax-double-taxation-relief).

Germany's official 1-January-2026 schedule lists inheritance/gift agreements with Denmark, France, Greece, Switzerland and the US. Its Sweden row expressly ends application on 31 December 2023, with removal of inheritance/gift provisions from 1 January 2024. Do not retain Sweden as an operative 2026 inheritance treaty. ErbStG §21 unilateral credit is conditional on qualifying foreign property and assessed/paid nonrefundable foreign tax, the country/time limitations and required evidence. [BMF2026 treaty schedule: inheritance/gift section](https://ao.bundesfinanzministerium.de/lsth/2026/B-Anhaenge/Anhang-12/I/3-Geltende-Abkommen.pdf?__blob=publicationFile&v=4); [ErbStG §21](https://www.gesetze-im-internet.de/erbstg_1974/BJNR109330974.html).

France's convention index published 29 April 2026 covers agreements in force on 1 January 2026. It identifies succession coverage for Algeria, Austria, Bahrain, Belgium, Cameroon, Canada, Italy, Lebanon, Monaco, the US and UK among the original routes. It marks Mauritius and Québec as income/wealth coverage, not succession coverage. Canada is not limited to Québec in this index. The actual treaty, event-date applicability and covered succession/donation tax must still be read before a credit or exemption is claimed. [BOI-ANNX-000306: index and original-country rows](https://bofip.impots.gouv.fr/bofip/2509-PGP.html/identifiant=BOI-ANNX-000306-20260429).

EU Regulation650/2012 does not govern revenue/tax. In participating states it addresses civil succession: ordinary jurisdiction/habitual-residence law, subject to exceptions and a valid nationality-law choice; recognition and the European Certificate of Succession. It does not bind Denmark or Ireland, and did not bind the UK. An EU civil-law choice cannot choose the inheritance-tax country. Obtain succession counsel for the actual forum/exception rather than treat these defaults as will-drafting instructions. [Reg650/2012 art.1; recitals82-83](https://eur-lex.europa.eu/eli/reg/2012/650/oj/eng); [Reg650/2012 arts.4,21-22,69](https://eur-lex.europa.eu/eli/reg/2012/650/oj/eng).

## Worked cases

These are new arithmetic illustrations with assumed eligibility, not live filing conclusions. The original contained no worked cases or case inputs.

### Danish gift: child versus grandparent

Assume a cash gift of DKK 100,000 in 2026, no other gifts from this donor to this recipient during the year, Danish gift-duty jurisdiction established, and no business/special exemption. For a qualifying child, subtract DKK 80,600 and apply 15%: DKK 2,910. For a grandparent recipient, the same ordinary threshold with 36.25% gives DKK 7,032.50. The relationship changes the outcome; neither is a case of treating all family gifts alike. A person outside the covered relationship/cohabitation rules needs an income-tax analysis rather than this computation. [Skattestyrelsen gift thresholds and relationship table](https://skat.dk/borger/gaver-gevinster-og-legater/gaver-saa-meget-maa-du-give).

```oa-check
name: Denmark 2026 gift relationship comparison
inputs:
  gift: 100000
  annual_threshold: 80600
steps:
  - taxable_gift: max(0, gift - annual_threshold)
  - child_tax: taxable_gift * 0.15
  - grandparent_tax: taxable_gift * 0.3625
  - difference: grandparent_tax - child_tax
expected:
  taxable_gift: 19400
  child_tax: 2910
  grandparent_tax: 7032.50
  difference: 4122.50
```

### Dutch inheritance: child versus grandchild

Assume a single Dutch-taxable 2026 net inheritance of EUR 300,000 to one natural child, with the full ordinary allowance available, no partner aggregation, special exemption or credit. The EUR 26,230 allowance leaves EUR 273,770: EUR 158,669 at 10% plus EUR 115,101 at 20% gives EUR 38,887.10. For a grandchild under the same stated facts, the allowance is also EUR 26,230, but 18%/36% gives EUR 69,996.78. The original broad second-degree label would misclassify other relatives. [Belastingdienst allowances](https://www.belastingdienst.nl/wps/wcm/connect/nl/erfbelasting/content/vrijstelling-erfbelasting); [2026 rates](https://www.belastingdienst.nl/wps/wcm/connect/nl/erfbelasting/content/tarieven-erfbelasting).

```oa-check
name: Netherlands 2026 child versus grandchild
inputs:
  net_inheritance: 300000
  allowance: 26230
  first_band_limit: 158669
steps:
  - taxable: max(0, net_inheritance - allowance)
  - first_band: min(taxable, first_band_limit)
  - excess: max(0, taxable - first_band_limit)
  - child_tax: first_band * 0.10 + excess * 0.20
  - grandchild_tax: first_band * 0.18 + excess * 0.36
expected:
  taxable: 273770
  first_band: 158669
  excess: 115101
  child_tax: 38887.10
  grandchild_tax: 69996.78
```

## Output specification

The reviewer brief must include:

1. **Decedent / donor profile** : residence, citizenship, domicile/LTR status, prior gift history
2. **Asset inventory** by situs with valuation methodology and supporting documentation
3. **Beneficiary inventory** with relationship classification per jurisdiction
4. **Exemption / allowance schedule** per applicable jurisdiction
5. **Relief schedule** : Agricultural Property Relief, Business Property Relief, Pacte Dutreil, German Verschonung, US marital deduction
6. **Tax computation** per jurisdiction
7. **Double taxation analysis** : credits available, treaty article references
8. **Filing deadlines and forms** per jurisdiction
9. **Inherited-asset basis analysis** for every beneficiary for whom US income-tax basis is relevant
10. **Reviewer questions** : open items flagged as [T2] or [T3]

For item 9, basis can decrease as well as increase; use the conditional rule above. For item 10, preserve the original [T2]/[T3] reviewer flags and mark held operative matters STOP; no tax result may depend on an unresolved flag. The former IRPH trigger is not an inheritance-tax rule and provides no tax conclusion.

## Completion checklist

- [ ] Domicile / LTR / residence tested per each jurisdiction's specific definition
- [ ] Asset situs determined per each jurisdiction's rules, not assumed by analogy
- [ ] Relationship classification per jurisdiction (Classes I-III in DE; Groups I-IV in ES)
- [ ] Exemptions per jurisdiction applied to net not gross
- [ ] Business property reliefs verified for qualifying conditions (active business, holding period, payroll)
- [ ] Charitable and spousal deductions confirmed
- [ ] Treaty foreign tax credits applied where bilateral treaty exists
- [ ] Filing forms and deadlines per jurisdiction plotted
- [ ] US step-up basis recorded for beneficiary income tax planning
- [ ] Output flags every [T2]/[T3] item for reviewer judgement

Apply each allowance to its own statutory base. The treaty check requires actual covered-tax/person/property eligibility and a supported credit computation; treaty existence alone is insufficient. No checked box may override a Not yet confirmed stop.

## When to refuse or refer

- **Do not** infer a complete transaction-tax exemption from a country's absence of estate tax. Check the deceased's final income-tax position and inherited-asset basis separately; the Canada and Australia limitations below remain STOP items.
- **Do not** apply pre-FA-2025 UK domicile rules to FY 2025/26 cases : long-term residence applies from 6 April 2025.
- **Do not** treat Spanish ISD as eliminated nationally because Madrid has a rebate : regional variation is the rule, not the exception.
- **Do not** apply the ordinary US citizen/domiciliary exclusion to a nonresident noncitizen estate. Establish its USD 60,000 filing test, actual credit and treaty position separately.
- **Do not** apply Pacte Dutreil or German Verschonung without confirming the holding-period and payroll commitments are sustainable post-transmission.

The original refusal topics are preserved with their corrected conditions; their exact former text remains in the original-topic map. Apply the precise US NRA filing and credit rule above. Do not infer Spanish national elimination from a regional quota rebate, or treat the original 2025 US exclusion as a 2026 amount. Refer any unresolved residence/situs, trust, relief qualification, treaty or held country issue before calculating or filing; do not invent a higher-tax answer to substitute for evidence.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Cross-border succession is highly fact-specific and irreversibly affects family wealth. Every output must be reviewed and signed off by credentialed estate planning practitioners in each affected jurisdiction before any return is filed.

## Sources

Read on records actual reading of the stated provision and adjoining qualifications, including retained readings that remain applicable. It does not mean that an entire statute or every linked treaty was read. The 2025 Form 709 instructions support the unchanged procedural and exclusion conditions; the 2026 indexed gift amounts come from Rev. Proc. 2025-32. Most authority pages are scoped guidance, not the complete statute. Treaty rows establish dated index scope only; their individual treaties were not all read. Failed access attempts are not in this read table.

| Source and what was actually read | URL | Read on |
|---|---|---|
| Read for: Form 706 general instructions: resident; Form 706: exclusion by year; Form 706 general instructions: filing; Form 706: gross estate; Form 706: portability relief; Form706 ScheduleR PartI: separate GST allocation; Form 706 Table A; Form 706 Schedule M | https://www.irs.gov/instructions/i706 | 2026-11-17 |
| Read for: IRS gift FAQ: basis | https://www.irs.gov/businesses/small-businesses-self-employed/frequently-asked-questions-on-gift-taxes | 2026-11-16 |
| Read for: IRS NRA estate scope | https://www.irs.gov/businesses/small-businesses-self-employed/estate-tax-for-nonresidents-not-citizens-of-the-united-states | 2026-11-16 |
| Read for: IRS: estate/gift treaty index | https://www.irs.gov/businesses/small-businesses-self-employed/estate-gift-tax-treaties-international | 2026-11-16 |
| Read for: IRS gifts/inheritances basis FAQ | https://www.irs.gov/faqs/interest-dividends-other-types-of-income/gifts-inheritances/gifts-inheritances | 2026-11-16 |
| Read for: HMRC IHT overview | https://www.gov.uk/inheritance-tax | 2026-11-16 |
| Read for: HMRC Agricultural Relief: 6-Apr-2026 rules; HMRC Agricultural Relief: allocation and transfer | https://www.gov.uk/guidance/agricultural-relief-on-inheritance-tax | 2026-11-16 |
| Read for: HMRC Business Relief: eligibility; HMRC Business Relief: allowance | https://www.gov.uk/business-relief-inheritance-tax/what-qualifies-for-business-relief | 2026-11-16 |
| Read for: HMRC paying IHT | https://www.gov.uk/paying-inheritance-tax | 2026-11-16 |
| Read for: ErbStG §§2,15; ErbStG §§14,16; ErbStG §19(1)-(3); ErbStG §13a; ErbStG §13b; ErbStG §13a(3): payroll; ErbStG §13a(10); ErbStG §30; ErbStG §31; ErbStG §21 | https://www.gesetze-im-internet.de/erbstg_1974/BJNR109330974.html | 2026-11-16 |
| Read for: DGFiP gifts: allowances and aggregation; DGFiP gifts: grandchildren | https://www.impots.gouv.fr/particulier/calcul-et-paiement-des-droits | 2026-11-16 |
| Read for: DGFiP: death calculation; DGFiP: death exemptions; CGI art.777; DGFiP death calculation; DGFiP death: disability | https://www.impots.gouv.fr/particulier/questions/comment-dois-je-calculer-les-droits-de-succession | 2026-11-17 |
| Read for: Ley 29/1987 arts.20-22; Ley 29/1987 art.24; Ley 29/1987 art.20(2),(5); Ley29/1987 art.20(2)(a): disability; Ley 29/1987 art.21; Ley 29/1987 art.22; Ley29/1987 art.21: top tariff boundary; Ley 29/1987 art.20(2)(c),(6); Ley 29/1987 art.20(2)(c) | https://www.boe.es/buscar/act.php?id=BOE-A-1987-28141 | 2026-11-17 |
| Read for: Belastingdienst: 2026 inheritance allowances | https://www.belastingdienst.nl/wps/wcm/connect/nl/erfbelasting/content/vrijstelling-erfbelasting | 2026-11-16 |
| Read for: Belastingdienst: 2026 inheritance tariffs | https://www.belastingdienst.nl/wps/wcm/connect/nl/erfbelasting/content/tarieven-erfbelasting | 2026-11-17 |
| Read for: Belastingdienst: partner conditions | https://www.belastingdienst.nl/wps/wcm/connect/nl/erfbelasting/content/partners-voor-de-erfbelasting | 2026-11-16 |
| Read for: Skattestyrelsen: 2026 gift thresholds and relationship table; Skattestyrelsen: recipient class | https://skat.dk/borger/gaver-gevinster-og-legater/gaver-saa-meget-maa-du-give | 2026-11-17 |
| Read for: NTA No15001: basic exemption, base and filing; NTA No15001: full taxpayer classification table | https://www.nta.go.jp/english/taxes/others/02/15001.htm | 2026-11-16 |
| Read for: ch.ch: inheritance tax, scope and cantonal exceptions; rendered official web body, raw HTML is a shell | https://www.ch.ch/en/family-and-partnership/inheritance/inheritance-tax | 2026-11-17 |
| Read for: Flanders government: direct-line/partner tariff | https://www.vlaanderen.be/belastingen-en-begroting/vlaamse-belastingen/erfbelasting/tarieven-in-de-erfbelasting/algemeen-tarief-in-de-erfbelasting | 2026-11-17 |
| Read for: Flanders government: partnerabattement | https://www.vlaanderen.be/belastingen-en-begroting/vlaamse-belastingen/erfbelasting/partnerabattement-voor-de-roerende-goederen-in-de-erfbelasting | 2026-11-17 |
| Read for: Skattestyrelsen: boafgift table; Skattestyrelsen: additional duty | https://skat.dk/borger/skatter-og-afgifter-ved-doedsfald | 2026-11-17 |
| Read for: SARS: estate duty scope/base | https://www.sars.gov.za/types-of-tax/estate-duty/ | 2026-11-17 |
| Read for: SARS: donations duty rate and aggregation | https://www.sars.gov.za/types-of-tax/donations-tax/ | 2026-11-17 |
| Read for: CRA: special transactions, gifts and inheritances | https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/tax-return/completing-a-tax-return/personal-income/line-12700-capital-gains/special-rules-other-transactions.html | 2026-11-17 |
| Read for: Skatteetaten: inheritance tax abolition and continuity | https://www.skatteetaten.no/en/person/taxes/get-the-taxes-right/gift-and-inheritance/inheritance-tax-is-abolished/ | 2026-11-17 |
| Read for: BMF2008 abolition information §1 | https://findok.bmf.gv.at/findok/iwg/35/35732/35732.1.pdf | 2026-11-17 |
| Read for: IRD7-Jan-2026 gifting overview | https://www.taxtechnical.ird.govt.nz/overviews/gifting | 2026-11-17 |
| Read for: IRAS: estate duty commencement | https://www.iras.gov.sg/taxes/other-taxes/estate-duty/estate-duty | 2026-11-17 |
| Read for: IRD: Revenue(Abolition of Estate Duty)Ordinance2005 | https://www.ird.gov.hk/eng/tax/edu.htm | 2026-11-17 |
| Read for: HMRC: long-term UK residence; HMRC LTR: transition and trusts; HMRC LTR: restricted trust protection | https://www.gov.uk/guidance/inheritance-tax-if-youre-a-long-term-uk-resident | 2026-11-16 |
| Read for: HMRC gifts: seven-year rule | https://www.gov.uk/inheritance-tax/gifts | 2026-11-17 |
| Read for: HMRC outside-UK death scope | https://www.gov.uk/inheritance-tax/when-someone-living-outside-the-uk-dies | 2026-11-16 |
| Read for: HMRC: check type of estate | https://www.gov.uk/valuing-estate-of-someone-who-died/check-type-of-estate | 2026-11-16 |
| Read for: HMRC: IHT double taxation relief, treaty and unilateral branches | https://www.gov.uk/guidance/inheritance-tax-double-taxation-relief | 2026-11-16 |
| Read for: NAV2026 amounts/rates, pp.3-4; NAV2026 family exemptions | https://nav.gov.hu/pfile/file?path=%2Fen%2Ftaxation%2Ftaxinfo%2Famounts-and-rates-of-duties | 2026-11-17 |
| Read for: Finanční správa: exempt income | https://financnisprava.gov.cz/cs/dane/dane/dan-z-prijmu/fyzicke-osoby/ostatni | 2026-11-17 |
| Read for: Finančná správa: inheritance/gift receipts and exceptions | https://podpora.financnasprava.sk/327616-Predmetom-dane-z-pr%C3%ADjmov-fyzickej-osoby-FO-nie-je- | 2026-11-17 |
| Read for: LISR art.93(XXII)-(XXIII), SAT reproduction; LISR art.93(XXIII)(b): upward gifts | https://wwwmat.sat.gob.mx/articulo/15199/articulo-93 | 2026-11-17 |
| Read for: Beijing property-inheritance FAQ, main text dated24-Apr-2022 | https://ghzrzyw.beijing.gov.cn/qaknowledge/202205/t20220505_2700412.html | 2026-11-17 |
| Read for: Form 706-NA Part IV line 7; Form 706-NA Part V: stock; Form 706-NA Part V: expatriates; Form 706-NA Part V: deposits; Form 706-NA Part V: debt; Form 706-NA Part V: insurance; Form 706-NA Part II line 7; Form 706-NA Part IV | https://www.irs.gov/instructions/i706na | 2026-11-17 |
| Read for: Form 709: DSUE; Form 709: rates; Form 709: educational and medical exclusions; Form 709: when to file | https://www.irs.gov/instructions/i709 | 2026-11-17 |
| Read for: HMRC RNRB: taper | https://www.gov.uk/guidance/inheritance-tax-residence-nil-rate-band | 2026-11-17 |
| Read for: IHTM22042: quick succession relief | https://www.gov.uk/hmrc-internal-manuals/inheritance-tax-manual/ihtm22042 | 2026-11-17 |
| Read for: RD 1629/1991 arts.67-68 | https://www.boe.es/buscar/act.php?id=BOE-A-1991-27678 | 2026-11-17 |
| Read for: Reg650/2012 art.1; recitals82-83; Reg650/2012 arts.4,21-22,69 | https://eur-lex.europa.eu/eli/reg/2012/650/oj/eng | 2026-11-17 |
| Read for: NTA No4155: statutory-heir count; NTA No4155: 2026 rate calculation | https://www.nta.go.jp/taxes/shiraberu/taxanswer/sozoku/4155.htm | 2026-11-17 |
| Read for: BOI-ENR-DMTG-10-20-40-10 §§1-60,70-210; BOI-ENR-DMTG-10-20-40-10 §180: thresholds; BOI-ENR-DMTG-10-20-40-10 §§270-395; BOI-ENR-DMTG-10-20-40-10 §330; BOI-ENR-DMTG-10-20-40-10 §380: direction; BOI-ENR-DMTG-10-20-40-10 §§400-500; BOI-ENR-DMTG-10-20-40-10 §490: exclusive allocation | https://bofip.impots.gouv.fr/bofip/6509-PGP.html/identifiant=BOI-ENR-DMTG-10-20-40-10-20260810 | 2026-11-17 |
| Read for: Buenos Aires2026 tax law arts.47-48; Buenos Aires2026 art.47: highest stranger marginal rate | https://www.arba.gov.ar/archivos/Publicaciones/leyimpositiva2026.pdf | 2026-11-17 |
| Read for: NTS: inheritance rate section | https://www.nts.go.kr/nts/cm/cntnts/cntntsView.do?cntntsId=7957&mi=6529 | 2026-11-17 |
| Read for: Converted DL200/2025, art.4(5), Gazette61 of 14-Mar-2026 | https://www.gazzettaufficiale.it/do/gazzetta/downloadPdf?dataPubblicazioneGazzetta=20260314&edizione=0&estensione=pdf&numeroGazzetta=61&numeroSupplemento=0&progressivo=0&tipoSerie=SG&tipoSupplemento=GU | 2026-11-17 |
| Read for: Madrid: beneficios fiscales, close-family rebate | https://www.comunidad.madrid/atencion-contribuyente/beneficios-fiscales | 2026-11-17 |
| Read for: Murcia: inheritance FAQ 21-24 | https://agenciatributaria.carm.es/sucesiones?inheritRedirect=true | 2026-11-17 |
| Read for: ATC: death-quota rebates, points 1-6 | https://atc.gencat.cat/es/tributs/isd/herencies/bonificacio/ | 2026-11-17 |
| Read for: ATRIGA 2026, DL 1/2011 art.6(2),(5) | https://www.atriga.gal/documents/20632401/21043974/BeneficiosFiscales-Sucesiones-es-01-01-2026.pdf/1b2c418f-b912-4439-9698-41aa782a002c | 2026-11-17 |
| Read for: BMF current gift-reporting guidance | https://www.bmf.gv.at/themen/steuern/steuern-von-a-bis-z/schenkungsmeldung.html | 2026-11-17 |
| Read for: Riksdagen: repealed Act1941:416 metadata | https://data.riksdagen.se/dokument/sfs-1941-416.html | 2026-11-17 |
| Read for: Income Tax Act1999:1229 ch.8 §2 | https://data.riksdagen.se/dokument/sfs-1999-1229.html | 2026-11-17 |
| Read for: Senate Resolution9/1992 arts.1-2 | https://legis.senado.leg.br/norma/590017/publicacao?tipoDocumento=RSF&tipoTexto=PUB | 2026-11-17 |
| Read for: AdE Circular 3/E, 16-Apr-2025 §4; TUS arts.7,56; AdE Circular 3/E §9: commencement; TUS art.7: qualifying disability; TUS art.31, reproduced in AdE Circular 3/E; TUS arts.27,33,37; AdE Circular 3/E §§2,5; native official embedded XML/CDATA reconstructed without executing scripts | https://def.finanze.it/DocTribFrontend/getPrassiDetail.do?id=%7B94E7FE33-0385-403D-8228-BE658CC58749%7D&primoPiano=true | 2026-11-17 |
| Read for: DGFiP: succession payment | https://www.impots.gouv.fr/particulier/questions/comment-puis-je-payer-les-droits-de-succession | 2026-11-17 |
| Read for: BMF2026 treaty schedule: inheritance/gift section | https://ao.bundesfinanzministerium.de/lsth/2026/B-Anhaenge/Anhang-12/I/3-Geltende-Abkommen.pdf?__blob=publicationFile&v=4 | 2026-11-17 |
| Read for: Belastingdienst: survivor pension reduction | https://www.belastingdienst.nl/wps/wcm/connect/nl/erfbelasting/content/geen-of-minder-erfbelasting-betalen | 2026-11-17 |
| Read for: IHTM47030: spouse exemption | https://www.gov.uk/hmrc-internal-manuals/inheritance-tax-manual/ihtm47030 | 2026-11-17 |
| Read for: DGFiP: death declaration deadlines | https://www.impots.gouv.fr/particulier/questions/quand-dois-je-deposer-les-declarations-de-revenu-et-de-succession-en-cas-de | 2026-11-17 |
| Read for: Cantabria DL 62/2008 art.8 | https://boe.es/buscar/act.php?id=BOCT-c-2008-90028&p=20260430&tn=0 | 2026-11-17 |
| Read for: NTS: gift rate section | https://www.nts.go.kr/nts/cm/cntnts/cntntsView.do?cntntsId=7960&mi=6533 | 2026-11-17 |
| Read for: BOI-ANNX-000306: index and original-country rows | https://bofip.impots.gouv.fr/bofip/2509-PGP.html/identifiant=BOI-ANNX-000306-20260429 | 2026-11-17 |
| Read for: HMRC threshold table; HMRC RNRB threshold table | https://www.gov.uk/government/publications/rates-and-allowances-inheritance-tax-thresholds-and-interest-rates/inheritance-tax-thresholds-and-interest-rates | 2026-11-17 |
| Read for: Andalucía Ley 5/2021 arts.26,39-40 | https://www.boe.es/eli/es-an/l/2021/10/20/5/con | 2026-11-17 |
| Read for: HMRC trusts and IHT | https://www.gov.uk/trusts-taxes/trusts-and-inheritance-tax | 2026-11-17 |
| Read for: Rev. Proc. 2025-32 §2.14; Rev.Proc.2025-32 §2.14: GST; Rev. Proc. 2025-32 §4.42; retained14-Nov download, actual16-Nov scoped reading | https://www.irs.gov/irb/2025-45_IRB | 2026-11-17 |
| Read for: ch.ch: gift-tax scope and cantonal exceptions | https://www.ch.ch/de/familie-und-partnerschaft/erbschaft/schenkungssteuer/ | 2026-11-17 |
| Read for: Income-tax Act1961 s.56(2)(x), official gift guidance | https://www.incometaxindia.gov.in/en/deemed-income-including-gifts- | 2026-11-17 |
| Read for: Income Tax Department new-Act transition FAQ21 | https://www.incometax.gov.in/iec/foportal/help/all-topics/e-filing-services/objective-and-scope-new-act-faq | 2026-11-17 |

Not yet confirmed: the following specifically held legacy claims and every unresolved case-specific nexus, base, relief, treaty, return or payment condition. All entries below are NONUSABLE; they are retained to prevent topic loss, not offered as alternative guidance. No whole-country absence of tax is inferred from an unread source or an index.

**H01 Unlocated German ruling.** Original claim retained for review: Bundesfinanzhof July 2024 ruling on business property relief constitutionality; BFH 27 May 2024: confirmed need for partial restriction on company-size grounds; transitional rules pending. **STOP:** No identified official judgment was supplied or located in the retained preparation. These incompatible date/holding claims are not authority. Apply the actual §§13a/13b conditions above; do not assert a pending transition.

**H02 Spanish succession agreements.** Original claim retained for review: Family operations: pacto sucesorio (heredamientos) in Cataluña and Balearic Islands receives favorable treatment. **STOP:** Art.24 establishes a taxable-event route, not blanket favorable treatment. The relevant civil agreement, regional tax law and any income-tax interaction have not been fully read for a specific case; STOP this relief.

**H03 Italian valuation and proposals.** Original claim retained for review: Asset-by-asset valuation with cadastral values for real estate; FMV for movable; Periodic parliamentary discussion of rate increases / threshold reductions. **STOP:** The original categorical valuation formula and unspecified proposed increases were not established by the operative reform passages read. Obtain the specific asset valuation rule; no proposal is treated as enacted.

**H04 Swiss gifts and named cantons.** Original claim retained for review: Cantonal/municipal tax; no federal IHT/gift tax. Schaffhausen, Lucerne historically high; Schwyz, Obwalden, Nidwalden no IHT for direct line. **STOP:** The actual inheritance page confirms the federal inheritance-tax absence and Obwalden/Schwyz exceptions, not all gift regimes or the comparative Schaffhausen/Lucerne/Nidwalden claims. The separate gift overview establishes federal absence and ordinary cantonal scope, but current named-canton rates and the Schaffhausen/Lucerne comparison remain nonusable until read.

**H05 Australia.** Original claim retained for review: No federal IHT/estate tax. Capital gains tax may apply on death depending on asset; small business CGT concessions. **STOP:** Ordinary ATO beneficiary/estate pages and the official content endpoint returned403; ordinary browser navigation failed internally, not because a legal passage was read. Preserve the topic, but do not use these claims or a concession until the applicable official body and conditions are available.

**H06 Canada broad absence claim.** Original claim retained for review: No estate/gift tax. Deemed disposition at FMV on death triggers capital gains tax on terminal T1. **STOP:** The actually read CRA page confirms ordinary deemed-proceeds/inherited-basis interaction and exceptions. It does not establish a complete federal/provincial no-estate/gift-tax opinion or clear the final-return calculation. Use the bounded basis rule above; obtain the applicable final-return provisions before computing tax.

**H07 Singapore and Hong Kong gift absence.** Original claim retained for review: Singapore: No estate/gift tax. Hong Kong: No estate/gift tax. **STOP:** The official sources read establish estate-duty abolition for the specified death dates only. Their separate blanket gift-tax absence claims remain unconfirmed and cannot support a gift calculation.

**H08 UAE.** Original claim retained for review: No estate/gift tax. **STOP:** The retained official portal material does not establish this absence. Do not infer absence from silence or personal-income-tax treatment; current transfer and property-registration consequences remain unconfirmed.

**H09 India.** Original claim retained for review: No central IHT. Gift tax abolished 1998. Gifts > INR 50k generally treated as recipient's taxable income unless exempt category (relatives, marriage, will, inheritance). **STOP:** Ordinary HTTP routes returned403, but the official web reader subsequently supplied the old-Act gift body, full two-page section92 text and new-Act commencement FAQ. The readable pre-FinanceAct2026 section92 also contains the INR 50,000 aggregate rule and relative/marriage/will/inheritance exclusions. However, the current as-amended-by-FinanceAct2026 Act and FinanceAct2026 bodies returned403. STOP the new-Act tax-year2026-27 computation until that current amendment position is read; do not cite the old s.56 as its operative section. The categorical no-central-IHT and1998 abolition claims were not established by those income-tax passages and remain nonusable.

**H10 China national history.** Original claim retained for review: Periodic IHT proposals; never enacted. **STOP:** A bounded Beijing property FAQ does not prove this universal national historical/current claim. Do not infer all transfer-tax or gift consequences from that FAQ; the categorical assertion is nonusable.

**H11 Brazil minimum and state schedule.** Original claim retained for review: State-level ITCMD: 1-8% (varies by state) on death and inter-vivos gifts. **STOP:** The official Senate text confirms the8% ceiling. The1% minimum and actual state schedule/2026 progression/exemption/nexus must be read for the selected state before any calculation; do not use the old range as a rate card.

**H12 Argentina other provinces.** Original claim retained for review: Provincial IHT in Buenos Aires only (1.6-6.4%); other provinces have abolished. **STOP:** The actual2026 Buenos Aires law corrects its schedule above. No complete current all-other-province absence/abolition review was performed; that word only and the universal abolition assertion are nonusable.

**H13 Obsolete UK small-estate shortcuts.** Original claim retained for review: Form IHT205: smaller estates. Form C5: for Scotland confirmation. **STOP:** These original blanket routes are not established as current2026 instructions by the reporting page read. Do not select them from estate size alone; establish the current death-date/jurisdiction-specific excepted-estate/probate route.

**H14 US historical modified regime.** Original claim retained for review: Some carryover basis rules apply where modified estate tax regime elected. **STOP:** This unqualified original statement does not identify the historical year/election. It is not an available general2026 estate-tax election; do not apply it without the actual historical statute and event year.

**H15 Unverified default charitable or special-relief entitlement.** Original claim retained for review: Unlimited charitable deduction for qualified §501(c)(3) recipients; unlimited charitable exemption; quick succession relief tapered for transfers within5years. **STOP:** Eligible-recipient, property and actual relief-calculation conditions must be established under the relevant country provision. The matrix does not certify every charity or supply a QSR percentage schedule. Do not calculate these deductions/reliefs merely from those original labels.

**H16 Slovak abolition history.** Original claim retained for review: IHT abolished (Slovakia2004). **STOP:** The current receipt/exceptions source above was read; the specific historical abolition commencement was not independently established. The date is retained here, not used as current tax analysis.
