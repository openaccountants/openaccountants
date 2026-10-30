---
name: ee-company-formation
description: "Setting up a business in Estonia for tax year 2026, from the Commercial Code, State Fees Act, Income Tax Act and Value-Added Tax Act as consolidated on Riigi Teataja, and the Centre of Registers (RIK) e-Business Register help pages. Covers the legal forms (private limited company OÜ, public limited company AS, sole proprietor FIE, general and limited partnerships, branch of a foreign company), share capital (an OÜ from one cent, an AS from EUR 25,000), paying in the capital, the online and notary routes, the 2026 state fees (EUR 265 online, EUR 200 otherwise, EUR 20 for an FIE), e-Residency, and the first tax and filing duties after registration. Use for 'set up a company in Estonia', 'OÜ share capital', 'Estonian company registration fee', 'e-Residency company'. Out of scope: company tax detail (ee-corporate-income-tax), payroll (estonia-payroll), VAT returns (estonia-vat-return), cross-border (ee-cross-border)."
jurisdiction: EE
category: international
tax_year: 2026
last_updated: 2026-10-30
version: 0.2
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Estonia Company Formation & Entity Choice

This skill covers choosing a legal form in Estonia, registering it in 2026, and the first tax and filing duties that follow. Every figure comes from the law as consolidated on Riigi Teataja or from the registrar's own help pages, read on 30 October 2026. The tax computations sit in the pack's domain skills; where a domain skill and this skill ever differ, the domain skill wins.

Abbreviations: ÄS = Äriseadustik (Commercial Code); RLS = Riigilõivuseadus (State Fees Act); TuMS = Tulumaksuseadus (Income Tax Act); KMS = Käibemaksuseadus (Value-Added Tax Act); SMS = Sotsiaalmaksuseadus (Social Tax Act); RIK = Registrite ja Infosüsteemide Keskus (Centre of Registers and Information Systems), which runs the e-Business Register portal.

## Entity types, incorporation and annual compliance

- **Private limited company (osaühing, OÜ)**: a company whose share capital is divided into shares. Shareholders are not personally liable for its debts, and the company answers with all its assets. One or more persons can found it. _(ÄS §§ 135(1)-(3), 137(1))_
- **Public limited company (aktsiaselts, AS)**: a company whose share capital is divided into shares, with share capital of at least EUR 25,000. Shareholders are not personally liable. A registered share is freely transferable. In an OÜ, unless the articles say otherwise, a share can be transferred freely to another shareholder, and the other shareholders have a one-month pre-emption right on a transfer to an outsider. _(ÄS §§ 149(2), 221(1)-(2), 222, 229(1))_
- **Other forms**: a sole proprietor (füüsilisest isikust ettevõtja, FIE), which any natural person can be, must apply to be entered in the commercial register before starting business. A general partnership (täisühing, TÜ) has two or more partners who are jointly liable with all their assets. A limited partnership (usaldusühing, UÜ) has at least one general partner liable with all assets and at least one limited partner liable up to the contribution. The Commercial Code also lists the commercial association (tulundusühistu). A foreign company can register a branch (filiaal), which is not a legal person; the company is liable for it. _(ÄS §§ 2(1), 3(1)-(2), 79, 125(1), 384(1)-(2))_
- **Minimum share capital, OÜ**: EUR 0.01. Since 1 February 2023 the Code only says the share capital is stated in euros, and the smallest nominal value of a share is one cent. RIK: "The minimum capital of a is 0.01€ (if there is one shareholder). The minimum share amount of every shareholder is at least 0.01 €". _(ÄS §§ 136, 148(1); RIK, establishment of a private limited company)_
- **Paying in the capital, OÜ**: founders must pay for their shares in full before the registration application is filed. Founding an OÜ without paying in the contribution (old § 140^1) was repealed from 1 February 2023. Cash goes into a payment account opened in the name of the company being founded; under the expedited procedure it can also be paid as a deposit to the registrar's account. A bank or payment institution notice is needed only when the contribution is over EUR 50,000; up to that amount the founders confirm in the portal that it has been paid. If capital, or a share paid for in kind, is EUR 25,000 or more, an auditor must check the valuation of the in-kind contribution. _(ÄS §§ 140(2), 140^1, 141, 143(3), 144(1) p 3, 520(4^1); RIK)_
- **Minimum share capital, AS**: EUR 25,000. _(ÄS § 222)_
- **Incorporation method**: online through the RIK e-Business Register portal. The application can only be signed with an Estonian ID card (including the e-Residency card), Smart-ID or Mobile-ID, and everyone added to the application must be able to sign it digitally. The expedited procedure (kiirmenetlus) uses standard articles of association set by ministerial regulation. The founding can also be done before a notary: the Code refers to both notarial and non-notarial founding. _(ÄS §§ 139^1(1)-(2), 520(1); RIK)_
- **What the application holds**: the name with "Osaühing" or "OÜ" at the start or end; an address chosen from the Estonian address data system (if the company's address is abroad, a contact person must be added); an e-mail address; board members and founders; the share capital per founder; the articles; the beneficial owners. Optional extras sent on to the Tax and Customs Board (EMTA) once the company is entered: voluntary VAT registration and entries in the register of employees. The default financial year is the calendar year. _(RIK, establishment of a private limited company)_
- **Incorporation timeline**: after you submit, the application page shows the proceeding term by which the registrar must review it. The application goes to the register only after the state fee has reached the state treasury. _(RIK)_ The statutory review period is on the "Not yet confirmed" line below.
- **State fees in 2026**: entering an OÜ, AS, commercial association or foreign company branch costs EUR 200, or EUR 265 when filed under the expedited procedure. RIK states the fee for founding an OÜ electronically is EUR 265. Entering an FIE, general partnership or limited partnership costs EUR 20. Later changes to the entry cost EUR 25 for an OÜ, AS, commercial association or branch, and EUR 10 for an FIE or partnership. The same amounts are in the State Fees Act texts in force from 1 November 2026 and from 1 January 2027. _(RLS §§ 62(1)-(2), 63(1)-(2); RIK)_
- **e-Residency**: a government digital ID. With the e-Residency card you can log in to the e-Business Register and register a company fully online. e-Residency "does not affect your personal tax residency". A company founded under Estonian law is an Estonian tax resident. _(e-Residency, start a company; TuMS § 6(2))_
- **Annual report obligation**: the management board files the approved annual report, with the profit allocation proposal, sales revenue breakdown and the auditor's report where an audit is required, with the commercial register within six months of the end of the financial year. The same six months apply to an OÜ and an AS. _(ÄS §§ 179(4), 334(2))_
- **Ongoing tax compliance**: a resident legal person files the monthly income and social tax return (TSD) by the 10th of the following month. A person whose Estonian taxable turnover from the start of the calendar year exceeds EUR 40,000 must register for VAT, applying within three working days of crossing it. A VAT-registered person files the VAT return (KMD) by the 20th of the following month. _(TuMS § 54(2); KMS §§ 19(1), 20(1), 27(1))_ Detail: estonia-vat-return, estonia-payroll.
- **Company tax once formed**: a resident company pays income tax when it distributes profit as dividends or other distributions, not while profit is kept in the company. The rate is 22%, applied to the net amount divided by 0.78. Salaries carry social tax at 33%. _(TuMS §§ 4(1), 4(1^1), 50(1); SMS § 7(1))_ Detail: ee-corporate-income-tax, estonia-social-contributions.

## Which skill next

- Company tax on distributions, deemed distributions, participation exemption: ee-corporate-income-tax
- Salaries, TSD, social tax and unemployment premiums: estonia-payroll, estonia-social-contributions
- VAT registration and the KMD return: estonia-vat-return
- Non-resident owners, permanent establishments, treaties: ee-cross-border; related-party pricing: ee-transfer-pricing
- Sole proprietor (FIE) income tax: estonia-income-tax
- Whole-system map: ee-tax-overview

## Sources

| Source | URL | Read on |
|---|---|---|
| Äriseadustik (Commercial Code), consolidated text in force from 01.03.2024 (the text Riigi Teataja lists as in force on 30.10.2026), §§ 2, 3, 79, 125, 135-137, 139^1, 140, 140^1, 141, 143, 144, 148, 149, 179, 221, 222, 229, 334, 384, 520 | https://www.riigiteataja.ee/et/akt/106072023131 | 2026-10-30 |
| Riigilõivuseadus (State Fees Act), consolidated text in force 01.08.2026 to 30.10.2026, §§ 62, 63 | https://www.riigiteataja.ee/et/akt/111072026166 | 2026-10-30 |
| Riigilõivuseadus, consolidated texts in force 01.11.2026 to 31.12.2026 and from 01.01.2027, § 62 (same amounts) | https://www.riigiteataja.ee/et/akt/121102026010 and https://www.riigiteataja.ee/et/akt/121102026011 | 2026-10-30 |
| Tulumaksuseadus (Income Tax Act), consolidated text in force 01.10.2026 to 31.12.2026, §§ 4, 6, 50, 54 | https://www.riigiteataja.ee/et/akt/109072026066 | 2026-10-30 |
| Käibemaksuseadus (Value-Added Tax Act), consolidated text in force from 01.10.2026, §§ 19, 20, 27 | https://www.riigiteataja.ee/et/akt/130062026129 | 2026-10-30 |
| Sotsiaalmaksuseadus (Social Tax Act), consolidated text in force from 26.10.2026, § 7 | https://www.riigiteataja.ee/et/akt/116102026014 | 2026-10-30 |
| RIK help, establishment of a private limited company (OÜ) | https://abiinfo.rik.ee/en/applications-and-dashboard/establishment-new-legal-person/establishment-private-limited-company | 2026-10-30 |
| e-Residency (Government of Estonia), start a company | https://www.e-resident.gov.ee/start-a-company/ | 2026-10-30 |

Not yet confirmed: the statutory number of working days the registrar has to review an application (the old ÄS § 53 on procedure deadlines was repealed from 1 February 2023 and the rule now in force was not found; RIK shows the term on each application); notary fees on the notary route (Notary Fees Act not read); the pre-2023 minimum OÜ share capital (history only, not needed for 2026).

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
