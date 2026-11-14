---
name: is-company-formation
description: "Company formation and entity choice in Iceland for tax year 2026, from Act 138/1994 on private limited companies, Act 2/1995 on public limited companies, Act 50/2007 on partnerships, Act 3/2006 on annual accounts, Act 88/1991 on state fees and the Income Tax Act 90/2003, and Skatturinn's company register pages and 2026 fee list. Covers the ehf. (minimum capital ISK 500,000, fully paid before registration, one founder allowed), the hf. (ISK 4,000,000, two founders, board of three), partnerships and sole traders, the board residence rule, registration documents in the order the filer meets them, deadlines and fees (ehf. ISK 140,500), moving a sole trade into an ehf., annual accounts filing, the audit exemption and the 2026 company return deadlines (31 May, extension to 21 September). Use for set up a company in Iceland, ehf vs hf, Iceland company registration fee. Out of scope are company tax computation (is-corporate-income-tax), owner salary vs dividend planning (iceland-tax-optimizati"
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/is-company-formation"
  jurisdiction: "IS"
  tax_year: "2026"
  last_updated: "2026-11-14"
---

# Iceland Company Formation and Entity Choice v1.0

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

Figures are for 2026. This skill takes a founder from the choice of legal form to a registered company and its first annual filings in Iceland. Where a tax point is covered by a domain skill in this pack, the domain skill carries the detail and wins if the two ever differ.

The most common vehicle is the private limited company (einkahlutafélag, 'ehf.'). Companies are registered in the company register (fyrirtækjaskrá) run by Skatturinn (Iceland Revenue and Customs) _([Skatturinn, private limited companies](https://www.skatturinn.is/fyrirtaekjaskra/stofnun-felaga/einkahlutafelog/))_.

Out of scope: company tax computation (`is-corporate-income-tax`), owner salary against dividends (`iceland-tax-optimization`), VAT registration (`iceland-vat`), payroll (`iceland-payroll`), and regulated entities (banks, insurers, funds) that need a licence before registration.

## Ask the client first

- How many founders, and are they individuals or companies? (One founder can form an ehf.; an hf. needs two.)
- Where do the managing director and board members live, and are they EEA, EFTA or Faroese citizens or EEA residents?
- How much capital, and is any of it paid in kind?
- Is this a new business or an existing sole trade being moved into a company (the 30 April and 30 June dates apply)?
- Will the company pay wages or sell taxable goods or services above ISK 2,000,000 in 12 months?
- Expected balance-sheet total, turnover and staff, for the micro-company and audit tests.

## The method, step by step

### Step 1: choose the form

- **Private limited company (einkahlutafélag, 'ehf.').** No member is personally liable for the company's debts _(Act 138/1994, Article 1)_. One or more founders sign a written memorandum and subscribe for the shares _(Article 3)_, so one person can form an ehf. alone. Taxed as a separate entity at 20% _(Income Tax Act 90/2003, Articles 2(1)(1) and 71(1))_. Detail: `is-corporate-income-tax`.
- **Public limited company (hlutafélag, 'hf.').** Used for larger and listed companies. At least two founders _(Act 2/1995, Article 3)_, a board of at least three _(Article 63)_ and higher minimum capital (below). Taxed at 20% like an ehf. _(Income Tax Act, Article 71(1))_.
- **General partnership (sameignarfélag, 'sf.').** An arrangement between two or more parties for joint business _(Act 50/2007, Article 2)_; the partners are personally liable. A partnership registered in the company register is a separate taxpayer only if this is asked for at registration and a partnership agreement showing ownership shares, paid-in capital and how the partnership is wound up is handed in. Spouses alone, or with their minor children, cannot form a partnership that is a separate taxpayer _(Income Tax Act, Article 2(1)(3))_. A separately taxed partnership pays 37.6% _(Income Tax Act, Article 71(2))_. Otherwise the partners are taxed on their shares.
- **Limited partnership (samlagsfélag, 'slf.').** At least one partner has unlimited liability, and the firm name must carry the name of at least one such partner _(Firms Act 42/1903, Article 9)_. The Partnerships Act 50/2007 applies to general partnerships only _(Act 50/2007, Article 1)_. A limited partnership is entered in the company register _(Act 17/2003, Article 3)_. It is covered by the same separate-taxpayer rule and the same 37.6% rate as a general partnership _(Income Tax Act, Articles 2(1)(3) and 71(2))_.
- **Sole trader (einstaklingsrekstur).** Not a separate taxpayer. The owner is taxed as an individual and must set calculated remuneration (reiknað endurgjald) for own work _(Income Tax Act, Article 58)_. Detail: `iceland-income-tax`, `iceland-tax-optimization`.
- **Branch of a foreign company (útibú).** Its formation is notified to the company register _(Act 138/1994, Articles 111 and 115, for a foreign private limited company; Act 2/1995, Chapter XVI, for a foreign public limited company; Skatturinn fee list)_. The branch manager files a certified copy of the foreign company's annual accounts with the branch accounts no later than eight months after the year end _(Act 3/2006, Article 112)_. A non-resident company with an Icelandic permanent establishment pays 20% where it corresponds to an ehf. or hf., and 37.6% otherwise _(Income Tax Act, Articles 3 and 71)_. Detail: `is-cross-border`.

### Step 2: put up the capital

- **ehf. minimum share capital: ISK 500,000** _(Act 138/1994, Article 1(2))_. All of it is paid before registration: the company cannot be registered until the whole share capital is paid _(Articles 9 and 11)_. Skatturinn states the full capital is paid at formation _([Skatturinn, private limited companies](https://www.skatturinn.is/fyrirtaekjaskra/stofnun-felaga/einkahlutafelog/))_.
- **Capital in kind.** Where capital is paid in something other than money, a lawyer or chartered accountant (löggiltur endurskoðandi) confirms the asset exists _(Skatturinn, private limited companies)_.
- **hf. minimum share capital: ISK 4,000,000** _(Act 2/1995, Article 1(3))_. At least half of the subscribed capital must be paid before registration, and never less than the ISK 4,000,000 minimum _(Article 14)_.
- **Changes to the minimum.** The minister may change both minimums in line with the euro exchange rate, in whole hundreds of thousands of krónur, effective from the start of a year if announced by 15 December. A company that met the minimum when formed does not have to top up _(Act 138/1994, Article 1(2); Act 2/1995, Article 1(3))_.

### Step 3: appoint the board and manager

- **ehf. board.** At least three members, but where there are four or fewer shareholders one or two members are enough. A one-member board must have at least one alternate _(Act 138/1994, Article 39)_.
- **Residence of managers.** Managing directors and at least half the board must live in Iceland. This does not apply to citizens of EEA states, people living in the EEA, citizens of EFTA states or Faroese citizens. The minister can grant an exemption _(Act 138/1994, Article 42)_.

### Step 4: register with the company register

- **Registration authority.** The company register (fyrirtækjaskrá) at Skatturinn. An ehf. can be registered electronically through Skatturinn's service pages with electronic ID, or on paper _(Skatturinn, private limited companies)_.
- **Documents, one founder.** Notification form RSK 17.21 signed by all board members, articles of association (samþykktir), the memorandum (stofnskrá), the founding record (stofngerð) and the beneficial-owner notification _(Skatturinn, private limited companies)_.
- **Documents, two or more founders.** RSK 17.21, articles of association, memorandum of association (stofnsamningur) signed by the founders, minutes of the founding meeting (stofnfundargerð) and the beneficial-owner notification _(Skatturinn, private limited companies)_.
- **Deadline to register.** The ehf. board must notify the company for registration within two months of the date of the memorandum; a late notification is refused _(Act 138/1994, Article 9)_. For an hf. the limit is six months _(Act 2/1995, Article 14)_.
- **Processing time.** Skatturinn states that a paper application for an ehf. is generally processed in ten to twelve working days from complete documents and payment _(Skatturinn, private limited companies)_.

### Rates, bands and thresholds: registration fees 2026 ([Skatturinn fee list](https://www.skatturinn.is/fyrirtaekjaskra/gjaldskra/))

Skatturinn's fee list gives the amount payable. It includes, where relevant, the fee for issuing an ID number (kennitala) and for publication in the Legal Gazette (Lögbirtingablað). The statutory registration fee inside it is set by Act 88/1991, Article 13; a partnership is registered as a firm in the firm register _(Act 50/2007, Article 4)_, so its statutory fee is the line for a firm of two or more persons _(Act 88/1991, Article 13, item 5)_. The statutory amounts (ehf. ISK 134,000, hf. ISK 270,000, sf. and slf. ISK 89,000, firm of one person ISK 72,000, branch ISK 270,000, conversion ehf. to hf. ISK 134,000, additional notification ISK 2,200) were read in Act 88/1991 on 30 Oct 2026 and could not be reopened today; they are on the "Not yet confirmed:" line.

| Registration | Payable to Skatturinn, 2026 | Source |
|---|---:|---|
| ehf. | ISK 140,500 | https://www.skatturinn.is/fyrirtaekjaskra/gjaldskra/ |
| hf. | ISK 276,500 | same |
| sf. (general partnership) | ISK 95,500 | same |
| slf. (limited partnership) | ISK 95,500 | same |
| Sole trader's firm (firma eins manns) | ISK 73,500 | same |
| Branch of a foreign company | ISK 276,500 | same |
| Conversion ehf. to hf. | ISK 137,700 | same |
| Conversion hf. to ehf. | ISK 12,700 | same |
| Additional notification (aukatilkynning) or merger/division notice | ISK 3,700 | same |
| ehf. minimum share capital | ISK 500,000 | https://www.skatturinn.is/fyrirtaekjaskra/stofnun-felaga/einkahlutafelog/ |
| VAT registration turnover line, 12 months | ISK 2,000,000 | https://www.skatturinn.is/atvinnurekstur/ad-hefja-rekstur/almennt-um-vsk/ |

Registration fees for an ehf. or hf. are paid in advance, through a claim sent to the online bank of the person registering; credit cards are not accepted _(Skatturinn, fee list; Skatturinn, private limited companies)_. A sole trader's firm has no separate ID number and uses the owner's _(Skatturinn, fee list)_.

### Step 5: register for payroll and VAT before trading

A company that pays wages registers on the employer register, and one that sells taxable goods or services above ISK 2,000,000 in 12 months registers for VAT. Notify the activity at least 8 days before it starts. Detail: `iceland-payroll`, `iceland-vat`.

### Moving a sole trade into an ehf.

A sole trader can move the business into an ehf. without taxable income for the owner or the company, if the conditions are met. The ehf. takes over all assets and liabilities at book value, from a 31 December balance sheet no older than four months at formation, audited without qualification. So the transfer must be made by 30 April at the latest, and the formation documents must reach the company register by 30 June of the same year _(Skatturinn, private limited companies; Income Tax Act, Article 56; Regulation 223/2003)_. Detail: `is-corporate-income-tax`.

## Boundary and exception table

| Situation | Rule | Source |
| --- | --- | --- |
| One founder | Allowed for an ehf. (memorandum, stofnskrá); not for an hf. (two founders) | Act 138/1994, Art. 3; Act 2/1995, Art. 3 |
| Capital paid in kind | Lawyer or chartered accountant confirms the asset exists | Skatturinn, private limited companies |
| hf. capital | At least half paid before registration, never less than ISK 4,000,000 | Act 2/1995, Art. 14 |
| ehf. notified more than two months after the memorandum (six months for an hf.) | Registration refused; start again | Act 138/1994, Art. 9; Act 2/1995, Art. 14 |
| Manager or half the board outside Iceland and not EEA, EFTA or Faroese | Not allowed without a ministerial exemption | Act 138/1994, Art. 42 |
| Spouses alone, or with minor children, forming a partnership | Cannot be a separate taxpayer | Income Tax Act, Art. 2(1)(3) |
| Sole trade moved in after 30 April, or documents after 30 June | Tax-free transfer conditions not met | Skatturinn, private limited companies; Income Tax Act, Art. 56 |
| Company clearly reaching an audit limit from the start | Auditor appointed from formation | Act 3/2006, Art. 98 |

## Worked cases

### Case 1: cash a single founder needs to register an ehf. against an hf.

A founder wants a company in 2026 and asks how much cash she must have in hand on the day of registration. An ehf. needs the whole ISK 500,000 capital paid before registration plus the ISK 140,500 fee: ISK 640,500. An hf. needs two founders, and at least ISK 4,000,000 paid before registration (half the subscribed capital, never less than the minimum) plus the ISK 276,500 fee: ISK 4,276,500. The ehf. needs ISK 3,636,000 less. The figure that decides it is the minimum capital; both forms pay company tax at 20%.

```oa-check
name: IS 2026 cash at registration, ehf against hf
inputs:
  ehf_capital: 500000
  ehf_fee: 140500
  hf_subscribed: 4000000
  hf_minimum: 4000000
  hf_fee: 276500
steps:
  - ehf_cash: ehf_capital + ehf_fee
  - hf_paid: max(hf_subscribed * 0.5, hf_minimum)
  - hf_cash: hf_paid + hf_fee
  - difference: hf_cash - ehf_cash
expected:
  ehf_cash: 640500
  hf_cash: 4276500
  difference: 3636000
```

## When to refuse or refer

- Refer regulated activities (financial services, insurance, funds) that need a licence first.
- Refer a cross-border group structure or a foreign parent with an Icelandic branch for the permanent-establishment and treaty points (`is-cross-border`).
- Refer a sole-trade transfer that misses the 30 April balance-sheet date or lacks an unqualified audit of the 31 December balance sheet.
- Do not advise on a board that breaks the residence rule without a ministerial exemption in hand.
- Do not state the statutory Act 88/1991 fee amounts as current until confirmed (see Not yet confirmed).

## Filing and payment

- **Annual accounts.** Companies file their annual accounts with the Register of Annual Accounts (ársreikningaskrá) no later than one month after approval, and no later than eight months after the year end, so by 31 August for a calendar-year company _(Act 3/2006, Article 109)_.
- **Micro companies.** A micro company (örfélag) does not exceed two of these three limits at the balance-sheet date: total assets ISK 20,000,000, net turnover ISK 40,000,000, an average of 3 full-time staff _(Act 3/2006, Article 2)_. It may file an income statement and balance sheet built from its tax return instead of full accounts _(Article 3)_.
- **Statutory audit.** A company under two of these limits for the two previous financial years does not have to appoint an auditor: balance-sheet total ISK 200,000,000, net turnover ISK 400,000,000, an average of 50 full-time staff. Where it is clear at formation that a limit will be reached, an auditor must be appointed from the start. Public-interest entities and companies that do not restrict share transfers cannot use the exemption _(Act 3/2006, Article 98)_.
- **Annual company tax return.** For 2025 income, filed in 2026: general deadline 31 May 2026; professional preparers (auditors and bookkeepers) could get an extension up to 21 September 2026 _([Skatturinn, notice of 30 January 2026](https://www.skatturinn.is/um-rsk/frettir-og-tilkynningar/opnad-fyrir-skil-a-skattframtali-logadila-2026))_. Detail: `is-corporate-income-tax`.
- **Changes.** Changes to the articles or other registered details of an ehf. are notified within one month _(Act 138/1994, Article 123)_.
- **Other registrations.** A company that pays wages registers on the employer register, and one that sells taxable goods or services above ISK 2,000,000 in 12 months registers for VAT. Detail: `iceland-payroll`, `iceland-vat`.

## Completion checklist

- Form chosen, founders counted, and the residence rule met.
- Capital paid in full (ehf.) or to the hf. minimum, with confirmation for capital in kind.
- RSK 17.21 signed by all board members, articles, memorandum or founding record, and the beneficial-owner notification ready.
- Notified within two months of the memorandum (six for an hf.); fee paid through the online-bank claim.
- Employer register and VAT register notified at least 8 days before trading where needed.
- Annual accounts, tax return and change notifications diarised.

## Sources

Pages dated 2026-11-14 were opened again today and the figures named were found on them. Alþingi's law pages returned HTTP 403 on 14 Nov 2026 and keep their earlier read date.

| Source | URL | Read on |
|---|---|---|
| Read for Act 138/1994 on Private Limited Companies, consolidated text 158a of 1 October 2026, Articles 1, 3, 9, 11, 39, 42, 111, 115, 123; not reopened 14 Nov 2026 (403) | https://www.althingi.is/lagas/nuna/1994138.html | 2026-10-30 |
| Read for Act 2/1995 on Public Limited Companies, Articles 1, 3, 14, 63 and Chapter XVI; not reopened 14 Nov 2026 (403) | https://www.althingi.is/lagas/nuna/1995002.html | 2026-10-30 |
| Read for Act 50/2007 on Partnerships, Articles 1, 2, 4; not reopened 14 Nov 2026 (403) | https://www.althingi.is/lagas/nuna/2007050.html | 2026-10-30 |
| Read for Act 3/2006 on Annual Accounts, Articles 2, 3, 98, 109, 112; not reopened 14 Nov 2026 (403) | https://www.althingi.is/lagas/nuna/2006003.html | 2026-10-30 |
| Read for Act 88/1991 on State Fees, Article 13; not reopened 14 Nov 2026 (403) | https://www.althingi.is/lagas/nuna/1991088.html | 2026-10-30 |
| Read for Act 17/2003 on the Business Register, Article 3; not reopened 14 Nov 2026 (403) | https://www.althingi.is/lagas/nuna/2003017.html | 2026-10-30 |
| Read for Firms Act 42/1903, Article 9; not reopened 14 Nov 2026 (403) | https://www.althingi.is/lagas/nuna/1903042.html | 2026-10-30 |
| Read for Income Tax Act 90/2003, Articles 2, 56, 71; not reopened 14 Nov 2026 (403) | https://www.althingi.is/lagas/nuna/2003090.html | 2026-10-30 |
| Read for Skatturinn, private limited companies: capital ISK 500,000 paid at formation, capital in kind, RSK 17.21 and documents, ten to twelve working days, 30 April and 30 June transfer dates | https://www.skatturinn.is/fyrirtaekjaskra/stofnun-felaga/einkahlutafelog/ | 2026-11-14 |
| Read for Skatturinn, company register fee list (gjaldskrá): every amount in the fee table and the advance-payment rule | https://www.skatturinn.is/fyrirtaekjaskra/gjaldskra/ | 2026-11-14 |
| Read for Skatturinn, VAT general (almennt um VSK): ISK 2,000,000 in 12 months and notice 8 days before activity | https://www.skatturinn.is/atvinnurekstur/ad-hefja-rekstur/almennt-um-vsk/ | 2026-11-14 |
| Read for Skatturinn, notice of 30 January 2026: legal-entity returns 2026, deadline 31 May, extension to 21 September | https://www.skatturinn.is/um-rsk/frettir-og-tilkynningar/opnad-fyrir-skil-a-skattframtali-logadila-2026 | 2026-11-14 |
| Read for Skatturinn, key figures and rates 2026: company tax 20% and 37.6% | https://www.skatturinn.is/einstaklingar/helstutolur/2026/ | 2026-11-14 |

Not yet confirmed: the Alþingi texts as at 14 Nov 2026 (403 today), so the hf. capital ISK 4,000,000, the board, residence, deadline and audit rules, the micro-company and audit limits, and the statutory Act 88/1991 fees rest on the 30 Oct 2026 reading; processing time for an electronic ehf. registration (Skatturinn gives ten to twelve working days for paper only); the 2027 company return deadlines for 2026 income (not yet published); the old statement that the share capital is deposited in an Icelandic bank account (not in Act 138/1994 or on Skatturinn's page, so left out).

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-14. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `is-company-formation` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/is-company-formation. If neither is available, confirm every figure against the official source pages cited above before relying on it.
