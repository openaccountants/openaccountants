---
jurisdiction: UA
applicable: [IT-IND, IT-CORP, VAT, SC, PR, TP, XB]
not_applicable: {}
covered_by:
  IT-IND: ua-income-tax
  IT-CORP: ua-corporate-income-tax
  VAT: ukraine-vat
  SC: ua-social-contributions
  PR: ua-payroll
  TP: ua-transfer-pricing
  XB: ua-cross-border
partial:
  IT-IND: "Covers sole proprietors only (general system in ua-income-tax, single tax in ua-single-tax, crypto in ua-crypto-tax). Employment, investment, rental and property income of individuals who are not entrepreneurs, their annual declaration and the tax discount are not covered."
  IT-CORP: "ua-corporate-income-tax on main is a tax year 2025 stub. The 2026 rewrite from the Tax Code is in PR #959; remove this entry when it merges."
  VAT: "ukraine-vat on main carries tax year 2025. The 2026 rewrite from the Tax Code is in PR #966; remove this entry when it merges."
---

# Ukraine: tax pack

Calendar tax year. Currency: hryvnia (UAH). Authority: the State Tax Service of Ukraine (Державна податкова служба, tax.gov.ua); returns are filed electronically. The main law is the Tax Code of Ukraine (Податковий кодекс України, Law No. 2755-VI of 2 December 2010), consolidated on zakon.rada.gov.ua; martial law has applied since 24 February 2022 and several temporary rules sit in its section XX. Corporate income tax is 18% (art. 136.1). Personal income tax is 18% (art. 167.1), with a 5% military levy on individuals' income (section XX, subsection 10, point 16-1). VAT is 20% (art. 193.1). Withholding on Ukrainian-source income paid to non-residents is 15% unless a treaty gives less (art. 141.4.2). Amounts tied to the minimum wage and the subsistence minimum use the State Budget Law for the year: for 2026, a minimum wage of UAH 8,647 a month and a subsistence minimum for able-bodied persons of UAH 3,328 (Law No. 4695-IX, arts. 7 and 8).

## Domains

| Domain | Skill | Status |
|---|---|---|
| IT-IND, individual income tax | ua-income-tax: general-system sole proprietors, 18% PIT and 5% military levy on net profit (2026); with ua-single-tax (single-tax groups) and ua-crypto-tax (virtual assets from 2026). Individuals who are not entrepreneurs are not covered | partial; general template, not yet in the deep-tax shape |
| IT-CORP, corporate income tax | ua-corporate-income-tax: on main a 2025 stub; PR #959 rewrites it for 2026 (18%, 25% financial institutions, 50% banks in 2026, accounting-profit base, UAH 40 million option, losses, dividend advance, returns, penalties, withholding) | partial until PR #959 merges |
| VAT | ukraine-vat: on main tax year 2025; PR #966 rewrites it for 2026 (UAH 1,000,000 registration, 20% / 14% / 7% / 0%, invoices and blocking, monthly return, refunds, reverse charge, martial-law rules) | partial until PR #966 merges |
| SC, social contributions | ua-social-contributions: ЄСВ for sole proprietors and independent professionals, 22%, minimum and maximum base (2026); employer ЄСВ on salaries is in ua-payroll | general template, not yet in the deep-tax shape |
| PR, payroll withholding | ua-payroll: employer PIT 18%, 5% military levy and 22% ЄСВ on salaries, gross-to-net, reporting calendar (2026) | general template, not yet in the deep-tax shape |
| TP, transfer pricing | ua-transfer-pricing: controlled transactions (UAH 150 million income and UAH 10 million per counterparty), related persons, methods and the median rule, self-adjustment, report and group notice by 1 October, local file, master file (EUR 50 million), CbCR (EUR 750 million), fines (2026), PR #984 | checked against the law; awaiting merge |
| XB, cross-border | ua-cross-border: residence, non-residents, PE, art. 141.4 withholding and gross-up, treaty relief and residence certificates, foreign tax credits, CFC rules for companies and individuals, leaving Ukraine (2026), PR #986 | checked against the law; awaiting merge |

Other skills in the pack, outside the seven tax domains: ua-tax-overview (country map; 2026 rewrite in PR #974), ua-tax-optimization, ua-formation, ua-bookkeeping, ua-einvoice, ua-financial-statements.

## Official sources

- Tax Code of Ukraine, Law No. 2755-VI, consolidated text with amendments to Law No. 4967-IX of 3 September 2026: https://zakon.rada.gov.ua/laws/show/2755-17 (read 2026-10-30 from the web.archive.org capture of 12 October 2026, https://web.archive.org/web/20261012050950/https://zakon.rada.gov.ua/laws/show/2755-17/print, because zakon.rada.gov.ua timed out from our network)
- Law "On the State Budget of Ukraine for 2026", No. 4695-IX of 3 December 2025, arts. 7 and 8: https://zakon.rada.gov.ua/laws/show/4695-20 (read 2026-10-30 from the web.archive.org capture of 4 January 2026)
- Cabinet of Ministers Resolution No. 1045 of 27 December 2017, list of states under TCU art. 39.2.1.2: https://zakon.rada.gov.ua/laws/show/1045-2017-п (document card read 2026-10-30 from the web.archive.org capture of 14 October 2026)
- State Tax Service of Ukraine: https://tax.gov.ua (refused automated access on 2026-10-30)
