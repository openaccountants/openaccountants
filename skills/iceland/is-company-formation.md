---
name: is-company-formation
description: "Company formation and entity choice in Iceland for tax year 2026, from Act 138/1994 on private limited companies, Act 2/1995 on public limited companies, Act 50/2007 on partnerships, Act 3/2006 on annual accounts, Act 88/1991 on state fees and the Income Tax Act 90/2003 (althingi.is text 158a), and Skatturinn's company register pages and 2026 fee list. Covers the ehf. (minimum capital ISK 500,000, fully paid before registration, one founder allowed), the hf. (ISK 4,000,000, two founders, board of three), partnerships and sole traders, the board residence rule, registration documents, deadlines and fees (ehf. ISK 140,500), annual accounts filing, the audit exemption and the 2026 company return deadlines (31 May, extension to 21 September). Use for 'set up a company in Iceland', 'ehf vs hf', 'Iceland company registration fee'. Out of scope: company tax computation (is-corporate-income-tax), owner salary vs dividend planning (iceland-tax-optimization), VAT registration (iceland-vat), payroll (iceland-payroll)."
jurisdiction: IS
category: international
tax_year: 2026
last_updated: 2026-10-30
version: 0.2
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Iceland Company Formation & Entity Choice

## Iceland Company Formation v0.2

Figures are for 2026. Where a tax point is covered by a domain skill in this pack, the domain skill carries the detail and wins if the two ever differ.

## Entity types, incorporation and annual compliance

The most common vehicle is the private limited company (einkahlutafélag, 'ehf.'). Companies are registered in the company register (fyrirtækjaskrá) run by Skatturinn (Iceland Revenue and Customs) _([Skatturinn, private limited companies](https://www.skatturinn.is/fyrirtaekjaskra/stofnun-felaga/einkahlutafelog/))_.

### Choosing the form

- **Private limited company (einkahlutafélag, 'ehf.').** No member is personally liable for the company's debts _(Act 138/1994, Article 1)_. One or more founders sign a written memorandum and subscribe for the shares _(Article 3)_, so one person can form an ehf. alone. Taxed as a separate entity at 20% _(Income Tax Act 90/2003, Articles 2(1)(1) and 71(1))_. Detail: `is-corporate-income-tax`.
- **Public limited company (hlutafélag, 'hf.').** Used for larger and listed companies. At least two founders _(Act 2/1995, Article 3)_, a board of at least three _(Article 63)_ and higher minimum capital (below). Taxed at 20% like an ehf. _(Income Tax Act, Article 71(1))_.
- **General partnership (sameignarfélag, 'sf.').** An arrangement between two or more parties for joint business _(Act 50/2007, Article 2)_; the partners are personally liable. A partnership registered in the company register is a separate taxpayer only if this is asked for at registration and a partnership agreement showing ownership shares, paid-in capital and how the partnership is wound up is handed in. Spouses alone, or with their minor children, cannot form a partnership that is a separate taxpayer _(Income Tax Act, Article 2(1)(3))_. A separately taxed partnership pays 37.6% _(Income Tax Act, Article 71(2))_. Otherwise the partners are taxed on their shares.
- **Limited partnership (samlagsfélag, 'slf.').** At least one partner has unlimited liability, and the firm name must carry the name of at least one such partner _(Firms Act 42/1903, Article 9)_. The Partnerships Act 50/2007 applies to general partnerships only _(Act 50/2007, Article 1)_. A limited partnership is entered in the company register _(Act 17/2003, Article 3)_. It is covered by the same separate-taxpayer rule and the same 37.6% rate as a general partnership _(Income Tax Act, Articles 2(1)(3) and 71(2))_.
- **Sole trader (einstaklingsrekstur).** Not a separate taxpayer. The owner is taxed as an individual and must set calculated remuneration (reiknað endurgjald) for own work _(Income Tax Act, Article 58)_. Detail: `iceland-income-tax`, `iceland-tax-optimization`.
- **Branch of a foreign company (útibú).** Its formation is notified to the company register _(Act 138/1994, Articles 111 and 115, for a foreign private limited company; Act 2/1995, Chapter XVI, for a foreign public limited company; Skatturinn fee list)_. The branch manager files a certified copy of the foreign company's annual accounts with the branch accounts no later than eight months after the year end _(Act 3/2006, Article 112)_. A non-resident company with an Icelandic permanent establishment pays 20% where it corresponds to an ehf. or hf., and 37.6% otherwise _(Income Tax Act, Articles 3 and 71)_. Detail: `is-cross-border`.

### Capital

- **ehf. minimum share capital: ISK 500,000** _(Act 138/1994, Article 1(2))_. All of it is paid before registration: the company cannot be registered until the whole share capital is paid _(Articles 9 and 11)_. Skatturinn states the full capital is paid at formation _([Skatturinn, private limited companies](https://www.skatturinn.is/fyrirtaekjaskra/stofnun-felaga/einkahlutafelog/))_.
- **Capital in kind.** Where capital is paid in something other than money, a lawyer or chartered accountant (löggiltur endurskoðandi) confirms the asset exists _(Skatturinn, private limited companies)_.
- **hf. minimum share capital: ISK 4,000,000** _(Act 2/1995, Article 1(3))_. At least half of the subscribed capital must be paid before registration, and never less than the ISK 4,000,000 minimum _(Article 14)_.
- **Changes to the minimum.** The minister may change both minimums in line with the euro exchange rate, in whole hundreds of thousands of krónur, effective from the start of a year if announced by 15 December. A company that met the minimum when formed does not have to top up _(Act 138/1994, Article 1(2); Act 2/1995, Article 1(3))_.

### Board and management

- **ehf. board.** At least three members, but where there are four or fewer shareholders one or two members are enough. A one-member board must have at least one alternate _(Act 138/1994, Article 39)_.
- **Residence of managers.** Managing directors and at least half the board must live in Iceland. This does not apply to citizens of EEA states, people living in the EEA, citizens of EFTA states or Faroese citizens. The minister can grant an exemption _(Act 138/1994, Article 42)_.

### Registration

- **Registration authority.** The company register (fyrirtækjaskrá) at Skatturinn. An ehf. can be registered electronically through Skatturinn's service pages with electronic ID, or on paper _(Skatturinn, private limited companies)_.
- **Documents, one founder.** Notification form RSK 17.21 signed by all board members, articles of association (samþykktir), the memorandum (stofnskrá), the founding record (stofngerð) and the beneficial-owner notification _(Skatturinn, private limited companies)_.
- **Documents, two or more founders.** RSK 17.21, articles of association, memorandum of association (stofnsamningur) signed by the founders, minutes of the founding meeting (stofnfundargerð) and the beneficial-owner notification _(Skatturinn, private limited companies)_.
- **Deadline to register.** The ehf. board must notify the company for registration within two months of the date of the memorandum; a late notification is refused _(Act 138/1994, Article 9)_. For an hf. the limit is six months _(Act 2/1995, Article 14)_.
- **Processing time.** Skatturinn states that a paper application for an ehf. is generally processed in ten to twelve working days from complete documents and payment _(Skatturinn, private limited companies)_.

### Registration fees (2026)

Skatturinn's fee list gives the amount payable. It includes, where relevant, the fee for issuing an ID number (kennitala) and for publication in the Legal Gazette (Lögbirtingablað). The statutory registration fee is set by Act 88/1991, Article 13. A partnership is registered as a firm in the firm register _(Act 50/2007, Article 4)_, so its statutory fee is the line for a firm of two or more persons _(Act 88/1991, Article 13, item 5)_.

| Registration | Payable to Skatturinn | Statutory registration fee (Act 88/1991, Art 13) |
|---|---:|---:|
| ehf. | ISK 140,500 | ISK 134,000 |
| hf. | ISK 276,500 | ISK 270,000 |
| sf. (general partnership) | ISK 95,500 | ISK 89,000 |
| slf. (limited partnership) | ISK 95,500 | ISK 89,000 |
| Sole trader's firm (firma eins manns) | ISK 73,500 | ISK 72,000 |
| Branch of a foreign company | ISK 276,500 | ISK 270,000 |
| Conversion ehf. to hf. | ISK 137,700 | ISK 134,000 |
| Additional notification / change | ISK 3,700 | ISK 2,200 |

Registration fees for an ehf. or hf. are paid in advance, through a claim sent to the online bank of the person registering; credit cards are not accepted _(Skatturinn, fee list; Skatturinn, private limited companies)_. A sole trader's firm has no separate ID number and uses the owner's _(Skatturinn, fee list)_.

### Moving a sole trade into an ehf.

A sole trader can move the business into an ehf. without taxable income for the owner or the company, if the conditions are met. The ehf. takes over all assets and liabilities at book value, from a 31 December balance sheet no older than four months at formation, audited without qualification. So the transfer must be made by 30 April at the latest, and the formation documents must reach the company register by 30 June of the same year _(Skatturinn, private limited companies; Income Tax Act, Article 56; Regulation 223/2003)_. Detail: `is-corporate-income-tax`.

### Annual compliance

- **Annual accounts.** Companies file their annual accounts with the Register of Annual Accounts (ársreikningaskrá) no later than one month after approval, and no later than eight months after the year end, so by 31 August for a calendar-year company _(Act 3/2006, Article 109)_.
- **Micro companies.** A micro company (örfélag) does not exceed two of these three limits at the balance-sheet date: total assets ISK 20,000,000, net turnover ISK 40,000,000, an average of 3 full-time staff _(Act 3/2006, Article 2)_. It may file an income statement and balance sheet built from its tax return instead of full accounts _(Article 3)_.
- **Statutory audit.** A company under two of these limits for the two previous financial years does not have to appoint an auditor: balance-sheet total ISK 200,000,000, net turnover ISK 400,000,000, an average of 50 full-time staff. Where it is clear at formation that a limit will be reached, an auditor must be appointed from the start. Public-interest entities and companies that do not restrict share transfers cannot use the exemption _(Act 3/2006, Article 98)_.
- **Annual company tax return.** For 2025 income, filed in 2026: general deadline 31 May 2026; professional preparers (auditors and bookkeepers) could get an extension up to 21 September 2026 _([Skatturinn, notice of 30 January 2026](https://www.skatturinn.is/um-rsk/frettir-og-tilkynningar/opnad-fyrir-skil-a-skattframtali-logadila-2026))_. Detail: `is-corporate-income-tax`.
- **Changes.** Changes to the articles or other registered details of an ehf. are notified within one month _(Act 138/1994, Article 123)_.
- **Other registrations.** A company that pays wages registers on the employer register, and one that sells taxable goods or services above ISK 2,000,000 in 12 months registers for VAT. Detail: `iceland-payroll`, `iceland-vat`.

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

## Sources

| Source | URL | Read on |
|---|---|---|
| Act 138/1994 on Private Limited Companies (lög um einkahlutafélög), consolidated text 158a of 1 October 2026, Articles 1, 3, 9, 11, 39, 42, 111, 115, 123 | https://www.althingi.is/lagas/nuna/1994138.html | 2026-10-30 |
| Act 2/1995 on Public Limited Companies (lög um hlutafélög), consolidated text 158a, Articles 1, 3, 14, 63 and Chapter XVI | https://www.althingi.is/lagas/nuna/1995002.html | 2026-10-30 |
| Act 50/2007 on Partnerships (lög um sameignarfélög), consolidated text 158a, Articles 1, 2, 4 | https://www.althingi.is/lagas/nuna/2007050.html | 2026-10-30 |
| Act 3/2006 on Annual Accounts (lög um ársreikninga), consolidated text 158a, Articles 2, 3, 98, 109, 112 | https://www.althingi.is/lagas/nuna/2006003.html | 2026-10-30 |
| Act 88/1991 on State Fees (lög um aukatekjur ríkissjóðs), consolidated text 158a, Article 13 | https://www.althingi.is/lagas/nuna/1991088.html | 2026-10-30 |
| Act 17/2003 on the Business Register (lög um fyrirtækjaskrá), consolidated text 158a, Article 3 | https://www.althingi.is/lagas/nuna/2003017.html | 2026-10-30 |
| Firms Act 42/1903 (lög um verslanaskrár, firmu og prókúruumboð), consolidated text 158a, Article 9 | https://www.althingi.is/lagas/nuna/1903042.html | 2026-10-30 |
| Income Tax Act 90/2003 (lög um tekjuskatt), consolidated text 158a, Articles 2, 56, 71 | https://www.althingi.is/lagas/nuna/2003090.html | 2026-10-30 |
| Skatturinn, private limited companies (registration, capital, documents, processing time, sole-trade transfer) | https://www.skatturinn.is/fyrirtaekjaskra/stofnun-felaga/einkahlutafelog/ | 2026-10-30 |
| Skatturinn, company register fee list (gjaldskrá) | https://www.skatturinn.is/fyrirtaekjaskra/gjaldskra/ | 2026-10-30 |
| Skatturinn, notice of 30 January 2026: legal-entity returns 2026, deadline 31 May, extension to 21 September | https://www.skatturinn.is/um-rsk/frettir-og-tilkynningar/opnad-fyrir-skil-a-skattframtali-logadila-2026 | 2026-10-30 |
| Skatturinn, key figures and rates 2026 (company tax 20% / 37.6%) | https://www.skatturinn.is/einstaklingar/helstutolur/2026/ | 2026-10-30 |

Not yet confirmed: processing time for an electronic ehf. registration (Skatturinn gives ten to twelve working days for paper only); the 2027 company return deadlines for 2026 income (not yet published); the old statement that the share capital is deposited in an Icelandic bank account (not in Act 138/1994 or on Skatturinn's page, so left out).
