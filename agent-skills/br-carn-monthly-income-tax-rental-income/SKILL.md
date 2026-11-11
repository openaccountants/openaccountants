---
name: br-carn-monthly-income-tax-rental-income
description: "Brazil calendar 2026 rental income received by a resident individual from an individual tenant: identify the taxable recipient and receipt month, establish rental-specific exclusions, allocate co-owned or marital-property rent and prepare Carnê-Leão Web records. Covers an estate agency collecting for an individual tenant, subletting, registered usufruct, tenant improvements offset against rent and judicial release. Load the shared monthly computation and payment owner for current IRPF bands, legal versus simplified deductions, the separate reduction and ordinary late charges. Trigger on aluguel, locador, locatário, imobiliária, sublocação, usufruto, condomínio, comunhão and rental Carnê-Leão. Includes two rental computations and annual handoff; specialist foreign, nonresident, entity and disputed-assessment components remain separate."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/br-carn-monthly-income-tax-rental-income"
  jurisdiction: "BR"
  tax_year: "2026"
  last_updated: "2026-11-11"
---

# Brazil individual rental income and Carnê-Leão, 2026 v0.1

> **General reference only.** This Guide is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

**Quick answer.** A Brazilian-resident individual receiving taxable rent from an individual tenant ordinarily brings that rent into Carnê-Leão in the tenant's payment month, including payment to an administrator. Establish the actual taxable owner or usufructuary, gross receipt and permitted rental exclusions first. Keep gross rent and exclusions separately in the Web records, then send the resulting taxable rental receipt and the taxpayer's other relevant monthly receipts to [br-estimated-tax](br-estimated-tax.md). That Guide owns the shared current monthly table, deduction comparison, separate reduction, payment and ordinary late-charge computation. This Guide owns the rental-specific facts and exclusions; it does not maintain a competing general rates card. [RFB scope](https://www.gov.br/receitafederal/pt-br/assuntos/meu-imposto-de-renda/pagamento/carne-leao); [RFB rental rules](https://www.gov.br/receitafederal/pt-br/assuntos/meu-imposto-de-renda/pagamento/carne-leao/rendimentos).

## Who this applies to

Calendar 2026 rent received by an individual resident in Brazil from an individual tenant, including a property administrator collecting it. Identify the tenant rather than treating the administrator's legal form as the payer's tax classification. If the tenant is a company, use the legal-entity/withholding route and the annual owner, not a second Carnê-Leão calculation for that receipt. RIR art.688 expressly places rent paid by a legal entity to an individual in the source-withholding route. Salary taxed at source is not another Carnê-Leão receipt. [RFB agency guidance](https://www.gov.br/receitafederal/pt-br/assuntos/meu-imposto-de-renda/malha-fiscal/antecipacao/rendimentos-recebidos-de-empresa/recebo-alugueis-de-uma-imobiliaria); [RIR688](https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/decreto/d9580.htm); [RFB scope](https://www.gov.br/receitafederal/pt-br/assuntos/meu-imposto-de-renda/pagamento/carne-leao).

The rental variants below retain their own conditions. A bank account receiving all the money does not by itself decide beneficial ownership. Use the property documents, contract and actual rights. Nonresident/departure and foreign-property or foreign-tax components go to [brazil-cross-border-tax](brazil-cross-border-tax.md) with the monthly owner. A company or activity treated as an entity needs [brazil-corporate-tax](brazil-corporate-tax.md). Continue confirmed resident-rental components while identifying the separate unresolved branch.

## Rates, bands and thresholds

| Rental decision | Rule and conditions | Official source |
|---|---|---|
| Property held in condominium by several people | Allocate the individual-tenant rent in the proportion belonging to each, according to the contractual clause. Do not assume equal shares merely because a single administrator collects it | [RFB, Imóvel em condomínio](https://www.gov.br/receitafederal/pt-br/assuntos/meu-imposto-de-renda/pagamento/carne-leao/rendimentos) |
| Property in marital communion | Tax 50% in each spouse's name or, optionally, the whole in one spouse's name. Establish that it is common property and reconcile the choice with the actual monthly and annual records | [RFB, Imóvel em comunhão](https://www.gov.br/receitafederal/pt-br/assuntos/meu-imposto-de-renda/pagamento/carne-leao/rendimentos) |
| Usufruct | Individual-tenant rent is the usufructuary's Carnê-Leão receipt when the public usufruct deed is registered. Without a registered deed, the owner is taxable; preserve the property/beneficiary disclosure described below | [RFB, Usufruto](https://www.gov.br/receitafederal/pt-br/assuntos/meu-imposto-de-renda/pagamento/carne-leao/rendimentos) |
| Shared monthly table, reduction and personal deductions | Load br-estimated-tax for all bands, rates, current dependent/simplified limits, the legal/simplified comparison and the distinct reduction. Its taxable-earnings input is before personal deductions; the rental exclusions below are separately excluded from rental gross income | [RFB 2026 monthly table/reduction](https://www.gov.br/receitafederal/pt-br/assuntos/meu-imposto-de-renda/tabelas/2026); [RIR art.42](https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/decreto/d9580.htm); [Lei 15.270 art.3-A](https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2025/lei/l15270.htm) |
| Annual limits and special pension exemption | Annual dependent, education and simplified limits, annual reduction and minimum-tax interaction belong to br-income-tax. A pension-specific older-person exemption is not an exemption for rent | [RFB 2026 table, distinct monthly pension and annual sections](https://www.gov.br/receitafederal/pt-br/assuntos/meu-imposto-de-renda/tabelas/2026) |

## The base

### Identify recipient and receipt month

Use the tenant's payment to the owner **or administrator** as the receipt date. Delayed remittance, failure to notify the landlord or the administrator appropriating the money does not move that receipt to a later month. Unpaid contractual rent is distinct from money actually received. A rent amount deposited in court enters Carnê-Leão when released by the judicial authority. [RFB, Data do pagamento and Aluguel depositado judicialmente](https://www.gov.br/receitafederal/pt-br/assuntos/meu-imposto-de-renda/pagamento/carne-leao/rendimentos).

For a registered usufruct, the bare owner's asset declaration identifies the usufruct in favour of the beneficiary. Without a registered deed, the owner reports the property, indicates the income was donated to the beneficiary and remains the rental-income taxpayer under the cited guidance. Any separate gift-tax consequences need their own facts and source work. Condominium proportions and marital-property choices identify whose monthly calculation receives the rent; reconcile the corresponding expenses and do not deduct the same invoice for both people. [RFB, Usufruto/Imóvel em condomínio/Imóvel em comunhão](https://www.gov.br/receitafederal/pt-br/assuntos/meu-imposto-de-renda/pagamento/carne-leao/rendimentos).

### Gross rent and rental-specific exclusions

Include tenant-paid improvements in the month's rent when the lease allows their cost to offset rent due. Do not include every tenant improvement automatically: RIR art.45 distinguishes improvements that contractually compensate the owner from those that do not. Retain the contract, value and offset evidence, not just the smaller cash remittance. Lease premiums, key money and other use/occupation receipts can also be rental income; classify their actual terms. [RFB, Benfeitorias/Luvas](https://www.gov.br/receitafederal/pt-br/assuntos/meu-imposto-de-renda/pagamento/carne-leao/rendimentos); [RIR arts.41 and 45, including §3](https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/decreto/d9580.htm).

From rent received, exclude the following amounts **when the burden was exclusively the landlord's**. Retain proof of the charge, payment, property and any tenant reimbursement. [RFB rental exclusions](https://www.gov.br/receitafederal/pt-br/assuntos/meu-imposto-de-renda/pagamento/carne-leao/rendimentos); [RIR art.42](https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/decreto/d9580.htm).

| Exclusion | Apply only within this scope | Official source |
|---|---|---|
| Property taxes, fees and emoluments | Must concern the property producing the rent. A label such as maintenance fee does not make a private charge a tax | [RFB exclusions and Q445](https://www.gov.br/receitafederal/pt-br/centrais-de-conteudo/publicacoes/perguntas-e-respostas/dirpf/p-r-irpf-2026-v1-00-2026-04-23.pdf); [RIR art.42 I](https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/decreto/d9580.htm) |
| Rent paid for the property being sublet | Deduct the rent paid onward to that property's owner from qualifying individual-tenant sublet income. Rent paid for the taxpayer's separate personal home is not this exclusion | [RFB, Sublocação](https://www.gov.br/receitafederal/pt-br/assuntos/meu-imposto-de-renda/pagamento/carne-leao/rendimentos); [RFB Q448](https://www.gov.br/receitafederal/pt-br/centrais-de-conteudo/publicacoes/perguntas-e-respostas/dirpf/p-r-irpf-2026-v1-00-2026-04-23.pdf) |
| Collection or receipt costs | Paid costs to collect or receive this rent, including the properly supported administrator's fee. A statement's net bank payment still needs reconciliation to gross rent and this exclusion | [RFB agency guidance](https://www.gov.br/receitafederal/pt-br/assuntos/meu-imposto-de-renda/malha-fiscal/antecipacao/rendimentos-recebidos-de-empresa/recebo-alugueis-de-uma-imobiliaria); [RIR art.42 III](https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/decreto/d9580.htm) |
| Condominium expenses | Actual qualifying landlord-borne condominium charges, with the relevant property/payment evidence. Do not turn every improvement or owners' association charge into a condominium exclusion | [RFB exclusions/Q445](https://www.gov.br/receitafederal/pt-br/assuntos/meu-imposto-de-renda/pagamento/carne-leao/rendimentos); [RFB Q445](https://www.gov.br/receitafederal/pt-br/centrais-de-conteudo/publicacoes/perguntas-e-respostas/dirpf/p-r-irpf-2026-v1-00-2026-04-23.pdf) |

The full exclusion list is now read. It is not a general deduction for mortgage capital, depreciation, repairs or every letting-related expense. Q447 denies the stated eviction-lawyer and pre-letting renovation expenses; Q445 excludes the listed separately charged cleaning, parking, pet and similar fees from allowable exclusions and rejects the owners' association maintenance fee. Use actual classification rather than a blanket percentage of rent. Rental income cannot use Livro Caixa; a person's separate eligible professional activity needs its own records and the monthly owner. [RFB Q445/447](https://www.gov.br/receitafederal/pt-br/centrais-de-conteudo/publicacoes/perguntas-e-respostas/dirpf/p-r-irpf-2026-v1-00-2026-04-23.pdf); [RFB deductions, Livro Caixa restriction](https://www.gov.br/receitafederal/pt-br/assuntos/meu-imposto-de-renda/pagamento/carne-leao/deducoes).

Maintain an IPTU paid/used/available schedule for the rental property. Q446's expressly calendar-2025 illustrations allow landlord-paid IPTU within the rental-income year, whether paid at once or in instalments, to be used against that year's rental receipts, tracking the remaining paid balance and excluding unpaid instalments. They illustrate allocation, not a current tax band or authority to carry an unused balance into another year. Apply the current monthly owner's table to the actual 2026 receipts. Other cross-month expense categories or a claimed rental loss require the specific rule before creating a carry. [RFB Q446, used only for its stated IPTU method](https://www.gov.br/receitafederal/pt-br/centrais-de-conteudo/publicacoes/perguntas-e-respostas/dirpf/p-r-irpf-2026-v1-00-2026-04-23.pdf).

### Shared monthly computation and annual handoff

Keep `gross_rent`, `taxable_non_cash_rent`, each `rental_exclusion`, actual ownership allocation and `taxable_rental_receipt` separately. Rental exclusions under RIR art.42 are not the monthly personal deductions exchanged for the simplified alternative. Send the taxable rental receipt, other qualifying monthly receipts and supported personal-deduction facts to br-estimated-tax. Do not run a separate table for each property or ignore another relevant receipt because this rent alone is small. Do not subtract administration fees both from the statement net amount and again as an exclusion. [RIR art.42](https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/decreto/d9580.htm); [RFB payment calculation](https://www.gov.br/receitafederal/pt-br/assuntos/meu-imposto-de-renda/pagamento/carne-leao/pagar).

Official social-security contributions, qualified dependants and qualifying family-law alimony can enter the legal-deduction package only within their actual conditions and without reuse against withholding income. The simplified alternative replaces that personal package; it is not stacked with it. Medical/education annual deductions and the pension-specific exemption are not invented monthly rent deductions. Private-pension annual treatment is not an unrestricted monthly rental deduction: Lei9.250 art.4§1 limits its monthly application to the stated employment/administrator or pension circumstances. Use the monthly owner's complete comparison and the annual owner's separate annual choice. [RFB deductions](https://www.gov.br/receitafederal/pt-br/assuntos/meu-imposto-de-renda/pagamento/carne-leao/deducoes); [Lei9.250 art.4 §§1–2](https://www2.camara.leg.br/legin/fed/lei/1995/lei-9250-26-dezembro-1995-362566-normaatualizada-pl.html).

## Deadlines and filing

1. Use the official [Apurar carnê-leão service](https://www.gov.br/pt-br/servicos/apurar-carne-leao) and its current authorised GOV.BR route. Configure the actual calendar year and whether the person really has autonomous-work or foreign items. Rental alone does not justify enabling a professional Livro Caixa.
2. In the current manual's **Rendimentos** entry, select the actual rental nature, receipt date, source and history; provide payer/beneficiary identity where required. Enter gross rent and its rental exclusion/deduction separately. The system calculates net rental income. Preserve the administrator's gross-to-net reconciliation and property/recipient trail.
3. Maintain eligible personal deductions and actual dependants. Changing the Identificação dependant count also requires the monthly Demonstrativo counts to be checked. Optional import into someone else's return requires that person's CPF authorisation and the taxpayer actually being their dependant; it is not an unrestricted sharing instruction.
4. Review the **Demonstrativo de Apuração**, its monthly details, exclusions, personal-deduction choice and reduction. Save the resulting records. If importing escrituração, follow the current official layout and analyse errors: imported rows are added, so reconcile duplicates and partial/rejected rows rather than re-importing blindly. This Guide does not certify a taxpayer's actual portal session or submit anything.
5. Generate supported **DARF 0190** and use br-estimated-tax for the actual due date, minimum-payment accumulation and ordinary late charges. Ordinary payment is due by the last business day of the following receipt month. Preserve the actual assessment period, CPF, principal, maturity, reference-field treatment, charges and receipt. The shared owner covers the small-balance rule and named-field/reference treatment. The former numbered-field layout is not certified against an actual current generated DARF. A generated DARF is not proof it was paid. From calendar 2026 the current manual prohibits manually adding “Imposto Pago”; confirmed payments are imported from Receita's systems. Reconcile any delay or mismatch with the actual payment record.
6. Reconcile the year to [br-income-tax](br-income-tax.md) and [br-return-assembly](br-return-assembly.md). The current MIR describes recovery of Carnê-Leão data when starting the return; verify the actual exercise's service availability. Monthly **paid principal** is the advance credit, excluding mora/interest. Reconcile gross rent/exclusions, recipient choice, other income, imported principal and outstanding debts; monthly zero tax does not establish annual zero tax. The current MIR also warns imported alimony data are informational and require their actual annual payment entries. Complete exercise-2027 filing thresholds/calendar/screens remain with the annual owners, not assumed from the exercise-2026 manual.

These steps use the current [Carnê-Leão manual](https://www.gov.br/receitafederal/pt-br/assuntos/meu-imposto-de-renda/pagamento/carne-leao/manual), [payment page](https://www.gov.br/receitafederal/pt-br/assuntos/meu-imposto-de-renda/pagamento/carne-leao/pagar) and [MIR Carnê-Leão/deduction sections](https://www.gov.br/receitafederal/pt-br/assuntos/meu-imposto-de-renda/preenchimento/manual-mir/pagamentos-ou-doacoes/despesas-dedutiveis). Neither this workflow nor the intake/assembly routes grant authority to file, pay or elect for a person.

## Penalties and interest

Use br-estimated-tax's current Lei9.430 art.61 computation for ordinary mora and SELIC, with the actual maturity, payment date and official calculation. Do not restore the older payment page's “first business day” wording over the statute's first day after maturity. The old daily rate, cap, minimum DARF and interest-month rules remain at that shared owner; this rental Guide does not create a competing formula. [Lei9.430 art.61](https://www2.camara.leg.br/legin/fed/lei/1996/lei-9430-27-dezembro-1996-367738-normaatualizada-pl.html).

Separately, Lei9.430 art.44 II(a) provides an **isolated assessed fine of 50% of the omitted mandatory monthly payment**, even if the annual adjustment finds no tax payable. This is an assessment rule, not a routine instruction to add 50% to every voluntary late DARF. The actual assessment, procedural position, reductions and any interaction with another penalty need case-specific review. Continue the supported rental/principal reconciliation while isolating that dispute. [Current statutory text, art.44 caput/II(a) and neighbouring paragraphs](https://www2.camara.leg.br/legin/fed/lei/1996/lei-9430-27-dezembro-1996-367738-normaatualizada-pl.html).

## Cross-border points

Resident status, departure, foreign property/source, actual currency dates and foreign-tax evidence can change the result. Foreign tax is not an unrestricted deduction from rent: the manual has a separate monthly foreign-credit limit and same-year excess tracking. Route that calculation to br-estimated-tax with brazil-cross-border-tax; confirm treaty/reciprocity and the actual foreign tax before any credit. Nonresident Brazilian-source rent follows its proper withholding route. This reference does not certify a particular treaty or nonresident calculation. [RFB foreign-income/residence sections](https://www.gov.br/receitafederal/pt-br/assuntos/meu-imposto-de-renda/pagamento/carne-leao/rendimentos); [manual, Compensação de imposto pago no exterior](https://www.gov.br/receitafederal/pt-br/assuntos/meu-imposto-de-renda/pagamento/carne-leao/manual).

## Two worked examples that recompute

These fictional cases show rental-specific inputs followed by the **shared** 2026 calculation. They are not rate cards or approved returns. The example coefficients and deduction/reduction values are from the [RFB 2026 monthly table](https://www.gov.br/receitafederal/pt-br/assuntos/meu-imposto-de-renda/tabelas/2026) and [Lei15.270 art.3-A](https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2025/lei/l15270.htm). In both, the individual has no other qualifying monthly receipts, personal legal deductions, foreign credit or small-balance carry. Actual other income or deductions require a new comparison.

### Case 1: administrator receives before remitting

Assume an individual tenant pays 6,000 to the administrator in January. The administrator remits in February. Supported landlord-only charges are administration 300, property tax 200 and condominium 500. January gross rent is 6,000; exclusions are 1,000; taxable rental receipt is 5,000. The simplified personal alternative is 607.20, giving base 4,392.80. Table tax is 312.89 and the distinct reduction is capped at that tax, leaving zero monthly principal. Do not shift receipt to February or deduce the same fees again. Annual results remain separate. [RFB receipt/exclusions](https://www.gov.br/receitafederal/pt-br/assuntos/meu-imposto-de-renda/pagamento/carne-leao/rendimentos).

```oa-check
name: BR rental agency receipt and separate personal deduction
inputs:
  gross_rent: 6000
  administration: 300
  property_tax: 200
  condominium: 500
  simplified: 607.20
steps:
  - rental_exclusions: administration + property_tax + condominium
  - taxable_rental: gross_rent - rental_exclusions
  - personal_base: taxable_rental - simplified
  - table_tax: round(max(0, personal_base * 0.225 - 675.49), 2)
  - reduction: min(table_tax, 312.89)
  - principal: table_tax - reduction
expected:
  rental_exclusions: 1000
  taxable_rental: 5000
  personal_base: 4392.80
  table_tax: 312.89
  principal: 0
```

### Case 2: sublet rent and collection costs

Assume individual subtenants pay 10,000 in the month. The sublessor pays 3,000 rent to the owner of that same property, collection costs 500 and qualifying landlord-borne condominium expenses 500, all supported and not reimbursed. Rental exclusions total 4,000 and taxable rental receipt is 6,000. With the stipulated personal facts above, the simplified base is 5,392.80; table tax 574.29 less the separate reduction 179.75 gives principal 394.54. A separate personal-home rent payment would not be an exclusion. [RFB sublet/exclusion rules](https://www.gov.br/receitafederal/pt-br/assuntos/meu-imposto-de-renda/pagamento/carne-leao/rendimentos); [Q448](https://www.gov.br/receitafederal/pt-br/centrais-de-conteudo/publicacoes/perguntas-e-respostas/dirpf/p-r-irpf-2026-v1-00-2026-04-23.pdf).

```oa-check
name: BR rental subletting exclusions and shared monthly reduction
inputs:
  subrent: 10000
  owner_rent: 3000
  collection_cost: 500
  condominium: 500
  simplified: 607.20
steps:
  - rental_exclusions: owner_rent + collection_cost + condominium
  - taxable_rental: subrent - rental_exclusions
  - personal_base: taxable_rental - simplified
  - table_tax: round(max(0, personal_base * 0.275 - 908.73), 2)
  - reduction: round(978.62 - 0.133145 * taxable_rental, 2)
  - principal: round(max(0, table_tax - min(table_tax, reduction)), 2)
expected:
  rental_exclusions: 4000
  taxable_rental: 6000
  personal_base: 5392.80
  table_tax: 574.29
  reduction: 179.75
  principal: 394.54
```

### Boundary checks

| Facts | Required treatment | Official source |
|---|---|---|
| Company tenant, individual landlord, agency intermediary | Keep legal-entity income/withholding route; the administrator does not turn it into individual-tenant Carnê-Leão | [RFB agency guidance](https://www.gov.br/receitafederal/pt-br/assuntos/meu-imposto-de-renda/malha-fiscal/antecipacao/rendimentos-recebidos-de-empresa/recebo-alugueis-de-uma-imobiliaria) |
| Tenant funds remain in court | Check judicial release before assigning a monthly receipt | [RFB judicial deposit rule](https://www.gov.br/receitafederal/pt-br/assuntos/meu-imposto-de-renda/pagamento/carne-leao/rendimentos) |
| Two contractual co-owners versus marital common property | Use actual contractual proportions for condominium; only the separate marital-common-property rule supplies the spouse allocation/election | [RFB ownership headings](https://www.gov.br/receitafederal/pt-br/assuntos/meu-imposto-de-renda/pagamento/carne-leao/rendimentos) |
| Tenant reimburses the charged expense or landlord claims it twice | Reconcile the actual burden and exclusion once; do not assume the landlord-only condition | [RFB exclusion condition](https://www.gov.br/receitafederal/pt-br/assuntos/meu-imposto-de-renda/pagamento/carne-leao/rendimentos) |
| Tenant improves the property without contractual rent offset | Do not assume every improvement is rent; distinguish RIR45§3 from its contractual-offset rule | [RIR45 IV/§3](https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/decreto/d9580.htm) |
| Monthly principal zero, or annual liability zero | Continue annual aggregation and unpaid-month/assessment checks; neither implies all obligations disappear | [MIR Carnê-Leão](https://www.gov.br/receitafederal/pt-br/assuntos/meu-imposto-de-renda/preenchimento/manual-mir/pagamentos-ou-doacoes/despesas-dedutiveis); [Lei9.430 art.44 II(a)](https://www2.camara.leg.br/legin/fed/lei/1996/lei-9430-27-dezembro-1996-367738-normaatualizada-pl.html) |

## Ask the client first

Read the existing file and supporting records before asking. Request only consequential missing facts:

- Residence/entry/departure dates and actual tenant identity, with contracts and amendments.
- Each property's ownership, marital-property regime and choice, or registered usufruct deed; distinguish the recipient from the collection account.
- Tenant-to-owner/administrator payment dates and gross statements, cash/noncash rent offsets, judicial deposit/release documents and remittance reconciliation.
- Each landlord-only charge, who paid it, reimbursements, sublet-to-owner rent and the IPTU paid/used balance.
- Other monthly receipts, supported personal deductions already used against withholding, qualifying dependants and the comparison with the simplified alternative.
- Existing Web records, actual principal payments/receipts, arrears/assessment notices and annual imports or amendments.

## When to refuse or refer

Do not guess recipient, receipt month, exclusion entitlement, monthly deduction or payment credit. Continue established components and isolate unsupported items. Company tenants need the withholding/annual route; nonresidents, foreign receipts/credits and departure require the cross-border/monthly owners; business/entity equivalence requires the company owner. High-income minimum IRPF and the annual reduction/choice belong to br-income-tax. Arrears use the ordinary monthly payment owner; an actual assessment or disputed isolated penalty needs professional review. Consumption-tax consequences are a separate [brazil-vat](brazil-vat.md) component and do not replace this personal-income calculation.

Find the Guide library and professional-review route at [OpenAccountants](https://www.openaccountants.com). Check the displayed year, version and actual review state. Drafted by OpenAccountants. Not yet reviewed or approved by a named accountant.

## Sources

Actually read on 2026-11-11: the named original portions below. Current Receita rental, deduction and manual content was also rendered in a real browser. The former general orientation URL redirected to a restricted login page; it supplies no current evidence here. Existing cached official statutes/PDFs were read as actual originals, not search snippets. The IRPF exercise-2026 PDF concerns calendar2025; its named rental interpretations/illustrations are distinguished from current2026 table values. No complete exercise2027 filing calendar or portal operation is certified.

| Source / actual portions read | Official URL | Read date |
|---|---|---|
| Read for this Guide: Current Carnê-Leão definition, resident/PF/foreign scope, source-taxed receipts excluded | https://www.gov.br/receitafederal/pt-br/assuntos/meu-imposto-de-renda/pagamento/carne-leao | 2026-11-11 |
| Read for this Guide: Rendimentos: complete rental/arrendamento paragraphs, date, all exclusions, usufruct, improvements, sublet, ownership and judicial release; foreign/residence paragraphs for referral only | https://www.gov.br/receitafederal/pt-br/assuntos/meu-imposto-de-renda/pagamento/carne-leao/rendimentos | 2026-11-11 |
| Read for this Guide: Deductions: initial legal package, no duplicate withholding use, Livro Caixa restriction; other professional-expense material not applied to rent | https://www.gov.br/receitafederal/pt-br/assuntos/meu-imposto-de-renda/pagamento/carne-leao/deducoes | 2026-11-11 |
| Read for this Guide: Agency guidance: PF/PJ tenant distinction, administrator-fee reconciliation and assessment evidence | https://www.gov.br/receitafederal/pt-br/assuntos/meu-imposto-de-renda/malha-fiscal/antecipacao/rendimentos-recebidos-de-empresa/recebo-alugueis-de-uma-imobiliaria | 2026-11-11 |
| Read for this Guide: RIR2018 arts.41–45 and688–689: rent, exclusions, receipt, contractual improvements; cached actual original, not its obsolete tables | https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/decreto/d9580.htm | 2026-11-11 |
| Read for this Guide: RFB original IRPF2026 Q445–448: exclusion limits, same-year IPTU illustrations, eviction/renovation and personal-home rent limits; calendar2025 examples, no2025 tax table adopted | https://www.gov.br/receitafederal/pt-br/centrais-de-conteudo/publicacoes/perguntas-e-respostas/dirpf/p-r-irpf-2026-v1-00-2026-04-23.pdf | 2026-11-11 |
| Read for this Guide: Current2026 monthly table/reduction and annual/pension headings, used to check owner boundary and both example coefficients | https://www.gov.br/receitafederal/pt-br/assuntos/meu-imposto-de-renda/tabelas/2026 | 2026-11-11 |
| Read for this Guide: Lei9.250 art.4, including monthly private-pension scope and simplified alternative; cached Câmara current compilation | https://www2.camara.leg.br/legin/fed/lei/1995/lei-9250-26-dezembro-1995-362566-normaatualizada-pl.html | 2026-11-11 |
| Read for this Guide: Lei15.270 adding art.3-A, caput/table/§§1–3: separate2026 reduction; annual provisions read for owner boundary only | https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2025/lei/l15270.htm | 2026-11-11 |
| Read for this Guide: Current manual: configuration/identification, rental receipt fields, payments including2026 import, Demonstrativo, foreign-credit display and escrituração safeguards | https://www.gov.br/receitafederal/pt-br/assuntos/meu-imposto-de-renda/pagamento/carne-leao/manual | 2026-11-11 |
| Read for this Guide: Current payment page: aggregation, deadline,0190/reference/principal/total and small-balance route; statutory mora wording controls its older shorthand | https://www.gov.br/receitafederal/pt-br/assuntos/meu-imposto-de-renda/pagamento/carne-leao/pagar | 2026-11-11 |
| Read for this Guide: MIR Carnê-Leão and deduction opening sections: actual paid principal, recovery, alimony-entry warning; not a whole-MIR reading | https://www.gov.br/receitafederal/pt-br/assuntos/meu-imposto-de-renda/preenchimento/manual-mir/pagamentos-ou-doacoes/despesas-dedutiveis | 2026-11-11 |
| Read for this Guide: Official service identity/access route only, not authenticated taxpayer operation | https://www.gov.br/pt-br/servicos/apurar-carne-leao | 2026-11-11 |
| Read for this Guide: Current Lei9.430 arts.44/61 with neighbouring assessment conditions: isolated fine distinct from ordinary mora; fresh Câmara44 and cached original61 read | https://www2.camara.leg.br/legin/fed/lei/1996/lei-9430-27-dezembro-1996-367738-normaatualizada-pl.html | 2026-11-11 |

Not yet confirmed: actual ownership/marital choice/registered usufruct, receipts and landlord-only burdens for a particular case; disputed allocation of expenses between owners, cross-month exclusions other than the stated IPTU illustration, negative rental amounts and any cross-year carry; special damages, gifts, rural/business/entity equivalence and nonresident/foreign-tax computations; actual portal permissions, payment matching and correction/amendment status; the former DARF field-number layout (code in04, reference in05 and principal/fine/interest mappings in07–09) against an actual current generated document; assessment-specific penalty reductions, cumulative-penalty disputes or relief; complete exercise2027 filing thresholds/calendar/screens and annual high-income interaction, which remain with the annual owners. No unresolved amount is assumed deductible, exempt, paid or professionally approved.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-11. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `br-carn-monthly-income-tax-rental-income` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/br-carn-monthly-income-tax-rental-income. If neither is available, confirm every figure against the official source pages cited above before relying on it.
