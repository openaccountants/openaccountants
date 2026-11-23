---
name: mt-us-retirement-accounts-non-dom
description: "Use this skill for a US citizen, green card holder or other holder of US retirement accounts who lives in Malta but is not domiciled in Malta. Trigger on \"Roth conversion Malta\", \"IRA Malta non-dom\", \"401(k) Malta\", \"US pension Malta tax\", \"Roth IRA Malta treaty\", \"Malta US tax treaty pensions\", \"article 17 Malta US treaty\", \"article 18 pension funds Malta\", \"remit IRA to Malta\", \"gift between spouses remittance Malta\", \"permanent residence certificate Malta tax\", or any question about how Malta taxes a US retirement account of a Malta resident. Covers the Malta charge on a traditional to Roth IRA conversion, later distributions kept abroad or brought into Malta, the EUR 35,000 test and EUR 5,000 minimum tax, the Malta-US treaty (arts 1(4), 1(5), 3(1)(k), 17, 18, 22(7), 23) and the 2021 competent authority arrangement, cash gifts between spouses outside Malta, and the long-term resident and permanent residence exclusion. Basis year 2026 (year of assessment 2027). The US side is in the US skills it names."
version: 1.0
jurisdiction: MT
tax_year: 2026
last_updated: 2026-11-23
depends_on:
  - mt-non-dom
  - malta-income-tax
category: international
tier: 2
domain: cross-border
type: situation-rules
---

# US retirement accounts of a Malta-resident non-dom: conversions, distributions, the treaty, gifts between spouses and permanent residence

## Scope and who this is for

This skill covers an individual who is resident in Malta, not domiciled in Malta, and holds US retirement accounts: a traditional IRA, a Roth IRA, a 401(k) or Roth 401(k), or a similar US plan. Most such people are US citizens; some are former green card holders or other non-citizens who kept their US accounts. It explains how Malta taxes a Roth conversion and later distributions, what the Malta-US treaty changes and what it does not, whether a cash gift between spouses outside Malta changes what is "received in Malta", and when the long-term resident and permanent residence exclusion ends the remittance basis.

- **Basis year 2026 = year of assessment 2027.** The return for 2026 income is due by 30 June 2027 (see `mt-non-dom`).
- **Load `mt-non-dom` first.** It owns the residence, domicile and ordinary residence tests, the remittance basis, the EUR 5,000 minimum tax mechanics, double tax relief and the rate tables. This skill applies them to US retirement accounts and does not repeat them.
- **The US side is not here.** For the US tax on a conversion, Form 8606, basis and the five-year rules, see `us-ira-and-roth-conversions-8606`. For US filing by a citizen living abroad, the foreign tax credit and the foreign earned income exclusion, see `us-citizen-moving-abroad-tax`. For FBAR and Form 8938 on Maltese accounts, see `us-fbar-and-fatca-8938`.

**Not covered here:** Maltese pension schemes (other than the treaty point in step 6), US Social Security (treaty art. 17(2) gives the US the sole right to tax it, see the treaty), US government pensions (treaty art. 19), annuities bought for value (art. 17(3)), Malta-domiciled or worldwide-basis individuals except where the exclusion in step 7 moves a person there, and the special residence programmes (see `mt-non-dom`).

## Ask the client first

- Which basis year are we working on? Are you resident, ordinarily resident and not domiciled in Malta in that year (see `mt-non-dom`)?
- Are you a US citizen, a green card holder, a former citizen or former long-term resident (and when did that status end), or a non-citizen with US accounts?
- Which accounts do you hold (traditional IRA, Roth IRA, 401(k), Roth 401(k), other), and how were they funded: cash contributions only, rollovers from another US plan, or anything else?
- In the year, did you convert, roll over or withdraw anything? How much, from which account, and where was the money paid: a US account, a third-country account or a Maltese account? How much of it was later brought into Malta?
- Are you married or in a civil union? Is your spouse ordinarily resident **and** domiciled in Malta? Are you taxed jointly (the default), with a separate computation under art. 50, or with a separate return election under art. 49A?
- Have you made or received a gift between spouses? When, from which account to which account, in whose name, with what written record, and what was done with the money afterwards?
- Do you hold long-term resident status, a permanent residence certificate or a permanent residence card? Have you applied for one? Are you, or is your spouse, an EU, EEA or Swiss citizen, and for how many continuous years have you lived in Malta legally?

## The method, step by step

All Malta steps apply the [Income Tax Act, Cap. 123](https://legislation.mt/eli/cap/123/eng/pdf). Treaty steps apply the Convention set out in the [Double Taxation Relief (Taxes on Income) (United States of America) Order, S.L. 123.123](https://legislation.mt/eli/sl/123.123/eng/pdf), which is Malta's official text of the treaty.

1. **Confirm the person is on the remittance basis.** Apply steps 1 to 4 of `mt-non-dom`. If the person is a long-term resident or holds a permanent residence certificate or card (step 7 below), or the spouse is ordinarily resident and domiciled in Malta, the remittance basis does not apply: every distribution and conversion is tested on the worldwide basis, and only the treaty (step 5) can take it out of Malta tax.
2. **List every account event in the year.** For each event record: account type, date, amount in euro at the date, US tax treatment (taxable, partly taxable or tax-free in the US, from the US skills), the account it was paid to, and every later transfer into Malta.
3. **Roth conversion (traditional IRA to Roth IRA).**
   - Under Malta domestic law, the Act does not say whether a conversion is income at all. It is not a payment to the person; it moves value from one US retirement account to another. If it is income, it is income arising outside Malta, and art. 4(1) proviso (i) taxes it only on "the amount received in Malta". A conversion that stays inside US retirement accounts puts nothing into Malta, so no Malta tax is payable on it under proviso (i).
   - Treaty art. 18 points the same way: income earned by a US pension fund "may be taxed as income of that individual only when, and ... to the extent that, it is paid to, or for the benefit of, that individual from the pension fund (and not transferred to another pension fund in that other State)". A Roth IRA is a US pension fund for the treaty (Treasury Technical Explanation, art. 3). So a conversion is, on the treaty's words, a transfer to another US pension fund, which Malta may not tax as the person's income. This is a reading of art. 18, not a ruling; no MTCA guidance or court decision on conversions was found.
   - **The EUR 35,000 test.** Art. 56(27)(ii) counts income "arising outside Malta and referred to in proviso (i) ... which is not received or not fully received in Malta". Whether a conversion counts is not settled. The cautious position, used in this skill unless written advice says otherwise, is to count the taxable amount of the conversion as foreign income not received in Malta. On that position a large conversion alone can bring an ordinarily resident non-dom into the EUR 5,000 minimum tax (Worked case 1). The opposite position (art. 18, or that a conversion is not income) keeps it out. Get written advice before relying on the lower figure.
   - The US tax on the conversion is not creditable in Malta when no Malta tax is charged on it: Malta relief is given only against Malta tax on the same income (`mt-non-dom`, double tax relief).
4. **Later distributions.** Treat each distribution as foreign income (a pension or annual payment under art. 4(1)(d), or other gains under art. 4(1)(g); the Act does not say which for a US account). Then:

   | Distribution | Kept outside Malta | Brought into Malta |
   |---|---|---|
   | Traditional IRA or 401(k), taxable part | Not taxed in Malta (proviso (i)); counts towards the EUR 35,000 test | Taxed at the resident rates on the amount received, grossed up for any creditable US tax (see step 6) |
   | Traditional IRA, part that is a return of non-deductible contributions (basis) | Exempt in Malta (treaty art. 17(1)(b)) | Exempt in Malta (art. 17(1)(b)) |
   | Qualified Roth IRA or Roth 401(k) distribution | Exempt in Malta (art. 17(1)(b)) | Exempt in Malta (art. 17(1)(b)) |
   | Non-qualified Roth distribution | The part the US would tax for a US resident is not exempt: treat as a traditional distribution; the part the US would not tax is exempt (art. 17(1)(b)) | same split |
   | Direct rollover to another US IRA or plan, not taxed in the US | Exempt in Malta (art. 17(1)(b)) and not paid to the person (art. 18) | Not applicable: nothing is paid out |

   Art. 17(1)(b) exempts "the amount of any such pension ... that, when received, would be exempt from taxation in that State if the beneficial owner were a resident thereof". The Treasury Technical Explanation gives the Roth IRA, the basis in a traditional IRA and a tax-free rollover to another US IRA as examples, and says the article covers both periodic and single-sum payments. Whether the US would exempt an amount is a US question: take it from `us-ira-and-roth-conversions-8606`.

   Whether a distribution that Malta must exempt under art. 17(1)(b) still counts towards the EUR 35,000 test is not settled. The Act counts income "referred to in proviso (i)"; an amount the treaty exempts is arguably not chargeable income at all. Run the test both ways and say which one the computation uses.
5. **What the treaty does and does not change for a remittance-basis non-dom.**
   - **It does not create a Malta charge.** Art. 17(1)(a) says pensions of a Malta resident "shall be taxable only in" Malta. That allocates the right to tax; Malta still taxes only under its own law, so a remittance-basis non-dom is still taxed only on what is received in Malta. Art. 1(2) confirms the treaty does not restrict any benefit under the laws of either state.
   - **It does take amounts out of Malta tax.** Art. 17(1)(b) (Roth, basis, tax-free rollovers) and art. 18 (no tax on the build-up inside a US pension fund until it is paid out, and not on a transfer to another US pension fund) bind Malta even for its own residents and for US citizens: art. 1(5)(a) lists art. 17(1)(b), art. 18 and art. 23 as exceptions to the saving clause.
   - **The saving clause.** Art. 1(4): the treaty "shall not affect the taxation by a Contracting State of its residents ... and its citizens", and a former citizen or former long-term resident "may, for the period of ten years following the loss of such status, be taxed" by that state under its own law. So the US keeps taxing a US citizen in Malta on IRA distributions and conversions under US law. The US side is in `us-citizen-moving-abroad-tax`.
   - **A non-citizen and the remittance basis.** Art. 22(7): where income arising in one state is relieved from tax there under the treaty and the other state taxes it only on "the amount thereof which is remitted to or received in" that state, the first state's relief "shall apply only to so much of the income or gains as is taxed in the other Contracting State". For a non-citizen Malta resident (not a former citizen within ten years), this means the US exemption for an IRA distribution under art. 17(1)(a) may be limited to the part that Malta actually taxes, which for a non-dom is the part brought into Malta. The US withholding and claim procedure is a US question: refer.
6. **Double tax relief on a distribution brought into Malta.** Art. 23(2) of the treaty gives a credit for US tax on US-source income included in a Malta assessment, under Malta law (Cap. 123 arts. 76 to 78, see `mt-non-dom`). For a **US citizen** resident in Malta, art. 23(4)(a) limits the Malta credit to the US tax that the US could impose under the treaty on a Malta resident who is not a US citizen, "other than taxes that may be imposed solely by reason of citizenship". Because art. 17(1)(a) gives Malta the sole right to tax a private pension of a non-citizen resident, that figure is in principle nil for a taxable IRA or 401(k) distribution: Malta gives no credit for the US tax, and art. 23(4)(b) and (c) make the US give the credit for the Malta tax instead. Confirm the US credit in `us-citizen-moving-abroad-tax`.
7. **Check the long-term resident and permanent residence exclusion every year.** The second "sohowever" proviso to art. 4(1) removes provisos (i) and (ii) for "an individual who is a long-term resident, or who holds a permanent residence certificate or a permanent residence card, in respect of any income derived by such individual in the year of being granted long-term resident status or the right of permanent residence and in subsequent years". See "Long-term resident and permanent residence" below.
8. **If there is a gift between spouses,** follow "Gifts between spouses" below before deciding what was received in Malta.
9. **Compute and test the minimum.** Malta-source income plus foreign income received in Malta, less treaty-exempt amounts, at the resident rates; then the EUR 35,000 test and EUR 5,000 minimum and the worldwide cap, all as in `mt-non-dom`. State which position was taken on the conversion and on treaty-exempt amounts in the test.

### Rates, bands and thresholds

| Item | Figure and conditions | Tax year | Source |
|---|---|---|---|
| Remittance basis, Cap. 123 art. 4(1) proviso (i) | foreign income of a person "not ordinarily resident in Malta or not domiciled in Malta" taxed "on the amount received in Malta" | Current | https://legislation.mt/eli/cap/123/eng/pdf |
| Exclusion, art. 4(1) second and third provisos | long-term resident or holder of a permanent residence certificate or card: provisos (i) and (ii) do not apply from the year of grant; spouse ordinarily resident and domiciled in Malta: same | Current | same |
| Non-dom minimum tax, art. 56(27) | EUR 5,000 a year where foreign income of at least EUR 35,000 (both spouses, if taxed jointly under art. 49) is not received or not fully received in Malta; tax before relief under arts. 76 to 89 | YA 2019 onwards, unchanged for YA 2027 | same |
| Treaty in force, S.L. 123.123 art. 2(c) | entered into force 23 November 2010; for taxes other than withholding, effective for taxable periods beginning on or after 1 January 2011 (Convention art. 28(2)(b)) | Current | https://legislation.mt/eli/sl/123.123/eng/pdf |
| Treaty art. 17(1)(a) | private pensions of a Malta resident taxable only in Malta, subject to the saving clause for US citizens (art. 1(4)) | Current | same |
| Treaty art. 17(1)(b) | Malta must exempt any pension amount the US would exempt for a US resident (Roth, basis, tax-free rollover); excepted from the saving clause by art. 1(5)(a) | Current | same |
| Treaty art. 18 | income of a US pension fund taxed by Malta only when paid to the member, not on a transfer to another US pension fund; excepted from the saving clause | Current | same |
| Treaty art. 1(4) | former citizen or former long-term resident may be taxed by that state for ten years after losing the status | Current | same |
| Competent authority arrangement, 30 Nov and 3 Dec 2021 | a fund that may take non-cash contributions, or does not limit contributions by earned income (except a qualified rollover from a pension fund in the same state), is not a treaty "pension fund"; US citizens and residents may not claim art. 17(1)(b) or art. 18 for it, including a Maltese personal retirement scheme under the Retirement Pensions Act of 2011 | From signature; stated to reflect original intent | https://www.irs.gov/pub/irs-lbi/malta-competent-authority-arrangement-pension-funds.pdf |
| Long-term resident status, S.L. 217.05 reg. 4(1) | granted by the Director on application, after five years of legal and continuous residence before the application | Current | https://legislation.mt/eli/sl/217.5/eng/pdf |
| EU citizen permanent residence, S.L. 460.17 art. 6(1) and art. 7(8) | the right arises after five years of continuous legal residence; the certificate is issued on application as proof | Current | https://legislation.mt/eli/sl/460.17/eng/pdf |

### The 2021 competent authority arrangement: what changed

The treaty defines a "pension fund" in art. 3(1)(k): for the US, a person "generally exempt from income taxation"; for Malta, "a licensed fund or scheme subject to tax only on income derived from immovable property situated in Malta"; in both cases "operated principally ... to administer or provide pension or retirement benefits" or to earn income for such funds.

In 2021 the competent authorities agreed, under art. 25(3), that a fund, scheme or arrangement established in either state that "is allowed to accept contributions from a participant in a form other than cash" or "does not limit contributions by reference to earned income from personal services (including self-employment) of the participant or the participant's spouse", except in the case of a qualified rollover from a pension fund in the same state, is not a pension fund. Its distributions are not "pensions or other similar remuneration" for art. 17(1)(b). US citizens and residents may not claim art. 17(1)(b) or art. 18 for such a fund, "including a personal retirement scheme established in Malta under the Retirement Pensions Act of 2011". The arrangement says it reflects "the original intent" of the two states.

What this means for this skill:

- **It was aimed at Maltese personal retirement schemes used by US persons.** A US person cannot get the Roth-style exemption in Malta by moving savings into such a Maltese scheme. The treaty's Technical Explanation already said a rollover to a pension fund in the other state is not covered by art. 17(1)(b).
- **Its test is written for funds in either state.** On its words it would also catch a US account that could take non-cash contributions or had no earned-income limit, other than through a qualified rollover from another US pension fund. Whether a particular US account meets the test (cash contributions only, limited by compensation, or funded by qualified rollovers) is a US-law question: take it from `us-ira-and-roth-conversions-8606`. If it fails the test, art. 17(1)(b) and art. 18 are not available and the account is treated as an ordinary foreign investment: income and gains inside it are tested under Malta law year by year. Refer that case.
- **It does not change** art. 17(1)(a), art. 22(7), art. 23 or the Malta remittance basis.

### Gifts between spouses

**The question.** Spouse A receives foreign retirement income outside Malta. A makes a completed cash gift of it, outside Malta, to spouse B. B invests it outside Malta. Later B transfers money into Malta. Is that a remittance of A's income?

**What the law says.**

- Art. 4(1) proviso (i) taxes foreign income of a remittance-basis person "on the amount received in Malta". The Act does not say who must bring it in, and does not define "received in Malta" for art. 4. The only definition, in art. 56(2)(d) ("the excess of the amount of income arising outside Malta and received in Malta over any sum transferred out of Malta"), is stated to apply only in paragraphs (a) to (c) of that sub-article.
- A gift is not one of the heads of income in art. 4(1)(a) to (g). In B's hands, a gift is capital.
- MTCA's remittance-basis guidance, section 5: "Income is received in Malta if it is paid to the recipient in Malta. Income paid into an account held abroad is also treated as received in Malta if it is subsequently remitted to Malta." Section 5.2: proceeds of a capital nature "are not income and the receipt in Malta is not captured". Section 5.3: remittances "for ordinary expenses, such as living expenses, are presumed to be remittances of income unless proven otherwise, regardless of the foreign account out of which the remittance is made"; remittances for a capital purpose are capital if the person shows they come from money held abroad as capital. The guidance does not deal with transfers between spouses.
- **Joint computation (art. 49, the default).** "The income of a married couple, where both spouses are living together, shall be charged to tax in the name of the responsible spouse"; both spouses are "jointly and severally responsible". The couple's income is one charge. Art. 56(27)(ii) counts the foreign income "derived by both spouses" for the EUR 35,000 test. A transfer inside the couple does not change whose return the income sits on, so the Commissioner could treat money B brings in as the couple's foreign income received in Malta, especially if it pays household costs (section 5.3 presumption).
- **Separate computation (art. 50).** Only the other spouse's employment income and "pension which is received in view of the past employment" can be computed separately; all other income is aggregated with the higher earner's, and the tax is still "charged in the name of the responsible spouse". It does not make the spouses separate taxpayers. Whether a distribution from an IRA funded by a rollover from an employer plan is a pension "in view of the past employment" is not settled.
- **Separate return election (art. 49A).** Each spouse is charged separately, and "the income of a spouse shall comprise all income derived by that spouse regardless of any right which the other spouse may have in respect of that income". This is the setting in which the capital reading is strongest: A derived the income, B received a gift. It is still not settled.
- **The spouse exclusion.** The third proviso to art. 4(1) removes the remittance basis from "an individual whose spouse is ordinarily resident and domiciled in Malta". If B is both, A is on the worldwide basis anyway and the gift question does not arise for A's income. The question only matters when both spouses are on the remittance basis (or B is only one of ordinarily resident or domiciled). MTCA guidance section 1.2 adds that in that case the worldwide basis "applies to the income and capital gains of both spouses", and that "spouse" includes a registered civil union partner.
- **Anti-avoidance (art. 51).** Where a scheme that reduces tax "is artificial or fictitious or is in fact not given effect to", the Commissioner disregards it; where its "sole or main purpose" is a tax advantage, the Commissioner may assess so as to "nullify or modify" it. A gift made so that the same money can come back into Malta for the couple's joint spending is exposed to both limbs.
- **Family law.** Whether a gift between spouses is valid and complete, and whether the money stops being shared property, depends on the couple's matrimonial property regime (Maltese Civil Code, Cap. 16, or a foreign law). This skill has not checked that law. Get legal advice on it.

**The answer.** The law does not settle it. Nothing in the Act or MTCA's guidance says that a completed gift outside Malta turns one spouse's foreign income into the other spouse's capital for the remittance basis, and nothing says it does not. The risk is highest under joint computation, where the couple's income is one charge. Do not treat B's later transfer as tax-free capital without **written advice from a Malta tax adviser**, and consider asking the Commissioner in writing before the transfer.

**Documentation that supports the capital position** (it supports the position; it does not guarantee it):

1. A dated written deed or declaration of gift, signed by both spouses, stating the amount, that it is unconditional, and that B owes nothing back. Legal advice on its validity under the couple's matrimonial regime.
2. Bank statements showing the source in A's sole-name account (the distribution in), the transfer out, and receipt in an account in B's sole name, outside Malta, holding nothing else.
3. Evidence that B alone controls and invests the money: account mandates, investment instructions in B's name, no power of attorney for A.
4. A separate account for the income the investment earns (interest, dividends): that income is B's own foreign income, taxable if brought into Malta. B's foreign capital gains on the investment are not taxed (proviso (ii)).
5. Transfers into Malta from the gift-capital account only, for a stated capital purpose (for example a property purchase in B's name), with the paper trail at both ends. Avoid using it for joint living costs (section 5.3 presumption).
6. A yearly schedule, kept with the return, linking each transfer into Malta to its source.
7. A note of the computation both ways (Worked case 3), so the exposure is known.

### Long-term resident and permanent residence

**The rule.** From "the year of being granted long-term resident status or the right of permanent residence", provisos (i) and (ii) do not apply. The whole of that year is on the worldwide basis, not just the part after the grant, and so is every later year. Every conversion and taxable distribution is then charged in Malta as it arises, whether or not brought in, subject only to the treaty (art. 17(1)(b), art. 18) and double tax relief. The EUR 5,000 minimum tax no longer applies, because it needs provisos (i) and (ii) to apply (`mt-non-dom`).

**Which document.** The Act gives the terms the meaning they have in S.L. 217.05 and S.L. 460.17.

| Person | Status that triggers the exclusion | How it is obtained | Source |
|---|---|---|---|
| US citizen (third country national), not a family member of an EU citizen | Long-term resident: "any third country national who has long-term resident status as provided for under regulations 4 to 7" | Granted by the Director on application after five years' legal and continuous residence (reg. 4(1), 4(5)); the status "shall be permanent" (reg. 8(1)) | https://legislation.mt/eli/sl/217.5/eng/pdf |
| EU, EEA or Swiss citizen (for example a dual US-EU national) | Permanent residence certificate | The right arises after five years' continuous legal residence (art. 6(1)); the certificate is issued "as soon as possible after an application" and proof (art. 7(8)) | https://legislation.mt/eli/sl/460.17/eng/pdf |
| Third country national family member of an EU citizen | Permanent residence card | Issued within six months of an application and proof (art. 7(9)) | same |
| EU citizen with only a registration certificate | None: a registration certificate is proof of the ordinary right of residence (art. 2 definition, art. 7(2) and (3)) | Required after three months (art. 7(2)) | same |

**Automatic right versus holding the document.**

- For a US citizen with no EU family link, there is no automatic status: until the Director grants it on an application, the person is not a "long-term resident", whatever the years of residence.
- For an EU citizen, the right of permanent residence arises by law after five years (S.L. 460.17 art. 6(1)), and possession of a certificate "shall under no circumstances be made a pre-condition for the exercise of a right" (art. 7(12)).
- The Act's test names the person who "holds a permanent residence certificate or a permanent residence card". On its words, an EU citizen who has the right but has not applied for and been issued the certificate does not hold one and is not caught. MTCA guidance section 1.2 uses the same document-based words: persons "in possession of a permanent residence certificate or a permanent residence card".
- **Not settled:** (1) for a person who holds a certificate, whether "the year of being granted ... the right of permanent residence" means the year the certificate is issued or the earlier year the right arose by law after five years, which could reach back to years already filed; (2) whether the Commissioner could argue that the right alone is enough. No court decision or MTCA statement on either point was found.
- **Practical rule:** treat the year the certificate, card or status is issued as caught in full. Before anyone applies, model the worldwide-basis cost of that year and later years (conversions and distributions included) and get written advice on the look-back point. Applying is the person's choice; the exclusion follows from it.
- The Malta Permanent Residence Programme certificate is issued under S.L. 217.26, not under either instrument above; see `mt-permanent-residence-programme`.

## Boundary and exception table

| Situation | Result | Rule |
|---|---|---|
| Roth conversion, nothing paid out of US retirement accounts | No Malta tax on it under the remittance basis; whether it counts for the EUR 35,000 test is not settled (cautious: count it) | Cap. 123 art. 4(1) proviso (i), art. 56(27); treaty art. 18 |
| Traditional IRA distribution kept outside Malta | Not taxed in Malta; counts towards the EUR 35,000 test | art. 4(1) proviso (i), art. 56(27) |
| Traditional IRA distribution brought into Malta | Taxed on the amount received at the resident rates; no Malta credit for US tax on a US citizen in principle | art. 4(1) proviso (i); treaty arts. 17(1)(a), 23(4) |
| Return of non-deductible contributions | Exempt in Malta, brought in or not | treaty art. 17(1)(b) |
| Qualified Roth distribution | Exempt in Malta, brought in or not; inclusion in the EUR 35,000 test not settled | treaty art. 17(1)(b) |
| Tax-free direct rollover between US accounts | Not taxed in Malta | treaty arts. 17(1)(b), 18 |
| US account that can take non-cash contributions or has no earned-income limit | Not a treaty pension fund; no art. 17(1)(b) or 18; refer | 2021 competent authority arrangement |
| Maltese personal retirement scheme of a US person | No art. 17(1)(b) or art. 18 benefit | 2021 competent authority arrangement |
| Non-citizen Malta resident, IRA distribution kept outside Malta | US treaty exemption may be limited to the part Malta taxes; refer the US side | treaty art. 22(7) |
| Former US citizen within ten years of expatriation | The US may still tax under its own law | treaty art. 1(4) |
| Spouse ordinarily resident and domiciled in Malta | Worldwide basis; the gift question does not arise | art. 4(1) third proviso |
| Completed gift between spouses outside Malta, recipient later brings money in | Not settled; risk of being treated as a remittance of the couple's income, highest under joint computation; get written advice | arts. 4(1), 49, 49A, 50, 51; MTCA guidance s. 5 |
| Long-term resident status or permanent residence certificate or card issued in 2026 | Worldwide basis for all of 2026 and later; no EUR 5,000 minimum | art. 4(1) second proviso |
| EU citizen, more than five years in Malta, no certificate applied for | Not caught on the words of the Act; look-back on a later certificate not settled | art. 4(1) second proviso; S.L. 460.17 arts. 6, 7 |
| US citizen, more than five years in Malta, no application | Not a long-term resident until status is granted | S.L. 217.05 regs. 2, 4 |

## Worked cases

Basis year 2026 (year of assessment 2027). Rates: the year of assessment 2027 tables in [Cap. 123 art. 56(1)](https://legislation.mt/eli/cap/123/eng/pdf), as set out in `mt-non-dom` and `malta-income-tax`: single, 0% to EUR 12,000, 15% band to EUR 16,000 less EUR 1,800, 25% band to EUR 60,000 less EUR 3,400, 35% above less EUR 9,400; married joint with no qualifying child, 0% to EUR 15,000, 15% band to EUR 23,000 less EUR 2,250, 25% band to EUR 60,000 less EUR 4,550. Invented people and round euro figures. No exclusion applies in any case unless stated. These are examples; check every fact before relying on them.

**Case 1: Roth conversion, single person (a decision on the EUR 35,000 test).**
- Facts: Dana, a single US citizen, ordinarily resident and not domiciled in Malta. In 2026 she converts EUR 100,000 from a traditional IRA to a Roth IRA (all taxable in the US, no basis). Foreign dividends EUR 10,000, of which EUR 8,000 is brought into Malta. No Malta income.
- Chargeable in Malta: EUR 8,000. Tax at the single table: nil (below EUR 12,000).
- **Cautious position (conversion counted):** foreign income EUR 110,000, at least EUR 35,000 and not fully received in Malta. Minimum tax applies: top-up EUR 5,000. Cap check: worldwide EUR 110,000 at 35% less EUR 9,400 = EUR 29,100, not below EUR 5,000. Tax EUR 5,000.
- **Treaty position (conversion not counted, art. 18):** foreign income EUR 10,000, below EUR 35,000. No minimum tax. Tax nil.
- The difference is EUR 5,000. Use the cautious figure unless written advice supports the treaty position. The US tax on the conversion earns no Malta credit, because Malta charges no tax on it.

**Case 2: married couple, distributions kept out and brought in.**
- Facts: Alex and Blair, married, taxed jointly, no qualifying children, both ordinarily resident non-doms, both US citizens. Alex takes a EUR 40,000 traditional IRA distribution (all taxable in the US) into a US account and brings EUR 20,000 into Malta. Blair takes a EUR 30,000 qualified Roth distribution and keeps it in the US.
- Blair's Roth distribution is exempt in Malta under art. 17(1)(b).
- Chargeable: EUR 20,000. Joint table: EUR 20,000 at 15% less EUR 2,250 = EUR 750.
- EUR 35,000 test: Alex's EUR 40,000 alone is at least EUR 35,000 and not fully received, so the result does not turn on whether the Roth amount counts. Top-up EUR 5,000 less EUR 750 = EUR 4,250.
- Cap check (Roth exempt, so left out): worldwide EUR 40,000 at 25% less EUR 4,550 = EUR 5,450, not below EUR 5,000. Tax EUR 5,000.
- No Malta credit for the US tax on Alex's distribution (treaty art. 23(4)(a)); the US credit for the Malta tax is in `us-citizen-moving-abroad-tax`.
- If Alex had brought in all EUR 40,000: tax EUR 5,450 on the joint table. Whether the minimum still applies then turns on whether Blair's exempt Roth amount is "not received" foreign income; either way the tax is EUR 5,450, because it is above EUR 5,000.

**Case 3: gift between spouses, the two readings.**
- Facts: Casey and Drew, married, taxed jointly, no qualifying children, both ordinarily resident non-doms. In February 2026 Casey takes a EUR 50,000 traditional IRA distribution into Casey's sole US account. In March Casey gives EUR 50,000 to Drew by signed deed, into Drew's sole-name account outside Malta. In October Drew brings EUR 50,000 into Malta to pay towards a flat in Drew's name. No other income.
- **Capital reading:** nothing of the couple's foreign income is received in Malta. Foreign income EUR 50,000, not received. Minimum tax applies: EUR 5,000. Cap check: worldwide EUR 50,000 at 25% less EUR 4,550 = EUR 7,950, not below EUR 5,000. Tax EUR 5,000.
- **Remittance reading:** the couple's foreign income of EUR 50,000 is received in Malta in full. Tax EUR 50,000 at 25% less EUR 4,550 = EUR 7,950. The foreign income is fully received, so the minimum tax does not apply.
- The difference is EUR 2,950. The law does not settle which reading is right; get written advice before filing on the capital reading, and keep the documentation listed above.

### Executable worked checks

```oa-check
name: Rothconversioncountedforthe35000testsingle
inputs:
  remitted_dividends: 8000
  conversion: 100000
  dividends_total: 10000
steps:
  - ordinary_tax: max(remitted_dividends - 12000, 0)
  - foreign_total: conversion + dividends_total
  - top_up: max(5000 - ordinary_tax, 0)
  - worldwide_tax: foreign_total * 0.35 - 9400
  - liability: min(ordinary_tax + top_up, worldwide_tax)
expected:
  ordinary_tax: 0
  foreign_total: 110000
  top_up: 5000
  worldwide_tax: 29100
  liability: 5000
```

```oa-check
name: Jointcoupleiraremittedrothexempt
inputs:
  ira_remitted: 20000
  ira_total: 40000
steps:
  - ordinary_tax: ira_remitted * 0.15 - 2250
  - top_up: max(5000 - ordinary_tax, 0)
  - worldwide_tax: ira_total * 0.25 - 4550
  - liability: ordinary_tax + top_up
expected:
  ordinary_tax: 750
  top_up: 4250
  worldwide_tax: 5450
  liability: 5000
```

```oa-check
name: Giftbetweenspousestworeadings
inputs:
  distribution: 50000
steps:
  - capital_reading: 5000
  - remittance_reading: distribution * 0.25 - 4550
  - difference: remittance_reading - capital_reading
expected:
  remittance_reading: 7950
  difference: 2950
```

## When to refuse or refer

Articles cited below are in the [Income Tax Act, Cap. 123](https://legislation.mt/eli/cap/123/eng/pdf) and the treaty in [S.L. 123.123](https://legislation.mt/eli/sl/123.123/eng/pdf).

- Refuse to give a final figure without the basis year, residence, domicile and ordinary residence, the spouse's domicile and ordinary residence, any long-term resident or permanent residence status, and the US tax treatment of each account event.
- Refer, and say the point is not settled, before relying on: the treaty position that a conversion is outside the EUR 35,000 test; leaving a treaty-exempt amount out of that test; the capital reading of a gift between spouses; the year a permanent residence certificate first bites.
- Refer any US account that may fail the 2021 competent authority test (non-cash contributions, no earned-income limit), any plan of moving US retirement money into a Maltese scheme, and any Maltese pension scheme of a US person.
- Refer non-citizens with US accounts (art. 22(7) and US withholding), former citizens and former long-term residents (art. 1(4)), US government pensions (art. 19) and Social Security (art. 17(2)).
- Refer every gift or transfer between spouses that is followed by money coming into Malta, and any arrangement that could fall under art. 51.
- Refer any question on applying for long-term resident status or a permanent residence certificate or card, and the immigration side of it, to a Maltese lawyer or licensed agent.
- Send every US filing question to the US skills named in Scope.

## Filing and payment

- The Malta return, self-assessment, payment date, interest and late-filing charges are as in `mt-non-dom` (basis year 2026: 30 June 2027).
- Declare foreign income received in Malta and any minimum-tax top-up in the return. Keep, with the working papers, the account-event list from step 2, the transfer schedule, the treaty position taken on each item, and any gift documentation.
- A treaty credit claim must be made within two years after the end of the year of assessment (`mt-non-dom`, art. 77(9)).
- US returns, FBAR and Form 8938 are filed separately: see `us-citizen-moving-abroad-tax` and `us-fbar-and-fatca-8938`.

## Completion checklist

- The person is confirmed on the remittance basis for the year: no long-term resident status, no permanent residence certificate or card, no spouse who is ordinarily resident and domiciled in Malta.
- Every account event is listed with its US treatment, where it was paid and what came into Malta.
- Conversions: no Malta tax unless something reached Malta; the position on the EUR 35,000 test is stated.
- Distributions: treaty-exempt amounts (Roth, basis, tax-free rollovers) are identified; taxable amounts brought into Malta are charged.
- Each account passes the 2021 competent authority test, or the case is referred.
- Double tax relief follows treaty art. 23(4) for a US citizen.
- Any gift between spouses has been analysed both ways, with the documentation on file and written advice obtained.
- The EUR 35,000 test, EUR 5,000 minimum and worldwide cap are run as in `mt-non-dom`.
- The output is labelled as an estimate until reviewed.

## Sources

| Source | URL | Read on |
|---|---|---|
| Income Tax Act, Cap. 123: read for art. 4(1) heads (a) to (g), provisos (i) and (ii) and both "sohowever" provisos; arts. 49, 49A, 50 (married couples); art. 51 (tax avoidance); art. 56(2)(d) (definition of "received in Malta", limited to that sub-article); art. 56(27) (minimum tax) | https://legislation.mt/eli/cap/123/eng/pdf | 2026-11-23 |
| Double Taxation Relief (Taxes on Income) (United States of America) Order, S.L. 123.123 (L.N. 560 of 2010), with the Convention in the Schedule: read for art. 2(c) (in force 23 November 2010) and Convention arts. 1(2), 1(4), 1(5), 3(1)(k), 17, 18, 22(7), 23 and 28 | https://legislation.mt/eli/sl/123.123/eng/pdf | 2026-11-23 |
| Competent Authority Arrangement on the meaning of "pension fund" (US 30 November 2021, Malta 3 December 2021): read in full | https://www.irs.gov/pub/irs-lbi/malta-competent-authority-arrangement-pension-funds.pdf | 2026-11-23 |
| US Treasury, Technical Explanation of the Convention signed 8 August 2008: read for art. 1(4) and (5), art. 3 (US pension funds, including Roth IRAs), art. 17(1), art. 18 and art. 22(7). The Treasury link no longer resolves; read from a copy of the Treasury text at the URL shown | https://freemanlaw.com/wp-content/uploads/2020/07/temalta09.pdf | 2026-11-23 |
| US Treasury press release of 23 November 2010: read for entry into force and the 1 January 2011 effective dates | https://home.treasury.gov/news/press-releases/tg978 | 2026-11-23 |
| MTCA, Guidance Note on the Remittance Basis of Taxation for Individuals: read in a browser (the site blocks scripts) for sections 1 to 6, in particular 1.2 (worldwide basis for long-term and permanent residents and spouses; footnote: spouse includes a civil union partner), 5.1 to 5.3 (received in Malta) and 6.3 (couple's EUR 35,000 threshold) | https://mtca.gov.mt/docs/default-source/documents/mtca-guidelines-on-the-remittance-under-the-income-tax.pdf | 2026-11-23 |
| Status of Long-Term Residents (Third Country Nationals) Regulations, S.L. 217.05: read for reg. 2 (definitions), reg. 4 (grant after five years), reg. 8 (status permanent) | https://legislation.mt/eli/sl/217.5/eng/pdf | 2026-11-23 |
| Free Movement of European Union Nationals and their Family Members Order, S.L. 460.17: read for art. 2 (definitions of registration certificate, permanent residence certificate and card), art. 6 (right of permanent residence) and art. 7 (certificates and cards, art. 7(12)) | https://legislation.mt/eli/sl/460.17/eng/pdf | 2026-11-23 |

Not yet confirmed: whether a Roth conversion is income for Malta at all, and whether it counts towards the EUR 35,000 test (no MTCA guidance or court decision found; the cautious position counts it); whether an amount exempt under treaty art. 17(1)(b) counts towards that test; whether an IRA distribution is a pension under art. 4(1)(d) or other gains under art. 4(1)(g), and whether an IRA funded from an employer plan is a pension "in view of the past employment" for art. 50; whether a completed gift between spouses outside Malta stops a later transfer into Malta being a remittance of the donor's or the couple's income (the Act and MTCA guidance do not address it); the validity of gifts between spouses under the Maltese Civil Code or a foreign matrimonial regime (not read); for a permanent residence certificate, whether the first year caught is the year of issue or the earlier year the right arose, and whether the right alone is enough; how US authorities apply treaty art. 22(7) to a non-citizen's IRA distributions (US side, not read); whether MTCA has issued any statement on the 2021 competent authority arrangement (the MTCA news page of 21 December 2021 was not read).
