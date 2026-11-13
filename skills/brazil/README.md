---
jurisdiction: BR
applicable: [IT-IND, IT-CORP, VAT, SC, PR, TP, XB]
not_applicable: {}
covered_by:
  IT-IND: br-income-tax
  IT-CORP: brazil-corporate-tax
  VAT: brazil-vat
  SC: br-inss
  PR: brazil-payroll
  TP: brazil-transfer-pricing
  XB: brazil-cross-border-tax
partial:
  IT-IND: "Ordinary annual calculation is covered; complete exercise 2027 filing thresholds, calendar, software and some personal-income components remain unconfirmed."
  IT-CORP: "Ordinary IRPJ/CSLL calculations are covered; current ECF field mappings and return-penalty amounts remain unconfirmed."
  VAT: "Federal and ordinary local-tax methods are covered; several ordinary state, municipal and product rates and local returns remain unconfirmed."
  SC: "Individual-contributor methods are covered; complete mixed own-account/company procedures remain unconfirmed. Employee and employer payroll has a separate owner."
  PR: "Ordinary 2026 employee/employer payroll is published as an unapproved draft. Complete common termination, rubric-incidence and payment procedures remain partial."
  TP: "Current arm's-length methods and documentation tests are covered; Local File body-language rules and current ECF/RTC field mappings remain unconfirmed."
  XB: "Ordinary residence, withholding and foreign-income methods are covered; some non-dividend remittance codes/deadlines and the exercise 2027 departure procedure remain unconfirmed."
---

# Brazil: tax pack

For calendar 2026 work, choose the owner below and check the linked file's actual year, publication status and gaps. Listing an owner does not establish that every proposed update is published. Amounts are in Brazilian reais (BRL). Brazil has federal, state and municipal taxes; the consumption-tax transition requires the actual transaction, taxpayer regime, place and date. The owning Guides contain the rates, calculations, official sources and read dates. This index does not maintain a second rates table.

Calendar year and filing exercise are separate. The published exercise 2026 questions concern calendar 2025; they do not establish a complete exercise 2027 filing calendar or software. Use each owner's dated procedure and keep an unpublished or unsupported step visibly partial.

## Approval

Each Guide shows **Built from the law** and either **Approved by [name]** or **Not yet approved**. Check the linked Guide's actual approval record and the version it identifies before relying on a named accountant credit.

As checked on 11 November 2026, the existing [rental-income Guide](br-carn-monthly-income-tax-rental-income.md) has no named accountant approval; the [live OpenAccountants record](https://www.openaccountants.com/skills/br-carn-monthly-income-tax-rental-income) also reports it as not yet approved. Its narrower rental scope and stated gaps remain. The published [payroll Guide](brazil-payroll.md) now covers 2026 as **Not yet approved**. The [earlier version reviewed by Ariane Marrocos](https://github.com/openaccountants/openaccountants/blob/157f7d8be741c4c7347a88c8a2970b529d175741/skills/brazil/brazil-payroll.md) is preserved with its original attribution. That earlier approval does not cover the revised text.

## Domains

“Partial” means an ordinary branch, computation or filing step is missing or unconfirmed. It does not mean the whole taxpayer's work should be refused. Continue supported components and name the dependent gap. Specialist regimes listed below also need their own source work.

| Tax | Owning Guide and route | Status and ordinary limits |
|---|---|---|
| Income tax | [Annual IRPF](br-income-tax.md); [monthly Carnê-Leão](br-estimated-tax.md); [individual-tenant rental income](br-carn-monthly-income-tax-rental-income.md) | Not yet approved; partial annual procedure and some income/deduction components. The monthly Guide owns the shared current computation, table, reduction, payment and ordinary late-charge method. The rental Guide supplies only confirmed rental variants; unsupported rental deductions and procedures remain partial |
| Company tax | [IRPJ and CSLL](brazil-corporate-tax.md) | Not yet approved; ordinary lucro real/presumido methods. ECF fields and filing-penalty details remain partial |
| VAT or sales tax | [PIS/Cofins and CBS/IBS transition](brazil-vat.md); [ICMS, ISS and IPI](br-indirect-tax.md) | Not yet approved; separate federal and local owners. Actual local/product rates, return fields and some credit branches remain partial |
| Social contributions | [Individual-contributor INSS](br-inss.md); employee/employer contributions in [payroll](brazil-payroll.md) | Not yet approved; mixed-source procedures remain partial. INSS plan selection is distinct from a complete benefit-entitlement opinion |
| Payroll | [Employee and employer payroll](brazil-payroll.md) | Not yet approved; published 2026 source-cited draft. Ordinary termination, incidence, entitlement and payment procedures remain partial |
| Transfer pricing | [Controlled transactions and documentation](brazil-transfer-pricing.md) | Not yet approved; current methods and documentation decisions. Some ordinary filing/language details remain partial |
| Cross-border | [Residence, foreign income and outbound withholding](brazil-cross-border-tax.md) | Not yet approved; some payment/reporting codes, deadlines and departure procedure remain partial |

## Regional and local coverage

Start with the [authority and regional router](br-jurisdiction-router.md) when the answer depends on location. Identify the taxable event, period, establishment, UF, municipality or DF, product/service and regime. Keep a separate location decision for each event. IBGE macroregions are a geographic index; a state, a municipality and an incentive's statutory territory are different legal fields. The DF has state and municipal legislative powers and cannot be divided into municipalities ([Constitution arts. 18, 32 and 43](https://www2.camara.leg.br/legin/fed/consti/1988/constituicao-1988-5-outubro-1988-322142-normaatualizada-pl.html)).

| Local job | National method and regional owner | What the additional coverage establishes, and what it does not |
|---|---|---|
| Goods, ICMS and destination differences | [National ICMS/ISS/IPI method](br-indirect-tax.md) with [state tax profiles](br-state-tax-profiles.md) | A profile for each state and the DF, with ordinary internal-rate evidence, FCP conditions, interstate/DIFAL distinctions and local administrative routes. Read each field's own verification status. A jurisdiction listed in the matrix does not certify every product, substitute-tax agreement, exemption, credit or local return. An unresolved rate is not zero |
| Services and municipal property taxes | [National classification/place method](br-indirect-tax.md) with [municipal taxes](br-municipal-taxes.md) | Capital-city and DF routes, selected local legal profiles, service-place/retention decisions, operational procedures and property-tax branches. National NFS-e lookup records are kept separate from the governing local statute and its conditions. A platform value, a blank field or a capital-city example does not certify every municipality or service |
| Regional investment and shipment incentives | [Ordinary company tax](brazil-corporate-tax.md), [consumption taxes](brazil-vat.md) and [regional incentives](br-regional-incentives.md) | Separate SUDAM, SUDENE, ZFM, Western Amazon, ALC and Amazonas state-project decisions; project/operation conditions, eligible tax attribution, restricted reinvestment and shipment evidence. A regional address or SUFRAMA number alone is insufficient. Product PPBs, state-fund calculations, specialist coefficients and named operational branches remain partial |
| Employee salary input | [Regional payroll selection](br-regional-payroll.md), then [national payroll](brazil-payroll.md) | Date/occupation-specific SP, PR, SC and RS floors; applicable collective instruments; RJ's invalidated historical table; telework territory and salary-change evidence. This supplement selects salary inputs; the separate national payroll Guide owns the 2026 gross-to-net computation and remains Not yet approved. Other-UF absence/presence checks, current RJ consolidation and employer-specific instruments remain partial |

The regional owners supplement the national computation owners. Do not replace a national method with one local percentage or apply a later consumption-tax provision to an earlier period. When a government comparison table or platform differs from current law, preserve both dated records and resolve the provision, classification, date and conditions. Continue supported components and isolate the dependent gap.

The domain-level `partial` entries above remain in force. Neither adding these owners nor listing every UF closes the missing product, city, procedure or accountant-approval branches. Each regional Guide has its own official-source ledger, read scope and `Not yet confirmed:` line.

## Other Guides and preparation routes

| Job | Guide | Boundary |
|---|---|---|
| Choose the relevant taxing authority and territory | [Brazil regional router](br-jurisdiction-router.md) | Select only the national and local owners required by the event; geography does not itself grant a tax benefit or filing authority |
| Small-business regime, annexes, factor R, DAS and MEI | [Simples Nacional and MEI](br-simples-nacional.md) | Owns eligibility and unified-regime figures. Exact occupation, document exceptions and some current administrative provisions remain partial |
| Digital assets | [Crypto tax](brazil-crypto-tax.md) | Separate supported gains, foreign-financial and reporting routes. Ordinary basis/location branches remain partial; specialist cases are listed under Out of scope |
| Fiscal documents | [Electronic invoices](brazil-einvoice.md) | Model/date/version, fields, authorisation and evidence. Complete executable schemas, some local duties and provider capabilities are not certified |
| Collect and organise an existing record | [Freelance intake](br-freelance-intake.md) | Optional documented intake for PF/autônomo, MEI and Simples owners. Ask only for consequential missing facts; it is not mandatory for a single tax question |
| Assemble papers and next actions | [Return assembly](br-return-assembly.md) | Workbook or usable equivalent, reviewer brief and action calendar. Preserve missing components; preparation is not authority to file, pay or elect |
| Primary-source and investment-project catalogue | [References](references.md) | Official source routes and the retained investment-project identities. Project descriptions and licence identities do not certify current tax calculations, security or integration compatibility |

## What still needs doing

An earlier-year linked file still needs its applicable current-year update before use. Close the ordinary gaps declared in `partial` and in each Guide's Sources section before marking a dependent result complete. In particular, an annual calculation is not a complete issued exercise 2027 filing service, and an invoice amount is not automatically tax paid or an allowable credit. Retain the work and identify the source, fact or owner needed.

## Out of scope

Specialist work includes treaty-specific schedules and social-security agreements, controlled foreign entities/trusts, special corporate/financial regimes, complex transfer-pricing valuations, sector/product consumption-tax and special input-credit regimes, special-payer contribution procedures, and native staking, mining, NFT-creator and DeFi cases. These are specific components to research or refer; they do not replace the ordinary gap list.

Pack work remains tracked in [\[BR\] Complete the pack](https://github.com/openaccountants/openaccountants/issues/277).

## Official sources

These are entry points, not a claim that every page or provision has been checked for every case. The owning Guide states the portion read and its limitations.

| Source | Use and read record |
|---|---|
| [Receita Federal's exercise 2026 questions](https://www.gov.br/receitafederal/pt-br/centrais-de-conteudo/publicacoes/perguntas-e-respostas/dirpf/p-r-irpf-2026-v1-00-2026-04-23.pdf) | Cover checked 11 November 2026: exercise 2026/calendar 2025. Follow the annual/monthly owners for the requested year |
| [LC 123: Simples Nacional](https://www2.camara.leg.br/legin/fed/leicom/2006/leicomplementar-123-14-dezembro-2006-548099-normaatualizada-pl.html) | Relevant eligibility, regime and owner-income provisions read 11 November 2026; actual current administrative exceptions remain with the Simples owner |
| [LC 214: consumption-tax reform](https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp214.htm) | Relevant taxpayer/regime and transition provisions read 11 November 2026; this is not a whole-law reading claim |
| [Signed Joint Act 4](https://cgibs.gov.br/upload/arquivos/202607/31091735-20260730-16h30-ato-conjunto-rfb-cgibs-na-c2-ba-4-260731-090909.pdf) | Complete act read 11 November 2026. Use the invoice/VAT owners for model, regime and date conditions |
| [Current Constitution](https://www2.camara.leg.br/legin/fed/consti/1988/constituicao-1988-5-outubro-1988-322142-normaatualizada-pl.html) and [IBGE Grande Região definition](https://www.ibge.gov.br/apps/quadrogeografico/pdf/qg_2024_010_GrandReg.pdf) | Relevant constitutional structure, DF powers, regional measures and tax allocations, plus the geographic definition/delimitation, read 11 November 2026. Geography is not a common local rate or an incentive award |
| [Full source catalogue](references.md) | Further Receita, Banco Central and original-law routes; preserve the distinction between a source index and an operative calculation |

The linked Guides retain their own licence notices. Find the public library and professional-review options at [OpenAccountants](https://openaccountants.com). Review the actual taxpayer's evidence and unresolved components with a qualified professional before filing or taking a tax position.
