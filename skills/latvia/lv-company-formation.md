---
name: lv-company-formation
description: "Setting up a business in Latvia for tax year 2026, from the Commercial Law (Komerclikums) in force from 1 January 2026, the Enterprise Register (Uzņēmumu reģistrs) service pages, and the tax laws and State Revenue Service (VID) pages the pack already uses. Covers the legal forms (limited liability company SIA, small-capital SIA, joint stock company AS, individual merchant IK, general and limited partnerships, branch of a foreign merchant), share capital (SIA EUR 2,800, small-capital SIA below that with a 25% reserve, AS EUR 25,000), paying in the capital, the registration steps, fees from EUR 20 to EUR 85, the 1 to 3 working day review, electronic-only filing from 7 January 2027, and the first tax and filing duties. Use for 'set up a company in Latvia', 'SIA share capital', 'Latvian company registration fee'. Out of scope: company tax detail (lv-corporate-income-tax), VAT returns (latvia-vat-return), payroll (latvia-payroll), cross-border (lv-cross-border)."
jurisdiction: LV
category: international
tax_year: 2026
last_updated: 2026-10-30
version: 0.2
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Latvia Company Formation & Entity Choice

This skill covers choosing a legal form in Latvia, registering it in 2026, and the first tax and filing duties that follow. Figures come from the Commercial Law (Komerclikums, KL) in its version in force from 1 January 2026, from the Enterprise Register (UR) service pages and from the tax laws, read on 30 October 2026. likumi.lv did not respond on 30 October 2026, so the Commercial Law was read from the Internet Archive copy of likumi.lv dated 2 August 2026, which shows the version in force from 1 January 2026 as the current one. The tax computations sit in the pack's domain skills; where a domain skill and this skill ever differ, the domain skill wins.

## Entity types and incorporation

- **Common entity types**: a merchant is either a natural person entered in the commercial register (individual merchant, individuālais komersants, IK) or a commercial company. Commercial companies are partnerships (general partnership, pilnsabiedrība, PS; limited partnership, komandītsabiedrība, KS) and capital companies (limited liability company, sabiedrība ar ierobežotu atbildību, SIA; joint stock company, akciju sabiedrība, AS). An SIA is a closed company whose shares are not publicly traded; an AS is an open company whose shares can be. A foreign merchant can open a branch (filiāle), entered in the commercial register on the merchant's application. _(KL arts. 1(1), 22, 25(2), 77(1), 118(1), 134(1)-(4))_
- **Individual merchant (IK)**: a natural person in business must register as an IK if annual turnover from the business exceeds EUR 284,600, or the business is that of a commercial agent or broker, or turnover exceeds EUR 28,500 and more than five employees work in the business at the same time. Anyone else may register voluntarily. _(KL art. 75(1)-(2))_
- **Partnerships**: in a PS, two or more partners trade under a common firm name without limiting their liability to the partnership's creditors. A KS is the same, except that at least one partner (komandīts) is liable only up to their contribution. _(KL arts. 77(1), 118(1))_
- **SIA minimum share capital (standard)**: EUR 2,800. Each share's nominal value must be at least one cent. _(KL arts. 185, 186(1); UR, SIA)_
- **Small-capital SIA (mazkapitāla SIA)**: share capital may be below EUR 2,800 only if all of these hold: the founders are natural persons, five at most; the members are natural persons, five at most; every board member is a member; each member is a member of only one such company. The company must put at least 25% of each year's profit into a mandatory reserve, and may pay dividends only from what is left. If one of the member, board or one-company conditions stops being met, the capital must be raised to EUR 2,800 within three months. In insolvency, members are jointly liable up to the gap between EUR 2,800 and the capital the founders paid. The law sets no separate lower figure; the one-cent minimum per share applies. _(KL arts. 185.1(1)-(7), 186(1); UR, small-capital SIA)_
- **AS minimum share capital**: EUR 25,000. _(KL art. 225(1))_
- **Paying in the capital**: founders subscribe and pay the whole share capital in the founding agreement before the registration application is filed. For an AS and a small-capital SIA the capital paid before filing must be paid only in money. Founders open a payment account in the name of the company being founded and pay the money into it. A bank (payment service provider) statement is needed only when cash contributions exceed EUR 50,000; below that, the founders confirm on form KR4 that the account is open and the capital paid. Contributions in kind need a valuation opinion; founders can give it themselves if in-kind contributions are at most EUR 25,000 in total and less than half the capital. _(KL arts. 146(1)-(2), 147(1), 154(2); UR, SIA registration)_
- **Registration authority**: the Enterprise Register of the Republic of Latvia (Uzņēmumu reģistrs), which keeps the commercial register. _(KL art. 6; UR)_
- **Core incorporation steps (UR)**: check the name; founding decision or founding agreement; articles of association; share capital; members' register section; beneficial owners; legal address (with the owner's consent and the cadastral designation); registration form KR4; signatures (secure e-signature to file online, or notarised to file on paper); submit and pay the fee online; register with VID for VAT if needed. Documents are prepared in Latvian. A single natural-person founder can use the online service with system-generated documents. You can apply for VAT payer or micro-enterprise tax status at the same time as registration. _(UR, SIA registration; UR, register a company)_
- **Typical incorporation timeline**: UR reviews an SIA, small-capital SIA, AS, IK or foreign branch application in 1 to 3 working days, not counting the day of submission. The statutory term can be extended under Administrative Procedure Law art. 64(2). _(UR registration pages)_
- **Registration costs in 2026 (UR)**: SIA from EUR 75; small-capital SIA from EUR 20; AS from EUR 85; IK EUR 30; foreign merchant's branch from EUR 30. These are the state fees in Cabinet Regulation No. 664 of 11 October 2016 (annex, part II, items 1-2), set under KL art. 15(1). For review within one working day the fee is three times the amount for a partnership, an SIA, a small-capital SIA or a foreign merchant's branch; for an individual merchant or a capital company with one founder, one-day review costs the listed amount. Review starts only after all documents are in and the fee is paid. _(KL art. 15(1); Cabinet Regulation No. 664, annex part II, notes 1 and 4; UR registration pages)_
- **Electronic filing from 2027**: from 7 January 2027 applications to UR must be filed electronically through registrs.ur.gov.lv (amendments to the law "On the Enterprise Register of the Republic of Latvia" approved by the Saeima on 15 October 2026). Documents drawn up before a notary will be sent to UR electronically by the notary. Applications to end activity, liquidate or be removed from the register can still go on paper by post until 30 June 2030. _(UR news, 15.10.2026)_
- **VAT registration on or after formation**: a domestic business has the right not to register for VAT only while its domestic supplies in the calendar year, without VAT, stay within the EUR 50,000 registration threshold. It can also register before reaching that amount. VAT returns are due 20 days after the end of the period and the tax 23 days after. _(VAT Law arts. 57(3), 59(1), 118(1), 119(1))_ Detail: latvia-vat-return.
- **Core annual compliance**: a company files its annual report with VID within one month of approval and no later than five months after the year end for a micro or small company, seven months for a medium or large company or a parent preparing consolidated accounts. Corporate income tax returns are due by the 20th of the month after the taxation period and the tax by the 23rd. The period is the calendar month, or the quarter for a company entitled under the Accounting Law to book documents quarterly; a month with no taxable base needs no return, except the last month of the reporting year. Employer payroll and social insurance reports: latvia-payroll. _(Annual Reports Law art. 97(1); CIT Law arts. 3(2)-(3), 17(1), (3), (7))_
- **Corporate income tax once formed**: a company pays tax only when it distributes profit (or makes deemed distributions): 20% of the taxable amount divided by 0.8. From 2026 a company whose members are only natural persons can apply 15% with a 0.85 divisor to dividends. _(CIT Law arts. 3(1), 3(5), 4(9), 4.2(1)-(2))_ Detail: lv-corporate-income-tax.
- **Micro-enterprise tax regime**: 25% of turnover. Only an individual merchant (IK), an individual enterprise, a farm or fishing holding, or a natural person registered with VID as carrying on business can become a micro-enterprise, so an SIA cannot choose it. The expected turnover must not exceed the VAT registration threshold, and the business must not plan to register for VAT before reaching it. _(VID, micro-enterprise tax; VID, micro-enterprise tax rate; VID information material "Mikrouzņēmumu nodoklis", updated 06.05.2026)_

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
| Komerclikums (Commercial Law), version in force from 01.01.2026, arts. 1, 6, 15, 22, 25, 75, 77, 118, 134, 146, 147, 154, 185, 185.1, 186, 225 (likumi.lv did not respond; read from the Internet Archive copy dated 02.08.2026, which marks the 01.01.2026 version as in force) | https://likumi.lv/ta/id/5490-komerclikums (archive: https://web.archive.org/web/20260802153145/https://likumi.lv/ta/id/5490-komerclikums) | 2026-10-30 |
| Uzņēmumu reģistrs, SIA / small-capital SIA / AS / IK / foreign branch descriptions and registration pages | https://apraksti.ur.gov.lv/lv/registre/uznemumu-vai-komersantu/sia (and /mazkapitala-sia, /akciju-sabiedriba, /individualais-komersants, /arvalstu-komersanta-filiale; registration steps at /lv/registre/dibinasana/registracija-uznemumu-registra-0, -4, -5, -2 and /registracija-uznemumu-registra) | 2026-10-30 |
| Uzņēmumu reģistrs, register company, organisation, contract, commercial pledge | https://www.ur.gov.lv/en/services/register-company-organisation-contract-commercial-pledge | 2026-10-30 |
| Uzņēmumu reģistrs, news 15.10.2026: applications electronic from 2027 | https://www.ur.gov.lv/lv/jaunums/no-2027-gada-pieteikumi-uznemumu-registra-bus-jaiesniedz-elektroniski | 2026-10-30 |
| Pievienotās vērtības nodokļa likums (VAT Law), arts. 57, 59, 118, 119 (Internet Archive copy dated 16.10.2026) | https://likumi.lv/ta/id/253451 | 2026-10-30 |
| Uzņēmumu ienākuma nodokļa likums (CIT Law), arts. 3, 4, 4.2, 17 (Internet Archive copy dated 04.10.2026) | https://likumi.lv/ta/id/292700 | 2026-10-30 |
| Gada pārskatu un konsolidēto gada pārskatu likums (Annual Reports Law), art. 97 (Internet Archive copy dated 18.08.2026) | https://likumi.lv/ta/id/277779 | 2026-10-30 |
| VID, micro-enterprise tax | https://www.vid.gov.lv/lv/mikrouznemumu-nodoklis | 2026-10-30 |
| VID information material "Mikrouzņēmumu nodoklis" (last updated 06.05.2026) | https://www.vid.gov.lv/lv/media/32306/download?attachment | 2026-10-30 |
| Cabinet Regulation No. 664 of 11.10.2016 on the state fee for entries in the commercial register, annex part II (likumi.lv did not respond; read from the Internet Archive copy dated 11.07.2025) | https://likumi.lv/ta/id/285320 | 2026-10-30 |
| VID, micro-enterprise tax rate | https://www.vid.gov.lv/lv/mikrouznemumu-nodokla-likme | 2026-10-30 |

Not yet confirmed: any amendment to Cabinet Regulation No. 664 after 11 July 2025 (the date of the only readable copy; its base amounts match UR's 2026 pages) and whether an official publication fee is charged on top; any Commercial Law amendment in force after 2 August 2026 (likumi.lv did not respond on 30 October 2026 and the latest archive copy, dated 2 August 2026, lists no later version); the Micro-enterprise Tax Law itself (the micro rules above come from VID), including whether an SIA that registered for micro-enterprise tax in an earlier year keeps that status (CIT Law arts. 2(4) and 4(11) still mention such an SIA).

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
