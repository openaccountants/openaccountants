import test from "node:test";
import assert from "node:assert/strict";
import { assessCarFringeBenefit } from "./index.mjs";

const check = (input) => assessCarFringeBenefit(input);
const figures = ["fbtYear", "method", "baseValue", "statutoryValue", "operatingCostValue", "businessUsePercentage", "taxableValue"];
const statutoryCar = {
  fbtYear: 2027,
  method: "statutory",
  commitmentBefore10May2011: false,
  carValue: "40000",
  earliestHoldingDate: "2026-04-01",
  laterAccessoriesCost: "0",
  privateUseDays: 365,
  recipientsPayment: "1000",
};
const records = { logBookYear: true, logBookRecordsMaintained: true, odometerRecordsMaintained: true, providerIsEmployer: true };
// ATO employer guide Example 31: operating costs $19,580, 75% business use, $2,000 recipient's payment.
const operatingCar = {
  ...statutoryCar,
  method: "operating_cost",
  carValue: "50000",
  earliestHoldingDate: "2026-01-15",
  recipientsPayment: "2000",
  operatingCost: "19580",
  businessKilometres: 15000,
  totalKilometres: 20000,
  ...records,
};

const assertNoFigures = (result) => {
  for (const key of figures) assert.equal(result[key], null, key);
  assert.equal(result.reason_codes.length, 1);
};

test("au-fbt Example 1: $40,000 base value for all 365 days less $1,000 is $7,000", () => {
  const result = check(statutoryCar);
  assert.equal(result.verdict, "taxable_value_calculated");
  assert.equal(result.method, "statutory");
  assert.equal(result.baseValue, "40000.00");
  assert.equal(result.statutoryValue, "7000.00");
  assert.equal(result.operatingCostValue, null);
  assert.equal(result.taxableValue, "7000.00");
  assert.deepEqual(result.reason_codes, ["caller_attested_inputs", "statutory"]);
  assert.equal(result.reason_codes.length, result.reasons.length);
  assert.doesNotThrow(() => JSON.stringify(result));
});

test("au-fbt Test 3: held before the fourth anniversary, base value $26,666.67 and $4,333.33", () => {
  const result = check({ ...statutoryCar, earliestHoldingDate: "2022-03-31" });
  assert.equal(result.baseValue, "26666.67");
  assert.equal(result.taxableValue, "4333.33");
  assert.ok(result.reason_codes.includes("base_value_reduced"));
});

test("the reduction starts only when the year begins later than the fourth anniversary", () => {
  const onAnniversary = check({ ...statutoryCar, earliestHoldingDate: "2022-04-01" });
  assert.equal(onAnniversary.baseValue, "40000.00");
  assert.ok(!onAnniversary.reason_codes.includes("base_value_reduced"));
  // ATO employer guide Example 26: held from 1 July 2016, reduced from the year beginning 1 April 2021.
  assert.equal(check({ ...statutoryCar, earliestHoldingDate: "2022-07-01" }).baseValue, "40000.00");
  assert.equal(check({ ...statutoryCar, earliestHoldingDate: "2016-07-01" }).baseValue, "26666.67");
});

test("later non-business accessories are added in full, never reduced", () => {
  const result = check({ ...statutoryCar, earliestHoldingDate: "2016-07-01", laterAccessoriesCost: "4000" });
  assert.equal(result.baseValue, "30666.67");
  assert.equal(result.taxableValue, "5133.33");
});

test("an accessory fitted at purchase is part of the cost price, so it is reduced too", () => {
  // ATO Example 26's $31,000 car including a $1,000 accessory: the guide gives $21,000; s 9(2)(a)(i) with s 136(1) 'cost price' gives 2/3 of $31,000.
  assert.equal(check({ ...statutoryCar, carValue: "31000", earliestHoldingDate: "2016-07-01" }).baseValue, "20666.67");
});

test("ATO Example 28: $60,000 car for 182 days less $1,000 is $4,983.56 (the guide shows whole dollars)", () => {
  const result = check({ ...statutoryCar, carValue: "60000", earliestHoldingDate: "2026-08-01", privateUseDays: 182 });
  assert.equal(result.statutoryValue, "4983.56");
});

test("ATO Example 31: $19,580 operating cost at 75% business use less $2,000 is $2,895", () => {
  const result = check(operatingCar);
  assert.equal(result.verdict, "taxable_value_calculated");
  assert.equal(result.method, "operating_cost");
  assert.equal(result.businessUsePercentage, "75.00");
  assert.equal(result.operatingCostValue, "2895.00");
  assert.equal(result.statutoryValue, "8000.00");
  assert.equal(result.taxableValue, "2895.00");
});

test("ATO Example 29: 6,000 of 19,000 kilometres is 31.58% business use", () => {
  assert.equal(check({ ...operatingCar, businessKilometres: 6000, totalKilometres: 19000 }).businessUsePercentage, "31.58");
});

test("s 10(5): a higher operating cost value gives way to the statutory formula; a tie keeps the election", () => {
  const higher = check({ ...operatingCar, operatingCost: "60000" });
  assert.equal(higher.operatingCostValue, "13000.00");
  assert.equal(higher.method, "statutory");
  assert.equal(higher.taxableValue, "8000.00");
  assert.deepEqual(higher.reason_codes, ["caller_attested_inputs", "statutory_lower", "statutory"]);
  const tie = check({ ...operatingCar, operatingCost: "40000" });
  assert.equal(tie.operatingCostValue, "8000.00");
  assert.equal(tie.method, "operating_cost");
  // Exactly $100.004 against $100.002: both round to $100.00, but s 10(5) compares the values themselves.
  const subCent = check({ ...operatingCar, carValue: "500.01", recipientsPayment: "0", operatingCost: "200", businessKilometres: 24999, totalKilometres: 50000 });
  assert.equal(subCent.operatingCostValue, "100.00");
  assert.equal(subCent.method, "statutory");
  assert.equal(subCent.taxableValue, "100.00");
});

test("without the records ss 10A and 10B require, business use is nil", () => {
  for (const missing of [
    { logBookRecordsMaintained: false },
    { odometerRecordsMaintained: false },
    { providerIsEmployer: false, recordsGivenBeforeDeclarationDate: false },
    { logBookYear: false, odometerRecordsMaintained: false },
  ]) {
    const result = check({ ...operatingCar, operatingCost: "10000", ...missing });
    assert.equal(result.businessUsePercentage, "0.00");
    assert.equal(result.operatingCostValue, "8000.00");
    assert.ok(result.reason_codes.includes("no_business_use_reduction"));
  }
  const nonLogBookYear = check({ ...operatingCar, logBookYear: false, logBookRecordsMaintained: undefined });
  assert.equal(nonLogBookYear.operatingCostValue, "2895.00");
  const otherProvider = check({ ...operatingCar, providerIsEmployer: false, recordsGivenBeforeDeclarationDate: true });
  assert.equal(otherProvider.operatingCostValue, "2895.00");
});

test("each records condition a business use reduction needs is its own required input", () => {
  for (const key of Object.keys(records)) {
    for (const value of [undefined, null, "yes"]) {
      const result = check({ ...operatingCar, [key]: value });
      assert.equal(result.verdict, "unknown", key);
      assert.deepEqual(result.reason_codes, ["business_use_records"]);
      assertNoFigures(result);
    }
  }
  const unstated = check({ ...operatingCar, providerIsEmployer: false });
  assert.equal(unstated.verdict, "unknown");
  assertNoFigures(unstated);
});

test("no business kilometres needs no records", () => {
  const result = check({ ...statutoryCar, method: "operating_cost", operatingCost: "5000", businessKilometres: 0, totalKilometres: 0 });
  assert.equal(result.businessUsePercentage, "0.00");
  assert.equal(result.operatingCostValue, "4000.00");
  assert.equal(result.method, "operating_cost");
});

test("values round half up to the cent, and a payment above the value gives nil", () => {
  const half = check({ ...operatingCar, operatingCost: "100.01", businessKilometres: 1, totalKilometres: 2, recipientsPayment: "0" });
  assert.equal(half.operatingCostValue, "50.01");
  const overpaid = check({ ...statutoryCar, recipientsPayment: "8000.01" });
  assert.equal(overpaid.taxableValue, "0.00");
});

test("private use days are bounded by the year and the earliest holding day", () => {
  assert.equal(check({ ...statutoryCar, privateUseDays: 0 }).taxableValue, "0.00");
  assert.equal(check({ ...statutoryCar, earliestHoldingDate: "2026-10-01", privateUseDays: 182, recipientsPayment: "0" }).taxableValue, "3989.04");
  for (const [earliestHoldingDate, privateUseDays] of [["2026-04-01", 366], ["2026-10-01", 183], ["2026-04-01", 1.5], ["2026-04-01", -1], ["2026-04-01", "365"]]) {
    const result = check({ ...statutoryCar, earliestHoldingDate, privateUseDays });
    assert.equal(result.verdict, "unknown");
    assert.deepEqual(result.reason_codes, ["private_use_days"]);
    assertNoFigures(result);
  }
  const later = check({ ...statutoryCar, earliestHoldingDate: "2027-04-01" });
  assert.deepEqual([later.verdict, later.reason_codes], ["refused", ["not_held_in_year"]]);
});

test("unsupported years, methods and the pre-2011 commitment give no figure", () => {
  for (const [change, verdict, code] of [
    [{ fbtYear: 2026 }, "refused", "unsupported_year"],
    [{ fbtYear: 2028 }, "refused", "unsupported_year"],
    [{ fbtYear: "2027" }, "refused", "unsupported_year"],
    [{ method: "logbook" }, "unknown", "method"],
    [{ commitmentBefore10May2011: true }, "refused", "pre_2011_commitment"],
    [{ commitmentBefore10May2011: undefined }, "unknown", "pre_2011_commitment"],
  ]) {
    const result = check({ ...statutoryCar, ...change });
    assert.equal(result.verdict, verdict);
    assert.deepEqual(result.reason_codes, [code]);
    assertNoFigures(result);
  }
});

test("malformed money, dates and kilometres give no figure", () => {
  for (const [change, code] of [
    [{ carValue: "0" }, "invalid_money"],
    [{ carValue: 40000 }, "invalid_money"],
    [{ carValue: "40,000" }, "invalid_money"],
    [{ laterAccessoriesCost: undefined }, "invalid_money"],
    [{ recipientsPayment: "-1" }, "invalid_money"],
    [{ recipientsPayment: "1.005" }, "invalid_money"],
    [{ earliestHoldingDate: "2026-02-30" }, "earliest_holding_date"],
    [{ earliestHoldingDate: "1/4/2026" }, "earliest_holding_date"],
    [{ operatingCost: "0" }, "operating_cost"],
    [{ operatingCost: undefined }, "operating_cost"],
    [{ businessKilometres: 20001 }, "kilometres"],
    [{ totalKilometres: undefined }, "kilometres"],
  ]) {
    const result = check({ ...operatingCar, ...change });
    assert.equal(result.verdict, "unknown");
    assert.deepEqual(result.reason_codes, [code]);
    assertNoFigures(result);
  }
  for (const input of [null, [], "car"]) assert.deepEqual(check(input).reason_codes, ["invalid_input"]);
});
