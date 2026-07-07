---
name: us-fbar-and-fatca-8938
description: Tier 2 US federal content skill for the dual foreign financial account disclosure regimes — FinCEN Form 114 (FBAR) under 31 USC §5314 and Form 8938 (FATCA) under IRC §6038D. Covers tax year 2025 including the $10,000 aggregate FBAR threshold (per Bittner 2023 non-willful penalty is per-form not per-account), Form 8938 specified person and SFFA thresholds ($50k/$100k/$200k/$400k tiers), the differences in coverage (signature authority for FBAR, ownership for 8938, foreign mutual funds for 8938 only), willful and non-willful penalty severity, and the Streamlined Foreign Offshore / Domestic Offshore compliance paths for catching up.
jurisdiction: US
domain: federal-tax
tax_year: 2025
tier: 2
last_updated: 2026-07-06
---

# us-fbar-and-fatca-8938

## US FBAR + FATCA Form 8938 — Foreign Financial Account Disclosure (Tax Year 2025)

## 1. Scope and Purpose

This skill covers the two overlapping but legally distinct foreign financial account disclosure regimes that apply to US persons for tax year 2025:

1. **FinCEN Form 114** — the Report of Foreign Bank and Financial Accounts ("FBAR"), administered by the Financial Crimes Enforcement Network (FinCEN) of the US Treasury under the Bank Secrecy Act (31 USC §5314 and 31 CFR §1010.350).
2. **Form 8938** — the Statement of Specified Foreign Financial Assets, administered by the IRS under the Foreign Account Tax Compliance Act (FATCA), codified at IRC §6038D.

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
| Threshold | $10,000 aggregate at any time | $50k–$600k depending on filing status and residence |
| Who | "US person" with financial interest OR signature authority | "Specified person" with ownership of SFFAs |
| Foreign real estate | Out of scope | Out of scope (when held directly) |
| Foreign mutual funds held by foreign broker | In scope | In scope (also triggers PFIC) |
| Foreign pensions | Generally in scope | In scope |
| Cash-value foreign life insurance | In scope | In scope |
| Signature authority only | **In scope** | **Out of scope** |
| Due date | April 15, automatic extension to October 15 | April 15 with return; October 15 with Form 4868 |
| Non-willful civil penalty (max) | $10,000 per form per year (Bittner 2023) | $10,000 + $50,000 continuing |
| Willful civil penalty | Greater of $100,000 or 50% of balance per violation | N/A — accuracy penalty 40% on unreported income |
| Criminal | Up to $250,000 + 5 years (willful) | Generally none independent of §7203/§7206 |
| Statute of limitations | 6 years from due date (31 USC §5321(b)(1)) | 6 years on return when §6038D omitted (§6501(e)(1)(A)(ii)) |

The threshold gap is wide: a single $11,000 foreign checking account triggers FBAR but not Form 8938. A married-joint US-resident couple with $90,000 spread across foreign accounts triggers FBAR but not 8938. Above the 8938 thresholds, both forms are almost always required because nearly every SFFA is also an FBAR-reportable account.

## 3. FBAR — FinCEN Form 114

### 3.1 Statutory basis

- **BSA authorizing statute** — The Bank Secrecy Act authorizes the Secretary of the Treasury to require reports of "transactions or relationships" with foreign financial agencies.  _(31 USC §5314)_
- **Implementing regulation requirement** — Requires each US person having a financial interest in, or signature or other authority over, a bank, securities, or other financial account in a foreign country to report such relationship to the Commissioner of Internal Revenue for each year in which such relationship exists.  _(31 CFR §1010.350)_

The form is not filed with the income tax return. It is filed electronically through the BSA E-Filing System operated by FinCEN. There is no paper option for routine filers.

### 3.2 Who must file

- **US person for FBAR purposes** — US citizens (regardless of where they reside); US residents — including green card holders and any individual who meets the substantial presence test of IRC §7701(b); US-formed entities — corporations, partnerships, LLCs (single-member or multi-member regardless of federal tax classification), and trusts and estates formed under US state or federal law.  _(31 CFR §1010.350(b))_
- **Single-member LLC FBAR treatment** — A single-member LLC that is disregarded for federal income tax purposes is not disregarded for FBAR purposes. The LLC files its own FBAR if it meets the threshold. The owner separately files an FBAR for the same accounts if the LLC's accounts are reportable by the owner under the financial-interest test (see §3.5). Joint filers may file a joint FBAR (Form 114a authorization) for accounts they jointly own with a spouse, but only if the only foreign accounts owned by the non-filing spouse are jointly owned with the filer.  _(31 CFR §1010.350(b))_

### 3.3 The $10,000 aggregate threshold

- **FBAR aggregate threshold** — $10,000 USD (aggregate maximum balance of all foreign financial accounts at any one point during the calendar year)  _(31 CFR §1010.350)_
- **Consequences of exceeding threshold** — If aggregate ever exceeds $10,000, every account must be reported — even an account that itself never exceeded $100, and even an account that was closed during the year. The threshold is calendar-year, not tax-year. Fiscal-year entities still apply a calendar-year FBAR. The threshold is per US person, not per account. A US person with five foreign accounts of $2,500 each, all at year-end, has $12,500 aggregate and must file. Currency conversion uses the Treasury Reporting Rate of Exchange in effect at the end of the calendar year (December 31). Use the same rate even for an account that was closed earlier in the year — the rule is "year-end rate applied to the maximum value during the year." Maximum value can be the highest end-of-month statement balance during the year if periodic statements are available; otherwise the highest value the account holder is aware of.  _(31 CFR §1010.350)_

### 3.4 What is a "foreign financial account"

- **Reportable account categories** — 1. Bank accounts — savings, checking, time deposits, certificates of deposit, demand deposits, fixed deposits, in any foreign bank or financial institution. 2. Securities accounts — brokerage accounts, custodial accounts holding stock or other securities, mutual fund accounts held at a foreign institution. 3. Other financial accounts — including: Foreign mutual fund accounts (counts as a financial account even when individual fund shares are titled to the holder); Cash-value foreign life insurance policies and annuities — the cash surrender value is the reportable amount; Certain foreign pension plans and retirement accounts when the holder has direct access to balance information and the institution acts as a custodian (this is fact-dependent; see §3.7); Online gambling accounts and certain prepaid value accounts where the underlying provider is a foreign financial institution.  _(31 CFR §1010.350(c))_
- **Foreign determined by institution location** — An account is "foreign" when the financial institution is physically located outside the United States — this is institution-location, not account-currency or owner-residence. A US-dollar account at a London branch of a US bank is foreign. A euro-denominated account at a New York branch of Deutsche Bank is not foreign for FBAR purposes (it is held at a US-located branch).  _(31 CFR §1010.350(c))_

### 3.5 Financial interest

- **Financial interest criteria** — The US person is the owner of record or holder of legal title — whether for their own benefit or as agent, nominee, or in another capacity for any other person; The owner of record is acting as agent, nominee, attorney, or in some other capacity on behalf of the US person; A corporation owns the account and the US person owns directly or indirectly more than 50% of the voting power or value; A partnership owns the account and the US person owns directly or indirectly more than 50% of the interest in profits or capital; A trust owns the account and the US person is the grantor and has an ownership interest under §§671–679 (the grantor-trust rules), or is the beneficiary of more than 50% of the income or assets.  _(31 CFR §1010.350(e))_

### 3.6 Signature or other authority

- **Signature or other authority definition** — "Signature or other authority" means the authority of an individual (alone or in conjunction with another) to control the disposition of money, funds, or other assets held in a financial account by direct communication (whether in writing or otherwise) to the person with whom the financial account is maintained.  _(31 CFR §1010.350(f))_

Treasurer or CFO of a US company with signing power on the company's foreign bank accounts; US individual serving as trustee of a foreign trust without beneficial interest; US individual serving as attorney-in-fact on an elderly relative's foreign account; Executor of an estate that owns foreign accounts; Spouse listed as authorized signer on a non-US-spouse's foreign account where the US spouse has no ownership.

> **AUDIT FLASH POINT — signature-only authority.** US executives at multinational companies routinely have signature authority on dozens of foreign subsidiary accounts. Each such account is reportable on FBAR even when the executive has no personal financial stake. Exemption available for certain officers/employees of publicly traded companies and certain regulated entities (31 CFR §1010.350(f)(2)) and for employees of banks examined by federal banking agencies — but the exemption is narrow. Always verify by reference to the regulation rather than assuming.

### 3.7 Foreign pensions — a recurring grey area

- **Foreign pension FBAR treatment** — Generally reportable: Defined-contribution accounts held with an identifiable financial institution custodian where the participant directs investments or can ascertain a balance (e.g., Australian superannuation self-managed funds, certain UK SIPPs, Canadian RRSPs held at a brokerage); Indian Public Provident Fund (PPF) accounts when held at an Indian bank; Indian Employees' Provident Fund (EPF) — IRS guidance has historically treated these as reportable. Often not reportable as accounts (though may still be reportable on other forms): Defined-benefit-only employer pensions where the employee has no individual account; Foreign social security analogues (e.g., UK State Pension, Indian Social Security). When in doubt, file. The non-willful penalty for over-reporting is zero; the non-willful penalty for under-reporting is $10,000.  _(IRS guidance (unspecified in source))_

### 3.8 Due date and filing mechanics

- **FBAR due date and extension** — The FBAR is due April 15 of the year following the calendar year being reported. Since 2017 a six-month automatic extension to October 15 has been available — no form needs to be filed to claim the extension; it is automatic for all filers. There is no further extension beyond October 15 except in narrow disaster-area circumstances.  _(31 CFR §1010.350)_
- **Filing mechanics detail** — Filing is through the BSA E-Filing System (bsaefiling.fincen.treas.gov). The form requires identification of each account: institution name, address, account number, maximum value during the year (in USD), and the relationship of the filer to the account. There is no fee. There is no paper option for routine cases. The signed form is retained by the filer (5-year retention under 31 CFR §1010.420). FinCEN may request supporting records during this period; failure to provide them is itself sanctionable.  _(31 CFR §1010.420)_

## 4. Form 8938 — Statement of Specified Foreign Financial Assets

### 4.1 Statutory basis

- **FATCA statutory basis** — FATCA was enacted as part of the Hiring Incentives to Restore Employment Act of 2010, adding §6038D to the Internal Revenue Code. The implementing regulations at Treas. Reg. §1.6038D-1 through §1.6038D-8 require a "specified person" to report "specified foreign financial assets" (SFFAs) for any tax year in which the aggregate value of those assets exceeds the applicable threshold. Form 8938 is attached to Form 1040 (or 1120, 1065, etc., for in-scope entities). It is filed with the income tax return and follows the income tax return's due date and extension.  _(IRC §6038D; Treas. Reg. §1.6038D-1 through §1.6038D-8)_

### 4.2 Specified person

- **Specified individual** — A US citizen, a resident alien for any portion of the year, a nonresident alien who elects to be treated as a resident under §6013(g) or §6013(h), or a bona fide resident of American Samoa or Puerto Rico (with modifications).  _(IRC §6038D; §6013(g); §6013(h))_
- **Specified domestic entity** — Under regulations effective for tax years beginning after December 31, 2015, a domestic corporation, partnership, or trust will be a specified domestic entity if it is "formed or availed of" for purposes of holding specified foreign financial assets. The regulations apply a presumption test based on passive income and asset composition (the 50% passive income or 50% passive asset thresholds).  _(Treas. Reg. §1.6038D-6)_
- **Single-member LLC 8938 treatment** — Single-member LLCs disregarded for federal income tax purposes are disregarded for §6038D purposes too. The owner reports the LLC's foreign accounts on the owner's own Form 8938 attached to the owner's Form 1040. This is the opposite of the FBAR rule.  _(IRC §6038D)_

### 4.3 What is a Specified Foreign Financial Asset (SFFA)

- **SFFA categories** — 1. Financial accounts maintained by a foreign financial institution — the FATCA-defined FFI is broader than the FBAR-defined "financial institution" but in practice covers the same retail accounts: foreign bank, brokerage, mutual fund, custodial accounts. 2. Foreign financial assets held outside of an account — this is the category that is in 8938 but not in FBAR: Stock or securities issued by a non-US person held in the taxpayer's own name (not in a custodial account); Interests in foreign partnerships (general or limited); Interests in foreign trusts and foreign estates (when the holder knows or has reason to know of the interest); Foreign-issued financial instruments and contracts with non-US counterparties (forward contracts, options, swaps, notes, debentures); Interests in foreign hedge funds and foreign private equity funds — typically held as limited partnership or non-US corporation interests; Cash-value foreign life insurance and annuity contracts.  _(§6038D(b))_

### 4.4 What is NOT an SFFA

- **SFFA exclusions** — Directly held foreign real estate — a vacation home in Spain titled in the US owner's name is not reportable on 8938 or FBAR. Income from it must still be reported on Schedule E. If the real estate is held through a foreign corporation or partnership, the entity interest is an SFFA. Foreign currency held directly — physical cash and bullion are not SFFAs (though gold held in a foreign bank account is, because the account is). Tangible personal property held directly — art, jewelry, collectibles, automobiles. Assets held in a US financial account — even if the underlying issuer is foreign. Foreign stock held at Fidelity is not an SFFA. Social Security analogues — foreign social security, social insurance, or other similar program of a foreign government is not an SFFA.  _(IRC §6038D)_

### 4.5 Form 8938 thresholds

**Form 8938 thresholds**  _(IRC §6038D)_

| Filer | Year-end | At any time during year |
| --- | --- | --- |
| Unmarried, US-resident | $50,000 | $75,000 |
| Married filing joint, US-resident | $100,000 | $150,000 |
| Married filing separate, US-resident | $50,000 | $75,000 |
| Unmarried, abroad (bona fide resident) | $200,000 | $300,000 |
| Married filing joint, abroad | $400,000 | $600,000 |
| Married filing separate, abroad | $200,000 | $300,000 |
| Specified domestic entity | $50,000 | $75,000 |

- **Abroad definition** — "Abroad" for these purposes generally means meeting the bona fide foreign residence test or the physical presence test under §911 (the foreign earned income exclusion residence tests). Mere absence from the US does not by itself put a filer in the higher-threshold category.  _(IRC §911)_

These thresholds are dramatically higher than the FBAR's flat $10,000. A typical fact pattern:

- A US-resident individual with €40,000 in a French bank account: FBAR yes, Form 8938 no.
- A US-resident married couple with $90,000 jointly in foreign accounts: FBAR yes, Form 8938 no.
- A married US expat couple in Singapore with $350,000 in Singapore bank accounts: FBAR yes, Form 8938 no (under the $400k/$600k expat thresholds).
- A married US expat couple in Singapore with $700,000: both forms required.

### 4.6 Due date and extension

- **Form 8938 due date and extension** — Form 8938 is attached to and follows the Form 1040 due date — April 15 for calendar-year individuals, with extension to October 15 via Form 4868 (or to December 15 via Form 2350 for certain expat filers). There is no separate filing platform. This is one of the practical differences from FBAR: FBAR's extension is automatic; Form 8938's extension requires filing the underlying return's extension request.  _(IRC §6038D)_

### 4.7 Specific line categories on Form 8938

- **Form 8938 parts** — Part I — Foreign Deposit and Custodial Accounts Summary (these are usually the same accounts reported on FBAR); Part II — Other Foreign Assets Summary (the assets not in financial accounts — direct stock, partnership interests, contracts); Part III — Summary of Tax Items Attributable to SFFAs (income, deductions, credits, and the form/schedule each item flows to); Part IV — Excepted Specified Foreign Financial Assets (assets reported on another international information return, principally Forms 3520, 5471, 8621, 8865 — Form 8938 cross-references them rather than duplicating); Part V — Detailed Information for Each Foreign Deposit and Custodial Account (one block per account); Part VI — Detailed Information for Each "Other" SFFA (one block per non-account asset).  _(Form 8938 instructions)_
- **Part IV duplicate-reduction mechanism** — Part IV is the duplicate-reduction mechanism: if the same asset is reported on Form 5471, 8865, 8621, or 3520, the filer references the other form's filing and avoids the Part V/VI detail. The summary value still counts toward threshold determination.  _(Form 8938 instructions)_

## 5. The Overlap and the Differences

### 5.1 Why both are usually required

- **Why both regimes usually apply** — For any US person above the Form 8938 threshold, the answer is almost always "file both." The reasons: A retail foreign bank or brokerage account is an FBAR-reportable financial account AND a §6038D specified foreign financial asset. The FBAR threshold ($10k) is so much lower than 8938's that anyone over 8938's threshold is virtually always also over FBAR's. The forms are not substitutes; each is its own statutory obligation with its own penalty regime.

### 5.2 When only FBAR is required

- **FBAR-only scenarios** — Aggregate offshore exposure between $10,000 and the applicable 8938 threshold; US person with signature authority but no financial interest (8938 does not apply to signature-only authority); US LLC owned by a US person — the LLC files its own FBAR while the owner files Form 8938 reporting the LLC's accounts as the owner's SFFA (different rules on entity look-through).

### 5.3 When only Form 8938 is required (rare)

- **8938-only scenario** — A US person whose only SFFAs are non-account assets — e.g., directly held foreign stock certificates or a foreign partnership interest — and who has no foreign deposit or custodial account at all. The FBAR test is not met because there are no "financial accounts." This is rare in practice; most foreign partnership interests are held alongside a foreign bank account that distributes earnings.

### 5.4 Signature authority — only on FBAR

- **Signature authority difference** — This is the single most important practical difference. Form 8938 requires beneficial ownership of an SFFA; signature authority without ownership is not reportable on 8938. FBAR explicitly requires reporting by anyone with signature authority over a foreign account, even with no beneficial interest. > **AUDIT FLASH POINT — corporate signature authority.** US-based CFOs, treasurers, and controllers with signing power on the company's foreign subsidiary accounts must file personal FBARs reporting every such account. The $10,000 threshold aggregates across all accounts they have authority over (including their personal accounts). Many companies neglect to brief their officers on this obligation. Always ask the question: "Are you a signer on any foreign account of any company you work for?"

### 5.5 Foreign mutual funds — important asymmetry

- **Foreign mutual fund asymmetric treatment** — A foreign mutual fund held through a foreign brokerage account is reportable on both forms. But the same fund held in the holder's own name with the fund's transfer agent — common in India, where mutual fund investments are often registered directly — is not in a "financial account" for FBAR purposes (because there is no account at a financial institution holding the fund); but is an SFFA for Form 8938 (because it is foreign stock/securities held outside an account). This is also the entry point to the PFIC regime under §1291. See §8.

## 6. FBAR Penalties

The FBAR penalty regime is among the harshest in the entire federal tax and financial-reporting code. The penalties are codified at 31 USC §5321 (civil) and 31 USC §5322 (criminal).

### 6.1 Non-willful civil penalty — Bittner v. United States (2023)

- **Pre-Bittner IRS/FinCEN position** — Pre-Bittner, the IRS and FinCEN took the position that the non-willful penalty under 31 USC §5321(a)(5)(B)(i) — capped at $10,000 (adjusted for inflation; $16,536 for 2024-reportable violations and $17,103 for 2025-reportable violations per FinCEN inflation adjustments) — applied per account per year. Under this view, a filer with 12 foreign accounts who failed to file a single FBAR faced a $120,000-plus penalty.  _(31 USC §5321(a)(5)(B)(i))_
- **Bittner holding** — In Bittner v. United States, 598 U.S. 85 (2023), the Supreme Court held that the non-willful penalty is per form per year, not per account. The Court reasoned that the BSA reporting obligation is to file an FBAR (a single form), and a single failure to file that form is a single violation. This is a major taxpayer victory. A non-willful penalty for a missed FBAR with twelve accounts is now capped at one inflation-adjusted $10,000 maximum, not twelve.  _(Bittner v. United States, 598 U.S. 85 (2023))_
- **Important caveats** — Bittner does not affect willful penalties, which remain per-account-per-year. The IRS still has discretion to assert lower amounts or no penalty under its mitigation guidelines (IRM 4.26.16). Reasonable-cause relief under 31 USC §5321(a)(5)(B)(ii) remains available. The six-year statute of limitations under 31 USC §5321(b)(1) remains six years from the FBAR's April 15 due date — so the FBAR for calendar year 2018 (due April 15, 2019; extended to October 15, 2019) was time-barred for civil penalty assessment after April 15, 2025.  _(31 USC §5321(a)(5)(B)(ii); 31 USC §5321(b)(1); IRM 4.26.16)_

### 6.2 Willful civil penalty — draconian

- **Willful civil penalty amount** — greater of $100,000 (inflation-adjusted, $165,353 for 2024 violations and $171,032 for 2025 violations per FinCEN adjustments) or 50% of the balance in the account at the time of the violation USD/percent (per violation per year; per account per year for willful)  _(31 USC §5321(a)(5)(C))_

This is per violation per year — and "per violation" for willful is per account per year. A willful filer with 12 accounts averaging $200,000 faces a starting-point penalty of $1.2 million (12 × $100,000) or 50% of $2.4 million = $1.2 million, whichever is greater.

### 6.3 What is willful

- **Willfulness standard for FBAR** — "Willful" in the FBAR context is broader than the criminal-law standard. The Tax Court and the Federal Circuits have repeatedly held that willfulness includes: Actual knowledge of the FBAR obligation combined with intentional failure to file (the classic case); "Willful blindness" — deliberate avoidance of learning the obligation when the filer has reason to suspect it exists; Reckless disregard — a serious risk that the filer should have known about, but failed to investigate (see United States v. Williams, 489 F. App'x 655 (4th Cir. 2012); United States v. McBride, 908 F. Supp. 2d 1186 (D. Utah 2012); United States v. Bohanec, 263 F. Supp. 3d 881 (C.D. Cal. 2016)). Signing a Form 1040 Schedule B without answering the foreign account questions accurately, or answering them as "no" while holding a foreign account, has been treated as evidence of willfulness or reckless disregard.  _(United States v. Williams, 489 F. App'x 655 (4th Cir. 2012); United States v. McBride, 908 F. Supp. 2d 1186 (D. Utah 2012); United States v. Bohanec, 263 F. Supp. 3d 881 (C.D. Cal. 2016))_

### 6.4 Criminal penalties

- **Criminal penalty structure** — Under 31 USC §5322(a), a willful violation of any provision of the BSA, including FBAR filing, is punishable by a fine of up to $250,000 and imprisonment for up to 5 years. If the violation is part of a pattern of illegal activity involving more than $100,000 in a 12-month period (§5322(b)), the maximum fine doubles to $500,000 and the prison term doubles to 10 years. Criminal prosecutions remain rare relative to civil enforcement but are not theoretical. The DOJ Tax Division has prosecuted dozens of FBAR cases since 2009 in connection with the Swiss bank disclosures and subsequent enforcement.  _(31 USC §5322(a); 31 USC §5322(b))_

> **AUDIT FLASH POINT — willful vs non-willful determination.** This determination is the single highest-leverage judgment in an FBAR delinquency case. A willful determination can produce a million-dollar penalty; a non-willful determination caps at roughly $17,000 per form per year. The taxpayer's contemporaneous knowledge, the accountant's prior advice (or absence of it), and the Schedule B answers in prior years are all relevant. Documenting reasonable-cause facts at the outset of any catch-up engagement is essential.

### 6.5 Reasonable cause

- **Reasonable cause exception** — The statute provides a reasonable-cause exception to the non-willful penalty at 31 USC §5321(a)(5)(B)(ii): no penalty shall be imposed if the violation was due to reasonable cause and the amount of the transaction or balance in the account was properly reported. The reasonable-cause standard is fact-intensive and follows familiar tax principles: ordinary business care and prudence, reliance on a competent advisor, ignorance of the law where the obligation was genuinely unknown. Reasonable cause is not available for willful violations.  _(31 USC §5321(a)(5)(B)(ii))_

### 7.1 Failure to file — $10,000 plus continuing

- **§6038D(d) failure-to-furnish penalty** — Under §6038D(d), a specified person who fails to furnish required information is subject to a $10,000 penalty. If the failure continues for more than 90 days after the IRS mails a notice of failure, an additional $10,000 penalty applies for each 30-day period (or fraction) during which the failure continues after the 90-day period, up to a maximum continuing-failure penalty of $50,000. The maximum combined failure-to-file penalty per year is therefore $60,000 ($10,000 initial + $50,000 continuing).  _(§6038D(d))_

### 7.2 Accuracy-related penalty — 40% on undisclosed income

- **Accuracy-related penalty on undisclosed SFFA understatement** — 40% percent (applies to the portion of an underpayment of tax attributable to any undisclosed foreign financial asset understatement; double the standard 20% accuracy-related penalty under §6662(a))  _(§6662(j))_

### 7.3 Reasonable cause

- **§6038D(g) reasonable cause defense** — Section 6038D(g) provides a reasonable-cause defense to the §6038D(d) penalty if the taxpayer establishes that the failure was due to reasonable cause and not willful neglect. The fact that a foreign jurisdiction would impose a civil or criminal penalty on the taxpayer for disclosure is, by statute, not reasonable cause (§6038D(g)). The 40% accuracy penalty under §6662(j) has its own reasonable-cause overlay through §6664(c).  _(§6038D(g); §6664(c))_

### 7.4 Extended statute of limitations — §6501(e)(1)(A)(ii)

- **Six-year assessment extension** — Under §6501(e)(1)(A)(ii) (as amended by FATCA), the period for assessing tax is extended to six years when the taxpayer omits from gross income any amount that exceeds $5,000 and is attributable to one or more assets with respect to which information was required to be reported under §6038D and the required information was not provided.  _(§6501(e)(1)(A)(ii))_
- **Indefinite statute when 8938 missing** — Under §6501(c)(8), the statute of limitations does not begin to run at all for the entire return until the §6038D information is furnished, if the failure to furnish information is due to gross negligence or worse. This means the IRS can audit a return indefinitely if Form 8938 was required but never filed — even for items unrelated to the foreign asset. The interaction is a powerful deterrent: a missing Form 8938 keeps the entire return open to IRS examination indefinitely.  _(§6501(c)(8))_

## 8. PFIC Interaction (§1291) — Refer Out

When a US person holds shares of a foreign mutual fund, foreign ETF, foreign exchange-traded vehicle, foreign hedge fund, foreign private equity fund, or many foreign insurance-wrapped investment products, the investment is almost always a Passive Foreign Investment Company under IRC §1297.

PFIC consequences:

- Punitive deemed-distribution tax regime under §1291: gain on disposition and "excess distributions" are taxed at the highest ordinary rate in effect in each year of the holding period (not the year of sale), with an interest charge for the deferral.
- Required filing of Form 8621 for each PFIC for each year in which the US person holds an interest, sells an interest, or receives a distribution. Form 8621 is filed with Form 1040.
- Available elections: Qualified Electing Fund (QEF) election under §1295 — requires the fund to provide a PFIC Annual Information Statement (most foreign funds will not); Mark-to-Market election under §1296 — available for marketable PFIC stock. Both elections must generally be made for the first year of the US person's holding period.
- Foreign mutual funds are flagged on Form 8938 as SFFAs and require separate Form 8621. Form 8938 Part IV cross-references Form 8621 to avoid duplicate detail.

> **AUDIT FLASH POINT — PFIC mutual funds.** Every Indian, UK, EU, Canadian, Australian, and other foreign mutual fund in a client's portfolio is almost certainly a PFIC. The catch-up cost of curing a multi-year unreported PFIC position is often greater than the entire investment return. This is one of the single most damaging tax exposures in international personal finance.

The detailed mechanics of §1291, §1295 QEF, §1296 mark-to-market, the §1298(f) Form 8621 filing thresholds, and the interaction with foreign tax credits are out of scope for this skill. Refer to a dedicated PFIC skill or specialist.

## 9. Compliance Paths for Late or Non-Filers

The IRS has published multiple programs for taxpayers who have failed to comply with FBAR, Form 8938, or related international information return obligations. Choosing the wrong program can produce dramatically different penalty outcomes. The current menu (as of 2025) is:

### 9.1 Streamlined Foreign Offshore Procedures (SFOP)

- **SFOP eligibility and penalty structure** — For US persons living abroad whose non-compliance is non-willful. Eligibility: Non-residency requirement met: for the most recent three tax years for which the US return due date has passed, the taxpayer did not have a US abode and was physically outside the US for at least 330 full days in at least one of those years. Non-willful certification on Form 14653. Three years of amended or original returns + six years of FBARs. Penalty structure: zero Title 26 miscellaneous offshore penalty AND zero FBAR penalty. The taxpayer pays the back income tax with interest, but no penalties. This is the single most favorable catch-up program for eligible expat filers.  _(Form 14653)_

### 9.2 Streamlined Domestic Offshore Procedures (SDOP)

- **SDOP eligibility and penalty structure** — For US residents whose non-compliance is non-willful and who fail the SFOP non-residency test. Eligibility: US-resident; failed to meet SFOP's 330-day-abroad test; Previously filed US returns for the three years involved (cannot use SDOP for non-filed returns at all — use a delinquent return program instead); Non-willful certification on Form 14654; Three years of amended returns + six years of FBARs. Penalty structure: a 5% Title 26 miscellaneous offshore penalty on the highest aggregate balance of unreported foreign financial accounts and SFFAs during the covered years. No FBAR penalty. No 40% §6662(j) accuracy penalty. No §6038D failure-to-file penalty. The 5% is calculated on the highest year-end balance during the covered period — not on understated income, and not on accumulated unreported income. This is a significant penalty but generally much smaller than the willful or even non-willful regime applied account-by-account.  _(Form 14654)_

### 9.3 Delinquent FBAR Submission Procedures (DFSP)

- **DFSP eligibility and penalty structure** — For taxpayers who had no unreported income and missed only the FBAR. Eligibility: All required FBARs have not been filed; All taxable income from the foreign accounts was properly reported on the income tax return; Taxpayer is not under examination or criminal investigation. Penalty structure: no FBAR penalty if the requirements are met. The taxpayer e-files the delinquent FBARs through the BSA E-Filing System with a statement explaining why they were filed late. This is the right path when, for example, a green-card holder properly reported interest income from a Swiss account on Schedule B but missed the FBAR.

### 9.4 Delinquent International Information Return Submission Procedures (DIIRSP)

- **DIIRSP eligibility and penalty structure** — For taxpayers who had no unreported income but missed an international information return such as Form 5471, 5472, 8865, 3520, 3520-A, 8858, or 8938. Under guidance updated in 2020, the DIIRSP no longer provides automatic penalty relief — the taxpayer must establish reasonable cause and may face a penalty. In practice, the program is used when the taxpayer files the late returns with a reasonable-cause statement and accepts that the IRS may still assess penalty.

### 9.5 Voluntary Disclosure Practice (VDP)

- **VDP history and structure** — The legacy Offshore Voluntary Disclosure Program (OVDP) closed September 28, 2018. It was replaced by the Updated Voluntary Disclosure Practice announced in IRS Memorandum LB&I-09-1118-014 (November 20, 2018). The VDP is the only path for taxpayers whose non-compliance is willful. Eligibility requires pre-clearance through IRS Criminal Investigation. The penalty structure is harsh: Civil fraud penalty (75%) on the year with the highest tax liability in the 6-year disclosure period; Willful FBAR penalty (50% of highest aggregate balance) for one year; Income tax, interest, and other penalties for the disclosure period. The benefit of VDP is the strong (though not absolute) protection against criminal prosecution. Taxpayers and their counsel must weigh this protection against the substantial financial penalty.  _(IRS Memorandum LB&I-09-1118-014 (November 20, 2018))_

### 9.6 Choosing the right path — decision framework

**Decision framework for compliance path selection**

| Fact pattern | Recommended path |
| --- | --- |
| Lived abroad 330+ days, non-willful, returns were filed but FBAR/8938 missed | SFOP |
| Lived in US, non-willful, returns were filed but FBAR/8938 missed | SDOP |
| Income properly reported, only FBAR missed | DFSP |
| Income properly reported, only Form 8938 (or 5471 etc.) missed | DIIRSP with reasonable cause |
| Willful conduct in any prior year | VDP — coordinate with counsel |
| Under IRS audit or criminal investigation | None of the above — coordinate with counsel |

> **AUDIT FLASH POINT — late catch-up program selection.** This is the highest-stakes decision in an FBAR / 8938 catch-up engagement. SFOP and SDOP are non-willful-only; a later determination of willfulness on the same facts can convert a $0 or 5% penalty into a 50%-of-balance disaster. Document the non-willful certification facts carefully and engage tax counsel if there is any doubt about the willfulness characterization. A taxpayer who has been signing Schedule B "no" while holding foreign accounts is a high-risk willfulness case regardless of subjective intent.

## 10. India Scenario Deep Dive

The Indian-American community is the single largest population of US persons with chronic FBAR/8938 non-compliance. The standard fact pattern combines several common elements, each with distinct reporting consequences.

### 10.1 NRE and NRO accounts

- **NRE/NRO account treatment** — NRE (Non-Resident External) accounts — repatriable, denominated in INR, often interest-bearing; held at an Indian bank; NRO (Non-Resident Ordinary) accounts — rupee account for income earned in India (rent, dividends, pension); also held at an Indian bank. Treatment: Both are foreign financial accounts for FBAR purposes; Both are specified foreign financial assets for Form 8938 purposes; Both generate interest income that is fully taxable in the US as worldwide income (the FATCA reporting does not change the income tax inclusion); A foreign tax credit is generally available for Indian TDS withheld on NRO interest under the US-India treaty and §901; NRE interest is exempt from Indian tax under Indian law; this means there is no foreign tax to credit, and the US tax on NRE interest must be paid out of pocket.  _(US-India tax treaty; §901)_

### 10.2 Public Provident Fund (PPF)

- **PPF treatment** — The PPF is a long-term retirement-style savings account at an Indian bank with government-set interest rates and a 15-year lock-in. It is widely treated in IRS practice as: A foreign financial account for FBAR purposes; A specified foreign financial asset for Form 8938; Not entitled to US tax deferral — the annual interest credit is currently taxable in the US. There is no US-India treaty provision deferring PPF earnings to distribution.

### 10.3 Life Insurance Corporation (LIC) policies

- **LIC policy treatment** — Many Indian-Americans hold LIC of India endowment, money-back, or unit-linked insurance plans (ULIPs) inherited from parents or purchased before US emigration. Treatment: Cash-value foreign life insurance is a foreign financial account for FBAR (the cash surrender value is the reportable amount); It is an SFFA for Form 8938; It is not a "life insurance contract" under §7702 (which has strict definitional requirements) — so the inside buildup is currently taxable in the US year by year as it accrues, not deferred to surrender; ULIPs that allocate to mutual fund sub-accounts are likely to contain PFIC exposures.  _(IRC §7702)_

### 10.4 Indian mutual funds

- **Indian mutual fund treatment** — Indian mutual funds (held directly with the fund house, e.g., HDFC AMC, ICICI Prudential, SBI Mutual Fund) are usually: Held in the holder's own name with the fund's registrar — not through an account at a financial institution; Therefore not an FBAR-reportable financial account (no account holding them); But still SFFAs for Form 8938 (foreign stock/securities not held in a financial account); Almost certainly PFICs under §1297 — triggering §1291 and Form 8621. This is the asymmetric-treatment fact pattern from §5.5 above and is one of the most expensive catch-up situations.  _(IRC §1297; IRC §1291)_

### 10.5 Employees' Provident Fund (EPF) and pension funds

- **EPF treatment** — Indian EPF contributions are a defined-contribution employer-sponsored plan with a member account. Practitioner consensus treats EPF as: An FBAR-reportable foreign financial account; An SFFA for Form 8938; Currently taxable in the US on the annual interest credit — there is no US-India tax treaty article that defers EPF buildup. This treatment is conservative. There is no published IRS guidance directly on point and there are arguments both ways. Practitioners take varying positions.

### 10.6 Indian inheritance

- **Indian inheritance reporting** — A US person who inherits Indian assets (real estate, accounts, gold, securities) from a non-US-person decedent files Form 3520 if the gift exceeds $100,000 (the threshold for gifts from non-US individuals) — separately from FBAR and 8938. Once the assets are received and titled in the US person's name, ongoing FBAR/8938 obligations begin for the inherited financial accounts. > **AUDIT FLASH POINT — Indian PFIC mutual funds.** This is the single most damaging hidden exposure in the Indian-American population. Inherited or pre-emigration mutual fund holdings often accumulate decades of §1291 deemed-distribution tax exposure. Curing the position requires Form 8621 for each year for each fund, with §1291 computations using highest-ordinary-rate-in-effect for each holding-period year. The professional fees alone often exceed the original investment.  _(Form 3520)_

## 11. Additional High-Risk Jurisdictions

### 11.1 Chinese accounts

- **Chinese accounts treatment** — US persons with bank accounts at the Bank of China, ICBC, or other Chinese banks face: Full FBAR and 8938 reporting (China is a treaty partner for tax purposes; nothing about US-China relations excuses disclosure); Currency-control concerns on the Chinese side (annual $50,000 outbound limit) — but this is a Chinese law issue, not a US reporting issue; Standard reporting; no special program.

### 11.2 Iranian accounts

- **Iranian accounts treatment** — US persons with Iranian accounts face additional risk under the Iranian Transactions and Sanctions Regulations administered by OFAC (31 CFR Part 560). US persons are generally prohibited from engaging in transactions with Iran absent a specific or general license. Holding a pre-existing account in Iran from before sanctions does not by itself violate sanctions, but using the account, accepting deposits to it, or transferring from it may. FBAR and 8938 reporting obligations apply regardless of sanctions issues — sanctions law does not excuse reporting law. Specialist coordination is essential.  _(31 CFR Part 560)_

### 11.3 Russian accounts

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

Aggregate FBAR-reportable accounts: NRE $32k + NRO $8k + PPF $14k + LIC $11k = $65k. (Mutual funds held directly with the fund house are not financial accounts for FBAR.) Above the $10k threshold — every account is reportable.

Aggregate SFFAs for Form 8938: All of the above plus the mutual funds = $87,000. Above the $50k unmarried-US-resident year-end threshold — Form 8938 required.

PFIC exposure: each of the three Indian mutual funds is a separate PFIC requiring its own Form 8621 with §1291 computation.

Catch-up path: Because Priya answered "no" to the Schedule B foreign account questions while holding foreign accounts, the willfulness analysis is sensitive. If she had no actual knowledge of the FBAR obligation and no professional advice on the question, the non-willful position is defensible. SDOP is the likely path, with three years of amended returns including the back-year interest income, six years of delinquent FBARs, and the 5% Title 31 penalty on the highest aggregate balance during the covered period.

The PFIC issue is independent of SDOP. SDOP does not eliminate §1291 tax. Form 8621 must be filed for each PFIC for each year, and the §1291 deemed-distribution tax is owed.

Estimated catch-up cost: SDOP 5% on roughly $65k highest aggregate FBAR balance = ~$3,250; back income tax on unreported interest (NRE + NRO + PPF + LIC inside buildup) over three years, perhaps $1,500–$3,000; §1291 PFIC tax on the mutual funds depending on holding period and distributions — potentially $5,000–$15,000 plus interest charge. Professional fees often $8,000–$15,000.

### Example 2 — US expat in the UK with large pension

Facts. James is a US citizen who has lived in London for 12 years. He works for a UK financial-services firm. He has:

- A Barclays current account; highest balance during 2025: £8,000 ($10,200).
- A NatWest savings account; highest balance during 2025: £12,000 ($15,300).
- An ISA (UK Individual Savings Account) at Hargreaves Lansdown holding £45,000 of UK equity funds; year-end value $57,300.
- A defined-contribution UK workplace pension with £180,000 in employer-sponsored funds; year-end value $229,200.
- A SIPP (Self-Invested Personal Pension) with £65,000 in directly held UK stocks; year-end value $82,800.

James is married filing jointly to a US spouse who has no foreign accounts. They meet the §911 bona fide residence test (married joint, abroad: $400k YE / $600k anytime threshold).

Aggregate at year-end: $10,200 + $15,300 + $57,300 + $229,200 + $82,800 = $394,800. Just below the $400k MFJ-abroad year-end threshold. Need to check the "any time during the year" max: if any of the accounts had a higher mid-year peak that brings the aggregate over $600k at any single date, Form 8938 is required. Suppose the pension was at $250k mid-year due to a market high — aggregate peak ~$415k. Below the $600k anytime threshold. No Form 8938 in 2025.

FBAR: aggregate is well above $10,000 — yes, every account reported.

PFIC exposure: every fund inside the ISA and the workplace pension is a UK-domiciled fund and a PFIC. The pension might be eligible for §402(b) / treaty-based exclusion from current PFIC inclusion (US-UK Tax Treaty, Article 18, and HMRC-recognized pension trust arguments) — but this is fact-intensive and contested. The ISA is not treaty-protected; it is fully taxable in the US year by year, the inside-buildup is currently includible, and every fund is a PFIC. ISA "tax-free" treatment is a UK-domestic rule with no US counterpart.

Catch-up needed if James has been missing this: full PFIC analysis on the ISA, possible §402(b) position on the workplace pension with disclosure, and consistent FBAR filing. SFOP available because he lives abroad and meets the 330-day test.

### Example 3 — US trustee of a foreign trust, signature-only authority

Facts. Sarah is a US citizen living in Boston. She has $4,000 in a personal Canadian RBC account (legacy from her university years in Montreal). She is also a co-trustee — without beneficial interest — of an offshore family trust in Jersey holding $2,300,000 of investments at HSBC Jersey. The trust beneficiaries are her UK-resident cousins.

Personal exposure: her own $4,000 account is below the FBAR threshold by itself.

But aggregate-with-signature-authority: as a co-trustee she has signature authority over a $2.3M foreign account. Her aggregate (financial-interest + signature-authority) crosses $10,000 — by a wide margin.

FBAR required, reporting both the personal Canadian account AND the trust account on which she has signature authority. The trust account is reported with the indicator that she has signature authority but no financial interest.

Form 8938: she has no beneficial interest in the trust. The Jersey trust account is not her SFFA. Her personal Canadian account at $4,000 is below the $50,000 unmarried-US-resident year-end threshold. No Form 8938 required.

This is the signature-authority asymmetry in action. She files FBAR every year for the $2.3M account on which she has authority but no ownership; she does not file Form 8938 for it.

There is also no immediate income tax consequence to Sarah from the trust's investment income (she has no beneficial interest). The trust's US-person beneficiaries — if any — would face their own Form 3520 obligations and potentially Form 3520-A trustee reporting. Sarah's US-person status as trustee may itself trigger Form 3520-A trustee obligations depending on how the trust is structured.

> **AUDIT FLASH POINT — co-trustee signature authority.** Sarah's filing risk is enormous relative to her personal involvement. A missed FBAR on a $2.3M account where she has signature authority exposes her personally to FBAR penalties regardless of her zero beneficial interest. Practitioners with clients serving on offshore trustee panels must specifically inquire about every trust account.

## 13. Schedule B — The Gateway Question

Schedule B (Form 1040) Part III asks two questions critical to FBAR and 8938 compliance:

> "At any time during 2025, did you have a financial interest in or signature or other authority over a financial account (such as a bank account, securities account, or brokerage account) located in a foreign country?"

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

- **Form 8938 recordkeeping requirements** — There is no separate retention period in §6038D, but the standard §6001 / Treas. Reg. §1.6001-1 recordkeeping obligation applies — generally records supporting items on a return must be kept for as long as their contents may be material to administration of the tax law (typically the statute-of-limitations period plus a margin; with §6501(c)(8) keeping the return open indefinitely when 8938 is missing, this becomes effectively indefinite for foreign-asset records).  _(§6001; Treas. Reg. §1.6001-1; §6501(c)(8))_

## 16. Coordination with Other International Information Returns

- **Form 8938 coordination with other forms** — Form 8938 explicitly coordinates with several other international forms via Part IV. Where the same asset is reported on another form, Form 8938 references the other form and skips the detail: Form 3520 — gifts from foreign persons over $100,000 or distributions from foreign trusts; Form 3520-A — annual return for foreign grantor trust with US owner; Form 5471 — US persons with interests in foreign corporations (10% or greater); Form 8621 — PFIC reporting; Form 8865 — US persons with interests in foreign partnerships (10% or greater); Form 8858 — foreign disregarded entities and foreign branches. The coordination is one-way: Form 8938 defers to these forms. Filing one of them does not satisfy FBAR. FBAR remains an independent obligation with its own form, due date, platform, and penalty regime.

## 17. Reviewer Self-Checks

Before signing off on any return implicating these forms, the reviewer should verify:

- **Schedule B Part III consistency** — Schedule B Part III has been answered consistently with FBAR/8938 filings and prior-year answers.
- **FBAR aggregate threshold computation** — FBAR aggregate threshold has been computed correctly (highest aggregate at any point during the calendar year, in USD at Treasury year-end rate).
- **Form 8938 thresholds applied correctly** — Form 8938 thresholds have been applied with the correct filing-status and residence tier.
- **All accounts reported on both forms where applicable** — All accounts are reported on both forms where applicable — same accounts on both forms in 99% of overlapping cases.
- **Signature-authority accounts reported on FBAR** — Signature-authority accounts are reported on FBAR even when not on 8938.
- **PFIC trigger consideration** — PFIC trigger has been considered for every foreign fund, ETF, or pooled investment.
- **Form 8621 filed for PFIC interests meeting threshold** — Form 8621 has been filed for every PFIC interest where the §1298(f) threshold is met.  _(§1298(f))_
- **Cross-references in Form 8938 Part IV** — Cross-references in Form 8938 Part IV correctly identify any 3520/5471/8621/8865/8858/3520-A filings.
- **Currency translation rate** — Currency translation uses the Treasury Reporting Rate of Exchange for the appropriate date.
- **Reasonable-cause documentation for late filings** — Reasonable-cause documentation is in the file if any late filings are involved.

A missed FBAR or 8938 is a reviewer responsibility under Circular 230. The advisor's name on a return with willfully or recklessly omitted disclosure exposes the advisor to §6694 preparer penalties and §10.51 Circular 230 discipline.

## 18. Quick Reference — Citations

- **31 USC §5314** — BSA authority for foreign account reports  _(31 USC §5314)_
- **31 CFR §1010.350** — FBAR filing requirement, definitions, exceptions  _(31 CFR §1010.350)_
- **31 CFR §1010.420** — FBAR recordkeeping  _(31 CFR §1010.420)_
- **31 USC §5321(a)(5)** — FBAR civil penalties  _(31 USC §5321(a)(5))_
- **31 USC §5322** — FBAR criminal penalties  _(31 USC §5322)_
- **IRC §6038D** — FATCA Form 8938 reporting  _(IRC §6038D)_
- **Treas. Reg. §1.6038D-1 through -8** — FATCA implementing regulations  _(Treas. Reg. §1.6038D-1 through -8)_
- **IRC §6662(j)** — 40% accuracy penalty on undisclosed foreign asset income  _(IRC §6662(j))_
- **IRC §6501(c)(8) and §6501(e)(1)(A)(ii)** — extended statute of limitations  _(IRC §6501(c)(8) and §6501(e)(1)(A)(ii))_
- **IRC §1291** — PFIC excess distribution regime  _(IRC §1291)_
- **IRC §1297** — PFIC definition  _(IRC §1297)_
- **IRC §1298(f)** — Form 8621 filing requirement  _(IRC §1298(f))_
- **Bittner v. United States, 598 U.S. 85 (2023)** — non-willful FBAR penalty per form, not per account  _(Bittner v. United States, 598 U.S. 85 (2023))_
- **United States v. Williams, 489 F. App'x 655 (4th Cir. 2012)** — willful FBAR willfulness standard  _(United States v. Williams, 489 F. App'x 655 (4th Cir. 2012))_
- **IRS Memorandum LB&I-09-1118-014 (Nov. 20, 2018)** — Updated Voluntary Disclosure Practice  _(IRS Memorandum LB&I-09-1118-014 (Nov. 20, 2018))_
- **IRM 4.26.16** — FBAR examination procedures  _(IRM 4.26.16)_
- **IRM 4.26.17** — FBAR penalty mitigation  _(IRM 4.26.17)_

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

## Talk to a verified accountant

This skill is a tool, not an engagement. Every taxpayer's situation is
different, and the rules in the skill may not match your specific facts.

To speak with one of the licensed accountants who verifies skills for your
jurisdiction — **no liability on either side until you and the accountant sign
a formal engagement letter** — book a free 30-minute call:

**→ [Book a call](https://calendly.com/openaccountants-info/30min)**

We'll route you to the named verifier covering your country or state. You can
also see the full list of verified accountants at
[openaccountants.com/network](https://openaccountants.com/network).
