---
name: us-fbar-and-fatca-8938
description: Tier 2 US federal content skill for the dual foreign financial account disclosure regimes — FinCEN Form 114 (FBAR) under 31 USC §5314 and Form 8938 (FATCA) under IRC §6038D. Covers tax year 2025 including the $10,000 aggregate FBAR threshold (per Bittner 2023 non-willful penalty is per-form not per-account), Form 8938 specified person and SFFA thresholds ($50k/$100k/$200k/$400k tiers), the differences in coverage (signature authority for FBAR, ownership for 8938, qualifying foreign mutual funds potentially reportable under both regimes), willful and non-willful penalty severity, and the Streamlined Foreign Offshore / Domestic Offshore compliance paths for catching up.
jurisdiction: US
tax_year: 2025
last_updated: 2026-11-25
version: "1.1"
source_checked: 2026-10-16
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
reviewed_by: "James Wallach"
reviewed_on: 2026-11-03
tier: 1
domain: cross-border
---

# US Fbar And FATCA 8938

## US FBAR + FATCA Form 8938 — Foreign Financial Account Disclosure (Tax Year 2025)

> **Correction draft for tax year 2025.** Independent source review and accountant approval of this changed version are pending. The retained approval metadata does not certify this draft. Passages explicitly marked as non-usable holds do not establish a filing or tax position.

## 1. Scope and Purpose

**Non-usable hold:** The separate regimes are confirmed; demographic/prevalence claims elsewhere are held.

This skill covers the two overlapping but legally distinct foreign financial account disclosure regimes that apply to US persons for tax year 2025:

1. **FinCEN Form 114** — the Report of Foreign Bank and Financial Accounts ("FBAR"), administered by the Financial Crimes Enforcement Network (FinCEN) of the US Treasury under the Bank Secrecy Act (31 USC §5314 and 31 CFR §1010.350).
2. **Form 8938** — the Statement of Specified Foreign Financial Assets, administered by the IRS under the Foreign Account Tax Compliance Act (FATCA), codified at IRC §6038D.

**Non-usable hold:** The prevalence assertion in this paragraph is unverified; apply each filing test separately.

These are two separate filings with overlapping but materially different scopes, thresholds, due dates, and penalty regimes. The vast majority of US persons with non-trivial offshore exposure must file **both**. They are not substitutes for one another and one does not satisfy the obligation of the other.

This skill is loaded alongside `us-tax-workflow-base` v0.2+. It is federal-only. It does **not** address:
- State income tax treatment of foreign account income (see state skills);
- The substantive income tax treatment of foreign earnings (see `us-foreign-earned-income-2555` and `us-foreign-tax-credit-1116`);
- The Passive Foreign Investment Company (PFIC) regime under IRC §1291 and Form 8621 in computational depth — this skill flags PFIC issues and refers out;
- Form 5471 (controlled foreign corporations), Form 8865 (controlled foreign partnerships), Form 3520/3520-A (foreign trusts and large foreign gifts) — these are separate disclosure regimes;
- Pre-immigration tax planning, expatriation under §877A, or covered-expatriate filings.

> **AUDIT FLASH POINT.** The combination of FBAR and Form 8938 is the single most common source of catastrophic-penalty exposure for US persons of immigrant origin. Penalties for non-compliance routinely exceed the underlying tax liability by orders of magnitude. Treat every client with foreign-sounding ties — birthplace abroad, family abroad, work abroad, pension abroad, inheritance abroad — as presumptively in scope until you have ruled it out in writing.

## 2. The Two Regimes at a Glance

**The Two Regimes at a Glance**  _(31 USC §5314; 31 CFR §1010.350; IRC §6038D; Treas. Reg. §1.6038D)_

| Feature | FBAR (FinCEN Form 114) | Form 8938 (FATCA) |
| --- | --- | --- |
| Authority | 31 USC §5314; 31 CFR §1010.350 | IRC §6038D; Treas. Reg. §1.6038D |
| Administrator | FinCEN (Treasury) | IRS |
| Filing platform | BSA E-Filing System | Attached to Form 1040 |
| Threshold | More than $10,000 aggregate of annual account maxima | $50k–$600k depending on filing status and residence |
| Who | "US person" with financial interest OR signature authority | "Specified person" with ownership of SFFAs |
| Foreign real estate | Out of scope | Out of scope (when held directly) |
| Foreign mutual funds held by foreign broker | Test reportable account and applicable exemptions | Test SFFA and return/threshold conditions; PFIC classification separately required |
| Foreign pensions | Generally in scope | In scope |
| Cash-value foreign life insurance | In scope | In scope |
| Signature authority only | **In scope** | **Out of scope** |
| Due date | April 15, automatic extension to October 15 | April 15 with return; October 15 with Form 4868 |
| Non-willful civil penalty (max) | $16,536 per report per year for penalties assessed on or after January 17, 2025; check the applicable assessment-date table ([31 CFR 1010.821](https://www.ecfr.gov/current/title-31/section-1010.821)) | $10,000 + $50,000 continuing |
| Willful civil penalty | Greater of $165,353 or 50% of the violation-date account balance for penalties assessed on or after January 17, 2025; ceiling, subject to discretion ([31 CFR 1010.821](https://www.ecfr.gov/current/title-31/section-1010.821)) | Accuracy penalty: 40% of attributable tax underpayment ([instructions](https://www.irs.gov/instructions/i8938)) |
| Criminal | Up to $250,000 + 5 years ordinarily; enhanced limb in §6.4 | Criminal penalties possible; exhaustive statutory classification held |
| Statute of limitations | Generally 6 years from the violation; protective dates and consent need review (§6.1) | Six years for more than $5,000 omitted gross income attributable to specified assets, irrespective of Form 8938 thresholds/exceptions; separate information-failure rule ([IRC 6501](https://uscode.house.gov/us/usc/119-124/t26/s6501/)) |

**Non-usable hold:** The examples require the separate filing and asset facts; the prevalence conclusion is unverified.

The threshold gap is wide: a single $11,000 foreign checking account triggers FBAR but not Form 8938. A married-joint US-resident couple with $90,000 spread across foreign accounts triggers FBAR but not 8938. Above the 8938 thresholds, both forms are almost always required because nearly every SFFA is also an FBAR-reportable account.

## 3. FBAR — FinCEN Form 114

### 3.1 Statutory basis

**Non-usable hold:** The full section 5314 statutory text/history was not independently read; the implementing rule is separately cited.

- **BSA authorizing statute** — The Bank Secrecy Act authorizes the Secretary of the Treasury to require reports of "transactions or relationships" with foreign financial agencies.  _(31 USC §5314)_
- **Implementing regulation requirement** — Requires each US person having a financial interest in, or signature or other authority over, a bank, securities, or other financial account in a foreign country to report such relationship to the Commissioner of Internal Revenue for each year in which such relationship exists.  _(31 CFR §1010.350)_

The form is not filed with the income tax return. It is filed electronically through the BSA E-Filing System operated by FinCEN. There is no paper option for routine filers.

### 3.2 Who must file

- **US person for FBAR purposes** — US citizens (regardless of where they reside); US residents — including green card holders and any individual who meets the substantial presence test of IRC §7701(b); US-formed entities — corporations, partnerships, LLCs (single-member or multi-member regardless of federal tax classification), and trusts and estates formed under US state or federal law.  _(31 CFR §1010.350(b))_
- **Single-member LLC FBAR treatment** — A single-member LLC that is disregarded for federal income tax purposes is not disregarded for FBAR purposes. The LLC files its own FBAR if it meets the threshold. The owner separately files an FBAR for the same accounts if the LLC's accounts are reportable by the owner under the financial-interest test (see §3.5). Joint filers may file a joint FBAR (Form 114a authorization) for accounts they jointly own with a spouse, only if every account the non-filing spouse is required to report is jointly owned with the filing spouse, the filing spouse timely files electronically, and both spouses sign and retain Form 114a. See the [spousal exception](https://www.irs.gov/irm/part4/irm_04-026-016).  _(31 CFR §1010.350(b))_

### 3.3 The $10,000 aggregate threshold

- **FBAR aggregate threshold**: more than $10,000 in the aggregate of each reportable account's maximum value during the calendar year, converted using the reporting year-end rate. The maxima need not occur on the same date. [Source](https://www.fincen.gov/system/files/shared/FBAR%20Line%20Item%20Filing%20Instructions.pdf).
- **Consequences of exceeding threshold** — If aggregate ever exceeds $10,000, every account must be reported — even an account that itself never exceeded $100, and even an account that was closed during the year. The threshold is calendar-year, not tax-year. Fiscal-year entities still apply a calendar-year FBAR. The threshold is per US person, not per account. A US person with five foreign accounts of $2,500 each, all at year-end, has $12,500 aggregate and must file. Currency conversion uses the Treasury Reporting Rate of Exchange in effect at the end of the calendar year (December 31). Use the same rate even for an account that was closed earlier in the year — the rule is "year-end rate applied to the maximum value during the year." Periodic statements may support the maximum only if they fairly reflect the account's maximum value during the year; their availability alone is insufficient. Otherwise use a reasonable approximation of the greatest value. [Source](https://www.fincen.gov/system/files/shared/FBAR%20Line%20Item%20Filing%20Instructions.pdf).  _(31 CFR §1010.350)_

### 3.4 What is a "foreign financial account"

**Non-usable hold:** Gaming/prepaid product classifications and specific pension schemes are held; the general account rule does not settle them.

- **Reportable account categories** — 1. Bank accounts — savings, checking, time deposits, certificates of deposit, demand deposits, fixed deposits, in any foreign bank or financial institution. 2. Securities accounts — brokerage accounts, custodial accounts holding stock or other securities, mutual fund accounts held at a foreign institution. 3. Other financial accounts — including: Foreign mutual fund accounts (counts as a financial account even when individual fund shares are titled to the holder); Cash-value foreign life insurance policies and annuities — the cash surrender value is the reportable amount; Certain foreign pension plans and retirement accounts when the holder has direct access to balance information and the institution acts as a custodian (this is fact-dependent; see §3.7); Online gambling accounts and certain prepaid value accounts where the underlying provider is a foreign financial institution.  _(31 CFR §1010.350(c))_
- **Foreign determined by institution location** — An account is "foreign" when the financial institution is physically located outside the United States — this is institution-location, not account-currency or owner-residence. A US-dollar account at a London branch of a US bank is foreign. A euro-denominated account at a New York branch of Deutsche Bank is not foreign for FBAR purposes (it is held at a US-located branch).  _(31 CFR §1010.350(c))_

### 3.5 Financial interest

- **Financial interest criteria** — The US person is the owner of record or holder of legal title — whether for their own benefit or as agent, nominee, or in another capacity for any other person; The owner of record is acting as agent, nominee, attorney, or in some other capacity on behalf of the US person; A corporation owns the account and the US person owns directly or indirectly more than 50% of the voting power or value; A partnership owns the account and the US person owns directly or indirectly more than 50% of the interest in profits or capital; A trust owns the account and the US person is the grantor and has an ownership interest under §§671–679 (the grantor-trust rules), or has a present beneficial interest in more than 50% of the trust assets, or receives more than 50% of its current income. Check the beneficiary exception where a US trust, trustee or agent files the required FBAR. [Source](https://www.ecfr.gov/current/title-31/subtitle-B/chapter-X/part-1010/subpart-C/section-1010.350).  _(31 CFR §1010.350(e))_

### 3.6 Signature or other authority

- **Signature or other authority definition** — "Signature or other authority" means the authority of an individual (alone or in conjunction with another) to control the disposition of money, funds, or other assets held in a financial account by direct communication (whether in writing or otherwise) to the person with whom the financial account is maintained.  _(31 CFR §1010.350(f))_

Treasurer or CFO of a US company with signing power on the company's foreign bank accounts; US individual serving as trustee of a foreign trust without beneficial interest; US individual serving as attorney-in-fact on an elderly relative's foreign account; Executor of an estate that owns foreign accounts; Spouse listed as authorized signer on a non-US-spouse's foreign account where the US spouse has no ownership.

> **AUDIT FLASH POINT — signature-only authority.** US executives at multinational companies routinely have signature authority on dozens of foreign subsidiary accounts. Signature authority can require reporting without a personal financial stake, subject to the employee exemptions and the modified detail rules for 25 or more accounts. [Source](https://www.ecfr.gov/current/title-31/subtitle-B/chapter-X/part-1010/subpart-C/section-1010.350). Exemption available for certain officers/employees of publicly traded companies and certain regulated entities (31 CFR §1010.350(f)(2)) and for employees of banks examined by federal banking agencies — but the exemption is narrow. Always verify by reference to the regulation rather than assuming.

### 3.7 Foreign pensions — a recurring grey area

**Non-usable hold:** Named plan classifications and unspecified historical guidance remain held; do not infer a filing result from a scheme name.

- **Foreign pension FBAR treatment** — Generally reportable: Defined-contribution accounts held with an identifiable financial institution custodian where the participant directs investments or can ascertain a balance (e.g., Australian superannuation self-managed funds, certain UK SIPPs, Canadian RRSPs held at a brokerage); Indian Public Provident Fund (PPF) accounts when held at an Indian bank; Indian Employees' Provident Fund (EPF) — IRS guidance has historically treated these as reportable. Often not reportable as accounts (though may still be reportable on other forms): Defined-benefit-only employer pensions where the employee has no individual account; Foreign social security analogues (e.g., UK State Pension, Indian Social Security). Resolve the actual account and exemption facts before filing; do not promise a zero-risk filing position. Reporting penalties depend on the applicable adjusted ceiling, reasonable cause and IRS discretion. [Source](https://www.ecfr.gov/current/title-31/section-1010.821).  _(IRS guidance (unspecified in source))_

### 3.8 Due date and filing mechanics

**Non-usable hold:** The statement that the listed relief is exhaustive remains held; the notice applies only to its covered classes.

- **FBAR due date and extension** — The FBAR is due April 15 of the year following the calendar year being reported. Since 2017 a six-month automatic extension to October 15 has been available — no form needs to be filed to claim the extension; it is automatic for all filers. There is no further extension beyond October 15 except in narrow disaster-area circumstances and FinCEN's annual notice for certain individuals with signature authority over, but no financial interest in, foreign financial accounts (Notice FIN-2025-NTC3 extends their 2025 FBAR to April 15, 2027).  _([31 CFR §1010.350](https://www.fincen.gov/system/files/2025-12/FBAR-FBAR-Filing-Requirement-for-Certain-Financial-Professionals.pdf))_
**Non-usable hold:** The no-fee assertion is not confirmed. The account-record duty and a retained FBAR copy are different.

- **Filing mechanics detail** — Filing is through the BSA E-Filing System (bsaefiling.fincen.treas.gov). The form requires identification of each account: institution name, address, account number, maximum value during the year (in USD), and the relationship of the filer to the account. There is no fee. There is no paper option for routine cases. Retain the required underlying account records for five years. IRS guidance does not require retention of a copy of the filed FBAR; Form 114a has its own retention requirement. [Source](https://www.irs.gov/irm/part4/irm_04-026-016). FinCEN may request supporting records during this period; failure to provide them is itself sanctionable.  _(31 CFR §1010.420)_

## 4. Form 8938 — Statement of Specified Foreign Financial Assets

### 4.1 Statutory basis

**Non-usable hold:** The historical enactment description is not verified here; use the operative filing conditions.

- **FATCA statutory basis** — FATCA was enacted as part of the Hiring Incentives to Restore Employment Act of 2010, adding §6038D to the Internal Revenue Code. The implementing regulations at Treas. Reg. §1.6038D-1 through §1.6038D-8 require a "specified person" to report "specified foreign financial assets" (SFFAs) for any tax year in which the aggregate value of those assets exceeds the applicable threshold. Form 8938 is attached to Form 1040 (or 1120, 1065, etc., for in-scope entities). It is filed with the income tax return and follows that return's due date and extension. If no income tax return is required, no Form 8938 is required even when asset values exceed the thresholds. [Source](https://www.irs.gov/instructions/i8938).  _(IRC §6038D; Treas. Reg. §1.6038D-1 through §1.6038D-8)_

### 4.2 Specified person

- **Specified individual** — A US citizen, a resident alien for any portion of the year, a nonresident alien who elects to be treated as a resident under §6013(g) or §6013(h), or a nonresident alien who is a bona fide resident of American Samoa or Puerto Rico.  _([IRC §6038D; §6013(g); §6013(h)](https://www.irs.gov/instructions/i8938))_
**Non-usable hold:** The historical effective-date statement remains held; current entity tests have separate trust conditions.

- **Specified domestic entity** — Under regulations effective for tax years beginning after December 31, 2015, a domestic corporation, partnership, or trust will be a specified domestic entity if it is "formed or availed of" for purposes of holding specified foreign financial assets. For a domestic corporation or partnership, apply the passive-income or passive-asset test (50%) and the closely-held test (at least 80% specified-individual ownership on the last day), including attribution, aggregation and exceptions. A domestic trust instead uses the specified-person current-beneficiary test and applicable trust exceptions; the corporation/partnership passive test is not a universal trust test. [Source](https://www.irs.gov/instructions/i8938).  _([Treas. Reg. §1.6038D-6](https://www.irs.gov/instructions/i8938))_
- **Single-member LLC 8938 treatment** — Single-member LLCs disregarded for federal income tax purposes are disregarded for §6038D purposes too. The owner reports the LLC's foreign accounts on the owner's own Form 8938 attached to the owner's Form 1040. This is the opposite of the FBAR rule.  _(IRC §6038D)_

### 4.3 What is a Specified Foreign Financial Asset (SFFA)

- **SFFA categories** — 1. Financial accounts maintained by a foreign financial institution — the FATCA-defined FFI is broader than the FBAR-defined "financial institution" but in practice covers the same retail accounts: foreign bank, brokerage, mutual fund, custodial accounts. 2. Foreign financial assets held outside an account and held for investment (stock is deemed held for investment); actual business-use interests/contracts need separate classification. This category can be within Form 8938 without being an FBAR account: Stock or securities issued by a non-US person held in the taxpayer's own name (not in a custodial account); Interests in foreign partnerships (general or limited); Interests in foreign trusts and foreign estates (when the holder knows or has reason to know of the interest); Foreign-issued financial instruments and contracts with non-US counterparties (forward contracts, options, swaps, notes, debentures); Interests in foreign hedge funds and foreign private equity funds — typically held as limited partnership or non-US corporation interests; Cash-value foreign life insurance and annuity contracts.  _(§6038D(b))_

### 4.4 What is NOT an SFFA

- **SFFA exclusions** — Directly held foreign real estate — a vacation home in Spain titled in the US owner's name is not reportable on 8938 or FBAR. Income from it must still be reported on Schedule E. If the real estate is held through a foreign corporation or partnership, the entity interest is an SFFA. Foreign currency held directly — physical cash and bullion are not SFFAs (though gold held in a foreign bank account is, because the account is). Tangible personal property held directly — art, jewelry, collectibles, automobiles. Assets held in a US financial account — even if the underlying issuer is foreign. Foreign stock held at Fidelity is not an SFFA. Apply the US-payer exclusion, including qualifying foreign branches/subsidiaries of US financial institutions; their accounts can still be foreign for FBAR. [Source](https://www.irs.gov/instructions/i8938). Social Security analogues — foreign social security, social insurance, or other similar program of a foreign government is not an SFFA.  _(IRC §6038D)_

### 4.5 Form 8938 thresholds

**Form 8938 thresholds**  _(IRC §6038D)_

| Filer | Year-end | At any time during year |
| --- | --- | --- |
| Unmarried, US-resident | $50,000 | $75,000 |
| Married filing joint, US-resident | $100,000 | $150,000 |
| Married filing separate, US-resident | $50,000 | $75,000 |
| Unmarried, abroad (qualifying bona fide residence or physical-presence route below) | $200,000 | $300,000 |
| Married filing joint, abroad | $400,000 | $600,000 |
| Married filing separate, abroad | $200,000 | $300,000 |
| Specified domestic entity | $50,000 | $75,000 |

- **Abroad definition** — "Abroad" for these purposes means having your tax home in a foreign country and either being a U.S. citizen who is a bona fide resident of a foreign country for an uninterrupted period that includes an entire tax year, or being a U.S. citizen or resident present in a foreign country at least 330 full days during any period of 12 consecutive months that ends in the tax year. Mere absence from the US does not by itself put a filer in the higher-threshold category.  _([IRC §911](https://www.irs.gov/instructions/i8938))_

These thresholds are dramatically higher than the FBAR's flat $10,000. A typical fact pattern:

**Non-usable hold:** The euro illustration has no confirmed exchange rate or valuation dates.

- A US-resident individual with €40,000 in a French bank account: FBAR yes, Form 8938 no.
- A US-resident married couple with $90,000 jointly in foreign accounts: FBAR yes, Form 8938 no.
**Non-usable hold:** The illustration lacks the return, residence and valuation facts needed for a filing conclusion.

- A married US expat couple in Singapore with $350,000 in Singapore bank accounts: FBAR yes, Form 8938 no (under the $400k/$600k expat thresholds).
**Non-usable hold:** The illustration lacks the return, residence and valuation facts needed for a filing conclusion.

- A married US expat couple in Singapore with $700,000: both forms required.

### 4.6 Due date and extension

- **Form 8938 due date and extension**: follows the underlying income tax return. Calendar-year individual returns are ordinarily due April 15, with Form 4868 extending filing to October 15. Qualifying overseas filers also have the automatic two-month extension with the required return statement. A discretionary extension to December 15 is requested by letter by October 15; Form 2350 is a separate extension to meet the residence/presence tests, generally to 30 days after qualification. These are not payment extensions. [Source](https://www.irs.gov/publications/p54).

### 4.7 Specific line categories on Form 8938

- **Form 8938 parts** — Part I — Foreign Deposit and Custodial Accounts Summary (these are usually the same accounts reported on FBAR); Part II — Other Foreign Assets Summary (the assets not in financial accounts — direct stock, partnership interests, contracts); Part III — Summary of Tax Items Attributable to SFFAs (income, deductions, credits, and the form/schedule each item flows to); Part IV — Excepted Specified Foreign Financial Assets (assets reported on another international information return, principally Forms 3520, 5471, 8621, 8865 — Form 8938 cross-references them rather than duplicating); Part V — Detailed Information for Each Foreign Deposit and Custodial Account (one block per account); Part VI — Detailed Information for Each "Other" SFFA (one block per non-account asset).  _(Form 8938 instructions)_
- **Part IV duplicate-reduction mechanism**: qualifying assets timely reported for the same tax year on Forms 3520, 3520-A, 5471, 8621 or 8865 need not be duplicated in Parts V/VI; apply the instructions' combined Form 3520/3520-A conditions for a foreign grantor trust. Specified individuals still include these assets for the Form 8938 threshold; specified domestic entities exclude assets qualifying for this listed-form exception from their threshold calculation. [Source](https://www.irs.gov/instructions/i8938).

## 5. The Overlap and the Differences

### 5.1 Why both are usually required

- **Apply both tests separately**: retail foreign bank/brokerage accounts can qualify for both forms, but Form 8938 also covers nonaccount assets and excludes qualifying US-payer accounts. Asset value alone does not establish both filing obligations. Neither form substitutes for the other. [Source](https://www.irs.gov/instructions/i8938). [Source](https://www.ecfr.gov/current/title-31/subtitle-B/chapter-X/part-1010/subpart-C/section-1010.350).

### 5.2 When only FBAR is required

- **FBAR-only scenarios**: reportable account maxima exceed $10,000 but the person has no required Form 8938 under its separate return, asset and threshold tests; or a person has reportable signature authority without the relevant Form 8938 interest, subject to FBAR exemptions. A disregarded domestic LLC and its owner are separate FBAR persons; the owner's potential Form 8938 filing does not make that structure universally FBAR-only. [Source](https://www.ecfr.gov/current/title-31/subtitle-B/chapter-X/part-1010/subpart-C/section-1010.350). [Source](https://www.irs.gov/instructions/i8938).

### 5.3 When only Form 8938 is required (rare)

**Non-usable hold:** The rarity/prevalence assertion is unverified.

- **8938-only scenario** — A US person whose only SFFAs are non-account assets — e.g., directly held foreign stock certificates or a foreign partnership interest — and who has no foreign deposit or custodial account at all. The FBAR test is not met because there are no "financial accounts." This is rare in practice; most foreign partnership interests are held alongside a foreign bank account that distributes earnings.

### 5.4 Signature authority — only on FBAR

**Non-usable hold:** Beneficial-ownership shorthand does not establish the complete Form 8938 interest test.

- **Signature authority difference** — This is the single most important practical difference. Form 8938 requires beneficial ownership of an SFFA; signature authority without ownership is not reportable on 8938. FBAR can require reporting for signature authority without beneficial interest; apply the employee exemptions and modified account-detail rules. [Source](https://www.ecfr.gov/current/title-31/subtitle-B/chapter-X/part-1010/subpart-C/section-1010.350). > **AUDIT FLASH POINT — corporate signature authority.** US-based CFOs, treasurers and controllers must test the threshold, exemptions and detail rules before deciding their personal filing obligations. [Source](https://www.ecfr.gov/current/title-31/subtitle-B/chapter-X/part-1010/subpart-C/section-1010.350). The $10,000 threshold aggregates across all accounts they have authority over (including their personal accounts). Many companies neglect to brief their officers on this obligation. Always ask the question: "Are you a signer on any foreign account of any company you work for?"

### 5.5 Foreign mutual funds — important asymmetry

- **Foreign mutual fund classification**: a foreign public mutual fund or similar pooled fund available to the general public with regular net-asset-value determination and regular redemptions can itself be a reportable financial account under 31 CFR 1010.350(c)(3)(iv), including direct registration with the fund. Direct fund-house registration is not an FBAR exemption. Form 8938 and PFIC obligations require their own asset, filing and classification tests. [Source](https://www.ecfr.gov/current/title-31/subtitle-B/chapter-X/part-1010/subpart-C/section-1010.350). [Source](https://www.irs.gov/instructions/i8938).

## 6. FBAR Penalties

The FBAR penalty regime is among the harshest in the entire federal tax and financial-reporting code. The penalties are codified at 31 USC §5321 (civil) and 31 USC §5322 (criminal).

### 6.1 Non-willful civil penalty — Bittner v. United States (2023)

- **Pre-Bittner IRS/FinCEN position** — Pre-Bittner, the IRS and FinCEN took the position that the non-willful penalty under 31 USC §5321(a)(5)(B)(i) — capped at $10,000 (adjusted for inflation; $16,536 for penalties assessed on or after January 17, 2025, per FinCEN inflation adjustments at 31 CFR 1010.821) — applied per account per year. Under this view, a filer with 12 foreign accounts who failed to file a single FBAR faced a $120,000-plus penalty.  _([31 USC §5321(a)(5)(B)(i)](https://www.ecfr.gov/current/title-31/section-1010.821))_
- **Bittner holding** — In Bittner v. United States, 598 U.S. 85 (2023), the Supreme Court held that the non-willful penalty is per form per year, not per account. The Court reasoned that the BSA reporting obligation is to file an FBAR (a single form), and a single failure to file that form is a single violation. This is a major taxpayer victory. A non-willful penalty for a missed FBAR with twelve accounts is now capped at one inflation-adjusted $10,000 maximum, not twelve.  _(Bittner v. United States, 598 U.S. 85 (2023))_
- **Important caveats** — Bittner does not affect willful penalties, which remain per-account-per-year. The IRS still has discretion to assert lower amounts or no penalty under its mitigation guidelines (IRM 4.26.16). Reasonable-cause relief under 31 USC §5321(a)(5)(B)(ii) remains available. The civil assessment period is generally six years from the violation. IRS procedures use April 15 as a protective date and direct Counsel consultation before a later assessment; consent can extend the period. The calendar-2018 FBAR (April 15, 2019 ordinary date; October 15, 2019 extension) cannot be declared absolutely barred after April 15, 2025 without checking these facts. [Source](https://www.irs.gov/irm/part4/irm_04-026-017r).  _(31 USC §5321(a)(5)(B)(ii); 31 USC §5321(b)(1); IRM 4.26.16)_

### 6.2 Willful civil penalty — draconian

- **Willful civil penalty amount** — greater of $100,000 (inflation-adjusted to $165,353 for penalties assessed on or after January 17, 2025, per FinCEN adjustments) or 50% of the balance in the account at the time of the violation USD/percent (per violation per year; per account per year for willful)  _([31 USC §5321(a)(5)(C)](https://www.ecfr.gov/current/title-31/section-1010.821))_

Willful penalties are per-account, per-year ceilings, not automatic assessments. If each of the 12 accounts had a $200,000 violation-date balance and the $165,353 assessment-date amount applies, the theoretical aggregate ceiling is 12 × max($165,353, 50% × $200,000) = $1,984,236. The printed $1.2 million is 50% of $2.4 million but ignores the greater adjusted floor. IRS discretion and mitigation can produce a lower assessment, including $1.2 million. [Source](https://www.ecfr.gov/current/title-31/section-1010.821). [Source](https://www.irs.gov/irm/part4/irm_04-026-016).

### 6.3 What is willful

**Non-usable hold:** The named judgments and court descriptions have not been separately read; do not treat the case citations as verified.

- **Willfulness standard for FBAR** — "Willful" in the FBAR context is broader than the criminal-law standard. The Tax Court and the Federal Circuits have repeatedly held that willfulness includes: Actual knowledge of the FBAR obligation combined with intentional failure to file (the classic case); "Willful blindness" — deliberate avoidance of learning the obligation when the filer has reason to suspect it exists; Reckless disregard — a serious risk that the filer should have known about, but failed to investigate (see United States v. Williams, 489 F. App'x 655 (4th Cir. 2012); United States v. McBride, 908 F. Supp. 2d 1186 (D. Utah 2012); United States v. Bohanec, 263 F. Supp. 3d 881 (C.D. Cal. 2016)). Signing a Form 1040 Schedule B without answering the foreign account questions accurately, or answering them as "no" while holding a foreign account, has been treated as evidence of willfulness or reckless disregard.  _(United States v. Williams, 489 F. App'x 655 (4th Cir. 2012); United States v. McBride, 908 F. Supp. 2d 1186 (D. Utah 2012); United States v. Bohanec, 263 F. Supp. 3d 881 (C.D. Cal. 2016))_

### 6.4 Criminal penalties

**Non-usable hold:** The criminal-case frequency assertion is unverified.

- **Criminal penalty structure** — Under 31 USC §5322(a), a willful violation of any provision of the BSA, including FBAR filing, is punishable by a fine of up to $250,000 and imprisonment for up to 5 years. If the willful violation occurs while violating another US law, or as part of a pattern of illegal activity involving more than $100,000 in a 12-month period (§5322(b)), the maximum fine doubles to $500,000 and the prison term doubles to 10 years. Criminal prosecutions remain rare relative to civil enforcement but are not theoretical. The DOJ Tax Division has prosecuted dozens of FBAR cases since 2009 in connection with the Swiss bank disclosures and subsequent enforcement.  _(31 USC §5322(a); 31 USC §5322(b))_

> **AUDIT FLASH POINT — willful vs non-willful determination.** This determination is the single highest-leverage judgment in an FBAR delinquency case. A willful determination can produce a million-dollar penalty; a non-willful determination caps at $16,536 per form per year (penalties assessed on or after January 17, 2025). The taxpayer's contemporaneous knowledge, the accountant's prior advice (or absence of it), and the Schedule B answers in prior years are all relevant. Documenting reasonable-cause facts at the outset of any catch-up engagement is essential.

### 6.5 Reasonable cause

**Non-usable hold:** Ignorance/adviser reliance is fact-intensive and not established as a defense by this paragraph.

- **Reasonable cause exception** — The statute provides a reasonable-cause exception to the non-willful penalty at 31 USC §5321(a)(5)(B)(ii): no penalty shall be imposed if the violation was due to reasonable cause and the amount of the transaction or balance in the account was properly reported. The reasonable-cause standard is fact-intensive and follows familiar tax principles: ordinary business care and prudence, reliance on a competent advisor, ignorance of the law where the obligation was genuinely unknown. Reasonable cause is not available for willful violations.  _(31 USC §5321(a)(5)(B)(ii))_

### 7.1 Failure to file — $10,000 plus continuing

- **§6038D(d) failure-to-furnish penalty** — Under §6038D(d), a specified person who fails to furnish required information is subject to a $10,000 penalty. If the failure continues for more than 90 days after the IRS mails a notice of failure, an additional $10,000 penalty applies for each 30-day period (or fraction) during which the failure continues after the 90-day period, up to a maximum continuing-failure penalty of $50,000. The maximum combined failure-to-file penalty per year is therefore $60,000 ($10,000 initial + $50,000 continuing).  _(§6038D(d))_

### 7.2 Accuracy-related penalty: 40% of attributable tax underpayment

- **Accuracy-related penalty on undisclosed SFFA understatement** — 40% percent (applies to the portion of an underpayment of tax attributable to any undisclosed foreign financial asset understatement; double the standard 20% accuracy-related penalty under §6662(a))  _(§6662(j))_

### 7.3 Reasonable cause

**Non-usable hold:** The section 6664(c) overlay and its exceptions remain unverified.

- **§6038D(g) reasonable cause defense** — Section 6038D(g) provides a reasonable-cause defense to the §6038D(d) penalty if the taxpayer establishes that the failure was due to reasonable cause and not willful neglect. The fact that a foreign jurisdiction would impose a civil or criminal penalty on the taxpayer for disclosure is, by statute, not reasonable cause (§6038D(g)). The 40% accuracy penalty under §6662(j) has its own reasonable-cause overlay through §6664(c).  _(§6038D(g); §6664(c))_

### 7.4 Extended statute of limitations — §6501(e)(1)(A)(ii)

- **Six-year assessment extension**: IRC 6501(e)(1)(A)(ii) applies when omitted gross income exceeds $5,000 and is attributable to specified foreign assets. For this test the statute disregards the Form 8938 dollar thresholds and exceptions. A missing Form 8938 is not an additional condition. [Source](https://uscode.house.gov/us/usc/119-124/t26/s6501/).
- **Indefinite statute when 8938 missing** — Under §6501(c)(8), the time for assessment does not expire before 3 years after the §6038D information is furnished; if the failure to furnish the information is due to reasonable cause and not willful neglect, this applies only to the items related to the failure. The failure can therefore leave the assessment period open until the information is furnished; where reasonable cause and no willful neglect are established, only related items receive this extension. Do not describe every missing Form 8938 as indefinitely opening unrelated items. [Source](https://uscode.house.gov/us/usc/119-124/t26/s6501/).  _([§6501(c)(8)](https://www.law.cornell.edu/uscode/text/26/6501))_

## 8. PFIC Interaction (§1291) — Refer Out

**Non-usable hold:** The categorical PFIC classification is not verified; actual foreign-corporation, income/asset and exception tests are required.

When a US person holds shares of a foreign mutual fund, foreign ETF, foreign exchange-traded vehicle, foreign hedge fund, foreign private equity fund, or many foreign insurance-wrapped investment products, the investment is almost always a Passive Foreign Investment Company under IRC §1297.

PFIC consequences:

- Section 1291 allocates excess distributions and disposition gain across the holding period. Current-year and pre-PFIC allocations are ordinary income; prior PFIC-year allocations use the highest rate for those years plus the statutory interest charge. Do not apply the prior-year highest-rate treatment to every allocation. [Source](https://www.irs.gov/instructions/i8621).
- Test each Form 8621 filing gateway and exception. The annual-report exception can apply under the $25,000/$50,000 conditions where there is no excess distribution or gain, but other reporting/election gateways remain. Holding a PFIC does not invariably require a separate annual form. [Source](https://www.irs.gov/instructions/i8621).
- Available elections: Qualified Electing Fund (QEF) election under §1295 — requires the fund to provide a PFIC Annual Information Statement (most foreign funds will not); Mark-to-Market election under §1296 — available for marketable PFIC stock. A first-year election can avoid adverse coordination consequences, but is not a universal election deadline: later mark-to-market elections have section 1291 coordination, and later QEF/purging routes require their own conditions. [Source](https://www.irs.gov/instructions/i8621).
- Foreign mutual funds are flagged on Form 8938 as SFFAs and require separate Form 8621. Form 8938 Part IV cross-references Form 8621 to avoid duplicate detail.

**Non-usable hold:** The categorical PFIC statement and comparative professional-cost prediction are unverified.

> **AUDIT FLASH POINT — PFIC mutual funds.** Every Indian, UK, EU, Canadian, Australian, and other foreign mutual fund in a client's portfolio is almost certainly a PFIC. The catch-up cost of curing a multi-year unreported PFIC position is often greater than the entire investment return. This is one of the single most damaging tax exposures in international personal finance.

The detailed mechanics of §1291, §1295 QEF, §1296 mark-to-market, the §1298(f) Form 8621 filing thresholds, and the interaction with foreign tax credits are out of scope for this skill. Refer to a dedicated PFIC skill or specialist.

## 9. Compliance Paths for Late or Non-Filers

The IRS has published multiple programs for taxpayers who have failed to comply with FBAR, Form 8938, or related international information return obligations. Choosing the wrong program can produce dramatically different penalty outcomes. The current menu (as of 2025) is:

### 9.1 Streamlined Foreign Offshore Procedures (SFOP)

- **SFOP eligibility and penalty structure**: apply all general and foreign-streamlined conditions, including non-willful failure to report foreign gross income/pay tax and required information, and the examination/investigation restrictions. For citizens and lawful permanent residents, in at least one of the three covered tax years there must be no US abode and at least 330 full days abroad. A noncitizen who was not a lawful permanent resident instead uses the substantial-presence-test nonresidency branch. Both spouses must meet the applicable nonresidency requirement for a joint submission. Submit the required three return years and six FBAR years whose due dates have passed, Form 14653, tax and interest. Conditional penalty relief does not abate previously assessed penalties; new deficiencies and fraudulent/willful conduct can carry penalties. [Source](https://www.irs.gov/individuals/international-taxpayers/us-taxpayers-residing-outside-the-united-states).

### 9.2 Streamlined Domestic Offshore Procedures (SDOP)

- **SDOP eligibility and penalty structure**: apply all general/domestic streamlined conditions, including non-willful foreign-income/tax/information failures, the applicable nonresidency test and examination/investigation restrictions. Required income returns for each of the three covered tax years must previously have been filed; a year with no required return is not automatically disqualifying. Submit amended required returns, six required FBAR years and Form 14654 with tax, interest and the 5% penalty. The base is the highest annual year-end aggregate of covered accounts/assets across the covered return/FBAR years, including relevant omitted Form 8938 assets and reported assets whose income was omitted. Conditional FBAR, information-return and accuracy-penalty relief excludes prior assessments and can be lost for new deficiencies, fraud or willfulness. Non-willful FBAR reporting penalties are per report, not account-by-account. [Source](https://www.irs.gov/individuals/international-taxpayers/us-taxpayers-residing-in-the-united-states).

### 9.3 Delinquent FBAR Submission Procedures (DFSP)

**Non-usable hold:** Current program availability, eligibility and automatic penalty relief are not established. Do not choose this procedure or promise no penalty from this paragraph.

- **DFSP eligibility and penalty structure** — For taxpayers who had no unreported income and missed only the FBAR. Eligibility: All required FBARs have not been filed; All taxable income from the foreign accounts was properly reported on the income tax return; Taxpayer is not under examination or criminal investigation. Penalty structure: no FBAR penalty if the requirements are met. The taxpayer e-files the delinquent FBARs through the BSA E-Filing System with a statement explaining why they were filed late. This is the right path when, for example, a green-card holder properly reported interest income from a Swiss account on Schedule B but missed the FBAR.

### 9.4 Delinquent International Information Return Submission Procedures (DIIRSP)

- **DIIRSP eligibility and penalty structure**: delinquent international information returns can be filed under the current procedure where its conditions are met, including not being under civil examination or criminal investigation and not previously contacted about the delinquent returns. The procedure is not limited categorically to no-unreported-income cases. Penalties may be assessed; apply the current form-specific reasonable-cause processing rules, including the different treatment of Forms 3520/3520-A. Do not promise automatic relief. [Source](https://www.irs.gov/individuals/international-taxpayers/delinquent-international-information-return-submission-procedures).

### 9.5 Voluntary Disclosure Practice (VDP)

**Non-usable hold:** The historical closure/memorandum facts and the assertion of legal exclusivity remain unverified; counsel must determine the available procedure.

- **VDP history and structure** — The legacy Offshore Voluntary Disclosure Program (OVDP) closed September 28, 2018. It was replaced by the Updated Voluntary Disclosure Practice announced in IRS Memorandum LB&I-09-1118-014 (November 20, 2018). The VDP is the only path for taxpayers whose non-compliance is willful. Eligibility requires pre-clearance through IRS Criminal Investigation. The penalty structure is harsh: Under the operative income-tax procedure, the civil fraud penalty generally uses the highest tax-deficiency year, not total correctly reported liability; section 6663 uses the fraudulent underpayment base. Delinquent/amended returns and procedure exceptions require separate analysis. Willful FBAR treatment follows current IRS guidelines with discretion, allocation and caps; a single 50%-of-highest-balance year is not guaranteed. [Source](https://www.irs.gov/irm/part4/irm_04-063-003r). [Source](https://uscode.house.gov/us/usc/119-124/t26/s6663/). Income tax, interest, and other penalties for the disclosure period. The benefit of VDP is the strong (though not absolute) protection against criminal prosecution. Taxpayers and their counsel must weigh this protection against the substantial financial penalty.  _(IRS Memorandum LB&I-09-1118-014 (November 20, 2018))_

### 9.6 Choosing the right path — decision framework

**Decision framework for compliance path selection**

**Non-usable hold:** The DFSP rows are not program clearance; current availability and relief remain unresolved under §9.3. Other rows require the complete conditions in the referenced section.

| Fact pattern | Recommended path |
| --- | --- |
| Meets applicable SFOP nonresidency branch and all foreign-streamlined eligibility conditions, including non-willful foreign income/tax/information failure | Consider SFOP; obtain required certification |
| Meets all domestic-streamlined conditions, including prior filing where required and non-willful foreign income/tax/information failure | Consider SDOP; obtain required certification |
| Income properly reported, only FBAR missed | DFSP |
| Income properly reported, only Form 8938 (or 5471 etc.) missed | DIIRSP with reasonable cause |
| Willful conduct in any prior year | VDP — coordinate with counsel |
| Under IRS audit or criminal investigation | None of the above — coordinate with counsel |

> **AUDIT FLASH POINT — late catch-up program selection.** This is the highest-stakes decision in an FBAR / 8938 catch-up engagement. SFOP and SDOP are non-willful-only; a later determination of willfulness on the same facts can convert a $0 or 5% penalty into a 50%-of-balance disaster. Document the non-willful certification facts carefully and engage tax counsel if there is any doubt about the willfulness characterization. A taxpayer who has been signing Schedule B "no" while holding foreign accounts is a high-risk willfulness case regardless of subjective intent.

## 10. India Scenario Deep Dive

The Indian-American community is the single largest population of US persons with chronic FBAR/8938 non-compliance. The standard fact pattern combines several common elements, each with distinct reporting consequences.

### 10.1 NRE and NRO accounts

**Non-usable hold:** Specific US/treaty income and Indian withholding-credit/exemption treatment has not been confirmed; no credit or exemption is established by withholding alone.

- **NRE/NRO account treatment** — NRE (Non-Resident External) accounts — repatriable, denominated in INR, often interest-bearing; held at an Indian bank; NRO (Non-Resident Ordinary) accounts — rupee account for income earned in India (rent, dividends, pension); also held at an Indian bank. Treatment: Both are foreign financial accounts for FBAR purposes; Both are specified foreign financial assets for Form 8938 purposes; Both generate interest income that is fully taxable in the US as worldwide income (the FATCA reporting does not change the income tax inclusion); A foreign tax credit is generally available for Indian TDS withheld on NRO interest under the US-India treaty and §901; NRE interest is exempt from Indian tax under Indian law; this means there is no foreign tax to credit, and the US tax on NRE interest must be paid out of pocket.  _(US-India tax treaty; §901)_

### 10.2 Public Provident Fund (PPF)

**Non-usable hold:** Indian plan law, term and US tax/treaty classification remain unverified.

- **PPF treatment** — The PPF is a long-term retirement-style savings account at an Indian bank with government-set interest rates and a 15-year lock-in. It is widely treated in IRS practice as: A foreign financial account for FBAR purposes; A specified foreign financial asset for Form 8938; Not entitled to US tax deferral — the annual interest credit is currently taxable in the US. There is no US-India treaty provision deferring PPF earnings to distribution.

### 10.3 Life Insurance Corporation (LIC) policies

**Non-usable hold:** ULIP subaccount classification and tax treatment require the actual policy and vehicle facts.

- **LIC policy treatment** — Many Indian-Americans hold LIC of India endowment, money-back, or unit-linked insurance plans (ULIPs) inherited from parents or purchased before US emigration. Treatment: Cash-value foreign life insurance is a foreign financial account for FBAR (the cash surrender value is the reportable amount); It is an SFFA for Form 8938; Whether it is a life insurance contract under §7702 depends on the applicable-law, cash-value/premium and corridor tests. A foreign issuer alone does not establish failure of those tests or annual inside-buildup taxation; obtain the contract and specialist classification. [Source](https://uscode.house.gov/us/usc/119-124/t26/s7702/). ULIPs that allocate to mutual fund sub-accounts are likely to contain PFIC exposures.  _(IRC §7702)_

### 10.4 Indian mutual funds

- **Indian mutual fund treatment**: direct fund-house registration (including HDFC AMC, ICICI Prudential or SBI Mutual Fund holdings) does not itself remove FBAR reporting. Test the public pooled-fund definition in §3.4/§5.5 and the separate Form 8938 investment/interest rules. PFIC status and Form 8621 depend on entity classification, income/assets, exceptions and elections, rather than the fund name alone. [Source](https://www.ecfr.gov/current/title-31/subtitle-B/chapter-X/part-1010/subpart-C/section-1010.350). [Source](https://www.irs.gov/instructions/i8938). [Source](https://www.irs.gov/instructions/i8621).

### 10.5 Employees' Provident Fund (EPF) and pension funds

**Non-usable hold:** Current taxation and treaty treatment are unverified; no filing/tax position is cleared.

- **EPF treatment** — Indian EPF contributions are a defined-contribution employer-sponsored plan with a member account. Practitioner consensus treats EPF as: An FBAR-reportable foreign financial account; An SFFA for Form 8938; Currently taxable in the US on the annual interest credit — there is no US-India tax treaty article that defers EPF buildup. This treatment is conservative. There is no published IRS guidance directly on point and there are arguments both ways. Practitioners take varying positions.

### 10.6 Indian inheritance

**Non-usable hold:** Gift aggregation, return exceptions and inherited-fund basis/holding-period treatment remain unverified.

- **Indian inheritance reporting** — A US person who inherits Indian assets (real estate, accounts, gold, securities) from a non-US-person decedent files Form 3520 if the gift exceeds $100,000 (the threshold for gifts from non-US individuals) — separately from FBAR and 8938. Once the assets are received and titled in the US person's name, ongoing FBAR/8938 obligations begin for the inherited financial accounts. **Non-usable hold:** Inherited-fund holding-period/basis treatment, universal annual filing and professional-cost claims below are unverified.

> **AUDIT FLASH POINT — Indian PFIC mutual funds.** This is the single most damaging hidden exposure in the Indian-American population. Inherited or pre-emigration mutual fund holdings often accumulate decades of §1291 deemed-distribution tax exposure. Curing the position requires Form 8621 for each year for each fund, with §1291 computations using highest-ordinary-rate-in-effect for each holding-period year. The professional fees alone often exceed the original investment.  _(Form 3520)_

## 11. Additional High-Risk Jurisdictions

### 11.1 Chinese accounts

**Non-usable hold:** The foreign outbound-transfer limit is unverified; this skill does not provide foreign-law clearance.

- **Chinese accounts treatment** — US persons with bank accounts at the Bank of China, ICBC, or other Chinese banks face: Full FBAR and 8938 reporting (China is a treaty partner for tax purposes; nothing about US-China relations excuses disclosure); Currency-control concerns on the Chinese side (annual $50,000 outbound limit) — but this is a Chinese law issue, not a US reporting issue; Standard reporting; no special program.

### 11.2 Iranian accounts

**Non-usable hold:** The sanctions permissions/exceptions are unverified; refer to sanctions counsel.

- **Iranian accounts treatment** — US persons with Iranian accounts face additional risk under the Iranian Transactions and Sanctions Regulations administered by OFAC (31 CFR Part 560). US persons are generally prohibited from engaging in transactions with Iran absent a specific or general license. Holding a pre-existing account in Iran from before sanctions does not by itself violate sanctions, but using the account, accepting deposits to it, or transferring from it may. FBAR and 8938 reporting obligations apply regardless of sanctions issues — sanctions law does not excuse reporting law. Specialist coordination is essential.  _(31 CFR Part 560)_

### 11.3 Russian accounts

**Non-usable hold:** The orders, designations and restrictions are unverified; refer to sanctions counsel.

- **Russian accounts treatment** — Following the 2022 sanctions, US persons with Russian accounts face similar OFAC issues under Executive Orders 14066, 14068, 14071 and subsequent. FBAR and 8938 obligations are unaffected. Coordinate with sanctions counsel.  _(Executive Orders 14066, 14068, 14071)_

## 12. Worked Examples

### Example 1 — Indian-American family, mid-level non-compliance

Facts. Priya is a US citizen by naturalization, living in New Jersey. She moved to the US in 2015. She has the following:

- An NRE savings account at HDFC Bank in Mumbai. Highest balance during 2025: $32,000.
- An NRO account at the same bank. Highest balance during 2025: $8,000.
- A PPF account at SBI. Year-end balance: $14,000.
- A 15-year-old LIC of India endowment policy. Cash surrender value at 12/31/2025: $11,000.
- Three Indian mutual fund holdings held directly with the fund house. Aggregate year-end value: $22,000.

She has never filed an FBAR or Form 8938. She has been filing Form 1040 each year but answered "no" to the Schedule B foreign account questions.

FBAR: the NRE/NRO annual maxima alone total $40,000, so the stipulated bank accounts cross $10,000. The printed $65,000 sum (32 + 8 + 14 + 11 thousand) mixes bank maxima and other year-end values and excludes funds categorically. Directly registered qualifying public funds can also be reportable; obtain classification and each account's annual maximum before computing the reportable total. [Source](https://www.ecfr.gov/current/title-31/subtitle-B/chapter-X/part-1010/subpart-C/section-1010.350). [Source](https://www.fincen.gov/system/files/shared/FBAR%20Line%20Item%20Filing%20Instructions.pdf).

Form 8938: the supplied displayed values add to $87,000, but are not a demonstrated year-end aggregate because the bank inputs are maxima. Obtain year-end/maximum values, filing status, return obligation and any timely other-form exception before applying the $50,000 unmarried-US-resident year-end threshold. No filing conclusion is established by the sum alone. [Source](https://www.irs.gov/instructions/i8938).

PFIC exposure: classify each of the three holdings and test Form 8621 gateways/exceptions before deciding the forms or section 1291 computation. The $22,000 balance alone does not establish tax or a universal annual filing duty. [Source](https://www.irs.gov/instructions/i8621).

**Non-usable hold:** The supplied knowledge/advice facts do not establish nonwillfulness or SDOP eligibility; obtain full facts and human certification.

Catch-up path: Because Priya answered "no" to the Schedule B foreign account questions while holding foreign accounts, the willfulness analysis is sensitive. If she had no actual knowledge of the FBAR obligation and no professional advice on the question, the non-willful position is defensible. SDOP is the likely path, with three years of amended returns including the back-year interest income, six years of delinquent FBARs, and the 5% Title 26 miscellaneous offshore penalty on the highest aggregate year-end balance/value during the covered period.

The PFIC issue is independent of SDOP. SDOP does not eliminate §1291 tax. Apply Form 8621 filing exceptions and elections for each year. Section 1291 tax requires distribution/disposition and holding-period facts; an account balance alone does not establish a tax charge. [Source](https://www.irs.gov/instructions/i8621).

Conditional penalty illustration: 5% × $65,000 = $3,250 is arithmetic, but an FBAR-only base omits potentially subject Form 8938 assets. If $87,000 were the highest covered year-end aggregate of all subject accounts/assets, 5% would be $4,350 ($1,100 more). Neither amount is the actual penalty without the covered histories and full SDOP eligibility. The original back-tax estimate ($1,500–$3,000), PFIC estimate ($5,000–$15,000 plus interest) and fee estimate ($8,000–$15,000) are unverified inputs and unavailable for reliance; no replacement tax or fee estimate is made. [Source](https://www.irs.gov/individuals/international-taxpayers/us-taxpayers-residing-in-the-united-states).

```oa-check
name: Example 1 conditional displayed totals and SDOP base
inputs:
  nre_max: 32000
  nro_max: 8000
  ppf_year_end: 14000
  lic_year_end: 11000
  funds_year_end: 22000
steps:
  displayed_subtotal: nre_max + nro_max + ppf_year_end + lic_year_end
  displayed_all: displayed_subtotal + funds_year_end
  narrow_penalty: displayed_subtotal * 0.05
  conditional_penalty: displayed_all * 0.05
  difference: conditional_penalty - narrow_penalty
expected:
  displayed_subtotal: 65000
  displayed_all: 87000
  narrow_penalty: 3250
  conditional_penalty: 4350
  difference: 1100
```

### Example 2 — US expat in the UK with large pension

**Non-usable hold:** All supplied GBP/USD conversions, pension classification/valuation, treaty treatment and resulting filing conclusions remain held; the original inputs are preserved for illustration.

Facts. James is a US citizen who has lived in London for 12 years. He works for a UK financial-services firm. He has:

- A Barclays current account; highest balance during 2025: £8,000 ($10,200).
- A NatWest savings account; highest balance during 2025: £12,000 ($15,300).
- An ISA (UK Individual Savings Account) at Hargreaves Lansdown holding £45,000 of UK equity funds; year-end value $57,300.
- A defined-contribution UK workplace pension with £180,000 in employer-sponsored funds; year-end value $229,200.
- A SIPP (Self-Invested Personal Pension) with £65,000 in directly held UK stocks; year-end value $82,800.

James is married filing jointly to a US spouse who has no foreign accounts. They meet the §911 bona fide residence test (married joint, abroad: $400k YE / $600k anytime threshold).

The displayed values sum to $394,800, but the first two are bank maxima, so that sum is not an established year-end aggregate. Replacing the $229,200 pension input with $250,000 gives $415,600 (about $415,000); this single assumed peak does not prove the annual maximum. Obtain the actual valuations, special pension valuation facts, correct exchange rates and complete history before comparing with $400,000 year-end/$600,000 any-time thresholds. No Form 8938 conclusion is established from the supplied values. [Source](https://www.irs.gov/instructions/i8938).

**Non-usable hold:** Bank maxima establish the threshold, but the pension/account classification and each annual maximum are not established.

FBAR: aggregate is well above $10,000 — yes, every account reported.

**Non-usable hold:** Fund classification and UK-pension treaty/section 402(b) treatment remain held.

PFIC exposure: every fund inside the ISA and the workplace pension is a UK-domiciled fund and a PFIC. The pension might be eligible for §402(b) / treaty-based exclusion from current PFIC inclusion (US-UK Tax Treaty, Article 18, and HMRC-recognized pension trust arguments) — but this is fact-intensive and contested. UK ISA tax exemption alone does not determine US treatment. Ordinary taxable income, section 1291 distribution/disposition rules and QEF/mark-to-market elections differ; there is no universal annual inclusion of every unrealized ISA gain. Fund classification and the pension treaty/§402(b) question remain held for specialist analysis. [Source](https://www.irs.gov/instructions/i8621). ISA "tax-free" treatment is a UK-domestic rule with no US counterpart.

Catch-up needed if James has been missing this: full PFIC analysis on the ISA, possible §402(b) position on the workplace pension with disclosure, and consistent FBAR filing. SFOP is not established merely by London residence or the stated bona fide residence test: confirm the applicable covered-year no-US-abode/330-day facts for both spouses and every other program condition. [Source](https://www.irs.gov/individuals/international-taxpayers/us-taxpayers-residing-outside-the-united-states).

```oa-check
name: Example 2 displayed values only; valuation and FX held
inputs:
  bank_1_max: 10200
  bank_2_max: 15300
  isa_year_end: 57300
  pension_year_end: 229200
  sipp_year_end: 82800
  assumed_pension_peak: 250000
steps:
  displayed_sum: bank_1_max + bank_2_max + isa_year_end + pension_year_end + sipp_year_end
  single_replacement: displayed_sum - pension_year_end + assumed_pension_peak
expected:
  displayed_sum: 394800
  single_replacement: 415600
```

### Example 3 — US trustee of a foreign trust, signature-only authority

Facts. Sarah is a US citizen living in Boston. She has $4,000 in a personal Canadian RBC account (legacy from her university years in Montreal). She is also a co-trustee — without beneficial interest — of an offshore family trust in Jersey holding $2,300,000 of investments at HSBC Jersey. The trust beneficiaries are her UK-resident cousins.

Personal exposure: her own $4,000 account is below the FBAR threshold by itself.

But aggregate-with-signature-authority: as a co-trustee she has signature authority over a $2.3M foreign account. Her aggregate (financial-interest + signature-authority) crosses $10,000 — by a wide margin.

FBAR required, reporting both the personal Canadian account AND the trust account on which she has signature authority. Before selecting the signature-only indicator, establish who holds legal title/record ownership. A trustee can have an FBAR financial interest despite no beneficial interest. [Source](https://www.ecfr.gov/current/title-31/subtitle-B/chapter-X/part-1010/subpart-C/section-1010.350).

Form 8938: she has no beneficial interest in the trust. The Jersey trust account is not her SFFA. Her personal Canadian account at $4,000 is below the $50,000 unmarried-US-resident year-end threshold. No Form 8938 required.

This illustrates the potential signature-authority asymmetry only after checking legal title and the separate Form 8938 interest test; no beneficial interest alone does not settle both tests.

**Non-usable hold:** No beneficial interest alone does not establish the trust ownership/power/income-tax result.

There is also no immediate income tax consequence to Sarah from the trust's investment income (she has no beneficial interest). The trust's US-person beneficiaries — if any — would face their own Form 3520 obligations and potentially Form 3520-A trustee reporting. Form 3520-A requires a foreign trust with at least one US owner; US trustee status alone does not establish that gateway. Trust ownership, powers and income-tax consequences require separate analysis. [Source](https://www.irs.gov/instructions/i3520a).

> **AUDIT FLASH POINT — co-trustee signature authority.** Sarah's filing risk is enormous relative to her personal involvement. A missed FBAR on a $2.3M account where she has signature authority exposes her personally to FBAR penalties regardless of her zero beneficial interest. Practitioners with clients serving on offshore trustee panels must specifically inquire about every trust account.

```oa-check
name: Example 3 stipulated account values only
inputs:
  personal_account: 4000
  trust_account: 2300000
steps:
  combined: personal_account + trust_account
expected:
  combined: 2304000
```

## 13. Schedule B — The Gateway Question

**Non-usable hold:** Exact 2025 question wording and the $500 illustration below have not been reconciled with the operative form instructions. Do not use the quoted wording or filing conclusion without that check.

Schedule B (Form 1040) Part III asks two questions critical to FBAR and 8938 compliance:

> "At any time during 2025, did you have a financial interest in or signature authority over a financial account (such as a bank account, securities account, or brokerage account) located in a foreign country?"

> "During 2025, did you receive a distribution from, or were you the grantor of, or transferor to, a foreign trust?"

A "no" answer to the first question while holding a foreign account is one of the strongest pieces of evidence the IRS uses in willfulness determinations. A "yes" answer requires identifying the country and triggers the FBAR filing requirement question.

The Schedule B questions are independent of the dollar threshold — they ask about the existence of the account, not the balance. A US person with a $500 foreign account must answer "yes" even though no FBAR is required. The honest "yes" with no FBAR filing because under threshold is the right answer. The dishonest "no" while above threshold is the foundation of willfulness cases.

## 14. Practitioner Workflow Checklist

For every new client engagement, ask explicitly:

1. Citizenship and residence history. Place of birth, citizenships held, green card, prior foreign residence, immigration date.
2. Family abroad. Any inheritance received from non-US persons (Form 3520 trigger). Any expected inheritance from non-US parents.
3. Foreign accounts personal. Any bank, brokerage, investment account held outside the US, in any currency, in any amount.
4. Foreign accounts signature. Any signing authority on any foreign account — corporate, employer, family, trust, estate.
5. Foreign retirement/pension. Any pension account, retirement account, social security analogue, or government provident fund in any country other than the US.
6. Foreign insurance. Any life insurance, endowment, annuity, ULIP issued by a non-US insurer with cash value.
7. Foreign business interests. Any ownership in a non-US corporation, partnership, LLC, or trust.
8. Foreign mutual funds and ETFs. Any directly held foreign fund — common in India and the UK in particular.
9. Foreign real estate. Not reportable on FBAR or 8938 if held directly, but rental income is Schedule E; ownership via foreign entity changes treatment.
10. Schedule B history. Review prior-year Schedule B answers. A "no" answer in a prior year while accounts existed is a willfulness flag.

Document the answers in the file. A negative attestation contemporaneously documented is critical for reasonable-cause defenses.

## 15. Recordkeeping

### 15.1 FBAR records

- **FBAR recordkeeping requirements** — Under 31 CFR §1010.420, each US person filing an FBAR must retain for 5 years from the FBAR due date: Name maintained on the account; Number or other designation of the account; Name and address of the foreign bank or other person with whom the account is maintained; Type of account; Maximum value of the account during the reporting period. The IRS may request these records during an examination; failure to produce is a separate violation.  _(31 CFR §1010.420)_

### 15.2 Form 8938 records

**Non-usable hold:** The full section 6001/regulation retention analysis remains unverified.

- **Form 8938 recordkeeping requirements** — There is no separate retention period in §6038D, but the standard §6001 / Treas. Reg. §1.6001-1 recordkeeping obligation applies — generally records supporting items on a return must be kept for as long as their contents may be material to administration of the tax law (typically the statute-of-limitations period plus a margin; §6501(c)(8) can keep assessment open until information is furnished, but reasonable cause and no willful neglect limit that extension to related items; do not treat all unrelated items as invariably open indefinitely).  _(§6001; Treas. Reg. §1.6001-1; §6501(c)(8))_

## 16. Coordination with Other International Information Returns

**Non-usable hold:** The gift and 10%-interest summaries are not complete filing gateways; categories, aggregation and attribution remain unverified.

- **Form 8938 coordination with other forms** — Form 8938 explicitly coordinates with several other international forms via Part IV. Where the same asset qualifies under the timely same-year other-form exception (and the combined foreign-grantor-trust conditions where applicable), Form 8938 references the other form and skips the detail; apply the individual/entity threshold distinction in §4.7: Form 3520 — gifts from foreign persons over $100,000 or distributions from foreign trusts; Form 3520-A — annual return for foreign grantor trust with US owner; Form 5471 — US persons with interests in foreign corporations (10% or greater); Form 8621 — PFIC reporting; Form 8865 — US persons with interests in foreign partnerships (10% or greater); Form 8858 is not on the Part IV list (Part IV covers only Forms 3520, 3520-A, 5471, 8621 and 8865). The coordination is one-way: Form 8938 defers to these forms. Filing one of them does not satisfy FBAR. FBAR remains an independent obligation with its own form, due date, platform, and penalty regime.  _(https://www.irs.gov/instructions/i8938)_

## 17. Reviewer Self-Checks

Before signing off on any return implicating these forms, the reviewer should verify:

- **Schedule B Part III consistency** — Schedule B Part III has been answered consistently with FBAR/8938 filings and prior-year answers.
- **FBAR aggregate threshold computation** — FBAR aggregate threshold has been computed correctly (aggregate of each reportable account's annual maximum, whether or not contemporaneous, in USD at the reporting year-end rate). [Source](https://www.fincen.gov/system/files/shared/FBAR%20Line%20Item%20Filing%20Instructions.pdf).
- **Form 8938 thresholds applied correctly** — Form 8938 thresholds have been applied with the correct filing-status and residence tier.
- **All accounts reported on both forms where applicable** — All accounts are reported on both forms where applicable — the original 99% population assertion is unverified and unavailable for reliance; reconcile each asset under each regime.
- **Signature-authority accounts reported on FBAR** — Signature-authority accounts are tested for FBAR reporting, applicable employee exemptions and detail rules even when not on Form 8938. [Source](https://www.ecfr.gov/current/title-31/subtitle-B/chapter-X/part-1010/subpart-C/section-1010.350).
- **PFIC trigger consideration** — PFIC trigger has been considered for every foreign fund, ETF, or pooled investment.
- **Form 8621 filed for PFIC interests meeting threshold** — Form 8621 has been filed for every PFIC interest where the §1298(f) threshold is met.  _(§1298(f))_
- **Cross-references in Form 8938 Part IV** — Cross-references in Form 8938 Part IV correctly identify any 3520/5471/8621/8865/3520-A filings.  _(https://www.irs.gov/instructions/i8938)_
- **Currency translation rate** — Currency translation uses the Treasury Reporting Rate of Exchange for the appropriate date.
- **Reasonable-cause documentation for late filings** — Reasonable-cause documentation is in the file if any late filings are involved.

**Non-usable hold:** The precise section 6694/Circular 230 elements are unverified; the preparer name or an omission alone does not establish liability.

A missed FBAR or 8938 is a reviewer responsibility under Circular 230. The advisor's name on a return with willfully or recklessly omitted disclosure exposes the advisor to §6694 preparer penalties and §10.51 Circular 230 discipline.

## 18. Quick Reference — Citations

- **31 USC §5314** — BSA authority for foreign account reports  _(31 USC §5314)_
- **31 CFR §1010.350** — FBAR filing requirement, definitions, exceptions  _(31 CFR §1010.350)_
- **31 CFR §1010.420** — FBAR recordkeeping  _(31 CFR §1010.420)_
- **31 USC §5321(a)(5)** — FBAR civil penalties  _(31 USC §5321(a)(5))_
- **31 USC §5322** — FBAR criminal penalties  _(31 USC §5322)_
- **IRC §6038D** — FATCA Form 8938 reporting  _(IRC §6038D)_
- **Treas. Reg. §1.6038D-1 through -8** — FATCA implementing regulations  _(Treas. Reg. §1.6038D-1 through -8)_
- **IRC §6662(j)** — 40% accuracy penalty on attributable tax underpayment  _(IRC §6662(j))_
- **IRC §6501(c)(8) and §6501(e)(1)(A)(ii)** — extended statute of limitations  _(IRC §6501(c)(8) and §6501(e)(1)(A)(ii))_
- **IRC §1291** — PFIC excess distribution regime  _(IRC §1291)_
- **IRC §1297** — PFIC definition  _(IRC §1297)_
- **IRC §1298(f)** — Form 8621 filing requirement  _(IRC §1298(f))_
- **Bittner v. United States, 598 U.S. 85 (2023)** — non-willful FBAR penalty per form, not per account  _(Bittner v. United States, 598 U.S. 85 (2023))_
- **United States v. Williams, 489 F. App'x 655 (4th Cir. 2012)** — willful FBAR willfulness standard  _(United States v. Williams, 489 F. App'x 655 (4th Cir. 2012))_
- **IRS Memorandum LB&I-09-1118-014 (Nov. 20, 2018)** — Updated Voluntary Disclosure Practice  _(IRS Memorandum LB&I-09-1118-014 (Nov. 20, 2018))_
- **IRM 4.26.16** — FBAR examination procedures  _(IRM 4.26.16)_
- **IRM 4.26.17** — FBAR penalty procedures (mitigation is discussed in IRM 4.26.16)  _(IRM 4.26.17)_

## 19. Refusal Catalogue

This skill does **not** address:

- **Pre-immigration/expatriation matters** — Pre-immigration tax planning, expatriation under §877A, or covered-expatriate filings  _(§877A)_
- **PFIC §1291 computational depth** — Computational depth of PFIC §1291 — the skill flags PFICs and refers to a dedicated PFIC skill  _(§1291)_
- **Form 5471 CFC analysis** — Form 5471 controlled foreign corporation analysis — separate skill
- **Form 3520/3520-A foreign trust analysis** — Form 3520/3520-A foreign trust analysis — separate skill
- **Section 962 election analysis** — Section 962 election analysis
- **GILTI / FDII / BEAT** — GILTI / FDII / BEAT — separate skill (`us-gilti-fdii-beat`)
- **Foreign earned income exclusion** — Foreign earned income exclusion — separate skill (`us-foreign-earned-income-2555`)
- **Foreign tax credit computation** — Foreign tax credit computation — separate skill (`us-foreign-tax-credit-1116`)
- **Sanctions and OFAC analysis** — Sanctions and OFAC analysis — refer to sanctions counsel
- **Non-US tax law** — Non-US tax law (treatment of accounts in the foreign jurisdiction)
- **Estate and gift tax with foreign components** — Estate and gift tax with foreign components — partial coverage in `us-estate-gift-706-709`
- **State income tax treatment of foreign account income** — State income tax treatment of foreign account income — refer to state skills

For any matter outside the scope above, refer to the appropriate dedicated skill or external specialist.


## Sources

The linked authorities below were read on 22 November 2026 within the stated scope. This correction retains tax-year 2025 coverage and does not establish tax-year 2026 guidance.

| Authority | Actual read scope and short source wording | Read on |
| --- | --- | --- |
| [31 CFR1010.350](https://www.ecfr.gov/current/title-31/subtitle-B/chapter-X/part-1010/subpart-C/section-1010.350) | Read in the linked authority (bounded scope): Actual (b),(c),(e),(f),(g) read; public-fund definition, legal title, indirect interests and exemptions. Excerpt: “mutual fund or similar pooled fund”. | 2026-11-22 |
| [FinCEN line-item instructions](https://www.fincen.gov/system/files/shared/FBAR%20Line%20Item%20Filing%20Instructions.pdf) | Read in the linked authority (bounded scope): Actual general definitions, valuation pp9–10 and filing/authorization passages read; current FinCEN hub links this PDF despite its legacy extracted title. Excerpt: “aggregate of the maximum account values”. | 2026-11-22 |
| [IRS IRM4.26.16](https://www.irs.gov/irm/part4/irm_04-026-016) | Read in the linked authority (bounded scope): Actual 26Aug2025 revision: reporting, valuation, married filings, records, penalties and discretion. Not a read of every case it cites. Excerpt: “single non-willful reporting violation”. | 2026-11-22 |
| [FinCEN FIN2025NTC3](https://www.fincen.gov/system/files/2025-12/FBAR-FBAR-Filing-Requirement-for-Certain-Financial-Professionals.pdf) | Read in the linked authority (bounded scope): Both pages read. Covered prior-extension classes only; 2025 signature-authority extension is15Apr2027. Excerpt: “April 15, 2027”. | 2026-11-22 |
| [31 CFR1010.821](https://www.ecfr.gov/current/title-31/section-1010.821) | Read in the linked authority (bounded scope): Actual current table read, displayed up to date19Nov2026:16,536/165,353 assessed on/after17Jan2025. Do not invent another annual amount. Excerpt: “16,536”. | 2026-11-22 |
| [IRS Form8938 instructions](https://www.irs.gov/instructions/i8938) | Read in the linked authority (bounded scope): Actual substantive filing, entity, threshold, interest, valuation, exception, penalty and PartI–VI passages read. Current revision11/2021 remains published; do not reject solely for age. Excerpt: “If you do not have to file an income tax return”. | 2026-11-22 |
| [Official IRC6501](https://uscode.house.gov/us/usc/119-124/t26/s6501/) | Read in the linked authority (bounded scope): Actual (c)(8),(e)(1)(A)(ii) read; official text through15Oct2026. Cornell inline URL opened too, but official counterpart supplies authority. Excerpt: “without regard to the dollar threshold”. | 2026-11-22 |
| [Official31USC5321](https://uscode.house.gov/us/usc/119-124/t31/s5321/) | Read in the linked authority (bounded scope): Actual(a)(5),(b) read: statutory caps, balance at violation, reasonable cause and assessment period. Excerpt: “the balance in the account at the time of the violation”. | 2026-11-22 |
| [Official31USC5322](https://uscode.house.gov/us/usc/119-124/t31/s5322/) | Read in the linked authority (bounded scope): Actual(a),(b) read: enhanced criminal limb includes another US-law violation, alternatively the100k pattern. Excerpt: “while violating another law of the United States”. | 2026-11-22 |
| [31 CFR1010.420](https://www.ecfr.gov/current/title-31/section-1010.420) | Read in the linked authority (bounded scope): Actual account record contents and5-year period read, not just header. Excerpt: “retained for a period of 5 years”. | 2026-11-22 |
| [IRS domestic streamlined](https://www.irs.gov/individuals/international-taxpayers/us-taxpayers-residing-in-the-united-states) | Read in the linked authority (bounded scope): Actual eligibility,3/6periods, annualYE penalty base and relief qualifications read. Excerpt: “year-end account balances and year-end asset values”. | 2026-11-22 |
| [IRS foreign streamlined](https://www.irs.gov/individuals/international-taxpayers/us-taxpayers-residing-outside-the-united-states) | Read in the linked authority (bounded scope): Actual alternative nonresidency tests, both-spouse requirement, filings and relief qualifications read. Excerpt: “Any previously assessed penalties”. | 2026-11-22 |
| [IRS delinquent information returns](https://www.irs.gov/individuals/international-taxpayers/delinquent-international-information-return-submission-procedures) | Read in the linked authority (bounded scope): Actual full operative short page read, including3520/3520A exception and current reasonable-cause processing note. Excerpt: “Penalties may be assessed”. | 2026-11-22 |
| [IRS current FBAR page](https://www.irs.gov/businesses/small-businesses-self-employed/report-of-foreign-bank-and-financial-accounts-fbar) | Read in the linked authority (bounded scope): Actual exceptions, delinquent filing and record passages read; standalone legacy DFSP URL returned404. Excerpt: “may subject you to penalties”. | 2026-11-22 |
| [IRS VDP page](https://www.irs.gov/compliance/criminal-investigation/irs-criminal-investigation-voluntary-disclosure-practice) | Read in the linked authority (bounded scope): Actual eligibility/timeliness and proposal-status paragraphs read. Dec2025proposal is expressly not final/effective; not substituted as enacted procedure. Excerpt: “before the proposal is finalized and placed into effect”. | 2026-11-22 |
| [IRS IRM4.63.3](https://www.irs.gov/irm/part4/irm_04-063-003r) | Read in the linked authority (bounded scope): Actual current VDP penalty/disclosure-period passages read; procedures and case facts control. Excerpt: “highest tax deficiency”. | 2026-11-22 |
| [IRS IRM4.26.17](https://www.irs.gov/irm/part4/irm_04-026-017r) | Read in the linked authority (bounded scope): Actual assessment, extension and six-year guidance read. Old non-r path404; corrected r-path works. Excerpt: “contact Counsel for advice”. | 2026-11-22 |
| [IRS2025 Publication54](https://www.irs.gov/publications/p54) | Read in the linked authority (bounded scope): Actual2025 extension passages read: discretionary letter forDec15 versus2350residency-test extension. Excerpt: “send the IRS a letter”. | 2026-11-22 |
| [IRS2025 Form8621 instructions](https://www.irs.gov/instructions/i8621) | Read in the linked authority (bounded scope): Actual PFIC definition, filing exception, QEF/MTM timing and1291 allocation passages read; no full PFIC computation review. Excerpt: “in a year other than the first year”. | 2026-11-22 |
| [IRS2025 Form3520A instructions](https://www.irs.gov/instructions/i3520a) | Read in the linked authority (bounded scope): Actual purpose/filing and owner responsibility read; continuous-use2025andlater untilsuperseded. Excerpt: “foreign trust with at least one U.S. owner”. | 2026-11-22 |
| [Official IRC7702](https://uscode.house.gov/us/usc/119-124/t26/s7702/) | Read in the linked authority (bounded scope): Actual definition(a),(b) read: contract tests, not a categorical foreign-issuer disqualification. Excerpt: “meets the cash value accumulation test”. | 2026-11-22 |
| [FinCEN FBAR hub](https://www.fincen.gov/report-foreign-bank-and-financial-accounts) | Read in the linked authority (bounded scope): Actual10k gateway and linked instructions inspected. Hub is not proof every special notice was read. Excerpt: “exceeds $10,000”. | 2026-11-22 |
| [Official IRC6663](https://uscode.house.gov/us/usc/119-124/t26/s6663/) | Read in the linked authority (bounded scope): Actual full operative(a)–(c) read; fraudulent underpayment and joint-return qualification. Excerpt: “75 percent of the portion of the underpayment”. | 2026-11-22 |

**Not yet confirmed; non-usable holds:** The inline holds remain unresolved. They cover historical enactment and notice claims; demographic/prevalence and fee predictions; named pension/provident and gaming/prepaid classifications; joint-asset and special pension valuation; exact foreign-currency conversions and incomplete worked-case histories; the full Form 8938 interest test; named judgments and precise defense/preparer-liability elements; current DFSP availability/relief and form-specific delinquent-return processing; VDP history/exclusivity; foreign plan/treaty, inherited-fund and foreign-law/sanctions assertions; exact Schedule B wording; complete record-retention and other-information-return gateways. No held assertion may be used to choose a filing, program, legal position, tax amount or fee. Original case inputs are illustrations only where the missing facts are stated.

Independent source review and accountant approval of the changed version are pending.
