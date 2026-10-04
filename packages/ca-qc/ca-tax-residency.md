---
name: ca-tax-residency
description: "Canada tax residency: factual resident, deemed resident (183-day sojourner), deemed non-resident, departure return, departure tax on deemed disposition. Trigger on: \"Canadian tax resident\", \"CRA residency\", \"leaving Canada taxes\", \"departure return Canada\", \"factual resident Canada\", \"183 days Canada\", \"sojourner Canada\", \"deemed resident Canada\", \"moving to Canada taxes\", \"residential ties Canada\", \"NR73\"."
version: 1.0
jurisdiction: CA
tax_year: 2026
last_updated: 2026-09-27
authored_by: OpenAccountants team
review_status: pending_review
trust_label: Written by the OpenAccountants team
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Canada: individual tax residence, moving in or out, departure tax and non-residents

## Scope and who this is for ([CRA Income Tax Folio S5-F1-C1](https://www.canada.ca/en/revenue-agency/services/tax/technical-information/income-tax/income-tax-folios-index/series-5-international-residency/folio-1-residency/income-tax-folio-s5-f1-c1-determining-individual-s-residence-status.html))

This Guide explains how to decide whether an individual is resident in Canada for federal income tax purposes, and what follows from the answer. It is written for **tax year 2026** (the calendar year 2026, returns filed in 2027), with a dated section for **2025 returns** that are being filed and assessed now. The residence rules come from the Income Tax Act (ITA) and CRA's Folio S5-F1-C1; they are not indexed and did not change for 2026. CRA's web pages were still written for the 2025 return when this Guide was prepared (25 September 2026), so where a date is quoted for 2025 the 2026 equivalent is shown next to it and worked out from the statutory rule.

It covers:

- factual residence (residential ties) and "ordinarily resident";
- deemed residence, including the 183-day sojourner rule in ITA s.250(1)(a);
- deemed non-residence under a tax treaty tie-breaker (ITA s.250(5));
- part-year residents: the year you arrive and the year you leave;
- departure tax (the deemed disposition in ITA s.128.1(4)), Forms T1243, T1161, T1244 and security;
- how non-residents are taxed: Part XIII withholding at 25%, treaty reductions, and the section 216 and section 217 elections;
- Forms NR73 and NR74.

It does **not** cover residence of corporations or trusts, Quebec provincial rules (Revenu Québec runs its own), foreign tax law in the other country, or detailed computation of capital gains. Residence is a question of fact decided on all the circumstances; this Guide gives the method and the CRA's stated positions, not a ruling. See "When to refuse or refer".

**Why residence matters.** "An individual who is resident in Canada during a tax year is subject to Canadian income tax on his or her worldwide income from all sources." A non-resident "is only subject to Canadian income tax on income from sources inside Canada" (Folio ¶1.1). A person who is resident for only part of the year is taxed on worldwide income for the resident part and as a non-resident for the rest (Folio ¶1.1; [ITA s.114](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-114.html)).

**Provincial residence.** Provincial or territorial tax generally follows the province where the individual resides on **December 31**. If an individual is resident in more than one province on that date, they are resident only in the one where they have the most significant residential ties (Folio ¶1.2-1.3). For the year you leave Canada, use the tax package for the province or territory where you lived on the date you left ([CRA: Leaving Canada](https://www.canada.ca/en/revenue-agency/services/tax/international-non-residents/individuals-leaving-entering-canada-non-residents/leaving-canada-emigrants.html)).

**The five possible statuses**

| Status | Test | How taxed |
| --- | --- | --- |
| Factual resident | Ordinarily resident in Canada; keeps significant residential ties | Worldwide income, federal plus provincial tax |
| Deemed resident | Not a factual resident, but caught by s.250(1), e.g. sojourned 183 days or more in the calendar year | Worldwide income for the whole year; federal tax plus federal surtax instead of provincial tax |
| Deemed non-resident | Resident under the ITA, but resident of the other country under a treaty tie-breaker (s.250(5)) | Like a non-resident: Canadian-source income only |
| Non-resident | No significant ties, not deemed resident | Canadian-source income only: Part XIII withholding or a Canadian return |
| Part-year resident | Arrived or left during the year | Resident rules for the resident period, non-resident rules for the rest |

## Ask the client first

- What were your exact dates of arrival in and departure from Canada in 2026 (and 2025, if that return is still open)? Keep travel records; any part of a day in Canada counts as a day for the 183-day count.
- Do you own or rent a home in Canada, and is it available for you to live in? If it is let, is the tenant at arm's length, on market terms, and for how long?
- Where do your spouse or common-law partner and your dependants live? If you are separated, was it a breakdown of the relationship before you left?
- What secondary ties remain: car, furniture, Canadian bank accounts and credit cards, RRSP or securities accounts, provincial health coverage, driver's licence, vehicle registration, club or professional memberships, a Canadian passport?
- Why are you abroad (or here), and for how long? Was your return foreseen when you left, for example a job waiting for you in Canada?
- Which country are you going to (or coming from)? Does Canada have a tax treaty with it, and are you liable to tax there on your worldwide income?
- For a stay in Canada without ties: were you commuting daily from outside Canada, or staying here (including for holidays)?
- If leaving: what property do you own worldwide, and its fair market value (FMV) on the day you leave? When did you last become resident in Canada, and how many months were you resident in the 10 years before leaving?
- Have you told your Canadian banks and payers that you are a non-resident? Will you receive Canadian rent, pensions, RRSP or RRIF payments, dividends or interest after you leave?
- Have you ever filed Form NR73 or NR74, received a CRA residency opinion, or claimed treaty residence elsewhere?

## The method, step by step

Work through the steps in order. Each step only applies if the earlier one did not settle the question.

1. **Test factual residence first.** Ask whether the person is "ordinarily resident" in Canada: where "in the settled routine of his life he regularly, normally or customarily lives" (Folio ¶1.6, quoting *Thomson*). Weigh all the facts, "including residential ties with Canada and length of time, object, intention and continuity with respect to stays in Canada and abroad" (Folio ¶1.8). Use the ties framework below. A factual resident cannot also be a deemed resident under s.250(1) (Folio ¶1.30).
2. **Weigh the significant residential ties.** A dwelling place, a spouse or common-law partner, and dependants in Canada "will almost always be significant residential ties" (Folio ¶1.11). "Generally, unless an individual severs all significant residential ties with Canada upon leaving Canada, the individual will continue to be a factual resident of Canada" (Folio ¶1.10). Two refinements:
   - A home kept available for the person's use is a significant tie. A home **leased to a third party on arm's-length terms** may be treated as not significant on its own, depending on all the circumstances (Folio ¶1.12, 1.26-1.27).
   - A spouse or common-law partner the person was already living apart from because the relationship broke down is **not** a significant tie (Folio ¶1.13).
3. **Weigh the secondary ties together.** Secondary ties "must be looked at collectively"; it would be "unusual for a single secondary residential tie" to make someone resident while abroad (Folio ¶1.14). They include personal property (furniture, clothing, cars, recreational vehicles); social ties (Canadian recreational or religious memberships); economic ties (a Canadian employer, active involvement in a Canadian business, Canadian bank accounts, retirement savings plans, credit cards and securities accounts); landed immigrant status or work permits; provincial health coverage; a provincial driver's licence; a vehicle registered in a province; a seasonal dwelling or a leased dwelling; a Canadian passport; and Canadian union or professional memberships. A Canadian mailing address, post office box, safety deposit box, business cards, phone listings and subscriptions are of "limited importance" on their own (Folio ¶1.15).
4. **Look at intention, visits and ties abroad.** Where some ties remain, the CRA considers evidence of intention to permanently sever ties, regularity and length of visits to Canada, and residential ties outside Canada (Folio ¶1.16). There is "no particular length of stay abroad that necessarily results in an individual becoming a non-resident" (Folio ¶1.17). If a return to Canada was foreseen when the person left (for example, a contract of employment waiting in Canada), remaining ties carry more weight (Folio ¶1.17). An intention to return, "in and of itself and in the absence of any residential ties", does not make someone resident (Folio ¶1.16). Not establishing ties abroad makes remaining Canadian ties more significant (Folio ¶1.21). The CRA also looks at whether the person dealt with departure tax and told Canadian payers they were a non-resident (Folio ¶1.18-1.19).
5. **If not a factual resident, test deemed residence under [ITA s.250(1)](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-250.html).** A person is "deemed to have been resident in Canada throughout a taxation year" if they "sojourned in Canada in the year for a period of, or periods the total of which is, 183 days or more". Count every day or part day on which the person was sojourning (temporarily staying) in Canada in the calendar year. Do not count days on which a person commutes to work in Canada and returns each night to their home outside Canada; do count holiday days in Canada, and work days where the person does not leave Canada in their time off (Folio ¶1.33). The other deemed residents in s.250(1) are members of the Canadian Forces, certain federal or provincial officers and servants posted abroad, certain development-program workers, overseas Canadian Forces school staff, their dependent children, and certain treaty-exempt family members (Folio ¶1.34).
6. **If resident (factual or deemed) and also resident elsewhere, apply the treaty tie-breaker.** First confirm the person is "liable to tax" in the other country, meaning subject to its most comprehensive form of taxation, generally tax on worldwide income (Folio ¶1.41). Then apply the tie-breaker in the Residence article of that specific treaty (see "Treaty tie-breakers" below). If the treaty makes the person resident of the other country, s.250(5) deems them not resident in Canada "for all purposes of the Act", and the departure rules and Part XIII withholding apply from that date (Folio ¶1.38).
7. **Fix the dates.** For someone leaving, the CRA generally takes the date all residential ties are severed, usually the **latest** of: the date the person leaves; the date the spouse or common-law partner and dependants leave; and the date the person becomes resident in the new country (Folio ¶1.22). Exception: someone who lived in another country before coming to Canada and leaves to resettle there generally becomes a non-resident on the date they leave, even if a spouse stays behind temporarily to sell the home or let children finish a school year (Folio ¶1.23). For someone arriving who establishes ties, residence generally starts on the date of entry (Folio ¶1.28).
8. **Apply the consequences.** Part-year: worldwide income for the resident period only (s.114). Leaving: deemed disposition, T1243, T1161 if required, optional T1244 deferral. Arriving: FMV step-up on most property. Non-resident: Part XIII withholding, or a Canadian return for employment, business, taxable Canadian property, or a section 216 or 217 election.
9. **Get an opinion if the facts are close.** Form NR73 (leaving) or NR74 (entering) asks the CRA for an opinion. It is optional and "not binding on the CRA" (Folio ¶1.55). Where certainty is needed before a move, the Income Tax Rulings Directorate may issue a binding advance ruling if all facts can be known in advance (Folio ¶1.56). Dual-residence disputes with a treaty country can go to Competent Authority Services (Folio ¶1.57).

## Key figures and time limits (tax year 2026)

None of these amounts is indexed. Sources are linked in each row.

| Item | Figure or rule | Source |
| --- | --- | --- |
| Sojourner test | 183 days or more in the calendar year (any part day counts) | [ITA s.250(1)](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-250.html); Folio ¶1.33 |
| Short-term resident exception to departure tax | Resident in Canada for not more than 60 months in the 120 months before leaving | [ITA s.128.1(4)(b)(iv)](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-128.1.html) |
| Form T1161 required | Total FMV of reportable property more than $25,000 | [CRA: Dispositions of property](https://www.canada.ca/en/revenue-agency/services/tax/international-non-residents/individuals-leaving-entering-canada-non-residents/dispositions-property.html); ITA s.128.1(9) |
| Personal-use items left out of T1161 | Each item with FMV less than $10,000 | [CRA: Dispositions of property](https://www.canada.ca/en/revenue-agency/services/tax/international-non-residents/individuals-leaving-entering-canada-non-residents/dispositions-property.html) |
| Late T1161 penalty | $25 per day late, minimum $100, maximum $2,500 | [CRA: Dispositions of property](https://www.canada.ca/en/revenue-agency/services/tax/international-non-residents/individuals-leaving-entering-canada-non-residents/dispositions-property.html) |
| Security needed for T1244 deferral | Federal tax on the deemed disposition more than $16,500 (more than $13,777.50 for former Quebec residents) | [CRA: Dispositions of property](https://www.canada.ca/en/revenue-agency/services/tax/international-non-residents/individuals-leaving-entering-canada-non-residents/dispositions-property.html) |
| T1244 election deadline | April 30 of the year after the year you emigrate (2026 emigrant: April 30, 2027) | [CRA: Dispositions of property](https://www.canada.ca/en/revenue-agency/services/tax/international-non-residents/individuals-leaving-entering-canada-non-residents/dispositions-property.html) |
| Part XIII withholding, default rate | 25% of the gross amount | [ITA s.212(1)](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-212.html); [CRA T4058](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/t4058/non-residents-income-tax.html) |
| Canada-US treaty: portfolio dividends | Not more than 15% of the gross dividend (10% for a company owning at least 10% of the voting stock) | [Canada-US Convention Art. X](https://laws-lois.justice.gc.ca/eng/acts/C-10.7/FullText.html) |
| Canada-US treaty: periodic pension payments | Not more than 15% of the gross payment | [Canada-US Convention Art. XVIII](https://laws-lois.justice.gc.ca/eng/acts/C-10.7/FullText.html) |
| NR7-R refund of excess Part XIII tax | Within 2 years after the end of the calendar year the payer remitted the tax (longer under some treaties) | [CRA T4058](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/t4058/non-residents-income-tax.html) |
| Section 216 return (rent) | Within 2 years after year end; within 6 months if an NR6 undertaking was filed (2026 rent: December 31, 2028, or June 30, 2027 with an approved NR6) | [ITA s.216(1)](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-216.html); [CRA: When to file](https://www.canada.ca/en/revenue-agency/services/tax/international-non-residents/individuals-leaving-entering-canada-non-residents/electing-under-section-216/when-file.html) |
| Section 217 return (pensions, benefits) | Within 6 months after year end, so by June 30; balance due April 30 (2026 income: June 30, 2027 and April 30, 2027); the filing date may differ if employment, business or taxable Canadian property income is also reported | [ITA s.217(2)](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-217.html); [CRA: section 217 due dates](https://www.canada.ca/en/revenue-agency/services/tax/international-non-residents/individuals-leaving-entering-canada-non-residents/electing-under-section-217/when-file.html) |

## Treaty tie-breakers ([Canada-US Convention, Article IV](https://laws-lois.justice.gc.ca/eng/acts/C-10.7/FullText.html))

A treaty only helps someone who is resident of **both** countries under paragraph 1 of the Residence article, which usually turns on being "liable to tax" there. The CRA's view is that this means being subject to "the most comprehensive form of taxation as exists in the relevant country", for Canada generally tax on worldwide income; the onus is on the individual to show it (Folio ¶1.41, 1.43). A person need not actually pay tax in the other country, but an abusive "resident of convenience" arrangement is not accepted (Folio ¶1.42). The courts have held that a US green card holder is resident in the US for Article IV(1) of the Canada-US treaty (Folio ¶1.44).

Tie-breakers are in paragraph 2 of the Residence article of most of Canada's treaties (Folio ¶1.46), but wording and order differ between treaties: always read the treaty for the other country. The Canada-US treaty, Article IV(2), is typical:

1. **Permanent home.** Resident where the person "has a permanent home available to him". A permanent home is any dwelling kept for permanent, not occasional, use, owned or rented; it is the permanence that counts, not size or ownership (Folio ¶1.46-1.47). A Canadian home that is still available (not let at arm's length) plus a home abroad means two permanent homes, so this test fails and you move on (Folio ¶1.49).
2. **Centre of vital interests.** If there is a permanent home in both or neither, resident where "personal and economic relations are closer": family and social relations, occupation, political and cultural activities, place of business, where property is managed (Folio ¶1.50).
3. **Habitual abode.** If the centre of vital interests cannot be determined, resident where the person has "an habitual abode".
4. **Citizenship.** If habitual abode is in both or neither, resident of the state of which the person is a citizen.
5. **Mutual agreement.** If a citizen of both or neither, "the competent authorities of the Contracting States shall settle the question by mutual agreement".

If the tie-breaker makes the person resident of the other country, [ITA s.250(5)](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-250.html) deems them "not to be resident in Canada". From that time the departure rules (deemed disposition) and Part XIII withholding apply (Folio ¶1.38). Section 250(5) does not apply to an individual who was a treaty resident of the other country but otherwise resident in Canada on February 24, 1998, as long as that dual status has continued without a break since then (Folio ¶1.38).

## Leaving Canada: the departure year ([CRA: Leaving Canada (emigrants)](https://www.canada.ca/en/revenue-agency/services/tax/international-non-residents/individuals-leaving-entering-canada-non-residents/leaving-canada-emigrants.html))

You are generally an emigrant if you leave Canada to live in another country **and** sever your residential ties. If you leave but keep residential ties, you are usually still a factual resident, unless a treaty makes you a deemed non-resident, in which case the same rules apply as for emigrants (CRA: Leaving Canada). Someone working, studying or wintering abroad who keeps ties stays a factual resident and is taxed "as if you never left Canada" ([CRA: Factual residents temporarily outside Canada](https://www.canada.ca/en/revenue-agency/services/tax/international-non-residents/individuals-leaving-entering-canada-non-residents/factual-residents-temporarily-outside-canada.html)).

**The departure-year return.** File a return if you owe tax or want a refund. Enter the date of departure in the "Residence Information" area on page 1 and your spouse's or common-law partner's net world income. Report worldwide income up to the departure date and Canadian-source income after it (s.114). Certain federal non-refundable credits are limited for the non-resident part of the year. If you decide you do not have to file, "you should let the CRA know the date you left Canada as soon as possible". Tell Canadian payers and financial institutions that you are no longer resident, so they withhold Part XIII tax (CRA: Leaving Canada).

**After you leave.** You can keep a TFSA and its exemption, but you cannot contribute while non-resident and your room does not grow. You are generally not eligible for the Canada child benefit or the Canada Groceries and Essentials Benefit as a non-resident; tell the CRA your departure date (CRA: Leaving Canada).

## Departure tax: deemed disposition, T1243, T1161, T1244 ([CRA: Dispositions of property for emigrants](https://www.canada.ca/en/revenue-agency/services/tax/international-non-residents/individuals-leaving-entering-canada-non-residents/dispositions-property.html))

**The rule.** When an individual ceases to be resident, [ITA s.128.1(4)(b)](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-128.1.html) deems them to have disposed of each property they own, immediately before leaving, "for proceeds equal to its fair market value", and to have reacquired it at the same amount. Any gain is reported on the departure-year return: calculate it on **Form T1243** and carry it to **Schedule 3**.

**Property that is not deemed disposed of** (s.128.1(4)(b) and CRA):

- Canadian real or immovable property, Canadian resource property and timber resource property (Canada keeps the right to tax them when they are sold);
- capital property and inventory of a business carried on through a permanent establishment in Canada;
- "excluded rights or interests" in s.128.1(10): pension plans, annuities, RRSPs, PRPPs, RRIFs, RESPs, RDSPs, TFSAs, FHSAs, DPSPs, employee profit-sharing and benefit plans, salary deferral and retirement compensation arrangements, employee life and health trusts, certain employee security options subject to Canadian tax, interests in certain Canadian-resident personal trusts, and interests in Canadian life insurance policies (other than segregated fund policies);
- for a short-term resident (not a trust) who was resident in Canada for **not more than 60 months in the 120 months** before leaving: property owned when they last became resident, or inherited after that.

An emigrant may **elect** under s.128.1(4)(b)(v) and CRA Form **T2061A** to include Canadian real property or Canadian business property in the deemed disposition.

**Form T1161 (list of properties).** If the total FMV of all "reportable property" owned when you left was **more than $25,000**, file Form T1161 listing properties inside and outside Canada, with the departure-year return ([ITA s.128.1(9)](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-128.1.html)). Leave out: cash and bank deposits; the registered plans and other excluded rights listed above, except employee security options, interests in Canadian-resident personal trusts and interests in Canadian life insurance policies, which must still be listed (s.128.1(10) "reportable property" para (b) reads the excluded-rights definition "without reference to paragraphs (c), (j) and (l)"), so they count towards the more-than-$25,000 test; for a short-term resident, property owned on arrival that is not taxable Canadian property; and each personal-use item (household effects, clothing, cars, collectibles) with FMV of **less than $10,000**. T1161 is due by your filing due date "even if you do not have to file a return". The late-filing penalty is **$25 for each day late**, minimum **$100**, maximum **$2,500**.

**Deferring the tax (Form T1244).** You can elect under [ITA s.220(4.5)](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-220.html) to defer paying the departure tax, "regardless of the amount", and pay it "without interest" when you actually sell or otherwise dispose of the property. Conditions:

- File **Form T1244** by **April 30 of the year after you emigrate** (a 2026 emigrant: April 30, 2027).
- The election does not apply to a deemed disposition of an employee benefit plan.
- If federal tax owing on the deemed disposition is **more than $16,500** (more than **$13,777.50** for former Quebec residents), you must provide adequate security for the amount. Security may also be required for provincial or territorial tax. Contact the CRA before April 30 to agree the security.
- When you later dispose of the property, report it to Non-Resident T1 Adjustments at the Winnipeg Tax Centre; payment of the deferred tax is due by April 30 of the year after the disposition.

**Returning to Canada ("unwinding").** If you left after October 1, 1996 and become resident again while still owning property that was deemed disposed of, you can elect in writing, by your filing due date for the year you return, to adjust the departure deemed disposition (ITA s.128.1(6)). For taxable Canadian property, you reduce the gain reported in the emigration year by an amount you choose, up to that gain. For other property, you reduce the proceeds reported in the emigration year by the least of: the gain reported that year; the FMV of the property on the date you returned; and any other amount you choose, up to the lesser of those two. Include a list of the properties and the FMV of each. Security you gave may then be returned. If you had deferred departure tax, you may have to pay it when you come back (CRA: Dispositions of property).

**Selling taxable Canadian property later.** After emigrating, disposing of taxable Canadian property (for example Canadian real property or unlisted shares of Canadian corporations) may bring "additional reporting requirements" under section 116; see Information Circular IC72-17R6. This Guide does not cover section 116.

## Entering Canada: the arrival year ([CRA: Newcomers, completing your return](https://www.canada.ca/en/revenue-agency/services/tax/international-non-residents/individuals-leaving-entering-canada-non-residents/newcomers-canada-immigrants/completing-return-newcomers.html))

**When residence starts.** The same ties apply in reverse (Folio ¶1.25). A home, spouse or common-law partner, or dependants in Canada will almost always be significant ties. The CRA also treats landed immigrant (permanent resident) status plus provincial health coverage as usually significant, so that, "except in exceptional circumstances", the person is resident (Folio ¶1.25). Residence generally starts on the date of entry (Folio ¶1.28). A dwelling bought in Canada for future use and leased to a third party is not a significant tie on its own (Folio ¶1.26-1.27).

**Deemed acquisition at FMV.** On becoming resident, [ITA s.128.1(1)](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-128.1.html) deems the individual to have disposed of and reacquired most property at FMV. The CRA says: "the CRA considers you to have sold the property and to have immediately reacquired it at a cost equal to the fair market value (FMV) on the date that you became a resident of Canada." That FMV becomes the Canadian cost base, so keep a record of values on arrival. The step-up does not apply to taxable Canadian property, inventory and Class 14.1 property of a business carried on in Canada, and most excluded rights or interests (s.128.1(1)(b)).

**The arrival-year return.** Worldwide income is taxed from the date of arrival; income earned outside Canada before you became resident is not taxed in Canada, and credits are limited for the non-resident part (s.114). To receive benefits, newcomers report world income for up to two years before arrival ([CRA: Newcomers to Canada](https://www.canada.ca/en/revenue-agency/services/tax/international-non-residents/individuals-leaving-entering-canada-non-residents/newcomers-canada-immigrants.html)).

**Short visits without ties.** A person without ties who sojourns 183 days or more in 2026 is a deemed resident for **all** of 2026 and taxed on worldwide income for the whole year, unlike a factual resident who arrives or leaves part way through and is taxed on worldwide income only for the resident part (Folio ¶1.32). A deemed resident is not resident in any province, so pays the federal surtax instead of provincial tax and gets no provincial credits (Folio ¶1.30). Exception: someone who lived in Quebec just before leaving and is a deemed resident may be treated as a Quebec resident under Quebec law; if they owe both Quebec tax and the federal surtax, they can ask the CRA for relief from the surtax when filing (Folio ¶1.31). Refer these cases. CRA's T4058 notes that a person who "left or entered Canada permanently in the year" may not be a deemed resident; the part-year rules apply instead.

## Non-residents: how Canadian-source income is taxed ([CRA Guide T4058, Non-Residents and Income Tax](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/t4058/non-residents-income-tax.html))

A non-resident (or deemed non-resident) pays Canadian tax only on Canadian-source income, by one of two methods.

**Method 1: Part XIII withholding.** Under [ITA s.212(1)](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-212.html), "Every non-resident person shall pay an income tax of 25%" on listed amounts paid or credited by a Canadian resident. The payer withholds it. Common types: dividends, rent, pensions, OAS, CPP/QPP benefits, retiring allowances, RRSP, RRIF, FHSA and PRPP payments, annuities, royalties, estate or trust income, and interest paid to a non-arm's-length person (interest paid at arm's length is generally exempt). The withheld tax "is your final tax obligation to Canada on this income" and is not reported on a Canadian return (T4058).

- **Treaty reductions.** A treaty may cut the rate. For a US resident, the Canada-US treaty caps portfolio dividends at 15% and periodic pensions at 15% ([Articles X and XVIII](https://laws-lois.justice.gc.ca/eng/acts/C-10.7/FullText.html)). For other countries, check IC76-12R8 or the CRA non-resident tax calculator, and the treaty itself. Tell the payer your country of residence so the reduced rate is applied.
- **Too much withheld.** Apply on Form **NR7-R** within 2 years after the end of the calendar year the payer remitted the tax (for tax remitted in 2025, by December 31, 2027; for 2026, by December 31, 2028); some treaties allow longer (T4058).

**Method 2: a Canadian return.** Employment income in Canada, business income from carrying on business in Canada, taxable scholarships, and taxable capital gains from disposing of taxable Canadian property are taxed on a Canadian return under Part I ([ITA s.2(3)](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-2.html)), subject to any treaty relief.

**Section 216 election: rent from Canadian real property** ([ITA s.216](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-216.html); [CRA: Electing under section 216](https://www.canada.ca/en/revenue-agency/services/tax/international-non-residents/individuals-leaving-entering-canada-non-residents/electing-under-section-216.html))

- Without an election, 25% is withheld on **gross** rent and that is the final tax.
- The election lets a non-resident file a separate return and pay tax on **net** rental income (or timber royalties) instead; any excess withheld is refunded. All Canadian rental properties go on one return. Employment, business, capital gains and interest cannot go on it ([CRA: Who can elect](https://www.canada.ca/en/revenue-agency/services/tax/international-non-residents/individuals-leaving-entering-canada-non-residents/electing-under-section-216/who-file.html)).
- **Form NR6**: an undertaking to file a section 216 return. Once the CRA approves it, the agent may withhold 25% of net rent available after expenses during the year. Send the NR6, signed by you and your agent, "on or before January 1 of each year or before the first rental payment is due"; until the CRA approves it in writing, the agent withholds on gross rent ([CRA: Determine if you should elect](https://www.canada.ca/en/revenue-agency/services/tax/international-non-residents/individuals-leaving-entering-canada-non-residents/electing-under-section-216/determine-file.html)).
- **Deadlines**: within 2 years after the end of the year the rent was paid; within 6 months (June 30) if an NR6 was approved; by April 30 if the property was sold and CCA recapture is reported. File by the due date even with no tax, no refund, or a net loss where an NR6 was approved. A late return makes the election invalid; with an approved NR6, tax is then due on the gross rent ([CRA: When to file](https://www.canada.ca/en/revenue-agency/services/tax/international-non-residents/individuals-leaving-entering-canada-non-residents/electing-under-section-216/when-file.html)).

**Section 217 election: pensions and benefits** ([ITA s.217](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-217.html); [CRA: Electing under section 217](https://www.canada.ca/en/revenue-agency/services/tax/international-non-residents/individuals-leaving-entering-canada-non-residents/electing-under-section-217.html))

- Covers "Canadian benefits" such as OAS, CPP/QPP, pension and superannuation payments, RRSP, RRIF and PRPP payments, DPSP payments, death benefits, EI benefits and retiring allowances. You pay tax "at the same rate as Canadian residents" on this income and may get back some or all of the withholding.
- File the return "within 6 months after the end of the year" (June 30). A balance owing is due April 30. "The CRA cannot accept your section 217 election if you file after June 30th"; the withholding then stands as the final tax. Exception: CRA says the filing due date "may differ" if you also report other Canadian-source income, such as employment or business income, net Canadian partnership income as a limited or non-active partner, or taxable capital gains from disposing of taxable Canadian property; then use the due dates in the non-resident income tax guide ([CRA: section 217 due dates](https://www.canada.ca/en/revenue-agency/services/tax/international-non-residents/individuals-leaving-entering-canada-non-residents/electing-under-section-217/when-file.html)).
- Non-refundable credits are only allowed in full if "all or substantially all" of the person's income is included (s.217(4)); otherwise only some credits (s.217(5)).
- An emigrant who receives such income after leaving can use section 217 for that income (CRA: Leaving Canada). Form NR5 can reduce withholding in advance; an approved NR5 covers five tax years and requires a section 217 return each year (T4058).

## Boundaries and exceptions ([CRA Income Tax Folio S5-F1-C1](https://www.canada.ca/en/revenue-agency/services/tax/technical-information/income-tax/income-tax-folios-index/series-5-international-residency/folio-1-residency/income-tax-folio-s5-f1-c1-determining-individual-s-residence-status.html))

| Situation | Result | Authority |
| --- | --- | --- |
| Leaves Canada, keeps a home available and family in Canada | Still a factual resident | Folio ¶1.10-1.13 |
| Leaves, home let at arm's length, no other significant ties | Home may not be a significant tie on its own | Folio ¶1.12 |
| Only secondary ties remain (bank account, licence) | Unusual for these alone to make someone resident | Folio ¶1.14 |
| Intends to return but has no ties | Intention alone is not enough | Folio ¶1.16 |
| Not a factual resident; in Canada 183 days or more in the year | Deemed resident for the whole year | ITA s.250(1)(a) |
| Commutes daily from the US to work in Canada | Commuting days do not count as sojourning | Folio ¶1.33; T4058 |
| Dual resident; treaty tie-breaker favours the other country | Deemed non-resident (s.250(5)); departure rules apply from that time | Folio ¶1.37-1.38 |
| Resident 60 months or less in the 10 years before leaving | Property brought to Canada or inherited is not deemed disposed of | ITA s.128.1(4)(b)(iv) |
| Registered plans (RRSP, RRIF, TFSA) on departure | Not deemed disposed of; later payments face Part XIII | ITA s.128.1(10); T4058 |
| Section 216 or 217 return filed late | Election invalid; withholding is the final tax | ITA s.216(1), s.217(2) |

## Worked cases ([CRA: Dispositions of property for emigrants](https://www.canada.ca/en/revenue-agency/services/tax/international-non-residents/individuals-leaving-entering-canada-non-residents/dispositions-property.html))

**Case 1: departure with shares.** Priya, resident in Canada since birth, emigrates to Australia on 15 August 2026 and sells her Toronto condo before she leaves. She keeps listed shares with a cost of $40,000 and FMV of $100,000 on the day she leaves, plus an RRSP and a TFSA. The shares are deemed disposed of at $100,000, so the capital gain is $100,000 minus $40,000, which is $60,000, reported on Form T1243 and Schedule 3 of her 2026 return. The RRSP and TFSA are excluded rights and are not deemed disposed of. Reportable property is more than $25,000, so she files Form T1161. She may file Form T1244 by April 30, 2027 to defer the tax without interest; security is needed only if federal tax on the gain is more than $16,500.

**Case 2: T1161 penalty.** A T1161 filed 30 days late: 30 days at $25 a day gives $750, which is between the $100 minimum and the $2,500 maximum, so $750. Filed 3 days late: 3 days at $25 gives $75, raised to the $100 minimum. Filed 120 days late: 120 days at $25 gives $3,000, capped at $2,500.

**Case 3: short-term resident.** Tom moved to Canada from the UK in March 2022, bringing UK shares, and left in February 2026. He was resident for not more than 60 months in the 120 months before leaving, so the UK shares he owned on arrival are not deemed disposed of (s.128.1(4)(b)(iv)). Shares he bought while in Canada are.

**Case 4: sojourner** ([ITA s.250(1)](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-250.html)). A US retiree with no Canadian home, family or other ties stays in Canada for 190 days in 2026, counting part days. She is a deemed resident for all of 2026, taxed on worldwide income with the federal surtax instead of provincial tax. A US resident who drives into Canada to work each day and goes home each night is not sojourning on those days.

**Case 5: non-resident dividends** ([CRA T4058](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/t4058/non-residents-income-tax.html)). A US-resident individual receives a $1,000 dividend from a Canadian listed company. Default Part XIII tax at 25% is $250. The Canada-US treaty caps it at 15%, so $150 if the payer applies the treaty. If the payer withheld $250, the $100 excess can be claimed on Form NR7-R within the 2-year window.

**Case 6: rent** ([CRA: Electing under section 216](https://www.canada.ca/en/revenue-agency/services/tax/international-non-residents/individuals-leaving-entering-canada-non-residents/electing-under-section-216.html)). A non-resident receives $24,000 of gross Canadian rent in 2026. Without an election, 25% of gross is withheld: $6,000, final. With a section 216 return filed by December 31, 2028 (or June 30, 2027 if an NR6 was approved), tax is computed on net rent and the excess withholding is refunded.

## When to refuse or refer

- Refer where ties point both ways (for example a home kept in Canada, family abroad) and the answer decides a large tax bill; suggest Form NR73 or NR74, or an advance ruling if certainty is needed before the move (Folio ¶1.55-1.56).
- Refer dual-residence cases where the treaty tie-breaker reaches habitual abode, citizenship or mutual agreement, or the other country disputes residence: Competent Authority Services (Folio ¶1.57).
- Refer Quebec residents (Revenu Québec rules and the Quebec security threshold), trusts, corporations, and anyone selling taxable Canadian property (section 116).
- Refer departure tax where security must be negotiated with the CRA, or where the person holds private company shares, a business, stock options or foreign trusts.
- Do not state the foreign country's tax position, or a treaty rate you have not read in that treaty.
- Do not tell anyone they became non-resident because of days abroad alone; there is no day count for leaving (Folio ¶1.17).

## Filing and payment ([CRA: Leaving Canada (emigrants)](https://www.canada.ca/en/revenue-agency/services/tax/international-non-residents/individuals-leaving-entering-canada-non-residents/leaving-canada-emigrants.html))

**2026 (the year this Guide targets).** Dates are worked out from the statutory rules and CRA's 2025 pattern.

- Departure-year or arrival-year T1 return: due April 30, 2027 (June 15, 2027 for a self-employed person and their cohabiting spouse, with payment still due April 30, 2027). Forms T1243, T1161 and T2061A go with it; T1161 is due by the filing due date even without a return.
- T1244 deferral election and any security: April 30, 2027.
- Section 217 return for 2026 income: June 30, 2027; balance due April 30, 2027.
- Section 216 return for 2026 rent: December 31, 2028; June 30, 2027 with an approved NR6; April 30, 2027 if CCA recapture is reported.
- NR7-R for Part XIII tax remitted in 2026: December 31, 2028.
- A due date on a weekend or public holiday moves to the next business day.

**2025 returns (being filed and assessed now).** The 2025 T1 was due April 30, 2026 (June 15, 2026 for the self-employed, with payment due April 30, 2026). A 2025 emigrant's T1244 election was due April 30, 2026. The 2025 section 217 return was due June 30, 2026. The 2025 section 216 return is due December 31, 2027, or was due June 30, 2026 with an approved NR6 ([CRA T4058](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/t4058/non-residents-income-tax.html); [CRA: section 216 due dates](https://www.canada.ca/en/revenue-agency/services/tax/international-non-residents/individuals-leaving-entering-canada-non-residents/electing-under-section-216/when-file.html)).

**NR73 and NR74.** Form NR73 ([CRA: NR73](https://www.canada.ca/en/revenue-agency/services/forms-publications/forms/nr73.html)) is for someone who has "left or are planning to leave Canada temporarily or permanently"; Form NR74 ([CRA: NR74](https://www.canada.ca/en/revenue-agency/services/forms-publications/forms/nr74.html)) for someone who "entered or stayed briefly in Canada". Both are optional. The CRA's opinion rests entirely on the facts given and is not binding (Folio ¶1.55).

## Completion checklist

- [ ] Status decided in order: factual, deemed (s.250(1)), treaty tie-breaker (s.250(5)).
- [ ] Significant and secondary ties listed with evidence; dates of leaving or arrival fixed.
- [ ] Day count kept, with commuting days separated from sojourning days.
- [ ] For a treaty case, the specific treaty's Residence article read and "liable to tax" confirmed.
- [ ] Departure: property listed with FMV; exclusions applied; T1243 and Schedule 3 prepared; T1161 filed if reportable property is more than $25,000.
- [ ] T1244 considered by April 30 of the following year; security arranged if federal tax is more than $16,500.
- [ ] Arrival: FMV on arrival recorded as cost.
- [ ] Canadian payers and banks told of non-residence; treaty rate claimed; NR7-R, NR5 or NR6 filed where useful.
- [ ] Section 216 and 217 deadlines diarised.
- [ ] NR73 or NR74 considered where the facts are close.

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
