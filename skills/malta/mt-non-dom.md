---
name: mt-non-dom
description: "Use this skill for any Malta-resident individual who is not domiciled in Malta. Trigger on \"Malta non-dom\", \"non-domiciled Malta\", \"remittance basis Malta\", \"move to Malta taxes\", \"Malta ordinary resident\", \"foreign income Malta\", \"Malta minimum tax\", \"remit to Malta\", \"Malta global residence\", \"Malta non-dom status\", or any question about whether foreign income is taxed in Malta. Covers non-dom eligibility, remittance basis mechanics, minimum tax obligation, foreign capital gains treatment, and comparison with full resident taxation. ALWAYS load this skill before advising a non-Maltese-domiciled resident on their Malta tax position."
version: 2.1
jurisdiction: MT
tax_year: 2026
last_updated: 2026-11-26
depends_on:
  - malta-income-tax
category: international
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: cross-border
type: situation-rules
---

# Malta non-dom tax: residence, domicile, the remittance basis and the minimum tax

## Scope and who this is for

This skill covers individuals who live in Malta but are **not domiciled** in Malta, or are **not ordinarily resident** here. It explains when foreign income and foreign capital gains are taxed, the €5,000 minimum tax for non-doms, who cannot use the remittance basis, how to evidence what was brought into Malta, the special residence programmes, double tax relief and the filing duties.

- **Basis year 2026 = year of assessment 2027.** This is the primary year. Malta taxes a calendar basis year and charges the tax in the following year of assessment. For ordinary self-assessment the 2026 return is due by 30 June 2027, subject to the filing/notice exceptions below.
- **Basis year 2025 = year of assessment 2026.** See the dated section "2025 income (year of assessment 2026)" for returns being filed now.

The status tests (residence, domicile, ordinary residence, the minimum tax) are applied to the basis year: article 56(27) looks at the individual "during any year preceding the year of assessment".

**Not covered here:** the resident rate tables and deductions (see the Malta income tax Guide), non-resident computations, Maltese property and share disposals (see the Malta capital gains Guide), companies and trusts, and the detail of the residence programmes beyond their tax rate and minimum tax.

## Ask the client first

- Which basis year are we working on: 2026 (year of assessment 2027) or 2025 (year of assessment 2026)?
- Did you live in Malta in that year, apart from temporary absences? When did you arrive, and have you left?
- Where is your domicile: where do you regard as your permanent home, and what evidence supports the domicile of origin acquired at birth? Do you intend to stay in Malta permanently?
- Are you ordinarily resident in Malta, meaning Malta is your settled, habitual home year after year?
- Are you married? If so, is your spouse ordinarily resident **and** domiciled in Malta? Are you taxed jointly (the default) or separately?
- Do you hold the long-term/permanent status defined by S.L. 217.05 or S.L. 460.17? In which year was it granted? Have you applied for such status while in a special programme? Distinguish an MPRP residence-by-investment certificate.
- Are you in any special tax scheme: the Global Residence Programme, the Residence Programme, a Nomad Residence Permit, or another scheme with its own minimum tax?
- How much foreign income arose in the year, by type (salary, dividends, interest, rent, pensions)? How much of it was brought into Malta, and how?
- Did you realise foreign capital gains? Did you sell anything situated in Malta, such as Maltese property or shares in a Maltese company?
- Which accounts hold capital you had before you came to Malta, and which receive foreign income or gains? Are any of them mixed?
- How much foreign tax was paid, and in which country? Is there a tax treaty?
- Have you filed Maltese returns before? Has the Commissioner sent any notice?

## The method, step by step

All steps apply the [Income Tax Act, Cap. 123](https://legislation.mt/eli/cap/123/eng/pdf).

1. **Fix the year.** Work on one basis year at a time. Basis year 2026 is year of assessment 2027.
2. **Decide residence.** Article 2: an individual is "resident in Malta" if he "resides in Malta except for such temporary absences as to the Commissioner may seem reasonable". There is no day count in the Act. MTCA's published practice is that a person present in Malta for more than 183 days in a year is resident for that year ([MTCA, Tax Residence](https://mtca.gov.mt/personal-tax/individual/tax-residence), read 26 November 2026). A non-resident is taxed only on Malta-source income; refer that case.
3. **Decide domicile and ordinary residence.** The Act defines neither term. See "Residence, domicile and ordinary residence" below. Record the facts that support the conclusion.
4. **Check the exclusions.** The remittance basis does **not** apply to a long-term resident or holder of a permanent residence certificate or card, from the year that status was granted, as those statuses are defined by S.L. 217.05/S.L. 460.17, or to anyone whose spouse is ordinarily resident and domiciled in Malta. If an exclusion applies, the person is taxed on worldwide income and gains like any domiciled resident. Stop here and use the Malta income tax Guide.
5. **Split the income.** Malta-source income and gains: within the charge, subject to exemptions, special rates and treaty relief. Foreign income: taxed only on the amount received in Malta (article 4(1) proviso (i)). Foreign capital gains: excluded by proviso (ii), whether brought in or not, once source and capital rather than trading-income character are established.
6. **Measure what was received in Malta.** Trace each transfer into Malta to its source: pre-arrival capital, foreign capital gains, or foreign income. Only foreign income is taxed. Keep the evidence (see "Remittances: what counts and how to prove it").
7. **Compute the tax** on Malta income plus foreign income received in Malta, at the resident rates for the basis year and the person's status. The rate tables are in the Malta income tax Guide.
8. **Test the minimum tax** (article 56(27)). If the person is ordinarily resident, not domiciled, not in a minimum-tax scheme, and has at least €35,000 of foreign income not received or not fully received in Malta, the tax (before double tax relief) must reach €5,000. Tax paid under the Act counts; tax on article 5A property transfers does not. If worldwide tax would be lower, the person can prove it and pay that lower amount. ([ITA art. 56(27)](https://legislation.mt/eli/cap/123/eng/pdf))
9. **Apply double tax relief** on foreign income that is taxed in Malta. For a treaty credit, apply the ordinary two-year claim limit and article 77(10) adjustment exception below; establish the applicable relief first.
10. **File and pay.** For ordinary self-assessment, return and balance are due by 30 June of the year of assessment, subject to any extension. Check any election/notice route under Cap. 372 articles 12/12A and the settlement exception in S.L. 372.16 rule 5(a).

Order matters. Check the exclusions (step 4) before anything else: a non-dom whose spouse is domiciled and ordinarily resident in Malta, or who has long-term resident status, is taxed on everything, and every later step changes.

### Rates, bands and thresholds

| Item | Figure and conditions | Tax year | Source |
|---|---|---|---|
| Remittance basis, Cap. 123 art. 4(1) proviso (i) | foreign income of a person not ordinarily resident or not domiciled in Malta taxed only on "the amount received in Malta" | Current | https://legislation.mt/eli/cap/123/eng/pdf |
| Foreign capital gains, art. 4(1) proviso (ii) | not taxed for such a person, received in Malta or not | Current | https://legislation.mt/eli/cap/123/eng/pdf |
| Non-dom minimum tax, art. 56(27) | EUR 5,000 a year, tax before relief under arts. 76 to 89; tax paid under the Act counts; art. 5A tax does not | YA 2019 onwards, YA 2027 operative text read | https://legislation.mt/eli/cap/123/eng/pdf |
| Minimum tax trigger, art. 56(27)(ii) | at least EUR 35,000 of foreign income "not received or not fully received in Malta"; joint couple: both spouses | same | https://legislation.mt/eli/cap/123/eng/pdf |
| Single table, 2026 income, art. 56(1) | Ordinary single table only where the child/parent sub-tables do not apply: 0% to EUR 12,000; 15% minus EUR 1,800 to EUR 16,000; 25% minus EUR 3,400 to EUR 60,000; 35% minus EUR 9,400 above | YA 2027 | https://legislation.mt/eli/cap/123/eng/pdf |
| Married joint table (no qualifying child), 2026 income, art. 56(1) | 0% to EUR 15,000; 15% minus EUR 2,250 to EUR 23,000; 25% minus EUR 4,550 to EUR 60,000; 35% minus EUR 10,550 above | YA 2027 | https://legislation.mt/eli/cap/123/eng/pdf |
| Residence practice | more than 183 days in a year; ordinary residence possible after about three consecutive years | MTCA practice | https://mtca.gov.mt/personal-tax/individual/tax-residence |
| GRP and Residence Programme, rule 5(1) | 15% on remitted foreign income, minimum EUR 15,000 | Current | https://legislation.mt/eli/sl/123.148/eng/pdf |
| Nomad Residence Permit, rules 2-4 | 10% on eligible main applicant authorised-work chargeable income subject to relief; conditional initial 12-month exemption, written waiver and replacement-permit rules below | Current | https://legislation.mt/eli/sl/123.210/eng/pdf |
| Interest on late tax, Cap. 372 art. 44 | 0.6% per month or part, tax payable on or after 31 Aug 2022 | Current | https://legislation.mt/eli/cap/372/eng/pdf |

### Residence, domicile and ordinary residence

- **Resident.** The Act's only definition: "an individual who resides in Malta except for such temporary absences as to the Commissioner may seem reasonable and not inconsistent with the claim of such individual to be resident in Malta". Article 2 does not set a day count. MTCA guidance states that someone coming to establish residence becomes resident from arrival; do not infer full-year residence solely from arrival. MTCA's Tax Residence page (read 26 November 2026) says a person present in Malta for more than 183 days in a year is resident for that year; that is MTCA practice, not the Act. Arrival and departure years are decided on the facts; refer them.
- **Domicile.** Not defined in the Act. It is a general-law concept, not a tax test. In broad terms, a person keeps the domicile they had at birth (normally the parents’ domicile, as MTCA guidance section 3.3 describes it) until they settle in another country intending to stay there permanently. A residence of long or indefinite duration does not itself establish domicile of choice if the person intends eventually to return to the country of domicile or settle elsewhere (guidance section 3.4). This is background only; a disputed domicile must be referred.
- **Ordinary residence.** Not defined in the Act either. MTCA's guidance (section 2.3, read 26 November 2026): a person living in Malta on a permanent or indefinite basis is ordinarily resident; a person here for a temporary purpose may become so, for example after more than 183 days a year for "say, three consecutive years", or regular visits over about three years with personal and economic ties. In ordinary usage it means Malta is the person's settled, habitual home, year after year, rather than a temporary stay. A newly arrived person may be resident but not yet ordinarily resident. The Act gives no number of years; refer borderline cases.

Why the labels matter (the remittance-basis rows assume no defined-status or spouse exclusion):

| Status in the basis year | Foreign income | Foreign capital gains | €5,000 minimum tax (art. 56(27)) |
| --- | --- | --- | --- |
| Resident, domiciled and ordinarily resident | Taxed as it arises, worldwide | Taxed under art. 5 where chargeable | No |
| Resident, not domiciled, ordinarily resident | Taxed only when received in Malta | Not taxed | Yes, if the other conditions are met |
| Resident, not ordinarily resident (domiciled or not) | Taxed only when received in Malta | Not taxed | No: art. 56(27) needs "ordinarily resident in Malta but not domiciled" |
| Not domiciled, but a long-term resident or permanent-residence holder | Taxed as it arises, from the year the status was granted | Taxed where chargeable | No: the provisos do not apply |
| Not domiciled, spouse ordinarily resident and domiciled in Malta | Taxed as it arises | Taxed where chargeable | No: the provisos do not apply |

### The remittance basis

Article 4(1) charges income "accruing in or derived from Malta or elsewhere, and whether received in Malta or not". Two provisos cut this back:

- **Proviso (i), foreign income:** "in the case of income arising outside Malta to a person who is not ordinarily resident in Malta or not domiciled in Malta, the tax shall be payable on the amount received in Malta".
- **Proviso (ii), foreign capital gains:** "no tax shall be payable on capital gains arising outside Malta to a person who is not ordinarily resident in Malta or not domiciled in Malta".

The two tests are alternatives: **not** ordinarily resident **or** not domiciled. A Maltese-domiciled person who is resident but not ordinarily resident also qualifies.

**Who is excluded** (the "sohowever" provisos to article 4(1)):

- **Long-term residents and permanent residence.** Provisos (i) and (ii) "shall not apply to an individual who is a long-term resident, or who holds a permanent residence certificate or a permanent residence card, in respect of any income derived by such individual in the year of being granted long-term resident status or the right of permanent residence and in subsequent years". The terms take their meaning from the Status of Long-Term Residents (Third Country Nationals) Regulations (S.L. 217.05) and the Free Movement of European Union Nationals and their Family Members Order (S.L. 460.17). The whole year of grant is caught, not just the part after the grant date.
- **Spouse rule.** The provisos "shall not apply to an individual whose spouse is ordinarily resident and domiciled in Malta". Both conditions must be true of the spouse. A non-dom married to another non-dom, or to a Maltese-domiciled spouse who is not ordinarily resident, is not caught.

**What is taxed, for a person on the remittance basis:**

| Item | Treatment |
| --- | --- |
| Malta-source income (employment, rent, business, dividends or interest, once source is established) | Subject to the Act, including any exemption, final/special rate and treaty relief; do not assume all Maltese receipts use ordinary rates |
| Foreign income received in Malta (salary, dividends, interest, rent, pensions) | Taxed at the normal resident rates, on the amount received |
| Foreign income not received in Malta | Not taxed, but counts towards the €35,000 minimum-tax test |
| Foreign capital gains, received in Malta or not, on any capital asset (for example foreign shares or foreign property) | Not taxed (proviso (ii)) |
| Gains on Malta-situated assets (Maltese immovable property, shares in a Maltese company) | Taxed under art. 5 or the art. 5A final tax; see the Malta capital gains Guide |
| Income that a foreign capital gain later produces (interest on the proceeds) | Foreign income: taxed only if received in Malta |

Malta does charge tax on capital gains from securities: article 5(1)(a)(ii) covers "gains or profits arising from the transfer of the ownership or usufruct of ... any securities". Only the remittance-basis proviso takes **foreign** gains out of charge. A domiciled, ordinarily resident person is taxed on chargeable gains wherever they arise.

The ordinary remittance-basis provisos do not require a special residence-programme election. The provisos apply by law when the conditions are met. The return must still show the facts; For a particular return field, form or declaration: Check this point with one of our partner accountants.

### The €5,000 minimum tax for non-doms

Article 56(27) has applied since year of assessment 2019 (with an amendment from year of assessment 2020). It is read for the current 2026 computation. The separate historical 2025 paragraph below does not supply a fresh historical-consolidation audit.

**Who it applies to.** An individual who, in the basis year, meets **all** of these:

1. is "ordinarily resident in Malta but not domiciled in Malta";
2. is a person "to whom provisos (i) and (ii) of article 4(1) apply", so not a long-term resident, not a permanent-residence holder, and not married to a spouse who is ordinarily resident and domiciled in Malta;
3. "is not taxable in accordance with any scheme under the Act effectively establishing a minimum tax payable", so not a Global Residence Programme or Residence Programme beneficiary, for example; and
4. derives foreign income (the income covered by proviso (i)) "amounting to not less than thirty five thousand euro (€35,000)", "which is not received or not fully received in Malta". For a married couple taxed jointly under article 49, the income of both spouses counts.

**What it does.** The person's tax on their income must be "not less than five thousand euro (€5,000) per annum". If the tax on the income chargeable in Malta is lower, the person "shall be deemed to have received in Malta additional income arising outside Malta" so that total tax reaches €5,000. In practice, the shortfall is a top-up, not an extra charge on top of the normal tax.

**How to measure it.**

- **At least €35,000** ("not less than") means foreign income of exactly €35,000 is caught.
- The test uses the tax liability "before taking into account any relief granted in terms of articles 76 to 89", so double tax relief does not reduce the liability being compared with €5,000.
- Tax on article 5A property transfers is left out of both sides: the income from those transfers is excluded, and "tax imposed in terms of article 5A" does not count towards the minimum.
- Tax paid under the Act "whether by withholding or otherwise", on Malta or foreign income, counts towards the minimum. FSS tax on a Malta salary counts.
- **Cap.** If the person proves to the Commissioner that, taxed on a worldwide basis without provisos (i) and (ii), their total tax would be less than €5,000, the liability "shall be capped accordingly at the said lower amount". This needs a full worldwide computation, with evidence.

**Authority guidance on the threshold.** MTCA remittance-basis guidance section 6.3 describes foreign income below €35,000 as outside the minimum and uses the couple's total foreign income. Do not test only the unremitted balance. The statutory conditions, exclusions and the requirement that foreign income is not fully received still apply. Section 6.4 adds that the individual "may opt to be taxed on a worldwide basis, instead of the remittance basis, if his tax liability on a worldwide basis is less than the minimum tax", which is the Act's cap in other words. [Official guidance](https://mtca.gov.mt/docs/default-source/documents/mtca-guidelines-on-the-remittance-under-the-income-tax.pdf), read 26 November 2026.

**Married couples.** With joint taxation under article 49, both spouses' foreign income is counted and the test runs once, on the joint computation. Where the couple has opted for separate computation or separate assessment: Check this point with one of our partner accountants. This Guide does not apply the joint-couple example to separate computations/returns.

### Remittances: what counts and how to prove it

**What counts as "received in Malta".** The Act taxes "the amount received in Malta" but does not define it for article 4. (The only definition, in article 56(2)(d), is limited to that sub-article and does not apply here.) On a plain reading:

- money moved from a foreign account into a Maltese account is received in Malta;
- cash or cheques brought into Malta are received in Malta;
- income paid straight into a Maltese account is received in Malta.

Borderline cases are not settled by the Act: spending in Malta on a foreign card that is paid off from foreign income, foreign income used abroad to pay a Maltese debt, assets bought abroad with foreign income and then brought to Malta, and foreign loans secured on foreign income. Check this point with one of our partner accountants. Do not prescribe a taxable remittance from these facts alone.

**Capital is not income.** Money you owned before becoming resident, and the proceeds of foreign capital gains, are not "income arising outside Malta", so bringing them in is not taxed under proviso (i). But the Act has **no ordering rule** for a mixed account holding both capital and income. If a transfer comes from an account that also received income after you arrived, you may not be able to show it was capital.

**Practical evidence.**

1. Before arrival, close off a **capital account**: record its balance on the day before residence starts, with a bank statement.
2. Open separate foreign accounts for **income** (salary, dividends, interest, rent) and for **capital gains proceeds**. Pay nothing else into them.
3. Pay interest on the capital account into the income account, not into the capital account, so the capital stays clean.
4. Choose the funding account deliberately and document whether the transfer is capital, gains or income; an account label alone does not settle its character.
5. For each transfer into Malta, keep the statement from both ends, and a note of which account it came from and why.
6. Keep a yearly schedule: foreign income by type, the amount received in Malta, capital and gains transferred, and foreign tax paid. The same schedule drives the €35,000 test.
7. For the applicable retention period and assessment/enquiry window: Check this point with one of our partner accountants. Do not infer a statutory retention period from a normal assessment limit alone.

### Special residence programmes

GRP and Residence Programme establish their own rate/minimum if their status conditions hold. A Nomad Residence Permit has different rules and is not asserted here to create a minimum-tax scheme. Only the tax rate and minimum tax are given here, as the rules on legislation.mt state them. Eligibility, property and fee conditions, whether applications are still open, and the application process must be checked with the Commissioner (mtca.gov.mt) or Residency Malta Agency. Refer every programme case.

#### Global Residence Programme

- **Who:** a "third country national" who is not Maltese, EEA or Swiss, is not a rule 2 long-term resident (which includes an applicant for that status), and meets the rule 4 conditions (a qualifying owned or rented property as primary residence, stable resources, sickness insurance, a valid travel document, language and "fit and proper" tests). Applications go through an authorised registered mandatary.
- **Rate:** 15% ("fifteen cents (0.15) on every euro") on income arising outside Malta and received in Malta, for the beneficiary, the spouse and the rule 2(b)/(d) children meeting the custody/dependence, co-residence and incompatible-programme conditions, with double tax relief under article 74(a) and (b) available (rule 5(1)).
- **Minimum tax:** €15,000 "for any year of assessment", on the foreign income of those persons. It is payable in full in the year the status is granted and in the year it ends.
- **Other income:** income not taxed at 15% under the rules is "charged as separate income" at 35% (rule 5(2)).
- **When the minimum is paid:** by 30 April of the year immediately preceding the year of assessment, which is 30 April of the basis year itself (for year of assessment 2027, 30 April 2026), with a return proving the rule 4 conditions still hold. No continuation return is required in the grant year; where it is evident status will not be granted before 30 April, pay before grant. Tax paid under rule 5(1) is not refundable.
- **Status ends** (rule 6) if the person becomes Maltese, EEA or Swiss, stops holding the qualifying property (including by letting it), becomes a long-term resident, loses sickness insurance, the stay is not in the public interest, or "stays in any other jurisdiction for more than one hundred and eighty-three days in a calendar year". The person must notify the Commissioner within four weeks of becoming aware; the penalty for not doing so is €5,000.

#### Residence Programme, for EU, EEA and Swiss nationals

- **Who:** an "EU, EEA or Swiss national but ... not a Maltese national", not a rule 2 permanent resident of Malta (which includes an applicant for that status), meeting the rule 4 conditions (qualifying property, resources, insurance, travel document, language, fit and proper).
- **Rate:** 15% on income arising outside Malta and received in Malta, for the beneficiary, spouse and rule 2(b)/(d) children, subject to the same named-person, full-year-minimum and payment conditions described above; eligible treaty/unilateral relief under article 74(a)/(b) is available (rule 5(1)).
- **Minimum tax:** €15,000 for any year of assessment, payable in full in the first and last years.
- **Other income:** 35% as separate income (rule 5(2)).
- **Status ends** on the same kind of events, including becoming a permanent resident and staying elsewhere for more than 183 days in a calendar year (rule 6).

#### Nomad Residence Permit

The rules state a **10%** rate, not 15%.

- **Who:** an "eligible main applicant", meaning a holder of a valid nomad residence permit, a third country national licensed to do only "authorised work": remote work for an employer, or self-employed work for clients, who are not resident in Malta and have no fixed place of business in Malta.
- **Rate:** "ten percent (10%) on his chargeable income derived from authorised work", subject to double tax relief (rule 3(1)).
- **First 12 months:** no tax on authorised-work income before the end of 12 months from the permit date or 1 January 2024, whichever is later, unless the person files a written declaration with Residency Malta Agency that their residence is "not merely of a casual nature" (rule 3(3)).
- **Replacement permit:** rule 3(7) denies a new twelve-month exemption if a new permit is obtained within two years of ceasing to hold the original; after a period exceeding two years it can apply again.
- **Other income** of the permit holder, and all income of family members on the permit, is taxed under the normal Act, including the remittance basis where it applies (rule 3(4) and (5)).
- **No FSS** on the authorised-work salary (rule 3(6)). The holder must register for income tax, even for the first 12 months, and file a return unless rule 4(2)(c) excuses it.
- **Foreign tax of at least 10%:** if the holder proves to Residency Malta Agency that tax of at least 10% was paid abroad on the authorised-work income, rule 4(3) treats the tax as settled through relief. MTCA guidance requires reporting authorised-work income where there is other reportable chargeable income/gains or a joint computation with a spouse, with eligible relief claimed. Documentation is due by 31 March after the basis year; where final evidence is unavailable, follow the specified independent-explanation/interim-payment-evidence procedure and supply final certificate/receipts by expiry of the current permit. Do not infer a whole-return exemption from the income-specific rule.
- For interaction between the €5,000 minimum and a nomad permit: Check this point with one of our partner accountants.

### Double tax relief

Relief matters only for foreign income that is taxed in Malta, which for a non-dom means foreign income received in Malta (or deemed received under the minimum tax).

- **Four reliefs** (article 74): treaty relief (articles 76-78), unilateral relief (articles 79-88), Commonwealth income tax relief (article 89) and the flat-rate foreign tax credit (articles 92-95). The flat-rate credit is a company mechanism under article 92, not an individual non-dom entitlement.
- **Order** (article 75): unilateral relief applies only where treaty relief and Commonwealth relief are not available. The flat-rate foreign tax credit applies only where none of the other three is available.
- **Treaty credit** (article 77): the foreign tax is a credit against Malta tax on the same income, only if the person "is resident in Malta for the year immediately preceding the year of assessment". The credit cannot exceed the Malta tax on that income at the person's average rate (article 77(3)), and total treaty credits are also limited by article 77(4), excluding tax under articles 40, 69 and 73. An article 77(8) no-credit election and the actual treaty terms must be checked.
- **Gross-up for the remittance basis** (article 77(5)(b)): "where the income tax chargeable depends on the amount received in Malta the said amount shall be increased by the appropriate amount of the foreign tax". Tax is computed on the grossed-up amount, and the foreign tax is then credited.
- **Unilateral relief** (articles 80-81): available for foreign income that suffered "tax of a similar character" abroad, again only if the individual is resident in Malta for the basis year. The average-rate and total-credit limits in articles 83-84, gross-up in article 85 and proof required by article 88 must also be satisfied. Article 87 imports the article 77(8)-(10) election/time/adjustment provisions.
- **Time limit** (article 77(9)): a treaty credit claim must be made "not later than two years after the end of the year of assessment". For basis year 2026, the ordinary limit is 31 December 2029. Article 77(10) supplies a separate two-year window after all material tax adjustments/determinations where an adjustment makes the credit excessive or insufficient; do not discard that exception.
- **Minimum tax and relief are separate stages.** Article 56(27) compares the liability before relief under articles 76-89 with €5,000 and sets any top-up/cap. MTCA remittance guidance section 6.2 then states that the minimum is reduced by double tax relief due and limits relief to income actually remitted on which tax was paid abroad. These are not contradictory merely because the statutory comparison is pre-relief. Article 96(2) gives qualifying Commissioner guidance effect alongside the rules to the extent it does not conflict with the Acts/rules or later guidance. Compute only relief actually available under the applicable treaty or statutory route, with its caps/proof; do not grant a credit on unremitted income. For a contested eligibility, allocation or minimum-tax-relief computation: Check this point with one of our partner accountants.


## Boundary and exception table

Read the eligibility, exclusions and special-programme conditions above into every remittance/minimum row.

| Situation | Result | Rule |
| --- | --- | --- |
| Foreign income of exactly €35,000, part not brought in; ordinarily resident non-dom | Minimum tax test applies | art. 56(27) "not less than" |
| Foreign income below €35,000 | No minimum tax; only remitted foreign income and Malta income taxed | art. 56(27) |
| All foreign income brought into Malta | Outside the minimum tax (it covers income "not received or not fully received"); remitted income taxed at normal rates | art. 56(27), art. 4(1) proviso (i) |
| Resident, not domiciled, **not** ordinarily resident | Remittance basis applies; minimum tax does not | art. 4(1), art. 56(27)(i) |
| Domiciled in Malta, resident, not ordinarily resident | Remittance basis applies; minimum tax does not | art. 4(1) proviso (i) "or" |
| Long-term resident status granted during 2026 | Worldwide basis for all of 2026 and later years | art. 4(1) sohowever proviso |
| Spouse domiciled in Malta but not ordinarily resident | Remittance basis still available | spouse must be both |
| Spouse ordinarily resident and domiciled in Malta | No remittance basis; worldwide income and gains taxed | art. 4(1) sohowever proviso |
| GRP or Residence Programme beneficiary | Scheme's 15% rate and €15,000 minimum; not the €5,000 minimum | S.L. 123.148, S.L. 123.160, art. 56(27)(i) |
| Pre-residence savings brought into Malta | Capital, not income; not taxed if it can be proven | art. 4(1) proviso (i) |
| Foreign capital gain brought into Malta | Not taxed | art. 4(1) proviso (ii) |
| Gain on shares in a Maltese company | Malta-source; chargeable under art. 5 unless an exemption applies | art. 5(1)(a)(ii) |
| Tax before double tax relief below €5,000, worldwide tax would be lower still | Liability capped at the worldwide figure, if proven | art. 56(27) second proviso |
| Art. 5A final tax on a Maltese property sale | Does not count towards the €5,000 | art. 56(27) first proviso |

## Worked cases

Basis year 2026. Rate source: [Act III of 2026 rate tables](https://legislation.mt/getpdf/69d8ed326fe5fd3994d17430), consolidated in [Cap. 123 art. 56(1)](https://legislation.mt/eli/cap/123/eng/pdf).


The rates used are the year of assessment 2027 tables from Act III of 2026: single, 25% band over €16,000 and under €60,000, subtract €3,400; 35% over €60,000, subtract €9,400. Married joint with no qualifying child, 25% band over €23,000 and under €60,000, subtract €4,550. The full tables are in the Malta income tax Guide. These are examples; check every fact before relying on them.

The examples assume no other income, no foreign tax unless stated, and no defined-status/spouse exclusion unless the case expressly changes that fact. The single-table cases assume no qualifying parent/child table; a disposal gain is capital and foreign-source only if its evidence supports that classification.

**Case 1: minimum tax top-up.**
- Facts: single, ordinarily resident, not domiciled, no exclusion, no scheme. Malta salary €20,000 (FSS deducted). Foreign dividends €60,000 with no foreign tax, of which €10,000 was transferred to Malta.
- Chargeable in Malta: €20,000 + €10,000 = €30,000. Tax: €30,000 × 25% − €3,400 = €4,100.
- Foreign income is at least €35,000 and not all of it was received, so the minimum tax applies. Top-up: €5,000 − €4,100 = €900.
- Cap check: worldwide income €80,000 × 35% − €9,400 = €18,600, which is not lower than €5,000. No cap. Total tax €5,000, less FSS already deducted.

**Case 2: worldwide cap for a married couple.**
- Facts: married, taxed jointly, no qualifying children, both ordinarily resident non-doms. Foreign income €20,000 and €15,000, total €35,000, none brought into Malta. No Malta income.
- Tax on income chargeable in Malta: nil. Combined foreign income is at least €35,000, so the minimum tax applies.
- Worldwide computation on the joint table: €35,000 × 25% − €4,550 = €4,200. If they prove this, tax is capped at €4,200 instead of €5,000.

**Case 3: foreign capital gain brought in.**
- Facts: single, ordinarily resident non-dom. Sells foreign-listed shares at a gain of €200,000 and transfers all the proceeds to Malta. Foreign interest €20,000, none transferred.
- The gain is not taxed (article 4(1) proviso (ii)). The interest is not received in Malta, so it is not taxed.
- Foreign income is below €35,000, so no minimum tax. Tax: nil. Keep evidence that the transfer came from the sale proceeds and not from the interest.

**Case 4: spouse rule.**
- Facts: a non-domiciled individual married to a spouse who is ordinarily resident and domiciled in Malta. Foreign rent €30,000, none transferred to Malta.
- Provisos (i) and (ii) do not apply. The rent is taxed as it arises, and foreign gains are chargeable where article 5 reaches them. The minimum tax does not apply, because it needs the provisos to apply. Compute on the normal tables (Malta income tax Guide).

**Case 5: Global Residence Programme minimum.**
- Facts: a GRP beneficiary transfers €60,000 of foreign income to Malta in basis year 2026.
- Tax at 15%: €60,000 × 15% = €9,000. The minimum is €15,000, so €15,000 is due, payable by 30 April 2026 for year of assessment 2027, subject to the grant-year payment exception stated above. The €5,000 non-dom minimum does not apply (scheme with its own minimum).

**Case 6: Nomad Residence Permit.**
- Facts: permit issued 1 March 2024, no non-casual-residence declaration. Authorised-work salary from a foreign employer in 2026: €60,000, with no foreign tax.
- The 12 months ended on 28 February 2025, so all of 2026 is taxable. Tax: €60,000 × 10% = €6,000. No FSS is deducted; the holder registers, files and pays. If foreign tax of at least 10% has been proved to Residency Malta Agency under the applicable documentation rules, the limited no-return treatment can apply only where there is no other chargeable income/gains and no joint computation with a spouse. If either exception applies, report authorised-work income and claim eligible double tax relief. Documentation is due by 31 March after the basis year, with the guideline's specified interim-evidence procedure where final evidence is not yet available. [MTCA nomad guidance](https://mtca.gov.mt/docs/default-source/documents/personal-tax/legal-and-technical/guidelines/nomad-guidelines---12-03-2026.pdf?sfvrsn=f0cc9971_6), read 4 November 2026.

**Case 7: resident but not ordinarily resident.**
- Facts: arrived in Malta in March 2026 on a two-year secondment, foreign domicile, foreign investment income €80,000, of which €5,000 transferred.
- If the facts support "not ordinarily resident", the €5,000 received is taxed and the minimum tax does not apply, because it needs ordinary residence. If ordinary residence is arguable, refer; the difference is the minimum tax.

### Executable worked checks

The assumptions exclude legal-status/spouse exceptions and special programmes; there is no foreign-tax credit in either case.

```oa-check
name: Eligibleordinaryresidentnondom5000minimumtopup
inputs:
  malta_salary: 20000
  foreign_income_remitted: 10000
  foreign_income_total: 60000
steps:
  - ordinary_tax: (malta_salary + foreign_income_remitted) * 0.25 - 3400
  - top_up: max(5000 - ordinary_tax, 0)
  - total: ordinary_tax + top_up
expected:
  ordinary_tax: 4100
  top_up: 900
  total: 5000
```

```oa-check
name: Jointnondomcoupleworldwidecapwithoutqualifyingchildren
inputs:
  spouse_one_foreign: 20000
  spouse_two_foreign: 15000
steps:
  - combined: spouse_one_foreign + spouse_two_foreign
  - worldwide_tax: combined * 0.25 - 4550
  - liability_if_cap_proved: min(5000, worldwide_tax)
expected:
  combined: 35000
  worldwide_tax: 4200
  liability_if_cap_proved: 4200
```

## When to refuse or refer

Articles cited below are in the [Income Tax Act, Cap. 123](https://legislation.mt/eli/cap/123/eng/pdf).

- Refuse to give a final figure without the basis year, marital status and spouse's domicile and ordinary residence, long-term resident or permanent residence status, and the split of foreign income into received and not received.
- Refer any disputed domicile, any "ordinarily resident or not" question, and arrival and departure years.
- Refer mixed accounts where a transfer cannot be traced to capital, and every borderline remittance (card spending, debts, assets brought in, loans).
- Refer the worldwide cap claim under article 56(27); it needs a full worldwide computation and proof.
- Refer separate computation or separate assessment for married non-doms under the minimum tax.
- Refer all Global Residence Programme, Residence Programme and Nomad Residence Permit cases beyond the rate and minimum shown here, and any other special scheme: the Highly Skilled Individuals Rules ([L.N. 20 of 2026](https://legislation.mt/eli/ln/2026/20/eng/pdf)), which came into force on 1 January 2026 with a separate transition under rule 12 (under the old rules no determination is issued for applications made after 31 December 2025, and no benefit runs after year of assessment 2030, rule 12(2)), the retirement programme and returned migrants.
- For a contested treaty claim, company flat-rate credit or minimum-tax-relief computation: Check this point with one of our partner accountants. Apply the pre-relief comparison and available post-comparison credit as distinct stages ([ITA art. 56(27)](https://legislation.mt/eli/cap/123/eng/pdf)).
- Refer gains on Maltese property or Maltese company shares, trusts, and foreign companies you control.
- Refer anything that turns on an MTCA form, notice or online-filing extension you cannot see.

## Filing and payment


**Year-specific override, read 26 November 2026:** MTCA extended both manual and electronic individual returns for year of assessment 2026 (basis 2025), and the related tax payment, to **31 July 2026**. Use that actual date for late charges, not the general 30 June date. The statutory date for basis 2026 / assessment 2027 remains **30 June 2027** unless a later notice changes it. [MTCA notice, 3 June 2026](https://mtca.gov.mt/news-results-page/2026/06/03/tax-returns-submission-deadline).

| Item | Date or rule | Source |
| --- | --- | --- |
| Return and self-assessment, basis year 2026 | 30 June 2027 ("the thirtieth of June of the relative year of assessment") | S.L. 372.16 rule 2(c)(ii); ITMA art. 10 |
| Balance of tax (tax settlement date) | Ordinary self-assessment: same date as return; check rule 5(a) assessment-election/notice exception | S.L. 372.16 rule 5(b) |
| No notice received | A person chargeable to tax who has not received a notice to file is treated as if served with one, so the duty to file still applies | S.L. 372.16 rule 3 |
| Minimum tax top-up | Part of the self-assessment; due with the balance of tax | art. 56(27); S.L. 372.16 rule 5(b) |
| GRP and Residence Programme minimum tax | 30 April of the basis year (30 April 2026 for year of assessment 2027), with continuation proof; grant-year return/payment exception and no refund as stated above | S.L. 123.148 and S.L. 123.160 rule 5(3) |
| Nomad Residence Permit | Register for income tax; file a return unless rule 4(2)(c) excuses it | S.L. 123.210 rule 4 |
| Double tax relief claim | Treaty/unilateral ordinary claim: two years after YA; material tax-adjustment exception under article 77(10), applied to unilateral relief by article 87 | ITA arts. 77(9)-(10), 87 |
| Provisional tax | Payable in the basis year where there is a benchmark; see the Malta income tax Guide | ITMA; S.L. 372.18 |
| Online filing, forms and any extension | Check on mtca.gov.mt | - |

### Interest and penalties

- **Interest on late tax:** 0.6% for each month or part of a month, where the tax became payable on or after 31 August 2022, capped at the tax (ITMA art. 44).
- **Late return (individuals):** additional tax on a fixed scale, from €10 if filed within 6 months of the due date up to €500 if more than 60 months late (Income Tax Act, Schedule; see the Malta income tax Guide for the full scale).
- **GRP and Residence Programme:** failing to notify the Commissioner within four weeks that status has ended costs €5,000 (rule 6(2)).

### 2025 income (year of assessment 2026)

- The general statutory date was 30 June 2026, but MTCA extended both manual/electronic individual filing and the related payment to **31 July 2026**. Apply actual dates when determining late charges; the general date is not the operative 2026 deadline.
- For a historical 2025 computation and the precise version of the residence/minimum rules then in force: Check this point with one of our partner accountants. The historical filing extension above has been read; this Guide does not infer every historical rule from today’s consolidation.
- For 2025 rates and the applicable Act IX of 2025 tables: Check this point with one of our partner accountants; use the historical version of `malta-income-tax`.
- GRP and Residence Programme minimum tax for year of assessment 2026 was due by 30 April 2025.

## Completion checklist

- The basis year and year of assessment are stated.
- Residence, domicile and ordinary residence are recorded, with the facts behind each.
- The exclusions are checked: long-term resident or permanent residence (and the year granted), and the spouse's domicile and ordinary residence.
- Any special scheme is identified. Only a scheme effectively establishing a minimum engages the article 56(27)(i) scheme exclusion; do not assume every permit has that effect.
- Foreign income is listed by type, split into received and not received in Malta, with the evidence for each transfer.
- Foreign receipts are classified as income or capital gain with their source established; eligible foreign gains are excluded; Malta-situated gains are sent to the capital gains Guide.
- Tax is computed on Malta income plus foreign income received, at the right table for the year.
- The €35,000 test is run (joint income for a jointly taxed couple), the tax before double tax relief is compared with €5,000, article 5A tax is excluded, and any top-up is computed.
- If the worldwide cap is claimed, the worldwide computation and proof are on file.
- Double tax relief is claimed only where available, with gross-up, credit caps, proof, election checks and the applicable ordinary or adjustment claim limit.
- The ordinary return date, actual extension, statutory exception, payment and any late interest are checked against the applicable notice and year. For unseen portal fields/forms: Check this point with one of our partner accountants.
- The output is labelled as an estimate until reviewed.

## Sources

| Source | URL | Read on |
|---|---|---|
| Income Tax Act, Cap. 123: arts. 2, 4(1), 56(1)/(27), 74-77, 79-88, 92, 96(2), Schedule Table A read (residence, minimum, rates, relief caps/proof/adjustments, guidance, penalties) | https://legislation.mt/eli/cap/123/eng/pdf | 2026-11-26 |
| Act III of 2026: rate tables applicable from YA 2027 (same text as consolidated in Cap. 123), read for the single and married tables | https://legislation.mt/getpdf/69d8ed326fe5fd3994d17430 | 2026-11-26 |
| Income Tax Management Act, Cap. 372: arts. 10-12A and 44(2A) read (return/election/notice exceptions and interest) | https://legislation.mt/eli/cap/372/eng/pdf | 2026-11-26 |
| Income Tax (Statutory Dates) Rules, S.L. 372.16: read for rules 2, 3 and 5 (30 June return and payment) | https://legislation.mt/eli/sl/372.16/eng/pdf | 2026-11-26 |
| Global Residence Programme Rules, S.L. 123.148: read for rules 4, 5 and 6 | https://legislation.mt/eli/sl/123.148/eng/pdf | 2026-11-26 |
| Residence Programme Rules, S.L. 123.160: read for rules 4, 5 and 6 | https://legislation.mt/eli/sl/123.160/eng/pdf | 2026-11-26 |
| Nomad Residence Permits (Income Tax) Rules, S.L. 123.210: rules 2-4 read (scope, authorised work, permit re-entry and reporting) | https://legislation.mt/eli/sl/123.210/eng/pdf | 2026-11-26 |
| L.N. 20 of 2026, Highly Skilled Individuals Rules: read for rules 1 and 12 | https://legislation.mt/eli/ln/2026/20/eng/pdf | 2026-11-26 |
| MTCA, Tax Residence page: read for the 183-day practice, residence from arrival, ordinary residence over about three years | https://mtca.gov.mt/personal-tax/individual/tax-residence | 2026-11-26 |
| MTCA, Guidance Note on the Remittance Basis: read for sections 1 to 6 (spouse rule, domicile, arising and received in Malta, minimum tax, relief, excluded schemes) | https://mtca.gov.mt/docs/default-source/documents/mtca-guidelines-on-the-remittance-under-the-income-tax.pdf | 2026-11-26 |
| MTCA, notice of 3 June 2026: read for the 31 July 2026 YA 2026 deadline | https://mtca.gov.mt/news-results-page/2026/06/03/tax-returns-submission-deadline | 2026-11-26 |
| MTCA, Nomad Residence Permits guidelines (12 March 2026): sections 1-6 read for registration, reporting/joint-computation exceptions, 31 March/interim evidence and final-permit-expiry deadline | https://mtca.gov.mt/docs/default-source/documents/personal-tax/legal-and-technical/guidelines/nomad-guidelines---12-03-2026.pdf?sfvrsn=f0cc9971_6 | 2026-11-26 |

Not yet confirmed: no unconfirmed claim retained as usable guidance. Separate-return/computation minimum-tax cases, nomad/minimum interaction, disputed status, borderline remittances, certificate classification, retention/assessment windows and contested relief are explicitly referred above.
