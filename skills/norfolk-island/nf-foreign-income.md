---
name: nf-foreign-income
description: >
  Establish selected Norfolk Island foreign-income inclusion and foreign
  income tax offsets for 2026-27. Use for overseas interest, dividends,
  employment, rent, foreign gains, tax paid later, currency conversion and
  double-tax relief. Covers temporary-resident and foreign-service gates,
  eligible foreign tax, income matching, the ordinary offset limit and
  A$1,000 floor, non-refundable use, amendments and records. Includes current
  primary legislation, authority guidance and fictional components. Requires
  separate residence, income character, treaty, payment and translation
  evidence. Preserves applicable workflow outputs and holds specialised
  entity, minimum-tax and actual-return computations. This source-cited
  reference does not complete the cross-border or country pack.
jurisdiction: NF
category: international
tax_year: 2026
tax_year_notes: "Ordinary 1 July 2026 to 30 June 2027 income year; sources checked 18 October 2026; foreign income, foreign-tax payment and assessment years may differ; 2026 ATO return examples concern 2025-26"
tier: 2
last_updated: 2026-10-18
version: 0.1
review_status: pending_review
depends_on:
  - workflow-base
  - cross-border-workflow-base
  - nf-tax-system
  - nf-income-tax
  - nf-medicare
  - nf-company-tax
  - nf-cgt
  - nf-investment-withholding
---

# Norfolk Island: foreign income and foreign income tax offsets

Establish the person or entity, residence and temporary-residence history,
income character and source, Australian and foreign periods, gross income,
deductions, foreign-tax liability and payment, treaty conditions and
translation method. Record reviewer-held evidence readiness. Do not query
private client, identity, bank or ownership records through this reference.

Load `workflow-base`, `nf-tax-system`, `cross-border-workflow-base` and the
individual or corporate income-tax workflow base and country references
appropriate to the case. Preserve source and period gates, the confirmed
profile, refusals, four universal outputs, the cross-border compliance map
and every applicable domain output and check. Mandatory facts remain
Needs Input; unresolved law remains held. A preliminary receipt register
does not establish an assessable amount, credit or completed return.

## Territory, period and current source chain

The 1936 Assessment Act adopts the 1997 Act's geographical meaning of
Australia, which expressly includes **Norfolk Island**. A mainland/island
payment or an overseas account alone does not establish a foreign source,
foreign residence or eligible foreign tax. Use actual source and residence
tests. [ITAA36, section 6][ITAA36]; [DICT, section 960-505][DICT]

The latest published 1997 Act compilation checked was **C267,
27 August–30 September 2026**. Its live versions page identifies the
unincorporated October Acts 71 and 86. Their targets were checked against
the selected Division 770, Subdivision 768-R and section 960-50 provisions;
the selected wording is used with that amendment check, not a claim that
C267 alone is all-law current. The 1936 Act source is C193, effective
**1 October 2026**. [ACT-RECORD]; [ACT-VERSIONS]; [REFORM2]; [OCTOBER]; [ITAA36]

The current translation regulations are C16, effective **27 June 2026**.
The ATO's **2026** foreign-offset guidance was checked directly, including
its **30 May 2026** eligibility, limit, payment and recordkeeping pages.
Its return links and worked tax examples relate to **2025–26**; they do
not supply a 2026–27 personal rate table. Use `nf-income-tax`,
`nf-company-tax` and `nf-medicare` for their selected current components.
[REGS-RECORD]; [REGS]; [ATO-ELIGIBILITY]; [ATO-LIMIT]; [ATO-WHEN]; [ATO-RECORDS]

## Establish assessable income before relief

Sections 6-5 and 6-10 generally include a resident's ordinary and statutory
income from all sources; their foreign-resident branches have different
source and statutory-inclusion conditions. Section 6-15 separately
excludes exempt and non-assessable non-exempt (NANE) amounts. A foreign
currency, foreign payer, remittance or account label is not the legal
classification. [CORE]

| Lead | Required classification and hold |
|---|---|
| Foreign interest, dividend or rental receipt | Establish residence/temporary residence, source, gross amount, deductions and translation. Test foreign tax separately. An underlying company's profits tax is not automatically tax paid on a shareholder's dividend. [CORE]; [FITO]; [ATO-WHEN] |
| Overseas salary or service income | Establish employment/service character and period, temporary-resident exceptions and any foreign-service exemption before inclusion or credit. The absence of Australian withholding does not establish an exemption. [TEMP]; [ITAA36] |
| Foreign asset disposal | Apply the relevant CGT event, proceeds, bases, losses and discount first using `nf-cgt`. Only the eligible proportion of foreign tax on an amount actually included can count. [FITO]; [ATO-WHEN] |
| Company foreign branch, equity distribution or attributed income | Establish the relevant exemption, participation, attribution and gross-up rules separately. A company does not claim every foreign tax shown in a group account. Actual corporate branch, CFC and special distribution calculations remain held here. [FITO]; [ATO-WHEN] |
| Foreign pension, trust, joint receipt or mixed transfer | Establish the actual taxpayer, character and statutory/treaty treatment. Do not infer a pension deduction, trust entitlement, income, gift or loan from its label. [CORE]; [FITO]; [ATO-WHEN] |

### Temporary residents

The section 995-1 definition requires a temporary visa and the specified
**Social Security Act** non-residence conditions for both the person and
their spouse, with an additional prior-status exclusion. Those tests are
distinct from income-tax residence. A visa, foreign passport or intended
short stay alone does not establish eligibility. [DICT]

Section **768-910** generally makes a temporary resident's foreign-source
ordinary and statutory income NANE, with separate derivation timing for
statutory income. Its exceptions include remuneration for employment or
services undertaken while temporary resident, related statutory income
and Division 86 amounts. The exception removes this particular NANE
treatment; it does not decide whether another provision supplies relief.
Net capital gains use the separate section **768-915** test and ESS
exception, rather than being treated as ordinary foreign interest.
[TEMP]

Residence changes, market-value/acquisition adjustments under sections
768-950–768-955, ESS, CFC and trust modifications have their own conditions.
Keep actual eligibility and values held until those facts and source
requirements are satisfied. Foreign tax on an ordinary NANE amount does
not gain an offset merely because it was paid overseas. [TEMP]; [FITO]

### Foreign service

Section **23AG** is a conditional exemption for a resident natural person
engaged in foreign service for a continuous period of **at least 91 days**.
The service must also be directly attributable to a listed activity:
specified development assistance, qualifying funds/institutions,
disciplined-force deployment or a prescribed activity. The development
assistance limb excludes an Australian government-agency employer.
Employer or project labels alone do not establish these conditions.
[ITAA36, subsections 23AG(1)–(1AA)][ITAA36]

Read subsection (2)'s exclusions where foreign exemption arises only from
specified treaty, general employment/personal-services exemption,
absence-of-tax or immunity provisions. Do not replace that test with a
rule that foreign tax must always have been paid. Death, permitted leave,
illness and continuity across service periods have separate conditions;
the total-absence test in subsection (6A) uses **one-sixth** of total
foreign service. [ITAA36]

Exempt foreign earnings can affect tax on other income under subsections
(3)–(4). This guide does not compute that formula or select actual exemption
or return entries. Approved-project section 23AF, treaties, foreign law and
actual service-day determinations require their own source work. Exempt
foreign employment income generally supplies no FITO. [ITAA36]; [FITO];
[ATO-WHEN]

## Which foreign tax counts

Section **770-10** generally requires foreign income tax paid in respect
of an amount included in assessable income for the Australian year.
Section **770-15** requires tax imposed by a non-Australian law on income,
profits or gains, or another tax covered by an applicable agreement.
The foreign law and treaty/allocation agreement must correctly impose it;
excess foreign withholding is not automatically creditable in Australia.
Actual foreign refund procedures and treaty entitlement remain separate.
[FITO]; [ATO-WHEN]

Keep these gates distinct:

1. **Payment:** liability or an unpaid assessment alone is insufficient.
   Establish actual payment or a qualifying deemed payment. Section 770-130
   covers specified payments by another entity; a certificate, joint payment
   or trust distribution still needs the right taxpayer and income link.
   [FITO]; [ATO-WHEN]
2. **Income matching:** only the relevant eligible share counts. A partly
   included gain, discount or capital-loss offset can reduce that share;
   an overall net capital loss can leave no included gain and no offset.
   Do not automatically apply the same net-gain rule to gross business
   income or a deferred non-commercial loss. [FITO]; [ATO-WHEN]
3. **Refund/benefit:** section 770-140 treats tax as not paid to the extent
   the taxpayer **or another entity becomes entitled** to a refund or the
   specified tax-linked benefit. Do not wait automatically for cash refund
   receipt. [FITO]
4. **Exempt/NANE income:** generally no offset, with the particular
   section 23AI/23AK exception in subsection 770-10(2). It is not an
   exception for every NANE dividend or temporary-resident receipt. [FITO]
5. **Other exclusions:** the residence-based foreign-tax exception in
   subsection 770-10(3), credit-absorption/unitary taxes and foreign
   IIR/UTPR taxes require separate attention. Foreign DMT tax has its
   own benefit-reduction and definition rules in sections 770-145–770-150;
   it is not automatically excluded or fully creditable. Actual MNE,
   attributed-income and fund computations remain held. [FITO]

The ATO distinguishes income tax from inheritance, wealth, net-worth,
production taxes, penalties, fines and interest. A foreign authority's
invoice total is therefore not itself the eligible tax amount. Keep gross
income and foreign tax separate; do not report only the net remittance as
assessable income. [ATO-WHEN]

## Ordinary limit and non-refundable use

For an ordinary case without a section 770-80 increase:

1. Sum the foreign tax that **counts** under the eligibility rules. This
   amount can differ from tax paid, assessed, withheld or shown on a
   statement. [FITO, section 770-70][FITO]
2. Work out Australian income tax on the actual taxable income and on the
   statutory counterfactual, **disregarding tax offsets** in both. The
   relevant Medicare levy and surcharge are included in the FITO method.
   [FITO, section 770-75][FITO]; [ATO-LIMIT]
3. For the counterfactual, disregard the assessable amounts on which
   eligible foreign tax was paid **and other foreign-source assessable
   income**. Remove debt deductions attributable to an overseas PE and
   applicable reasonably related **non-debt** deductions. Do not add back
   every foreign-interest expense merely because it relates to foreign
   income. Historical converted losses and special loss rules need their
   own analysis. [FITO]; [ATO-LIMIT]
4. The ordinary offset limit is the **greater of A$1,000 and the difference
   between those two tax amounts**. Reduce the eligible foreign tax to that
   limit where necessary. A particular section 770-80 increase must be
   considered separately if relevant. [FITO]
5. Determine the amount usable after the applicable other offsets and tax
   ordering. FITO is **non-refundable**: unused offset or foreign tax above
   the limit is not carried forward or refunded as a FITO. This does not
   decide a return balance involving withholding or other credits.
   [ATO-LIMIT]; [FITO]

If the intended FITO claim is **A$1,000 or less**, section 770-75 does not
require the full counterfactual working. This also permits choosing that
shorter calculation where eligible foreign tax exceeds A$1,000. It does
not grant a free A$1,000 credit, waive eligibility or make an unused amount
refundable. [FITO, subsection 770-75(2) and note 1][FITO]; [ATO-LIMIT]

## Translate the right amounts at the right times

Section **960-50** generally requires Australian currency, translating
calculation elements before calculating totals. Its table is modified by
regulation **960-50.01**. For the selected ordinary branches:

| Amount | Relevant timing, subject to the applicable rules |
|---|---|
| Ordinary income | Receipt if at or before derivation; otherwise derivation. |
| Statutory income other than the net capital gain | Receipt if at or before the first inclusion requirement; otherwise when that requirement arises. |
| Ordinary deduction within modified item 8 | Payment if at or before deductibility; otherwise when deductible. Bad debts, depreciating assets and other special items have their own rules. |
| Foreign tax payment within residual item 11 | Payment time. Do not automatically reuse the income-date rate. |
| CGT proceeds, cost and other relevant elements | The relevant transaction/event times. Do not simply translate a foreign net gain at one disposal-date rate. |

[DICT, section 960-50][DICT]; [REGS]

Schedule 2 to the regulations provides alternative methods and consistency
requirements. An average-rate period cannot exceed **12 months** and must
reasonably approximate the otherwise applicable rates. Required rates come
from non-associated external sources unless the Commissioner permits the
specified alternative. Daily-rate and financial-report/record methods
have their own conditions. Missing rate evidence does not authorise an
arbitrary annual average. Actual functional-currency, special-accrual,
TOFA, election and forex gain/loss computations remain held. [REGS]

## Years, amendments and records

The offset belongs to the Australian year in which the relevant income is
included, even if eligible foreign tax is paid earlier or later. A later
payment can require amendment of that income year's assessment, rather
than adding a credit to the payment year. [FITO, section 770-10][FITO]

Section **770-190** provides a **four-year** amendment period from a
qualifying payment, increase or reduction event occurring **after the
return was lodged**. It is not a general four-year extension for every
incorrect limit calculation or other tax error. The ordinary amendment
rules and actual notice dates still matter. Do not submit an amendment
through this reference. [FITO]; [ATO-LIMIT]

Record the original-currency gross income/gain, foreign year, tax type and
amount, payment date and whether it is advance, instalment or final tax.
An assessment that does not show payment may need separate payment proof.
Keep the translation method/rates, income matching, eligible-tax and
counterfactual workings, refund/benefit status and reviewer decisions.
The ATO generally requires records for **five years after preparation or
obtaining them, or completion of the relevant transactions/acts, whichever
is later**, with longer retention where the applicable extended review
period requires it. Do not reduce this to five years from lodgment in
every case. Actual offshore notices, extensions and longer asset-specific
retention require separate checks. [ATO-RECORDS]

## Fictional 2026–27 components and checks

These examples assume all eligibility, source, residence and period facts
have been established. Tax amounts used in limit examples are stipulated
results from the separate income-tax working, before offsets and with
the relevant levy/surcharge. They are not calculated whole returns or
actual foreign-country/treaty rates.

| Stipulated facts | Selected result |
|---|---|
| Eligible foreign tax A$800; intended claim at most A$1,000 | The full counterfactual calculation can be omitted. The gross offset cannot exceed **A$800**; remaining Australian tax still limits its use. |
| Eligible foreign tax A$1,500; actual tax A$12,000 and counterfactual tax A$11,500 | Difference **A$500**; ordinary limit **A$1,000**; gross offset **A$1,000**, assuming sufficient remaining tax. A difference-only cap of A$500 is wrong. |
| Eligible foreign tax A$8,000; actual tax A$16,120 and counterfactual tax A$9,720 | Difference and limit **A$6,400**; gross offset **A$6,400**; **A$1,600** above the limit is unavailable as a carried-forward/refunded FITO. |
| Eligible/gross offset A$800; tax available after the applicable earlier offsets A$300 | Use **A$300**; **A$500** is unused. This reference does not compute any prepayment refund or final balance. |
| Foreign tax A$2,000 on a gain; only A$10,000 of the A$20,000 taxed gain is included after the established CGT working | Eligible proportion **A$1,000**. If the included gain is zero, none of that gain's foreign tax counts. Actual loss allocation and discount conditions use `nf-cgt`. |
| Income of 1,000 foreign-currency units at 0.50 units per A$1; foreign tax of 100 units paid later at 0.625 units per A$1 | Gross income **A$2,000**; foreign tax **A$160** before the other eligibility gates. Reusing the income rate would incorrectly give A$200 tax. |
| A$1,200 foreign tax paid; entitlement to a qualifying A$200 refund established | At most **A$1,000** remains before other eligibility/limit tests. Do not wait for the refund to arrive in cash. |
| Qualifying employer/activity and exactly 91 continuous service days, but foreign-law exemption reason unknown | The inclusive duration limb is met; actual section 23AG eligibility remains held. Ninety days ordinarily fails that duration limb; statutory exceptions require their own facts. |
| Temporary visa established, spouse's Social Security Act status unknown | Needs Input on temporary-resident eligibility; do not select NANE treatment or worldwide-income taxation from the visa alone. |
| A$1,200 eligible tax but intended claim only A$1,000 | The optional shorter claim does not require a full limit calculation. It remains subject to eligibility and non-refundable use. |

Review the A$1,000 boundary, eligible-versus-paid distinction, refund
entitlement, actual-versus-counterfactual tax, debt/non-debt deductions,
Australian year, separate FX dates and final usable credit. Preserve
unresolved treaty, foreign-law, special-entity, CFC, hybrid, minimum-tax,
corporate branch/distribution, foreign-pension, full forex, exempt-income
progression and actual filing requirements. Transfer pricing and the
other open cross-border/country slots remain separate work. Neither these
components nor repository checks confer practitioner sign-off or
comprehensive-country acceptance.

[ACT-RECORD]: https://www.legislation.gov.au/C2004A05138/latest/details
[ACT-VERSIONS]: https://www.legislation.gov.au/C2004A05138/latest/versions
[CORE]: https://www.legislation.gov.au/C2004A05138/2026-08-27/2026-08-27/text/original/epub/OEBPS/document_1/document_1.html
[DICT]: https://www.legislation.gov.au/C2004A05138/2026-08-27/2026-08-27/text/original/epub/OEBPS/document_10/document_10.html
[TEMP]: https://www.legislation.gov.au/C2004A05138/2026-08-27/2026-08-27/text/original/epub/OEBPS/document_9/document_9.html
[FITO]: https://www.legislation.gov.au/C2004A05138/2026-08-27/2026-08-27/text/original/epub/OEBPS/document_9/document_9.html
[ITAA36]: https://www.legislation.gov.au/C1936A00027/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_1/document_1.html
[REFORM2]: https://www.legislation.gov.au/C2026A00071/asmade/2026-08-26/text/original/epub/OEBPS/document_1/document_1.html
[OCTOBER]: https://www.legislation.gov.au/C2026A00086/asmade/2026-09-15/text/original/epub/OEBPS/document_1/document_1.html
[REGS-RECORD]: https://www.legislation.gov.au/F2021L00206/latest/details
[REGS]: https://www.legislation.gov.au/F2021L00206/2026-06-27/2026-06-27/text/original/epub/OEBPS/document_1/document_1.html
[ATO-ELIGIBILITY]: https://www.ato.gov.au/forms-and-instructions/foreign-income-tax-offset-rules-guide-2026/eligibility-and-rules-for-the-fito
[ATO-LIMIT]: https://www.ato.gov.au/forms-and-instructions/foreign-income-tax-offset-rules-guide-2026/calculate-your-fito-or-offset-limit
[ATO-WHEN]: https://www.ato.gov.au/forms-and-instructions/foreign-income-tax-offset-rules-guide-2026/when-a-fito-applies
[ATO-RECORDS]: https://www.ato.gov.au/forms-and-instructions/foreign-income-tax-offset-rules-guide-2026/record-keeping-for-fito

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained in the
[ryanduguid/openaccountants fork](https://github.com/ryanduguid/openaccountants).
Check its quality tier, recorded review status and cited sources before use.
Choose a practitioner whose credentials and engagement scope you have verified.
The links below are optional upstream services; they do not publish or verify
this fork's changes.

- Upstream connection service: https://www.openaccountants.com/connect
- Upstream accountant network: https://www.openaccountants.com/network
