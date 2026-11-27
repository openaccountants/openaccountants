---
name: de-return-assembly
description: Assemble and reconcile the 2026 German self-employed return reviewer package from intake, VAT, income tax/EÜR, social contributions, trade tax and prepayment outputs. Full-year resident natural persons using EÜR only; unresolved inputs remain explicit holds.
version: 1.1
jurisdiction: DE
tax_year: 2026
last_updated: 2026-11-27
drafted_by: OpenAccountants
approved_by: pending
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
type: filing-howto
---

# Assembling a German freelancer's yearly tax return package

Assemble one reviewer package for **2026**, with a separate **2027** planning calendar. Keep the VAT, EÜR, income tax, social insurance, trade tax, credit and payment reconciliations visible. A missing computation is a hold, never zero. This Guide prepares documents for professional review; it does not transmit, sign or pay.

## Scope

One full-year German-resident natural person, one self-employed business, cash-basis profit under § 4(3) EStG. German residence or habitual abode establishes unlimited income-tax liability; full-year residence and one business are workflow restrictions ([§ 1 EStG](https://www.gesetze-im-internet.de/estg/__1.html)). Use EÜR only where there is no statutory bookkeeping/regular-accounts duty and no voluntary books and accounts; otherwise R-DE-6 applies ([§ 4(3) EStG](https://www.gesetze-im-internet.de/estg/__4.html)).

Retain the intake classification as Freiberufler or Gewerbetreibender, with its evidence; a job title or trade registration alone does not settle the classification ([§ 18 EStG](https://www.gesetze-im-internet.de/estg/__18.html), [§ 15(2) EStG](https://www.gesetze-im-internet.de/estg/__15.html)). Do not silently decide an `unsettled` field. Joint assessment needs both spouses' complete inputs; a splitting computation alone is not a complete joint return.

## Ask the client first

Read the intake, documents and existing answers first. Ask only for missing facts: filer/adviser and any tax-office demand; business classification; municipality and assessed multiplier; church membership, state and assessment; all other income; current prepayment notices; complete spouse information where relevant. Name the records already checked.

Use the intake's actual authority to prepare the package; invocation does not establish consent to file or pay. Continue authorised preparation without pacing questions. Preserve missing items, assumptions and source citations beside the affected output.

## The method, step by step

### 1. Read the intake contract

Read `tax_year` (must be 2026), `taxpayer.business_type`, `taxpayer.profit_method`, `taxpayer.vat_status`, `taxpayer.kirchensteuer`, `taxpayer.kirchensteuer_rate`, `vat.gesamtumsatz_prior_year`, `vat.gesamtumsatz_current_year`, `vat.ustva_period`, `vat.kleinunternehmer_waived`, `vat.dauerfristverlaengerung`, `vat.sondervorauszahlung`, `vat.vorsteuer_reclaimable`, `sozialversicherung.rentenversicherung.type`, `home_office.type`, `private_use.kfz_method`, `gewerbesteuer.applies`, `gewerbesteuer.hebesatz`, `gewerbesteuer.municipality`, `prior_year.festgesetzte_est`, `prior_year.gewinn`, `prior_year.afa_schedule`, `vorauszahlungen.*`, `open_flags`, `refusals_triggered`, `documents_received`.

Keep the intake enums and field names unchanged. `null` is unknown, not zero or false. `unsettled` business/VAT status, church rate, pension or home-office method remains flagged; show alternative worksheets only as provisional. Carry every intake flag into the brief. Missing prior depreciation schedules leave opening assets and total depreciation unresolved, rather than treating them as absent.

### 2. Run the content Guides in order

1. `germany-vat-return`: outstanding advance returns, annual VAT reconciliation, taxable/exempt/non-taxable turnover, recoverable/blocked VAT, extension and special-prepayment reconciliation.
2. `de-einkommensteuer-freelancer`: EÜR, asset/expense schedules, taxable-income computation, assessed income tax, solidarity surcharge and church tax. Historical `de-income-tax`, `germany-income-tax` and `de-self-employed-income-tax` references identify this step; do not invent a missing Guide.
3. `de-social-contributions`: health, care and pension reconciliation, contribution basis, certificate amounts, arrears/refunds and any KSK flag. Feed its supported deduction amounts back into income tax before finalising the assessment.
4. `de-trade-tax`: trade classification, adjusted trade income, base amount, municipality's tax and § 35 credit reconciliation; skip only after the non-trading position is supported. Uncertain classification remains held.
5. `de-estimated-tax`: paid advances and actual notices for 2027. No fallback division of assessed income tax by four.

Read each output's year, source, conditions, approval state and unresolved items. Upstream execution alone is not proof. If a Guide fails or has no supported result, continue assembling available schedules, mark the dependent totals **incomplete/non-usable**, and retain the exact gap for the reviewer. Never label that package ready to file.

### 3. Establish VAT status and filing period

These are domestic-business checks; they do not determine foreign/EU-wide scheme eligibility.

| Check | Operative condition | Official source |
| --- | --- | --- |
| Ordinary domestic small-business exemption | Previous-year Gesamtumsatz no more than EUR 25,000 **and** current-year Gesamtumsatz no more than EUR 100,000; no effective waiver | [§ 19(1), (3) UStG](https://www.gesetze-im-internet.de/ustg_1980/__19.html) |
| Start during the year | Current-year limit EUR 25,000; the receipt crossing the applicable current-year limit is already subject to ordinary taxation; earlier qualifying receipts remain exempt | [2026 EÜR instructions, Zeile 12](https://www.bundesfinanzministerium.de/Content/DE/Downloads/BMF_Schreiben/Steuerarten/Einkommensteuer/2026-09-01-anlage-EUER-2026.pdf?__blob=publicationFile&v=2) |
| Ordinary VAT advance-return period | Calendar quarter; monthly where previous-year VAT exceeds EUR 9,000. This is a VAT test, not turnover | [§ 18(2) UStG](https://www.gesetze-im-internet.de/ustg_1980/__18.html) |
| Release from advance returns/payments | Tax office **may** release where previous-year VAT is no more than EUR 2,000; obtain its decision | [§ 18(2) UStG](https://www.gesetze-im-internet.de/ustg_1980/__18.html) |

Gesamtumsatz uses received consideration and the statutory exclusions, including fixed-asset disposals and the specified exempt supplies; it is not automatically the EÜR receipts total. A waiver binds at least five calendar years. Qualifying domestic small businesses ordinarily have no § 18(1)–(4) declarations, but a tax-office demand and § 18(4a) duties remain; recipient VAT and taxable intra-EU acquisitions must not disappear ([§ 19(1)–(3), (6) UStG](https://www.gesetze-im-internet.de/ustg_1980/__19.html), [§ 18(4a) UStG](https://www.gesetze-im-internet.de/ustg_1980/__18.html)).

Startup filing-period rules, refund-surplus monthly elections, changes of VAT status, new vehicles, foreign small-business schemes and any uncertain recipient/acquisition liability: preserve the transactions and mark the affected filing treatment non-usable. Check this point with one of our partner accountants.

### 4. Perform all five reconciliations

**Cross-check 1: VAT turnover to EÜR receipts.** Build a bridge for cash versus invoice timing, VAT status, exemptions, asset disposals and private use. Do not force equality or accept an unexplained EUR 1 difference. EÜR receipts generally follow receipt timing; § 11 exceptions remain ([§ 11 EStG](https://www.gesetze-im-internet.de/estg/__11.html)). The following is the **2026** form mapping, not a 2025 fallback. Every row cites the [2026 EÜR form and instructions](https://www.bundesfinanzministerium.de/Content/DE/Downloads/BMF_Schreiben/Steuerarten/Einkommensteuer/2026-09-01-anlage-EUER-2026.pdf?__blob=publicationFile&v=2).

| Receipt | 2026 EÜR destination | Official source |
| --- | --- | --- |
| Qualifying Kleinunternehmer receipts | Zeile 12, gross actual receipts excluding amounts in Zeilen 18–22; Zeile 13 gives the specified non-taxable/excluded turnover information | [Form/instructions, Zeilen 12–13](https://www.bundesfinanzministerium.de/Content/DE/Downloads/BMF_Schreiben/Steuerarten/Einkommensteuer/2026-09-01-anlage-EUER-2026.pdf?__blob=publicationFile&v=2) |
| Ordinary taxable business receipts | Zeile 15, net; exclude zero-rate receipts and Zeilen 19–21 | [Instructions, Zeile 15](https://www.bundesfinanzministerium.de/Content/DE/Downloads/BMF_Schreiben/Steuerarten/Einkommensteuer/2026-09-01-anlage-EUER-2026.pdf?__blob=publicationFile&v=2) |
| Exempt, non-taxable, zero-rate or customer-liable § 13b receipts | Zeile 16, excluding Zeilen 19–21 | [Instructions, Zeile 16](https://www.bundesfinanzministerium.de/Content/DE/Downloads/BMF_Schreiben/Steuerarten/Einkommensteuer/2026-09-01-anlage-EUER-2026.pdf?__blob=publicationFile&v=2) |
| Received VAT and VAT on taxable withdrawals | Zeile 17: received VAT at receipt; withdrawal VAT when it arises | [Instructions, Zeile 17](https://www.bundesfinanzministerium.de/Content/DE/Downloads/BMF_Schreiben/Steuerarten/Einkommensteuer/2026-09-01-anlage-EUER-2026.pdf?__blob=publicationFile&v=2) |
| Tax-office VAT refunds/set-offs | Zeile 18; recurring prior-year refunds due **and** received within the first ten days belong to the prior year | [Instructions, Zeile 18](https://www.bundesfinanzministerium.de/Content/DE/Downloads/BMF_Schreiben/Steuerarten/Einkommensteuer/2026-09-01-anlage-EUER-2026.pdf?__blob=publicationFile&v=2) |
| Asset disposals/withdrawals; private car use; other withdrawals | Zeilen 19, 20, 21 respectively; withdrawal VAT remains separate in Zeile 17. Valuation must come from the supported computation | [Form/instructions, Zeilen 19–21](https://www.bundesfinanzministerium.de/Content/DE/Downloads/BMF_Schreiben/Steuerarten/Einkommensteuer/2026-09-01-anlage-EUER-2026.pdf?__blob=publicationFile&v=2) |
| Total receipts | Zeile 23, carried into Zeile 77; expense total Zeile 76 into Zeile 78; apply remaining adjustments through taxable profit/loss at Zeile 98 | [Form, pages 1–4](https://www.bundesfinanzministerium.de/Content/DE/Downloads/BMF_Schreiben/Steuerarten/Einkommensteuer/2026-09-01-anlage-EUER-2026.pdf?__blob=publicationFile&v=2) |

**Cross-check 2: profit and social insurance.** Compare EÜR profit with the income used by the fund and explain the difference. A voluntary member's contribution basis considers overall economic capacity; do not substitute Zeile 98 for the entire insurance base. Retain provisional/final assessments, health/care/pension status, certificates and arrears/refunds ([§ 240(1), (4a) SGB V](https://www.gesetze-im-internet.de/sgb_5/__240.html)). Health/care deductions require the qualifying basic-cover amounts, including the statutory sick-pay adjustment and refunds/subsidies, rather than the whole premium; apply the supported income-tax Guide calculation ([§ 10(1) no. 3, (2), (4b) EStG](https://www.gesetze-im-internet.de/estg/__10.html)). Pension/KSK and an unresolved insurance deduction remain non-usable: Check this point with one of our partner accountants.

**Cross-check 3: trade tax and income-tax credit.** Start from the trade profit, add § 8 amounts and subtract § 9 amounts ([§ 7 GewStG](https://www.gesetze-im-internet.de/gewstg/__7.html)). Keep evidence of every adjustment; do not apply the allowance directly to unadjusted EÜR profit.

| Sole-trader computation | Condition | Official source |
| --- | --- | --- |
| Round trade income down to a whole EUR 100; deduct allowance up to EUR 24,500 | Deduction cannot exceed rounded trade income | [§ 11(1) GewStG](https://www.gesetze-im-internet.de/gewstg/__11.html) |
| Base amount = remaining ordinary taxable trade income × 3.5% | Special homeworker treatment is held; municipality's multiplier is applied to the base amount | [§ 11(2)–(3) GewStG](https://www.gesetze-im-internet.de/gewstg/__11.html) |
| Trade tax = base amount × municipality's multiplier | Use the actual municipality/year's supported multiplier | [§ 16(1) GewStG](https://www.gesetze-im-internet.de/gewstg/__16.html) |

For the same assessment/collection year, the sole-trader § 35 credit starts at **four times** the assessed base amount, capped by trade tax actually **payable** and the statutory income-tax maximum. That maximum uses positive qualifying trade income / all positive income × reduced tariff tax, with the prescribed foreign-tax and other tax-reduction ordering. Carry the base and municipal notices into the file; no automatic refund, carryover or universal break-even conclusion follows ([§ 35(1), (3) EStG](https://www.gesetze-im-internet.de/estg/__35.html)). Missing cap data leaves the final credit held.

**Cross-check 4: notices and payments.** Income-tax advances are set by notice, ordinarily based on the last assessment after withholding credits, not necessarily the prior tax divided by four. Ordinary due dates are 10 March, 10 June, 10 September and 10 December. Initial advances require **at least EUR 400 for the calendar year and EUR 100 for one due date** ([§ 37(1), (3), (5) EStG](https://www.gesetze-im-internet.de/estg/__37.html)). Read each amount and any additional/adjusted date from its notice. Reconcile paid 2026 advances to the assessment credit; unpaid advances are not paid credits ([§ 36(2) EStG](https://www.gesetze-im-internet.de/estg/__36.html)).

**Cross-check 5: VAT expense bridge.** Deductible input VAT actually paid on supplier invoices goes to EÜR Zeile 58; VAT paid/set off with the tax office goes to Zeile 59. Do not copy VAT-return credits for reverse-charge or intra-EU acquisitions as though VAT was paid to the supplier. For a recurring prior-year VAT advance, both due date and payment must fall within the first ten days of the new year for prior-year treatment. Non-deductible input VAT belongs in the relevant gross cost, subject to its own deduction/capitalisation rules; it is not automatically an immediate expense. Personal/non-deductible expenses remain excluded ([2026 EÜR instructions, Zeilen 58–59](https://www.bundesfinanzministerium.de/Content/DE/Downloads/BMF_Schreiben/Steuerarten/Einkommensteuer/2026-09-01-anlage-EUER-2026.pdf?__blob=publicationFile&v=2), [§ 4(3), (5) EStG](https://www.gesetze-im-internet.de/estg/__4.html), [§ 12 no. 3 EStG](https://www.gesetze-im-internet.de/estg/__12.html)). Explain timing differences instead of forcing VAT and expense totals to match.

### 5. Assemble the asset schedules and reviewer package

Attach Anlage AVEÜR as a necessary EÜR component. For a sole trader, attach Anlage SZ where interest excluding loans financing acquisition/production of fixed assets exceeds **EUR 2,050**; attach the supported interest computation rather than treating the threshold as a disallowance ([2026 ministry letter, page 1](https://www.bundesfinanzministerium.de/Content/DE/Downloads/BMF_Schreiben/Steuerarten/Einkommensteuer/2026-09-01-anlage-EUER-2026.pdf?__blob=publicationFile&v=2)).

| Asset check | Conditions | Official source |
| --- | --- | --- |
| Optional immediate GWG deduction up to EUR 800 | Depreciable movable fixed asset capable of independent use; test cost/value less contained VAT. Above EUR 250, keep the prescribed running register unless equivalent details appear in the books | [§ 6(2) EStG](https://www.gesetze-im-internet.de/estg/__6.html) |
| Optional annual pool for cost/value above EUR 250 and no more than EUR 1,000, less contained VAT | Same asset conditions; uniform treatment of all qualifying acquisitions/production/contributions that year; one fifth in formation year and each of four following years; disposal does not reduce the pool | [§ 6(2a) EStG](https://www.gesetze-im-internet.de/estg/__6.html) |

Retain cost, acquisition date, useful life, method, annual depreciation and opening/closing values. Other depreciation methods, computer useful life, § 7g, gifts, entertainment, mixed telephone/internet, home-office room/day and car valuation are reviewed positions from `de-einkommensteuer-freelancer` / `germany-bookkeeping`, not deductions established by this assembler. If unsupported, label the individual position non-usable: Check this point with one of our partner accountants.

Produce three files using the environment's available artifact tools and authorised output location:

1. **`[client_slug]_2026_germany_master.xlsx`**: Cover; VAT periods plus annual reconciliation; EÜR; income-tax computation; AVEÜR/asset register; expense detail; social insurance; trade tax/credit where relevant; paid advances; 2027 notice calendar; five-check summary. Use formulas through the reconciled bridges, retain units/years and verify totals, references and absence of spreadsheet errors.
2. **`reviewer_brief.md`**: executive summary with all tax balances; VAT; EÜR/income tax (all income, special expenses including donations/church tax, taxable income, assessment type and tariff-zone checks); health/care/pension; trade tax/credit; advances; five checks with differences; every open flag; supported positions with source and operative conditions; 2027 planning (not assumed future law). Preserve the provisional/final status of every total.
3. **`client_action_list.md`**: required filings, period, responsible filer, actual deadline, notice-based payment amount/reference/payee, documents needed and ongoing records. Filing dates and payment dates are separate.

Keep solidarity surcharge (assessment type, child-adjusted base, exemption and transition zone) and church tax (membership, state, correct base/rate) as separate supported upstream computations. Never carry forward old limits or infer no church tax from a missing rate. Unsupported surcharge/church-tax results are non-usable: Check this point with one of our partner accountants.

## Worked cases

**2026 Case 1, original trade income EUR 30,000.** Assume an ordinary sole trader with adjusted trade income already established, no further reliefs or loss deductions. Rounded income remains EUR 30,000; less EUR 24,500 leaves EUR 5,500; at 3.5% the base is EUR 192.50 ([§ 11 GewStG](https://www.gesetze-im-internet.de/gewstg/__11.html)).

**2026 Case 2, original trade income EUR 40,000, multiplier 410%.** On the same assumptions, base EUR 542.50 and illustrative trade tax EUR 2,224.25. Four times the base is EUR 2,170.00. The final credit equals that amount **only if** the § 35 income-tax cap is at least that amount; without the cap inputs it remains non-usable. Local assessment/payment rounding is not established by this arithmetic ([§ 11 GewStG](https://www.gesetze-im-internet.de/gewstg/__11.html), [§ 16 GewStG](https://www.gesetze-im-internet.de/gewstg/__16.html), [§ 35 EStG](https://www.gesetze-im-internet.de/estg/__35.html)).

```oa-check
name: DE sole trader 2026, base amount after the allowance
inputs:
  trade_income: 30000
steps:
  - base: (trade_income - 24500) * 0.035
expected:
  base: 192.50
```

```oa-check
name: DE sole trader 2026, trade tax at multiplier 410%
inputs:
  trade_income: 40000
  hebesatz: 4.1
steps:
  - base: (trade_income - 24500) * 0.035
  - trade_tax: base * hebesatz
expected:
  trade_tax: 2224.25
```

```oa-check
name: DE sole trader 2026, Case 2 credit before the income-tax cap
inputs:
  trade_income: 40000
  hebesatz: 4.1
steps:
  - base: (trade_income - 24500) * 0.035
  - trade_tax: base * hebesatz
  - credit_before_income_tax_cap: min(base * 4, trade_tax)
expected:
  credit_before_income_tax_cap: 2170.00
```

**Historical 2025 illustrations, not a 2026 return.** Preserve the original 210 days × EUR 6 = EUR 1,260, and EUR 35,000 list price × 1% × 12 = EUR 4,200. These are arithmetic only, not proof of qualifying days, car method, private-use amount or a deduction. The historical MacBook Pro illustration assumed three-year depreciation without complete acquisition/use facts; no deduction is established here. Those historical outcomes are non-usable. Check this point with one of our partner accountants. The original 2025 package / 2026 planning years remain distinct from the current package.

## When to refuse or refer

- **R-DE-1 / R-DE-2 / R-DE-3:** missing upstream output, failed upstream check or unreconciled bridge. Name the dependency and difference; continue only independent work, with affected outputs held.
- **R-DE-4:** missing intake data. Check existing records first, then ask for the exact missing item.
- **R-DE-5:** rental, investment, crypto, foreign/treaty/progression income or another business. Preserve the inputs and route to `de-rental-income`, `de-capital-gains`, `de-crypto-tax` as appropriate. Do not present the business-only result as complete personal tax.
- **R-DE-6 / R-DE-7:** balance-sheet/bookkeeping duty (`germany-bookkeeping`), company or partnership; outside this workflow.
- Part-year residence, foreign establishment, incomplete spouse inputs, KSK/pension complexity, disputes, audit, objection, appeal or voluntary disclosure: affected outcome is non-usable. Check this point with one of our partner accountants.
- No request to sign/transmit/pay is executed by this Guide. Invoice/e-invoice rules, retention periods and actual-cost/Fahrtenbuch eligibility need their own supported position; retain them as ongoing action items, with unresolved treatment non-usable. Check this point with one of our partner accountants.

## Filing and payment

Use [Mein ELSTER](https://www.elster.de/): select the actual year and supported return/forms, reconcile portal totals, run validation, resolve flags, and obtain professional review before any authorised submission. Retain the transmitted dataset, protocol/receipt, assessment and notice reconciliation. This is a preparation checklist, not proof that every named form is currently available.

The EÜR is transmitted electronically under § 60(4) EStDV, with an application-based hardship alternative. Business income-tax returns follow § 25(4) EStG, including its § 46(2) nos. 2–8 exception and hardship route. VAT annual returns and trade-tax declarations have their own electronic/hardship provisions; check actual filing duties rather than infer them solely from a document's presence in the package ([§ 60(4) EStDV](https://www.gesetze-im-internet.de/estdv_1955/__60.html), [§ 25(4) EStG](https://www.gesetze-im-internet.de/estg/__25.html), [§ 18(3) UStG](https://www.gesetze-im-internet.de/ustg_1980/__18.html), [§ 14a GewStG](https://www.gesetze-im-internet.de/gewstg/__14a.html)).

| Calendar item | Date/condition | Official source |
| --- | --- | --- |
| Required 2026 calendar-year return, ordinary unrepresented deadline | Derived: 2 August 2027; seven months ends Saturday 31 July, then next working day. Check any actual demand/extension and local statutory holiday | [§ 149(1)–(2) AO](https://www.gesetze-im-internet.de/ao_1977/__149.html), [§ 108(3) AO](https://www.gesetze-im-internet.de/ao_1977/__108.html) |
| Covered adviser-prepared 2026 annual returns | 29 February 2028, subject to earlier demand under § 149(4); voluntary § 46(2) no. 8 returns excluded. Apply separately to each covered annual return | [§ 149(3)–(4) AO](https://www.gesetze-im-internet.de/ao_1977/__149.html) |
| Ordinary VAT advance return and payment | Tenth day after the period; approved Dauerfristverlängerung extends both by one month, subject to refusal/revocation if tax claim endangered | [§ 18(1) UStG](https://www.gesetze-im-internet.de/ustg_1980/__18.html), [§ 46 UStDV](https://www.gesetze-im-internet.de/ustdv_1980/__46.html) |
| 2027 income-tax advances | 10 March, 10 June, 10 September, 10 December; separate amounts from notice | [§ 37 EStG](https://www.gesetze-im-internet.de/estg/__37.html) |
| 2027 calendar-year trade-tax advances | Statutory 15 February, 15 May, 15 August, 15 November; derived weekend moves to 17 May and 16 August, subject to local statutory holidays; use actual notices | [§ 19(1) GewStG](https://www.gesetze-im-internet.de/gewstg/__19.html), [§ 108(3) AO](https://www.gesetze-im-internet.de/ao_1977/__108.html) |

The annual VAT return for **2027** is a separate later-period obligation, not due with the 2026 income-tax return. Keep applicable annual VAT and trade-tax duties/exceptions in the calendar. An income-tax closing balance is ordinarily due within one month after notification of the assessment, except overdue unpaid advances are payable immediately; use the assessment's actual date and amount, not the filing deadline ([§ 36(4) EStG](https://www.gesetze-im-internet.de/estg/__36.html)). Read bank details and reference from the verified notice; never invent them. Payment execution stays with the authorised payer.

## Completion checklist

DE1: all five upstream steps supported or held; DE2: receipts bridge explained; DE3: insurance base reconciled; DE4: notices and paid advances reconciled; DE5: regular VAT receipts/input/payments separated; DE6: small-business eligibility and exceptions tested; DE7: asset methods/registers checked; DE8: insurance deduction reconciled; DE9: assessment type and complete spouse data; DE10: period-specific filing/payment calendar; DE11: both credit caps; DE12: sources/conditions beside every position; DE13: surcharge computation; DE14: church membership/base/rate; DE15: every unsettled field carried forward.

Show pass, explained difference, not applicable or **non-usable hold** for each check. Supply all three files, or identify each missing/partial file. Include 2027 prepayment notices, fund reassessment, asset roll-forward, turnover monitoring and any source-proven law changes in planning. A partial package cannot be called complete or ready to file.

## Sources

Dates below distinguish today's reads from applicable completed official reads reused from the proven German ledgers. Reuse confirms the same rule/year/conditions, not a new fetch date.

| Official text and passage used | URL | Read on |
| --- | --- | --- |
| Residence § 1; business classification §§ 15, 18; EÜR conditions § 4(3) | https://www.gesetze-im-internet.de/estg/__1.html ; https://www.gesetze-im-internet.de/estg/__15.html ; https://www.gesetze-im-internet.de/estg/__18.html ; https://www.gesetze-im-internet.de/estg/__4.html | 2026-11-26, reused applicable completed reads |
| Cash timing § 11; private-tax exclusions § 12 | https://www.gesetze-im-internet.de/estg/__11.html ; https://www.gesetze-im-internet.de/estg/__12.html | 2026-11-27, reused applicable completed reads |
| GWG/pool § 6(2)–(2a); insurance § 10 conditions | https://www.gesetze-im-internet.de/estg/__6.html ; https://www.gesetze-im-internet.de/estg/__10.html | 2026-11-27 / 2026-11-26 respectively, reused applicable completed reads |
| Same-year trade-tax credit, ordering and caps § 35 | https://www.gesetze-im-internet.de/estg/__35.html | 2026-11-27, read operative subsection (1) and notices in (3) |
| Advances § 37; paid credits and closing balance § 36 | https://www.gesetze-im-internet.de/estg/__37.html ; https://www.gesetze-im-internet.de/estg/__36.html | 2026-11-26, reused applicable completed reads |
| Electronic income-tax/EÜR duties and exceptions | https://www.gesetze-im-internet.de/estg/__25.html ; https://www.gesetze-im-internet.de/estdv_1955/__60.html | 2026-11-26, reused applicable completed reads |
| VAT declaration/period/recipient exceptions § 18 | https://www.gesetze-im-internet.de/ustg_1980/__18.html | 2026-11-26 period rules reused; 2026-11-27 read annual/hardship and recipient exceptions (3)–(4a) |
| Domestic small-business turnover, exclusions, waiver and exceptions § 19 | https://www.gesetze-im-internet.de/ustg_1980/__19.html | 2026-11-27, read subsections (1)–(6) |
| Approved VAT extension § 46 | https://www.gesetze-im-internet.de/ustdv_1980/__46.html | 2026-11-26, reused applicable completed read |
| Voluntary statutory insurance base and reassessment § 240(1), (4a) | https://www.gesetze-im-internet.de/sgb_5/__240.html | 2026-11-27, read cited subsections |
| Trade income, rounding/allowance/base §§ 7, 11; electronic declaration § 14a; advance dates § 19 | https://www.gesetze-im-internet.de/gewstg/__7.html ; https://www.gesetze-im-internet.de/gewstg/__11.html ; https://www.gesetze-im-internet.de/gewstg/__14a.html ; https://www.gesetze-im-internet.de/gewstg/__19.html | 2026-11-27, reused applicable completed reads; today's § 11/19 fetches timed out |
| Municipality's multiplier § 16(1) | https://www.gesetze-im-internet.de/gewstg/__16.html | 2026-11-27, read subsection (1); no future minimum imported |
| Annual deadlines and earlier adviser demand § 149; weekend/holiday § 108(3) | https://www.gesetze-im-internet.de/ao_1977/__149.html ; https://www.gesetze-im-internet.de/ao_1977/__108.html | 2026-11-26, reused applicable completed reads |
| 2026 EÜR letter page 1; form pages 1–4; instructions Zeilen 12–23, 58–59, assets and profit section | https://www.bundesfinanzministerium.de/Content/DE/Downloads/BMF_Schreiben/Steuerarten/Einkommensteuer/2026-09-01-anlage-EUER-2026.pdf?__blob=publicationFile&v=2 | 2026-11-27, read those passages and form labels |

Not yet confirmed: 2026 income-tax main form, Anlage S/G/Vorsorgeaufwand/AUS/V/KAP and their current field destinations are non-usable holds; historical 2025 ELSTER instructions do not establish 2026 fields. Specific filing duties, unresolved special cases, deductions, penalties/interest and ongoing invoice/retention/car-record treatment need their own proof. Check this point with one of our partner accountants.

## End of Guide

## Disclaimer

This Guide and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this Guide. All outputs must be reviewed and signed off by a qualified professional (such as a Steuerberater, Wirtschaftsprüfer, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

> Contributed by OpenAccountants.
