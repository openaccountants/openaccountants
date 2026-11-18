---
name: lv-company-formation
description: "Setting up a business in Latvia for tax year 2026, from the Commercial Law (Komerclikums), Cabinet Regulation No. 664 on registration fees, the Enterprise Register (Uzņēmumu reģistrs) service pages, the Micro-enterprise Tax Law and the tax laws the pack already uses. Covers the legal forms (limited liability company SIA, small-capital SIA, joint stock company AS, individual merchant IK, general and limited partnerships, branch of a foreign merchant), share capital (SIA EUR 2,800, small-capital SIA below that with a 25% reserve, AS EUR 25,000), paying in the capital, the registration steps, fees from EUR 20 to EUR 85, the 1 to 3 working day review, electronic-only filing from 7 January 2027, and the first tax and filing duties. Use for 'set up a company in Latvia', 'SIA share capital', 'Latvian company registration fee'. Out of scope: company tax detail (lv-corporate-income-tax), VAT returns (latvia-vat-return), payroll (latvia-payroll), cross-border (lv-cross-border)."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/lv-company-formation"
  jurisdiction: "LV"
  tax_year: "2026"
  last_updated: "2026-11-17"
---

# Latvia Company Formation & Entity Choice

This skill covers choosing a legal form in Latvia, registering it in 2026, and the first tax and filing duties that follow. Figures come from the Commercial Law (Komerclikums, KL), Cabinet Regulation No. 664 of 11 October 2016 on the state fee for commercial register entries, the Enterprise Register (UR) service pages, the Micro-enterprise Tax Law and the tax laws, with the specified passages read from preserved official captures on 17 November 2026. likumi.lv states that its consolidated texts are informative and that the official publication prevails in a conflict. The tax computations sit in the pack's domain skills; where a domain skill and this skill ever differ, the domain skill wins.

## Scope

- **Who this is for:** a person or business setting up in Latvia in 2026: an individual merchant (IK), a general or limited partnership, a limited liability company (SIA), a small-capital SIA, a joint stock company (AS), or the branch of a foreign merchant.
- **What it covers:** the choice of form, share capital, paying in the capital, the registration steps at UR, fees and timing, and the first tax and filing duties.
- **Not covered here:** company tax computations (lv-corporate-income-tax), VAT returns (latvia-vat-return), payroll and social contributions (latvia-payroll, latvia-social-contributions), non-resident owners and treaties (lv-cross-border), related-party pricing (lv-transfer-pricing), and a self-employed person's income tax (latvia-income-tax).

## Ask the client first

- Which form: one person trading alone (IK or registered self-employed), partners with unlimited liability (PS, KS), or a capital company (SIA, small-capital SIA, AS)?
- How many founders, are they all natural persons, and will every board member be a member? (This decides whether a small-capital SIA is allowed.)
- How much capital, in money or in kind, and is any in-kind contribution above EUR 25,000 or at least half the capital?
- Is review within one working day wanted, and is there a single founder? (This changes the fee.)
- Expected annual turnover and domestic supplies (IK registration duty, VAT threshold, micro-enterprise tax)?
- Will the owners take dividends soon, or keep profit in the company? (Company tax is due only on distributions.)

## The method, step by step

### Key figures

| Item | Figure | Condition | Source |
|---|---|---|---|
| IK registration duty, turnover | Over EUR 284,600 a year | Or a commercial agent or broker; or turnover over EUR 28,500 with more than five employees at once (KL art. 75(1)); anyone else may register voluntarily (art. 75(2)) | [Komerclikums art. 75](https://likumi.lv/ta/id/5490-komerclikums) |
| SIA minimum share capital | EUR 2,800 | KL art. 185; each share's nominal value at least one cent (art. 186(1)) | [Komerclikums arts. 185, 186](https://likumi.lv/ta/id/5490-komerclikums) ; [UR, SIA](https://apraksti.ur.gov.lv/lv/registre/uznemumu-vai-komersantu/sia) |
| Small-capital SIA mandatory reserve | At least 25% of each year's profit | Capital below EUR 2,800 only if founders and members are natural persons, five at most, every board member is a member and each member is in only one such company (KL art. 185.1(1), (2)) | [Komerclikums art. 185.1](https://likumi.lv/ta/id/5490-komerclikums) |
| AS minimum share capital | EUR 25,000 | KL art. 225(1) | [Komerclikums art. 225](https://likumi.lv/ta/id/5490-komerclikums) |
| Bank statement for cash capital | Needed only when cash contributions exceed EUR 50,000 | Otherwise the founders confirm on form KR4 that the account is open and the capital paid (KL art. 149(3)(2), (4); UR SIA registration page) | [Komerclikums art. 149](https://likumi.lv/ta/id/5490-komerclikums) ; [UR, SIA registration](https://apraksti.ur.gov.lv/lv/registre/dibinasana/registracija-uznemumu-registra-0) |
| In-kind contributions valued by the founders | Total at most EUR 25,000 and less than half the capital | Ordinary SIA founding exception only; the separate securities/token exceptions remain in KL art. 154(2.1), (2.2); otherwise a qualified listed valuer gives the opinion (art. 154(1), (2)) | [Komerclikums art. 154](https://likumi.lv/ta/id/5490-komerclikums) |
| State fee: SIA or partnership | EUR 75 | Cabinet Regulation No. 664, annex part II, item 1.2 | [Cabinet Regulation No. 664](https://likumi.lv/ta/id/285320) |
| State fee: small-capital SIA | EUR 20 | Same annex, item 1.4 | [Cabinet Regulation No. 664](https://likumi.lv/ta/id/285320) |
| State fee: AS | EUR 85 | Same annex, item 1.3 | [Cabinet Regulation No. 664](https://likumi.lv/ta/id/285320) |
| State fee: IK | EUR 30 | Same annex, item 1.1 | [Cabinet Regulation No. 664](https://likumi.lv/ta/id/285320) |
| State fee: foreign merchant's branch | EUR 30 | Same annex, item 2 | [Cabinet Regulation No. 664](https://likumi.lv/ta/id/285320) |
| VAT registration threshold | EUR 50,000 of domestic supplies in a calendar year | Ordinary threshold only, subject to the value rules and exceptions in VAT Law art. 59(2), (3), (8)-(12); see Step 6 | [VAT Law art. 59](https://likumi.lv/ta/id/253451-pievienotas-vertibas-nodokla-likums) |
| Corporate income tax | 20% of distributed profit divided by 0.8; or 15% divided by 0.85 on dividends of a company owned only by individuals, plus 6% PIT on the dividend | CIT Law arts. 3(1), 3(5), 4(9), 4.2(1), (2); PIT Law s. 15(5.1). Detail: lv-corporate-income-tax | [CIT Law arts. 3, 4, 4.2](https://likumi.lv/ta/id/292700-uznemumu-ienakuma-nodokla-likums) |
| Micro-enterprise tax | 25% of turnover | Micro-enterprise Tax Law art. 6; not for an SIA (art. 1(3)) | [Micro-enterprise Tax Law](https://likumi.lv/ta/id/215302-mikrouznemumu-nodokla-likums) |

### Step 1. Choose the form

- **Common entity types**: a merchant is either a natural person entered in the commercial register (individual merchant, individuālais komersants, IK) or a commercial company. Commercial companies are partnerships (general partnership, pilnsabiedrība, PS; limited partnership, komandītsabiedrība, KS) and capital companies (limited liability company, sabiedrība ar ierobežotu atbildību, SIA; joint stock company, akciju sabiedrība, AS). An SIA is a closed company whose shares are not publicly traded; an AS is an open company whose shares can be. A foreign merchant can open a branch (filiāle), entered in the commercial register on the merchant's application. _(KL arts. 1(1), 22, 25(2), 77(1), 118(1), 134(1)-(4))_
- **Individual merchant (IK)**: a natural person in business must register as an IK if annual turnover from the business exceeds EUR 284,600, or the business is that of a commercial agent or broker, or turnover exceeds EUR 28,500 and more than five employees work in the business at the same time. Anyone else may register voluntarily. _(KL art. 75(1)-(2))_
- **Partnerships**: in a PS, two or more partners trade under a common firm name without limiting their liability to the partnership's creditors. A KS is the same, except that at least one partner (komandīts) is liable only up to their contribution. _(KL arts. 77(1), 118(1))_
- **SIA minimum share capital (standard)**: EUR 2,800. Each share's nominal value must be at least one cent. Founders can be natural or legal persons, and capital can be paid in money or in kind. _(KL arts. 185, 186(1); UR, SIA)_
- **Small-capital SIA (mazkapitāla SIA)**: share capital may be below EUR 2,800 only if all of these hold: the founders are natural persons, five at most; the members are natural persons, five at most; every board member is a member; each member is a member of only one such company. The company must put at least 25% of each year's profit into a mandatory reserve, and may pay dividends only from what is left. If one of the member, board or one-company conditions stops being met, the capital must be raised to EUR 2,800 within three months. In insolvency, members are jointly liable up to the gap between EUR 2,800 and the capital the founders paid. The law sets no separate lower figure; the one-cent minimum per share applies. _(KL arts. 185.1(1)-(7), 186(1); UR, small-capital SIA)_
- **AS minimum share capital**: EUR 25,000. _(KL art. 225(1))_

### Step 2. Check the name and prepare the documents

The UR steps for an SIA, in order: check the name; founding decision (one founder) or founding agreement; articles of association; share capital; members' register section; beneficial owners; legal address (the board's confirmation of reachability and a legal right to use the address, with its cadastral designation); registration form KR4; signatures (secure e-signature to file online, or notarised to file on paper); submit and pay the fee; register with VID for VAT if needed. Documents are prepared in Latvian. A single natural-person founder can use the online service with system-generated documents. Each board member's consent to take office is filed unless it is in the form. _(UR, SIA registration)_

### Step 3. Pay in the capital

Founders subscribe and pay the whole share capital in the founding agreement before the registration application is filed, unless the agreement sets an earlier date. For an AS and a small-capital SIA the capital paid before filing must be paid only in money. Founders open a payment account in the name of the company being founded and pay the money into it. A payment service provider's statement is needed only when cash contributions exceed EUR 50,000; below that, the founders confirm on form KR4 that the account is open and the capital paid. Contributions in kind need a valuation opinion from a listed valuer; founders can give it themselves if in-kind contributions are at most EUR 25,000 in total and less than half the capital, and then all founders sign it. _(KL arts. 146(1)-(2), 147(1), 149(3)-(4), 154(1)-(2); UR, SIA registration)_

### Step 4. File with the Enterprise Register and pay the fee

- **Registration authority**: the Enterprise Register of the Republic of Latvia (Uzņēmumu reģistrs), which keeps the commercial register. _(KL art. 6; UR)_
- **Fees in 2026**: SIA from EUR 75; small-capital SIA from EUR 20; AS from EUR 85; IK EUR 30; foreign merchant's branch from EUR 30. These are the state fees in Cabinet Regulation No. 664 (annex, part II, items 1-2), set under KL art. 15(1). The fee is paid before the application is filed, through a payment service provider or the UR online form (Regulation 664 para. 5). _(KL art. 15(1); Cabinet Regulation No. 664; UR registration pages)_
- **One-day review**: the fee is three times the amount for a partnership, an SIA, a small-capital SIA or a foreign merchant's branch (annex note 1); for an individual merchant or a capital company with one founder, one-day review costs the listed amount (annex note 4). Review starts only after all documents are in and the fee is paid. _(Cabinet Regulation No. 664, annex part II, notes 1 and 4; UR registration pages)_
- **Typical timeline**: UR reviews an SIA, small-capital SIA, AS, IK or foreign branch application in 1 to 3 working days, not counting the day of submission. The statutory term can be extended under Administrative Procedure Law art. 64(2). _(UR registration pages)_
- **If UR refuses or postpones**: the fee is not refunded, and is paid again if corrected documents come in after the deadline the state notary set. _(Cabinet Regulation No. 664, para. 8)_
- **Electronic filing from 2027**: UR announces that from 7 January 2027 applications to UR must be filed electronically through registrs.ur.gov.lv, subject to the transitional exceptions in the announcement (amendments to the law "On the Enterprise Register of the Republic of Latvia" approved by the Saeima on 15 October 2026). Documents drawn up before a notary will be sent to UR electronically by the notary. Applications to end activity, liquidate or be removed from the register can still go on paper by post until 30 June 2030. _(UR news, 15.10.2026)_

### Step 5. Choose the tax regime at registration

- **Micro-enterprise tax regime**: 25% of turnover. Only an individual merchant (IK), an individual enterprise, a farm or fishing household, or a natural person registered with VID as carrying on business can become a micro-enterprise, so an SIA cannot choose it. The expected turnover must not exceed the VAT registration threshold, and the business must not plan to register for VAT before reaching it (except under the special VAT scheme of VAT Law art. 139.2). Status can be requested together with the UR registration application, or with VID registration as a self-employed person; an existing business applies by 15 December for the next year. _(Micro-enterprise Tax Law arts. 1(3), 4(1), (3), (4), 6; VID, micro-enterprise tax)_
- **SIA micro-enterprise status ended**: an SIA that was a micro-enterprise taxpayer lost that status on 1 January 2022 and became a corporate income tax payer. CIT Law arts. 2(4) and 4(11) still mention such an SIA, but the Micro-enterprise Tax Law no longer admits one. _(Micro-enterprise Tax Law transitional provision 36, art. 1(3); CIT Law art. 4(11))_
- **Corporate income tax once formed**: ordinary distribution tax arises when a company distributes profit or makes deemed distributions: 20% of the taxable amount divided by 0.8. From 2026 a company whose members are only natural persons can apply 15% with a 0.85 divisor to dividends, with 6% personal income tax on the dividend under PIT Law s. 15(5.1), rather than the ordinary dividend exemption (s. 9(3.9)). _(CIT Law arts. 3(1), 3(5), 4(9), 4.2(1)-(2))_ The ordinary SIA annual minimum is EUR 50: if annual CIT is below that amount, the last-period return tops it up. It does not apply in the registration year, the year liquidation finishes, an insolvency case, or a year with at least EUR 100 of PIT or social contributions paid for an employee (CIT Law art. 17(11), (12)). Detail: lv-corporate-income-tax.

### Step 6. Register for VAT if needed

The ordinary domestic VAT registration threshold is EUR 50,000, computed under art. 59(1)-(3). It is not an unconditional exemption: prior-year excess and cross-border services can require registration below that figure, and special exempt-supply/person rules apply (art. 59(8)-(12)). Voluntary registration is possible. An excess of no more than EUR 5,000 permits year-end registration, but the application is due by 30 November or, for a later excess, 31 December (art. 59(4), (6), (7)); beyond the tolerance, apply by the 15th of the following month (art. 59(5)). VAT returns are due 20 days after the end of the period and the tax 23 days after. _(VAT Law arts. 59, 118(1), 119(1))_ Detail: latvia-vat-return.

## Boundary and exception table

| Situation | Rule | Source |
|---|---|---|
| Small-capital SIA gains a sixth member, a non-member board member, or a member who joins a second such company | Capital must reach EUR 2,800 within three months | KL art. 185.1(6)  [Official source](https://likumi.lv/ta/id/5490-komerclikums) |
| Small-capital SIA insolvent | Members jointly liable up to EUR 2,800 minus the capital the founders paid | KL art. 185.1(7)  [Official source](https://likumi.lv/ta/id/5490-komerclikums) |
| AS or small-capital SIA wants to pay capital in kind before filing | Not allowed: the capital paid before filing must be money | KL art. 146(2)  [Official source](https://likumi.lv/ta/id/5490-komerclikums) |
| Cash capital over EUR 50,000 | Payment service provider statement attached; KR4 confirmation is not enough | KL art. 149(3)(2), (4)  [Official source](https://likumi.lv/ta/id/5490-komerclikums) |
| Natural person below the compulsory IK turnover/employee thresholds, whose activity is neither commercial agency nor brokerage and who has no other KL art. 75(1) trigger | May trade as a registered self-employed person without becoming an IK; voluntary IK registration remains available | KL art. 75(1)-(2)  [Official source](https://likumi.lv/ta/id/5490-komerclikums) |
| SIA wants micro-enterprise tax | Not possible: only an IK, individual enterprise, farm or fishing household or registered individual | Micro-enterprise Tax Law art. 1(3)  [Official source](https://likumi.lv/ta/id/215302-mikrouznemumu-nodokla-likums) |

## Worked cases

### 1. SIA or small-capital SIA for two founders with EUR 1,000 (a decision)

Two individuals want a company quickly and have EUR 1,000 in cash. Both will sit on the board. They expect a first-year profit after tax of EUR 8,000.

- **Standard SIA:** needs EUR 2,800 of capital, so EUR 1,800 more than they have. Fee EUR 75; with one-day review, three times that: EUR 225.
- **Small-capital SIA:** EUR 1,000 is enough, paid in money. Fee EUR 20; one-day review EUR 60. At least 25% of the profit (EUR 2,000) goes to the mandatory reserve, so at most EUR 6,000 can be paid as dividends.
- **Decision:** if the founders cannot raise EUR 2,800, or will keep profit in the company anyway, the small-capital SIA works; if they want to pay out the whole EUR 8,000, or a sixth member, a corporate member or a non-member director is planned, the standard SIA avoids the reserve and the three-month top-up rule.

```oa-check
name: Two founders, EUR 1,000 cash, standard vs small-capital SIA, 2026
inputs:
  cash: 1000
  sia_min_capital: 2800
  sia_fee: 75
  small_fee: 20
  profit: 8000
steps:
  - sia_capital_gap: sia_min_capital - cash
  - sia_fee_one_day: sia_fee * 3
  - small_fee_one_day: small_fee * 3
  - small_reserve: profit * 0.25
  - small_max_dividend: profit - small_reserve
  - sia_max_dividend: profit
  - dividend_difference: sia_max_dividend - small_max_dividend
expected:
  sia_capital_gap: 1800
  sia_fee_one_day: 225
  small_fee_one_day: 60
  small_reserve: 2000
  small_max_dividend: 6000
  sia_max_dividend: 8000
  dividend_difference: 2000
```

### 2. Small-capital SIA that loses its conditions

A small-capital SIA with EUR 300 of paid capital appoints a board member who is not a member. It must raise its capital to EUR 2,800 within three months, a top-up of EUR 2,500. If it became insolvent first, the members would be jointly liable for the company's debts up to EUR 2,500.

```oa-check
name: Small-capital SIA, EUR 300 capital, top-up and liability cap
inputs:
  paid_capital: 300
  sia_min_capital: 2800
steps:
  - top_up: sia_min_capital - paid_capital
  - liability_cap: sia_min_capital - paid_capital
expected:
  top_up: 2500
  liability_cap: 2500
```

## When to refuse or refer

- Foreign founders without a Latvian personal code, national security restrictions, licensed activities (banking, insurance, gambling) or a cross-border merger: refer to a Latvian lawyer or notary.
- Questions about beneficial owner declarations beyond the UR step list: refer to UR guidance.
- Tax computations: route to lv-corporate-income-tax, latvia-income-tax, latvia-vat-return or latvia-payroll.

## Filing and payment

- **Core annual compliance**: a company files its annual report with VID within one month of approval and no later than five months after the year end for a micro or small company, seven months for a medium or large company or a parent preparing consolidated accounts. Corporate income tax returns are due by the 20th of the month after the taxation period and the tax by the 23rd. The period is the calendar month, or the quarter for a payer entitled under Accounting Law art. 13 to book documents quarterly; a month with no taxable base needs no return, except the last month of the reporting year. Employer payroll and social insurance reports: latvia-payroll. _(Annual Reports Law art. 97(1); CIT Law arts. 3(2)-(3), 17(1), (3), (7))_
- **Micro-enterprise tax returns**: quarterly, by the 15th of the month after a quarter with turnover; tax by the 23rd. _(Micro-enterprise Tax Law art. 7(2), (3))_

## Which skill next

- Company tax on distributions and deemed distributions: lv-corporate-income-tax
- VAT registration and returns: latvia-vat-return
- Salaries and social insurance: latvia-payroll, latvia-social-contributions
- Non-resident owners and treaties: lv-cross-border; related-party pricing: lv-transfer-pricing
- Individual merchant and self-employed income tax: latvia-income-tax
- Whole-system map: lv-tax-overview

## Sources

| Source | URL | Read on |
|---|---|---|
| Komerclikums (Commercial Law), consolidated, arts. 1, 6, 15, 22, 25, 75, 77, 118, 134, 146, 147, 149, 154, 185, 185.1, 186 and 225 read | https://likumi.lv/ta/id/5490-komerclikums | 2026-11-17 |
| Cabinet Regulation No. 664 of 11.10.2016 on the state fee for entries in the commercial register (in force, last amended by Regulation No. 583 of 24.08.2021), paras. 1 to 10 and annex part II with notes read | https://likumi.lv/ta/id/285320 | 2026-11-17 |
| Uzņēmumu reģistrs, SIA description page (minimum capital, founders, capital form read) | https://apraksti.ur.gov.lv/lv/registre/uznemumu-vai-komersantu/sia | 2026-11-17 |
| Uzņēmumu reģistrs, SIA registration page (steps, documents, 1 to 3 working days, fee from EUR 75 read for registration) | https://apraksti.ur.gov.lv/lv/registre/dibinasana/registracija-uznemumu-registra-0 | 2026-11-17 |
| Uzņēmumu reģistrs, small-capital SIA registration page (fee from EUR 20, review time read for registration) | https://apraksti.ur.gov.lv/lv/registre/dibinasana/registracija-uznemumu-registra-4 | 2026-11-17 |
| Uzņēmumu reģistrs, AS registration page (fee from EUR 85, review time read for registration) | https://apraksti.ur.gov.lv/lv/registre/dibinasana/registracija-uznemumu-registra-5 | 2026-11-17 |
| Uzņēmumu reģistrs, IK registration page (fee EUR 30, review time read for registration) | https://apraksti.ur.gov.lv/lv/registre/dibinasana/registracija-uznemumu-registra | 2026-11-17 |
| Uzņēmumu reģistrs, foreign merchant's branch registration page (fee from EUR 30, review time read for registration) | https://apraksti.ur.gov.lv/lv/registre/dibinasana/registracija-uznemumu-registra-2 | 2026-11-17 |
| Uzņēmumu reģistrs, small-capital SIA description (read for natural-person/member conditions) | https://apraksti.ur.gov.lv/lv/registre/uznemumu-vai-komersantu/mazkapitala-sia | 2026-11-17 |
| Uzņēmumu reģistrs, register company, organisation, contract, commercial pledge (English service page read) | https://www.ur.gov.lv/en/services/register-company-organisation-contract-commercial-pledge | 2026-11-17 |
| Uzņēmumu reģistrs, news of 15.10.2026: applications electronic from 2027 (full news text read) | https://www.ur.gov.lv/lv/jaunums/no-2027-gada-pieteikumi-uznemumu-registra-bus-jaiesniedz-elektroniski | 2026-11-17 |
| Mikrouzņēmumu nodokļa likums (Micro-enterprise Tax Law), consolidated, arts. 1, 2, 2.1, 4, 5, 6, 7 and transitional provisions 36, 45, 46 read | https://likumi.lv/ta/id/215302-mikrouznemumu-nodokla-likums | 2026-11-17 |
| Pievienotās vērtības nodokļa likums (VAT Law), consolidated, art. 59 and arts. 118(1), 119(1) read | https://likumi.lv/ta/id/253451-pievienotas-vertibas-nodokla-likums | 2026-11-17 |
| Uzņēmumu ienākuma nodokļa likums (CIT Law), consolidated, arts. 2, 3, 4, 4.2 and 17 read | https://likumi.lv/ta/id/292700-uznemumu-ienakuma-nodokla-likums | 2026-11-17 |
| Gada pārskatu un konsolidēto gada pārskatu likums (Annual Reports Law), consolidated, art. 97 read | https://likumi.lv/ta/id/277779-gada-parskatu-un-konsolideto-gada-parskatu-likums | 2026-11-17 |
| Grāmatvedības likums (Accounting Law), consolidated, art. 13 read | https://likumi.lv/ta/id/324249-gramatvedibas-likums | 2026-11-17 |
| VID, micro-enterprise tax (page updated 13.05.2026, body read for the subjects used above) | https://www.vid.gov.lv/lv/mikrouznemumu-nodoklis | 2026-11-17 |
| VID, micro-enterprise tax rate (page updated 22.05.2025, body read for the subjects used above) | https://www.vid.gov.lv/lv/mikrouznemumu-nodokla-likme | 2026-11-17 |
| Law On Personal Income Tax, s. 9(3.9), 15(5.1) read for the 15% dividend option | https://likumi.lv/ta/id/56880-par-iedzivotaju-ienakuma-nodokli | 2026-11-17 |

The specified source passages were read on 2026-11-17 from the preserved official-page captures made that day; the read date covers those passages, not every section of each law. The previous version (2026-10-30) read the Commercial Law, Regulation No. 664 and the tax laws from Internet Archive copies because likumi.lv did not respond that day, and relied on VID's information material for the micro-enterprise rules; the live consolidated texts and the Micro-enterprise Tax Law itself now replace them.

Not yet confirmed: whether an official publication fee is charged on top of the state fee (the UR pages read show the state fee only); the Micro-enterprise Tax Law changes starting on 1 April 2027 (new art. 7.2 and art. 1(1); transitional provision 46), whose 2027 wording was not read.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-17. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `lv-company-formation` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/lv-company-formation. If neither is available, confirm every figure against the official source pages cited above before relying on it.
