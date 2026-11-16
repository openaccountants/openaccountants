---
name: st-tax-overview
description: "Use this skill for tax year 2026 working papers in Sao Tome and Principe (STP, jurisdiction ST). It maps which taxes apply to a person or company, the authority, the currency, the main laws (IRS Law 17/2008 and 11/2009, IRC Law 16/2008 and 10/2009, the VAT Code of 2019, the General Tax Code Law 6/2007), the 2025 and 2026 Budget measures, and what could and could not be verified, then points to each skill in the pack. It says plainly which figures come from official texts and which remain held. Trigger phrases: Sao Tome tax, STP tax, Direccao dos Impostos, dobras, Sao Tome e Principe imposto, which taxes apply in Sao Tome. It is general reference for working papers, not for filing without review by a qualified professional in the country."
jurisdiction: ST
tax_year: 2026
last_updated: 2026-11-16
type: situation-rules
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
version: 0.3
category: international
tier: 2
domain: income-tax
---

# Sao Tome and Principe Tax Overview v0.3

> **Sourced from the law, in part.** Tax year 2026. The tax codes were read from the Ministry of Finance legacy site (ministerio.financas.st) and the Assembly's Diario. The newer Finance Ministry site (financas.gov.st) still refused access, so later amendments to the codes and the published 2026 Budget Law were not read on an official host. Held points sit on the `Not yet confirmed:` line. No accountant has signed this version.

## Who this applies to

Anyone needing a first map of the STP system: an individual (IRS), a company or other entity (IRC), a business making taxable supplies (VAT, called IVA), an employer (INSS and IRS withholding). The Direccao dos Impostos administers the internal taxes and the Autoridade Geral Aduaneira the customs duties, both under the Ministry of Economy and Finance ([Ministry presentation](https://www.britacom.org/zt/ThemeDay/Tenth/SEMINAR/202510/P020251021566751705880.pdf)).

Main laws, all read in part from official texts (see Sources):

- General Tax Code, Law 6/2007, published in Diario da Republica no. 18 of 15 May 2007.
- IRS code (personal income tax), Law 17/2008, first amended and republished by Law 11/2009 of 8 October 2009.
- IRC code (company income tax), Law 16/2008, first amended and republished by Law 10/2009 of 8 October 2009.
- VAT Code, approved by the law whose final text the Assembly published on 15 October 2019 (the pack calls it Law 13/2019, as the 2026 Budget Bill names it).
- Tax Process and Procedure Code, Law 7/2007 (the Ministry presentation names an amending Decree-Law 22/2026, not read); Investment Code, Law 7/2008 on the Ministry list, while the Ministry presentation cites Decree-Law 19/2016 as the Investment Code and Decree-Law 15/2016 as the Tax Benefits Code; Urban Property Contribution, Law 6/2008; Inheritance and Gift Tax Code, Law 8/2007; SISA transfer tax, Law 5/2007; vehicle tax, Decree-Law 13/93 (all listed on the [Ministry legislation page](https://ministerio.financas.st/index.php/publicacoes/documentos/category/69-legislacao)).

Tax year: the calendar year. The codes set annual returns "do ano seguinte" (of the following year) after a calendar year, and residence for IRS is tested on 31 December ([IRS code art. 36](https://ministerio.financas.st/phocadownload/Imposto/legislacao/Lei_N11_2009_Codigo_Imposto_Sobre_Rendimento_Pessoas_Singulares_IRS.pdf)). Currency: the dobra (Db). Amounts in the 2009 codes are printed in dobras before the later re-denomination; the conversion rule was not re-read, so convert them only after checking it.

## Rates, bands and thresholds

| Item | Amount / treatment | Tax year | Official source |
|---|---|---|---|
| VAT standard rate | 15%, see [VAT](st-vat-gst.md) | 2026 (2019 Code text; later amendments not read) | [VAT Code art. 16](https://www2.camara.leg.br/saotomeeprincipe/diarios-da-an/xi-legislatura-22-11-2018/ii-serie-a/2.a-sessao/DAN30-IIS.pdf) |
| VAT exemption regime limit | Turnover below Db 1,000,000 in the prior calendar year; see [VAT](st-vat-gst.md) | 2026 (2019 Code text) | [VAT Code art. 44(1)](https://www2.camara.leg.br/saotomeeprincipe/diarios-da-an/xi-legislatura-22-11-2018/ii-serie-a/2.a-sessao/DAN30-IIS.pdf) |
| Company tax general rate | 25%; see [company tax](st-corporate-income-tax.md) | 2009 code text, no later change found | [IRC code art. 81(1)](https://ministerio.financas.st/phocadownload/Imposto/legislacao/Lei_N10_2009%20_Codigo_Imposto_Sobre_Rendimento_Pessoas_Colectivas_IRC.pdf) |
| Minimum company tax | 2/1000 of turnover, at least 2400 dobras; see [company tax](st-corporate-income-tax.md) | 2026 | [debate of 11 Feb 2026, art. 8(10) as read and approved](https://www2.camara.leg.br/saotomeeprincipe/diarios-da-an/xii-legislatura-8-11-22-a-8-11-26/i-serie/7.a-sessao-legislativa/DAN13-IS.pdf) |
| Personal income tax bands | 0% to 25% annual table of 2009, in pre-redenomination dobras; see [income tax](st-income-tax.md). The 30% band of the 2024 Budget text is held | 2009 code text | [IRS Law 11/2009 art. 1, art. 66 table](https://ministerio.financas.st/phocadownload/Imposto/legislacao/Lei_N11_2009_Codigo_Imposto_Sobre_Rendimento_Pessoas_Singulares_IRS.pdf) |
| INSS | 6% employer and 4% employee in the official text; see [payroll](st-payroll-social.md), which owns these figures and the rate dispute | 2026 text | [REPSO art. 101(3)](https://inss.gov.st/assets/Leis/Lei_n_19_2022.pdf) |
| Environmental import tax, IEI | Levied on imports by weight or volume at customs clearance; rates per tariff chapter in the law | 2025, kept in the 2026 Bill | [2025 Budget Law 2/2025 art. 8(6)](https://ministerio.financas.st/phocadownload/Orcamento/oge/A-2025/Aprovado/lei%20oge2025.pdf) |
| Property, gifts, transfer, vehicles | Urban property tax Law 6/2008; inheritance and gifts Law 8/2007; SISA Law 5/2007; vehicles Decree-Law 13/93. Rates not read | 2026 | [Ministry legislation page](https://ministerio.financas.st/index.php/publicacoes/documentos/category/69-legislacao) |

## The base

See each skill for its base. Two points cut across the pack:

- **Budget power to amend by decree.** The 2026 Budget, as amended in the Assembly on 11 February 2026, lets the government amend by decree-law, within one year of the Budget entering into force, the customs tariff, the VAT Code, the excise (IEC) code and the IRS code, without creating new taxes ([art. 8(7) as amended](https://www2.camara.leg.br/saotomeeprincipe/diarios-da-an/xii-legislatura-8-11-22-a-8-11-26/i-serie/7.a-sessao-legislativa/DAN13-IS.pdf)). Any such decree overrides figures here; none was read.
- **Cash limit and billing software.** Taxpayers of IRC and IRS with organised accounts may not pay or receive Db 10,000 or more in cash, and turnover of Db 1,000,000 or more (or a duty to keep organised accounts) brings a duty to invoice through billing software ([2025 Budget Law arts. 8(12) and 9](https://ministerio.financas.st/phocadownload/Orcamento/oge/A-2025/Aprovado/lei%20oge2025.pdf); the same text is in the [2026 Budget Bill](https://www2.camara.leg.br/saotomeeprincipe/diarios-da-an/xii-legislatura-8-11-22-a-8-11-26/ii-serie/7.a-sessao-legislativa-1/DAN14-IIS.pdf) arts. 8(12) and 9, and the Assembly approved art. 9 unchanged on 11 February 2026). Detail in [company tax](st-corporate-income-tax.md).

## Deadlines and filing

| Duty | Deadline | Source |
|---|---|---|
| IRS annual return, Category A (employment) or D | During February of the following year | [IRS code art. 109(1)(b)](https://ministerio.financas.st/phocadownload/Imposto/legislacao/Lei_N11_2009_Codigo_Imposto_Sobre_Rendimento_Pessoas_Singulares_IRS.pdf) |
| IRS and IRC annual return, Group 1 (organised accounts) | By 30 April of the following year | IRS art. 109(1)(c); [IRC code art. 108(1)(b)](https://ministerio.financas.st/phocadownload/Imposto/legislacao/Lei_N10_2009%20_Codigo_Imposto_Sobre_Rendimento_Pessoas_Colectivas_IRC.pdf) |
| IRS and IRC annual return, Group 2 with simplified bookkeeping | During February of the following year | IRS art. 109(1)(d); IRC art. 108(1)(d) |
| Tax withheld on income | By the 10th of the following month | [IRS code art. 88(3)](https://ministerio.financas.st/phocadownload/Imposto/legislacao/Lei_N11_2009_Codigo_Imposto_Sobre_Rendimento_Pessoas_Singulares_IRS.pdf) |
| VAT monthly return and payment | By the last day of the following month, electronically | [VAT Code arts. 28(1), 37](https://www2.camara.leg.br/saotomeeprincipe/diarios-da-an/xi-legislatura-22-11-2018/ii-serie-a/2.a-sessao/DAN30-IIS.pdf) |
| INSS declaration and payment | By the 10th of the following month | [payroll](st-payroll-social.md) |

The older skill said personal returns were due by 31 March; the code read gives February or 30 April as above.

## Penalties and interest

Compensatory interest on late assessment runs daily at the Central Bank reference rate plus three percentage points a year ([General Tax Code art. 38](https://ministerio.financas.st/phocadownload/Imposto/legislacao/Lei_N6_2007_Lei_Que_Aprova_Codigo_Geral_Tributario.pdf)). Default interest on late payment is charged monthly at 1/6 of the Central Bank reference rate, a started month counting in full, for at most five years (General Tax Code arts. 53 and 54). Fines (multas) are in the General Tax Code and Tax Process Code; amounts not read. See each skill.

## Cross-border points

Residents of STP pay IRS and IRC on worldwide income and non-residents only on income from STP ([IRS code art. 35](https://ministerio.financas.st/phocadownload/Imposto/legislacao/Lei_N11_2009_Codigo_Imposto_Sobre_Rendimento_Pessoas_Singulares_IRS.pdf); [IRC code art. 4](https://ministerio.financas.st/phocadownload/Imposto/legislacao/Lei_N10_2009%20_Codigo_Imposto_Sobre_Rendimento_Pessoas_Colectivas_IRC.pdf)). Services bought by a taxable person from a non-resident without a permanent establishment are reverse-charged for VAT (see [VAT](st-vat-gst.md)). The environmental import tax (IEI) was created by the 2025 Budget Law art. 8(6) and the 2026 Bill keeps it ("É mantido"); its rates are set per customs tariff chapter. The older skill said the IEI first appeared in the 2026 Bill; the 2025 Law shows it already existed. Treaties: none read.

## Two worked examples that recompute

**Example 1.** A VAT line of Db 200,000 of standard-rated sales.

```oa-check
name: VAT line
inputs:
  sales: 200000
steps:
  - vat: sales * 0.15
expected:
  vat: 30000
```

**Example 2, decision on registration.** Prior-year turnover of Db 1,000,000 is not below the limit ("igual ou superior" excludes it from the exemption), so normal VAT applies; at Db 999,999 the exemption regime applies. The gap is one dobra.

```oa-check
name: Limit gap
inputs:
  limit: 1000000
  turnover: 999999
steps:
  - gap: limit - turnover
expected:
  gap: 1
```

## Ask the client first

- Person or company, and legal form (an SA or public company is always Group 1 and never on the VAT exemption regime)
- Resident or not (days in STP, home on 31 December, seat or effective management)
- Turnover in the last calendar year
- Whether organised accounts are kept
- Staff on payroll
- Activity (agriculture has a 50% exemption in both IRS and IRC)

## Sources

| Source | URL | Read on |
|---|---|---|
| IRS Law 11/2009 (Gazette no. 68, 8 Oct 2009): amending arts. 1 to 5 and republished code arts. 35, 36, 66, 69, 87 to 91, 108 to 113 read; art. 66 table checked on the rendered page | https://ministerio.financas.st/phocadownload/Imposto/legislacao/Lei_N11_2009_Codigo_Imposto_Sobre_Rendimento_Pessoas_Singulares_IRS.pdf | 2026-11-16 |
| IRC Law 10/2009 (Gazette no. 67, 8 Oct 2009), republished code arts. 2 to 4, 16 to 24, 52, 81 to 94, 107 to 108 read | https://ministerio.financas.st/phocadownload/Imposto/legislacao/Lei_N10_2009%20_Codigo_Imposto_Sobre_Rendimento_Pessoas_Colectivas_IRC.pdf | 2026-11-16 |
| General Tax Code, Law 6/2007, arts. 34 to 39 and 53 to 56 read | https://ministerio.financas.st/phocadownload/Imposto/legislacao/Lei_N6_2007_Lei_Que_Aprova_Codigo_Geral_Tributario.pdf | 2026-11-16 |
| Ministry of Finance legislation list (titles only) | https://ministerio.financas.st/index.php/publicacoes/documentos/category/69-legislacao | 2026-11-16 |
| 2025 Budget Law 2/2025 (Gazette no. 23, 16 May 2025), arts. 8 and 9 read (copy fetched 2026-11-15, sha256 fdcb13cc) | https://ministerio.financas.st/phocadownload/Orcamento/oge/A-2025/Aprovado/lei%20oge2025.pdf | 2026-11-16 |
| VAT Code final text, Assembly Diario II no. 30 of 15 Oct 2019, approving law arts. 1 to 6 and code arts. 16, 28, 37, 44 read (copy fetched 2026-11-15, sha256 dee8145b; the host answered 504 on 2026-11-16) | https://www2.camara.leg.br/saotomeeprincipe/diarios-da-an/xi-legislatura-22-11-2018/ii-serie-a/2.a-sessao/DAN30-IIS.pdf | 2026-11-16 |
| Assembly debate of 11 Feb 2026 on the 2026 Budget, art. 8 amendments and votes, pp. 315 to 321 read (copy fetched 2026-11-15, sha256 4a161493) | https://www2.camara.leg.br/saotomeeprincipe/diarios-da-an/xii-legislatura-8-11-22-a-8-11-26/i-serie/7.a-sessao-legislativa/DAN13-IS.pdf | 2026-11-16 |
| 2026 Budget Bill 51/XII/7.a/2025, arts. 8 and 9 read (copy fetched 2026-11-15, sha256 85eb8384) | https://www2.camara.leg.br/saotomeeprincipe/diarios-da-an/xii-legislatura-8-11-22-a-8-11-26/ii-serie/7.a-sessao-legislativa-1/DAN14-IIS.pdf | 2026-11-16 |
| Decree-Law 19/2022 consolidated text (INSS), art. 101(3) | https://inss.gov.st/assets/Leis/Lei_n_19_2022.pdf | 2026-11-01 |
| Ministry presentation of October 2025 on the tax administration (all pages read from the copy fetched 2026-11-15, sha256 8991e2ed; a presentation, not a statute) | https://www.britacom.org/zt/ThemeDay/Tenth/SEMINAR/202510/P020251021566751705880.pdf | 2026-11-16 |

The Assembly of Sao Tome and Principe publishes its Diario on www2.camara.leg.br, hosted by the Brazilian Chamber of Deputies; it is cited as the Assembly's own record. The Ministry presentation is hosted by the BRITACOM forum. The newer Finance Ministry site (financas.gov.st) answered 403 on 2026-11-16; the government gazette host dre.gov.st did not resolve on 2026-11-15.

Not yet confirmed: the published 2026 Budget Law (Law 3/2026) on an official host, and whether it matches the Bill as amended on 11 February 2026; any decree under the 2026 budget power; amendments to the IRS, IRC and VAT codes after the texts read (VAT Law 2/2023 and Decree-Law 12/2023 named in the 2026 Bill); the dobra re-denomination rule and the euro peg in 2026; the 30% IRS band (see income tax); IEI rates for 2026 (the 2025 Law prints food at "0,2 cêntimos de Dobra" per kilogram, the 2026 Bill "20 cêntimos de dobra"); fine amounts; treaties; Tax Directorate how-to pages.
