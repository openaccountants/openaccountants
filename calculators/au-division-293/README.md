# Australian Division 293 tax estimate

For one person and income year, how much Division 293 tax applies to their low tax
contributions?

This is an offline estimate for 2024-25, 2025-26 and 2026-27 under ITAA 1997 Subdivision 293-B.
It works out Division 293 income from the components of income for surcharge purposes, takes the
excess concessional contributions off the low tax contributed amounts, and applies the $250,000
threshold and the 15% rate. The ATO's Division 293 notice of assessment sets the tax. Division 296
(tax on earnings of large balances, `calculators/au-division-296/`) is a different tax.

```js
import { estimateDivision293 } from "./index.mjs";

const result = estimateDivision293({
  incomeYear: "2026-27",
  taxableIncomeForSurchargePurposes: "240000",
  reportableFringeBenefitsTotal: "0",
  netFinancialInvestmentLoss: "0",
  netRentalPropertyLoss: "0",
  lowTaxContributedAmounts: "15000",
  excessConcessionalContributions: "0",
  definedBenefitInterest: false,
  constitutionallyProtectedFund: false,
  stateHigherLevelOfficeHolder: false,
  commonwealthJustice: false,
  departingAustraliaSuperannuationPayment: false,
});
// verdict: "estimate_calculated", liable: true
// combinedAmount: "255000.00", taxableContributions: "5000.00",
// division293TaxEstimate: "750.00"
```

That is the ATO's example of Jan.

## Inputs and scope

Amounts are non-negative AUD decimal strings with at most 2 decimal places. Every amount is
required, `"0"` when there is none; a missing amount is not zero. Every input is the caller's
attestation, which the calculator does not verify.

| Input | Required meaning |
| --- | --- |
| `incomeYear` | `2024-25`, `2025-26` or `2026-27` |
| `taxableIncomeForSurchargePurposes` | Taxable income worked out disregarding any assessable FHSS released amount (the amount s 313-20 includes) and ITAA 1936 Sch 2F s 271-105(1) (s 995-1 'income for surcharge purposes' (a)). Without either, it is the taxable income. With either, work taxable income out again without them: the deductions and any tax loss deducted can change, so it need not equal taxable income less the one plus the other |
| `reportableFringeBenefitsTotal` | Reportable fringe benefits total (FBTAA s 135N) |
| `netFinancialInvestmentLoss` | Deductions for financial investments over their gross income (s 995-1 'total net investment loss' (a)) |
| `netRentalPropertyLoss` | Deductions for rental property over its gross income (the same definition, (b)) |
| `lowTaxContributedAmounts` | Contributions and amounts covered by s 293-30 for the year, under the law for that year |
| `excessConcessionalContributions` | The year's excess concessional contributions (s 291-20(1)) |
| `definedBenefitInterest` | `true` or `false`. `true` is refused: Subdivision 293-D changes the low tax contributions |
| `constitutionallyProtectedFund` | `true` or `false`: an interest in a constitutionally protected fund. `true` is refused: Subdivision 293-E and Imposition Act 2013 s 6 can change or remove the tax. This is wider than Subdivision 293-E, which also needs a declaration (s 293-145(1)), because whether s 6 stops the tax for a member outside it is a constitutional question the calculator cannot settle |
| `stateHigherLevelOfficeHolder` | `true` or `false`: at any time in the income year, holding a State office of a kind the regulations declare for Subdivision 293-E (s 293-145(1)(b)), whatever fund the person belongs to. `true` is refused: Imposition Act 2013 s 6 may stop the tax for such a person |
| `commonwealthJustice` | `true` or `false`: a justice or judge in s 293-190. `true` is refused (Subdivision 293-F) |
| `departingAustraliaSuperannuationPayment` | `true` or `false`. `true` is refused: a refund under Subdivision 293-G stops all Division 293 tax liabilities (s 293-240) |

A missing or malformed input gives `unknown` with no figures; a case outside these rules gives
`refused` with no figures. Excess concessional contributions above the low tax contributed amounts
also give `unknown`, as s 293-25 would then give a negative amount.

## Calculation

| Amount | Rule |
| --- | --- |
| `division293Income` | Taxable income for surcharge purposes plus the reportable fringe benefits total and both net investment losses: income for surcharge purposes (s 995-1) disregarding the reportable superannuation contributions (s 293-20(1)(a)). Its reduction by the s 301-20(3) amount is nil in these years: s 301-20(1) needs a lump sum received under 60 at or above preservation age, and under SISR reg 6.01(2) nobody is both from 1 July 2024 (preservation age is 60 for anyone born after 30 June 1964, and anyone born earlier is 60 by 30 June 2024) |
| `lowTaxContributions` | Low tax contributed amounts less excess concessional contributions (s 293-25) |
| `excessOverThreshold` | Division 293 income plus low tax contributions, less $250,000, not below nil (s 293-20(1)) |
| `taxableContributions` | The lesser of the low tax contributions and the excess; nil when the low tax contributions are nil (s 293-20(1) and (2)) |
| `division293TaxEstimate` | 15% of the taxable contributions (Imposition Act 2013 s 5) |

Amounts are exact in cents. The tax is rounded once to the nearest cent, half away from zero;
the Acts set no rounding, so this is a calculator convention. A combined amount of exactly
$250,000 does not exceed the threshold. `combinedAmount` is `division293Income` plus
`lowTaxContributions`.

## Outputs and limits

Results include the verdict, reason codes (`liable`, `not_above_threshold` or
`no_low_tax_contributions` after `caller_attested_inputs`), reasons, sources, the rounding note,
the limits and the amounts above.

Out of scope: which contributions are low tax contributed amounts, debt accounts, deferral,
release authorities, payment dates and interest (Subdivision 293-C). For 2024-25 and 2025-26,
s 293-30(4)(d) leaves out an amount an employer contributed and offset against superannuation
guarantee charge under the amnesty (SGAA s 23A). The Treasury Laws Amendment (Payday
Superannuation) Act 2025 (No. 57, 2025) repealed it from 1 July 2026, and its Schedule 1,
item 182(5) keeps the s 23A offset only for contributions made before that day, so there is
nothing for it to leave out in 2026-27. The Acts and the ATO's page were read on 18 November 2026
(ITAA 1997 compilation 268; compilation 250, in force from 1 July 2024, has the same text for
every provision used here). The compilation from 1 December 2026 adds only Schedule 1, items 41 to
45 of the Treasury Laws Amendment (Financial Reporting System Reform) Act 2026 (No. 61, 2026),
which amend ss 25-110(3), 715-375(1)(b), 715-379(1)(b) and 995-1 and change nothing used here.
Review later amendments before relying on the result. No runtime network or clock is consulted.

## Verification and provenance

Run `node --test calculators/au-division-293/` from the repository root on Node 20+ with JSON
import attributes; From the repository root, run `node --test calculators/*/index.test.mjs` to run every calculator suite. Tests reproduce the ATO's Jan
example in each year, the threshold at $250,000.00 and the cents above it, the lesser-of rule,
nil low tax contributions, the excess concessional deduction, each income component, and refusals
of malformed or out-of-scope inputs. No client data is used.

The rules were adapted from Ryan Duguid's independently authored `division-293` and
`income-tests` worksheets in
[australian-tax-calculators](https://github.com/ryanduguid/australian-accounting/tree/main/packages/australian-tax-calculators)
at revision `2e41b018a5a1c5229df2b3fe29de1fe716311fe9`. The other income measures of
`income-tests` are not ported. Paragraph (a) of income for surcharge purposes is one required
input here instead of taxable income adjusted for the FHSS and family trust amounts.
Code and this README: AGPL-3.0-only; `rules.json`: OA Guide License v1.0, following this
repository's licensing policy.

General reference and computational support only. Obtain qualified professional review before
lodging, paying or relying on any result.
