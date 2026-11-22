import test from "node:test";
import assert from "node:assert/strict";
import { estimateDivision293 } from "./index.mjs";
import rules from "./rules.json" with { type: "json" };

const base = {
  incomeYear: "2026-27",
  taxableIncomeForSurchargePurposes: "0",
  reportableFringeBenefitsTotal: "0",
  netFinancialInvestmentLoss: "0",
  netRentalPropertyLoss: "0",
  lowTaxContributedAmounts: "0",
  excessConcessionalContributions: "0",
  definedBenefitInterest: false,
  constitutionallyProtectedFund: false,
  stateHigherLevelOfficeHolder: false,
  commonwealthJustice: false,
  departingAustraliaSuperannuationPayment: false,
};
const check = (changes = {}) => estimateDivision293({ ...base, ...changes });
const figures = ["incomeYear", "liable", "division293Income", "lowTaxContributions", "combinedAmount", "excessOverThreshold", "taxableContributions", "division293TaxEstimate"];
const stopped = (result, verdict, code) => {
  assert.equal(result.verdict, verdict);
  assert.deepEqual(result.reason_codes, [code]);
  for (const key of figures) assert.equal(result[key], null);
};

test("ATO example: Jan's $240,000 and $15,000 give $5,000 taxable and $750 tax", () => {
  for (const incomeYear of rules.supported_years) {
    const result = check({ incomeYear, taxableIncomeForSurchargePurposes: "240000", lowTaxContributedAmounts: "15000" });
    assert.equal(result.verdict, "estimate_calculated");
    assert.equal(result.division293Income, "240000.00");
    assert.equal(result.combinedAmount, "255000.00");
    assert.equal(result.excessOverThreshold, "5000.00");
    assert.equal(result.taxableContributions, "5000.00");
    assert.equal(result.division293TaxEstimate, "750.00");
    assert.equal(result.liable, true);
    assert.deepEqual(result.reason_codes, ["caller_supplied_inputs", "liable"]);
    assert.doesNotThrow(() => JSON.stringify(result));
  }
});

test("$250,000.00 exactly is not over the threshold; each cent above is, rounded half away from zero", () => {
  const at = check({ taxableIncomeForSurchargePurposes: "230000", lowTaxContributedAmounts: "20000" });
  assert.equal(at.liable, false);
  assert.equal(at.taxableContributions, "0.00");
  assert.equal(at.division293TaxEstimate, "0.00");
  assert.deepEqual(at.reason_codes, ["caller_supplied_inputs", "not_above_threshold"]);
  for (const [income, taxable, tax] of [
    ["230000.01", "0.01", "0.00"], ["230000.03", "0.03", "0.00"], ["230000.04", "0.04", "0.01"],
    ["230000.10", "0.10", "0.02"], ["230000.30", "0.30", "0.05"], ["230001", "1.00", "0.15"],
  ]) {
    const result = check({ taxableIncomeForSurchargePurposes: income, lowTaxContributedAmounts: "20000" });
    assert.equal(result.taxableContributions, taxable, income);
    assert.equal(result.division293TaxEstimate, tax, income);
    assert.equal(result.liable, true);
  }
});

test("the taxable contributions are the lesser of the low tax contributions and the excess", () => {
  const result = check({ taxableIncomeForSurchargePurposes: "300000", lowTaxContributedAmounts: "20000" });
  assert.equal(result.excessOverThreshold, "70000.00");
  assert.equal(result.taxableContributions, "20000.00");
  assert.equal(result.division293TaxEstimate, "3000.00");
});

test("nil low tax contributions give no taxable contributions, whatever the income", () => {
  const result = check({ taxableIncomeForSurchargePurposes: "400000" });
  assert.equal(result.excessOverThreshold, "150000.00");
  assert.equal(result.taxableContributions, "0.00");
  assert.equal(result.liable, false);
  assert.deepEqual(result.reason_codes, ["caller_supplied_inputs", "no_low_tax_contributions"]);
  const allExcess = check({ taxableIncomeForSurchargePurposes: "400000", lowTaxContributedAmounts: "40000", excessConcessionalContributions: "40000" });
  assert.equal(allExcess.lowTaxContributions, "0.00");
  assert.equal(allExcess.liable, false);
});

test("excess concessional contributions come off the low tax contributed amounts", () => {
  const result = check({ taxableIncomeForSurchargePurposes: "260000", lowTaxContributedAmounts: "40000", excessConcessionalContributions: "7500" });
  assert.equal(result.lowTaxContributions, "32500.00");
  assert.equal(result.combinedAmount, "292500.00");
  assert.equal(result.taxableContributions, "32500.00");
  assert.equal(result.division293TaxEstimate, "4875.00");
  stopped(check({ lowTaxContributedAmounts: "7499.99", excessConcessionalContributions: "7500" }), "unknown", "components_inconsistent");
});

test("Division 293 income adds each surcharge income component, without super contributions", () => {
  const result = check({
    taxableIncomeForSurchargePurposes: "200000",
    reportableFringeBenefitsTotal: "20000",
    netFinancialInvestmentLoss: "3000",
    netRentalPropertyLoss: "7000",
    lowTaxContributedAmounts: "50000",
    reportableSuperannuationContributions: "50000",
  });
  assert.equal(result.division293Income, "230000.00");
  assert.equal(result.combinedAmount, "280000.00");
  assert.equal(result.taxableContributions, "30000.00");
  assert.equal(result.division293TaxEstimate, "4500.00");
});

// Paragraph (a) of 'income for surcharge purposes' is one statutory amount: taxable income worked out
// without the FHSS amount and Sch 2F s 271-105(1). Its parts are not accepted, so nothing approximates it.
test("taxable income for surcharge purposes is required; its old parts give no figure", () => {
  const rest = Object.fromEntries(Object.entries(base).filter(([key]) => key !== "taxableIncomeForSurchargePurposes"));
  const parts = { taxableIncome: "240000", assessableFhssReleasedAmount: "0", familyTrustDistributionAmounts: "0", lowTaxContributedAmounts: "15000" };
  stopped(estimateDivision293({ ...rest, ...parts }), "unknown", "invalid_money");
});

test("each exclusion is refused when true and has no figure when not stated", () => {
  for (const [key, code] of [
    ["definedBenefitInterest", "defined_benefit_interest"],
    ["constitutionallyProtectedFund", "constitutionally_protected_fund"],
    ["stateHigherLevelOfficeHolder", "state_higher_level_office_holder"],
    ["commonwealthJustice", "commonwealth_justice"],
    ["departingAustraliaSuperannuationPayment", "departing_australia_payment"],
  ]) {
    stopped(check({ [key]: true }), "refused", code);
    stopped(check({ [key]: undefined }), "unknown", code);
    stopped(check({ [key]: "false" }), "unknown", code);
  }
});

test("unsupported years and malformed or missing amounts give no figure", () => {
  for (const incomeYear of ["2023-24", "2027-28", "2026/27", 2026, undefined]) stopped(check({ incomeYear }), "refused", "unsupported_year");
  for (const key of Object.keys(base).filter((name) => typeof base[name] === "string" && name !== "incomeYear")) {
    for (const value of [undefined, "", "-1", "1.234", "1e6", "01", 1000, "1,000"]) stopped(check({ [key]: value }), "unknown", "invalid_money");
  }
  for (const input of [null, [], "facts"]) stopped(estimateDivision293(input), "unknown", "invalid_input");
});

test("rules: the $250,000 threshold and the 15% rate", () => {
  assert.equal(rules.threshold, "250000");
  assert.equal(rules.rate_percent, 15);
});
