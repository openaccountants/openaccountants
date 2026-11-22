import test from "node:test";
import assert from "node:assert/strict";
import { assessSuperGuaranteeCharge } from "./index.mjs";
import rules from "./rules.json" with { type: "json" };

const check = (input) => assessSuperGuaranteeCharge(input);
const money = ["sgAmount", "baseShortfall", "lateContributionsApplied", "lateContributionsNotApplied", "finalShortfall", "notionalEarnings", "administrativeUplift", "chargeBeforeChoiceLoading"];
const late = (receivedDay, amount) => ({ receivedDay, amount });
const record = (overrides) => ({
  qeDay: "2026-07-30",
  sgRateSchedule: "general",
  qualifyingEarnings: "1000",
  earlierQualifyingEarningsThisYear: "0",
  onTimeContributions: "0",
  lateContributions: [],
  assessmentDay: "2026-12-01",
  noCommissionerInitiatedAssessmentOrEstimate: true,
  ...overrides,
});

// An independent floating-point recount of s 19A from the published quarters: within half a cent of the exact result.
const next = (iso) => new Date(Date.parse(`${iso}T00:00:00Z`) + 86400000).toISOString().slice(0, 10);
function floatNotional(baseShortfall, fromDay, toDay, assumed) {
  let sum = baseShortfall;
  for (let day = fromDay; day <= toDay; day = next(day)) {
    const quarter = rules.notional_earnings.gic_quarters.find((row) => day >= row.from && day <= row.to);
    const annual = quarter ? Number(quarter.annual_percent) : assumed;
    sum *= 1 + annual / 100 / 365;
  }
  return sum - baseShortfall;
}

test("ATO Example 1's second QE day paid 14 days late, with the NT Picnic Day holiday", () => {
  const result = check(record({ lateContributions: [late("2026-08-25", "120")] }));
  assert.equal(result.verdict, "charge_estimated");
  assert.equal(result.latestReceiptDay, "2026-08-11");
  assert.equal(result.sgAmount, "120.00");
  assert.equal(result.finalShortfall, "0.00");
  assert.equal(result.notionalEarningsDays, 14);
  assert.equal(result.notionalEarningsTo, "2026-08-25");
  assert.equal(result.notionalEarnings, "0.53");
  assert.equal(result.upliftPercent, 40);
  assert.equal(result.administrativeUplift, "0.21");
  assert.equal(result.chargeBeforeChoiceLoading, "0.74");
  assert.ok(Math.abs(floatNotional(120, "2026-08-12", "2026-08-25") - 0.53) < 0.005);
});

// ATO, 'What to do if you miss a Payday Super contribution' (last updated 27 June 2026), Juliet's example: 30 employees'
// $120 each, $3,600 together, paid 25 days late or not at all, give $24.74 or $49.65 of notional earnings, which a 10%
// annual GIC rate reproduces. One employee with $30,000 of qualifying earnings has the same $3,600 shortfall. Every late
// day here is after the published table, so the assumed 10% applies throughout (2027 has 365 days).
test("ATO's Juliet example: $3,600 for 25 days or 50 days at an assumed 10%", () => {
  const input = record({ qeDay: "2026-12-22", qualifyingEarnings: "30000", noCommissionerInitiatedAssessmentOrEstimate: false, assumedGicAnnualPercent: "10" });
  const paid = check({ ...input, lateContributions: [late("2027-01-30", "3600")], assessmentDay: "2027-02-24" });
  assert.equal(paid.latestReceiptDay, "2027-01-05");
  assert.equal(paid.notionalEarningsDays, 25);
  assert.equal(paid.assumedGicDays, 25);
  assert.equal(paid.notionalEarnings, "24.74");
  assert.equal(paid.upliftPercent, 60);
  assert.equal(paid.administrativeUplift, "14.84");
  assert.deepEqual(paid.reason_codes, ["caller_supplied_inputs", "assumed_gic_rate"]);
  // The late period ends the day before the assessment (s 6(1)), so 50 days of earnings need an assessment on day 51.
  const unpaid = check({ ...input, assessmentDay: "2027-02-25" });
  assert.equal(unpaid.notionalEarningsDays, 50);
  assert.equal(unpaid.finalShortfall, "3600.00");
  assert.equal(unpaid.notionalEarnings, "49.65");
  assert.equal(unpaid.administrativeUplift, "2189.79");
  assert.equal(unpaid.chargeBeforeChoiceLoading, "5839.44");
});

test("part paid late across the October rate change, after an ATO-initiated assessment, with disclosure", () => {
  const input = record({ qeDay: "2026-08-06", qualifyingEarnings: "6500", lateContributions: [late("2026-09-02", "540")], assessmentDay: "2026-12-10", noCommissionerInitiatedAssessmentOrEstimate: false });
  for (const [lodged, percent, uplift, charge] of [["2026-09-04", 20, "53.69", "322.16"], ["2026-09-05", 25, "67.12", "335.59"]]) {
    const result = check({ ...input, voluntaryDisclosureLodgedDay: lodged });
    assert.equal(result.latestReceiptDay, "2026-08-17");
    assert.equal(result.baseShortfall, "780.00");
    assert.equal(result.lateContributionsApplied, "540.00");
    assert.equal(result.finalShortfall, "240.00");
    assert.equal(result.notionalEarningsDays, 114);
    assert.equal(result.notionalEarningsTo, "2026-12-09");
    assert.equal(result.notionalEarnings, "28.47");
    assert.equal(result.upliftPercent, percent, lodged);
    assert.equal(result.administrativeUplift, uplift, lodged);
    assert.equal(result.chargeBeforeChoiceLoading, charge, lodged);
  }
  assert.ok(Math.abs(floatNotional(780, "2026-08-18", "2026-12-09") - 28.47) < 0.005);
});

test("reg 13D: the QE day is day 1 of each period", () => {
  // QE day 3 August 2026 (due 13 August); assessed 1 March 2027 so every lodgment day is before it.
  for (const [lodged, without, withReduction] of [
    ["2026-08-03", 20, 0], ["2026-09-01", 20, 0], ["2026-09-02", 25, 5], ["2026-10-01", 25, 5],
    ["2026-10-02", 30, 10], ["2026-11-30", 30, 10], ["2026-12-01", 45, 25], ["2027-02-28", 45, 25],
  ]) {
    const input = record({ qeDay: "2026-08-03", lateContributions: [late("2026-08-20", "120")], assessmentDay: "2027-03-01", voluntaryDisclosureLodgedDay: lodged });
    assert.equal(check({ ...input, noCommissionerInitiatedAssessmentOrEstimate: false }).upliftPercent, without, lodged);
    assert.equal(check({ ...input, noCommissionerInitiatedAssessmentOrEstimate: true }).upliftPercent, withReduction, lodged);
  }
});

test("the ATO's uplift table without a disclosure: 60% or 40%", () => {
  const input = record({ lateContributions: [late("2026-08-25", "120")] });
  assert.equal(check({ ...input, noCommissionerInitiatedAssessmentOrEstimate: false }).upliftPercent, 60);
  assert.equal(check(input).upliftPercent, 40);
});

test("the maximum contributions base of $270,830 caps the SG amount (s 10A(6))", () => {
  const partial = check(record({ qeDay: "2026-09-03", earlierQualifyingEarningsThisYear: "270000", onTimeContributions: "99.60" }));
  assert.equal(partial.verdict, "no_shortfall");
  assert.equal(partial.sgAmount, "99.60");
  assert.deepEqual(partial.reason_codes, ["caller_supplied_inputs", "on_time_contributions_cover"]);
  const reached = check(record({ qeDay: "2026-09-03", earlierQualifyingEarningsThisYear: "270830" }));
  assert.equal(reached.sgAmount, "0.00");
  assert.deepEqual(reached.reason_codes, ["caller_supplied_inputs", "maximum_contributions_base_reached"]);
  const below = check(record({ qeDay: "2026-09-03", earlierQualifyingEarningsThisYear: "270829.99", onTimeContributions: "0" }));
  assert.equal(below.sgAmount, "0.00");
  assert.equal(below.verdict, "no_shortfall");
  assert.equal(check(record({ qeDay: "2026-09-03", earlierQualifyingEarningsThisYear: "270829.95" })).sgAmount, "0.01");
});

test("a missing or unrecognised rate schedule leaves the charge unknown", () => {
  const { sgRateSchedule: _schedule, ...missing } = record();
  for (const input of [missing, record({ sgRateSchedule: "" }), record({ sgRateSchedule: 12 }),
    Object.assign(Object.create({ sgRateSchedule: "general" }), missing)]) {
    const result = check(input);
    assert.equal(result.verdict, "unknown");
    assert.deepEqual(result.reason_codes, ["sg_rate_schedule"]);
    for (const key of money) assert.equal(result[key], null, key);
  }
});

test("transitional and mixed earnings carry no general-rate charge", () => {
  for (const sgRateSchedule of ["norfolk_island_transitional", "mixed"]) {
    const result = check(record({ sgRateSchedule }));
    assert.equal(result.verdict, "refused");
    assert.deepEqual(result.reason_codes, ["norfolk_island_transition"]);
    for (const key of money) assert.equal(result[key], null, key);
  }
});

test("the SG amount is 12% rounded half up to the cent", () => {
  assert.equal(check(record({ qualifyingEarnings: "0.04", onTimeContributions: "0.01" })).sgAmount, "0.00");
  assert.equal(check(record({ qualifyingEarnings: "0.05", onTimeContributions: "0.01" })).sgAmount, "0.01");
  assert.equal(check(record({ qualifyingEarnings: "1234.56", onTimeContributions: "148.15" })).sgAmount, "148.15");
});

test("the receipt day of the clearing contribution is counted, and the day before the assessment is the last", () => {
  const dayAfter = check(record({ lateContributions: [late("2026-08-12", "120")] }));
  assert.equal(dayAfter.notionalEarningsDays, 1);
  assert.equal(dayAfter.notionalEarnings, "0.04");
  const unpaid = check(record({ assessmentDay: "2026-08-20" }));
  assert.equal(unpaid.notionalEarningsDays, 8);
  assert.equal(unpaid.notionalEarningsTo, "2026-08-19");
  const assessedNextDay = check(record({ assessmentDay: "2026-08-12" }));
  assert.equal(assessedNextDay.notionalEarningsDays, 0);
  assert.equal(assessedNextDay.notionalEarnings, "0.00");
  assert.equal(assessedNextDay.chargeBeforeChoiceLoading, "168.00");
});

test("late contributions apply in the order received; a part payment does not stop the earnings", () => {
  const result = check(record({ lateContributions: [late("2026-09-30", "100"), late("2026-08-20", "50")] }));
  assert.equal(result.lateContributionsApplied, "120.00");
  assert.equal(result.lateContributionsNotApplied, "30.00");
  assert.equal(result.finalShortfall, "0.00");
  assert.equal(result.notionalEarningsTo, "2026-09-30");
  assert.equal(result.notionalEarningsDays, 50);
  assert.ok(Math.abs(floatNotional(120, "2026-08-12", "2026-09-30") - Number(result.notionalEarnings)) < 0.005);
});

test("an s 18C(2) extension moves the due day the late period starts from", () => {
  const first = record({ qeDay: "2026-07-09", firstContributionToFund: true });
  assert.equal(check({ ...first, lateContributions: [late("2026-08-06", "120")] }).verdict, "refused");
  const result = check({ ...first, lateContributions: [late("2026-08-10", "120")] });
  assert.equal(result.latestReceiptDay, "2026-08-07");
  assert.equal(result.governingRule, "item_1");
  assert.equal(result.notionalEarningsDays, 3);
});

test("every day of notional earnings agrees with an independent recount", () => {
  for (const [qeDay, received, assessmentDay] of [
    ["2026-07-01", "2026-07-31", "2026-09-01"], ["2026-09-15", "2026-10-20", "2026-11-30"],
    ["2026-07-01", null, "2026-12-31"], ["2026-10-01", null, "2026-12-15"],
  ]) {
    const result = check(record({ qeDay, qualifyingEarnings: "54321.09", lateContributions: received ? [late(received, "7000")] : [], assessmentDay }));
    const expected = floatNotional(Number(result.baseShortfall), next(result.latestReceiptDay), result.notionalEarningsTo);
    assert.ok(Math.abs(expected - Number(result.notionalEarnings)) < 0.005, qeDay);
  }
});

test("a late period past the published GIC table needs an assumed rate", () => {
  const input = record({ qeDay: "2026-11-05", qualifyingEarnings: "2000", assessmentDay: "2027-02-15" });
  const refused = check(input);
  assert.equal(refused.verdict, "unknown");
  assert.deepEqual(refused.reason_codes, ["assumed_gic_rate"]);
  assert.equal(refused.notionalEarnings, null);
  const result = check({ ...input, assumedGicAnnualPercent: "11.51" });
  assert.equal(result.latestReceiptDay, "2026-11-16");
  assert.equal(result.notionalEarningsDays, 90);
  assert.equal(result.assumedGicDays, 45);
  assert.equal(result.notionalEarnings, "6.91");
  assert.equal(check({ ...input, assessmentDay: "2027-01-01" }).verdict, "charge_estimated");
  assert.equal(check({ ...input, assessmentDay: "2027-01-02" }).verdict, "unknown");
});

const invalid = [
  ["a quarterly-regime QE day", { qeDay: "2026-06-30" }, "refused"],
  ["a QE day after 30 June 2027", { qeDay: "2027-07-01" }, "refused"],
  ["a QE day past the business-day calendar", { qeDay: "2027-09-01" }, "refused"],
  ["a malformed QE day", { qeDay: "2026-7-30" }, "unknown"],
  ["nil earnings", { qualifyingEarnings: "0" }, "unknown"],
  ["negative earnings", { qualifyingEarnings: "-1000" }, "unknown"],
  ["three decimal places", { qualifyingEarnings: "1000.001" }, "unknown"],
  ["a number for money", { qualifyingEarnings: 1000 }, "unknown"],
  ["missing earlier earnings", { earlierQualifyingEarningsThisYear: undefined }, "unknown"],
  ["missing on-time contributions", { onTimeContributions: undefined }, "unknown"],
  ["late contributions not a list", { lateContributions: undefined }, "unknown"],
  ["a late contribution without a day", { lateContributions: [{ amount: "120" }] }, "unknown"],
  ["a nil late contribution", { lateContributions: [late("2026-08-25", "0")] }, "unknown"],
  ["a late contribution received on the due day", { lateContributions: [late("2026-08-11", "120")] }, "refused"],
  ["a late contribution received on the assessment day", { lateContributions: [late("2026-12-01", "120")] }, "refused"],
  ["no assessment day", { assessmentDay: undefined }, "unknown"],
  ["an assessment day on the due day", { assessmentDay: "2026-08-11" }, "refused"],
  ["an assessment day past the engine's limit", { assessmentDay: "2031-07-01", assumedGicAnnualPercent: "11.51" }, "refused"],
  ["reg 13C not stated", { noCommissionerInitiatedAssessmentOrEstimate: undefined }, "unknown"],
  ["reg 13C as a string", { noCommissionerInitiatedAssessmentOrEstimate: "true" }, "unknown"],
  ["a disclosure before the QE day", { voluntaryDisclosureLodgedDay: "2026-07-29" }, "refused"],
  ["a disclosure on the assessment day", { voluntaryDisclosureLodgedDay: "2026-12-01" }, "refused"],
  ["a malformed disclosure day", { voluntaryDisclosureLodgedDay: "2026-02-30" }, "refused"],
  ["a nil assumed rate", { qeDay: "2026-11-05", assessmentDay: "2027-02-15", assumedGicAnnualPercent: "0" }, "unknown"],
  ["an assumed rate of 100%", { qeDay: "2026-11-05", assessmentDay: "2027-02-15", assumedGicAnnualPercent: "100" }, "unknown"],
];
for (const [label, overrides, verdict] of invalid) {
  test(`no charge for ${label}`, () => {
    const result = check(record(overrides));
    assert.equal(result.verdict, verdict);
    for (const key of [...money.filter((key) => key !== "sgAmount" && key !== "baseShortfall"), "upliftPercent"]) assert.equal(result[key], null, key);
    assert.equal(result.reason_codes.length, result.reasons.length);
  });
}

test("invalid records return a structured result", () => {
  for (const input of [undefined, null, [], 7, "2026-07-30"]) assert.equal(check(input).verdict, "unknown");
});

test("results are JSON-safe and do not expose the rules to mutation", () => {
  const first = check(record({ lateContributions: [late("2026-08-25", "120")] }));
  assert.doesNotThrow(() => JSON.stringify(first));
  first.sources.push("caller mutation");
  first.limits.length = 0;
  const second = check(record({ lateContributions: [late("2026-08-25", "120")] }));
  assert.ok(!second.sources.includes("caller mutation"));
  assert.ok(second.limits.length > 0);
  assert.equal(second.as_of, "2026-11-19");
});

test("the GIC quarters are contiguous and match the published rates", () => {
  const quarters = rules.notional_earnings.gic_quarters;
  assert.equal(quarters[0].from, rules.qe_days.from);
  quarters.forEach((quarter, index) => index > 0 && assert.equal(quarters[index - 1].to, new Date(Date.parse(`${quarter.from}T00:00:00Z`) - 86400000).toISOString().slice(0, 10)));
  assert.deepEqual(quarters.map((quarter) => quarter.annual_percent), ["11.43", "11.51"]);
});
