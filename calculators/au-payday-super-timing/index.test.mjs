import test from "node:test";
import assert from "node:assert/strict";
import { assessPaydaySuperTiming } from "./index.mjs";
import rules from "./rules.json" with { type: "json" };

const check = (input) => assessPaydaySuperTiming(input);
const dates = ["qeDay", "periods", "latestReceiptDay", "governingRule", "holidaysInWindow"];

// ATO, 'Payment deadlines for Payday Super' (last updated 29 September 2026), Examples 1 to 6.
for (const [label, input, due, rule] of [
  ["Example 1, QE day 1: first contribution for a new employee", { qeDay: "2026-07-09", firstContributionToFund: true }, "2026-08-07", "item_1"],
  ["Example 1, QE day 2: usual period", { qeDay: "2026-07-30" }, "2026-08-11", "usual_period"],
  ["Example 2, QE day 1: first contribution to a new fund", { qeDay: "2026-08-07", firstContributionToFund: true }, "2026-09-04", "item_1"],
  ["Example 2, QE day 2: usual period", { qeDay: "2026-09-04", firstContributionToFund: false }, "2026-09-15", "usual_period"],
  ["Example 3: out-of-cycle Christmas bonus", { qeDay: "2026-12-07", outOfCycleNextStandardQeDay: "2026-12-10" }, "2026-12-21", "item_2"],
  ["Example 4: out-of-cycle back payment", { qeDay: "2026-08-29", outOfCycleNextStandardQeDay: "2026-09-03" }, "2026-09-14", "item_2"],
  ["Example 5, QE day 1: determination made after the QE day", { qeDay: "2026-08-04", exceptionalCircumstancesDeterminationDay: "2026-08-07" }, "2026-09-04", "item_3"],
  ["Example 5, QE day 2: 20 business days after the QE day", { qeDay: "2026-08-18", exceptionalCircumstancesDeterminationDay: "2026-08-07" }, "2026-09-15", "item_3"],
  ["Example 6: bunching onto the earlier extended due day", { qeDay: "2026-07-23", earlierContributionLatestDueDay: "2026-08-07" }, "2026-08-07", "item_4"],
]) {
  test(`ATO ${label}`, () => {
    const result = check(input);
    assert.equal(result.verdict, "latest_receipt_day_calculated");
    assert.equal(result.latestReceiptDay, due);
    assert.equal(result.governingRule, rule);
    assert.equal(result.reason_codes.length, result.reasons.length);
    assert.doesNotThrow(() => JSON.stringify(result));
  });
}

test("ATO Example 6: the usual period alone would end on 4 August 2026", () => {
  assert.deepEqual(check({ qeDay: "2026-07-23", earlierContributionLatestDueDay: "2026-08-07" }).periods, {
    usual_period: "2026-08-04",
    item_4: "2026-08-07",
  });
});

test("a holiday for the whole of one territory delays every employer", () => {
  const result = check({ qeDay: "2026-07-30" });
  assert.deepEqual(result.holidaysInWindow.map((holiday) => [holiday.date, holiday.jurisdictions]), [["2026-08-03", ["NT"]]]);
});

for (const [label, qeDay, due] of [
  ["Victoria's Friday before the AFL Grand Final and the 5 October holidays", "2026-09-24", "2026-10-07"],
  ["Christmas, the Boxing Day additional day and New Year's Day", "2026-12-24", "2027-01-07"],
  ["Melbourne Cup Day is not a whole-state holiday", "2026-11-02", "2026-11-11"],
  ["Easter, without Tasmania's Easter Tuesday", "2027-03-25", "2027-04-07"],
  ["the part-day holidays on 24 and 31 December are business days", "2026-12-22", "2027-01-05"],
  ["a weekend QE day counts from the next day", "2026-08-01", "2026-08-12"],
  ["the first Payday Super QE day", "2026-07-01", "2026-07-10"],
  ["the last QE day whose usual period fits the calendar", "2027-08-20", "2027-08-31"],
]) {
  test(`usual period: ${label}`, () => {
    assert.equal(check({ qeDay }).latestReceiptDay, due);
  });
}

test("every usual period in the calendar ends on its seventh business day", () => {
  const holidays = new Set(rules.calendar.weekday_holidays.map((holiday) => holiday.date));
  const business = (iso) => ![0, 6].includes(new Date(`${iso}T00:00:00Z`).getUTCDay()) && !holidays.has(iso);
  const next = (iso) => new Date(Date.parse(`${iso}T00:00:00Z`) + 86400000).toISOString().slice(0, 10);
  for (let qeDay = rules.calendar.verified_from; qeDay <= "2027-08-20"; qeDay = next(qeDay)) {
    const due = check({ qeDay }).latestReceiptDay;
    let counted = 0;
    for (let day = next(qeDay); day <= due; day = next(day)) if (business(day)) counted += 1;
    assert.equal(counted, 7, qeDay);
    assert.ok(business(due), qeDay);
  }
});

test("the latest applicable period governs and ties keep the usual period", () => {
  const both = check({ qeDay: "2026-12-07", firstContributionToFund: true, outOfCycleNextStandardQeDay: "2026-12-10" });
  assert.deepEqual(both.periods, { usual_period: "2026-12-16", item_1: "2027-01-07", item_2: "2026-12-21" });
  assert.equal(both.governingRule, "item_1");
  const tie = check({ qeDay: "2026-07-30", earlierContributionLatestDueDay: "2026-08-11" });
  assert.equal(tie.governingRule, "usual_period");
  const earlierStill = check({ qeDay: "2026-07-30", earlierContributionLatestDueDay: "2026-08-05" });
  assert.equal(earlierStill.latestReceiptDay, "2026-08-11");
});

test("item 3 takes the later of the extended usual period and 20 business days after the determination", () => {
  assert.deepEqual(check({ qeDay: "2026-08-04", exceptionalCircumstancesDeterminationDay: "2026-07-01" }).periods, {
    usual_period: "2026-08-13",
    item_3: "2026-09-01",
  });
});

test("item 3's 20 business days include the day after the determination when it is a business day", () => {
  assert.deepEqual(check({ qeDay: "2026-07-01", exceptionalCircumstancesDeterminationDay: "2026-07-20" }).periods, {
    usual_period: "2026-07-10",
    item_3: "2026-08-18",
  });
});

test("the holiday table is sorted, unique, weekday-only and inside the calendar", () => {
  const codes = new Set(["ACT", "NSW", "NT", "QLD", "SA", "TAS", "VIC", "WA"]);
  const rows = rules.calendar.weekday_holidays;
  rows.forEach((row, index) => {
    assert.ok(index === 0 || rows[index - 1].date < row.date, row.date);
    assert.ok(row.date >= rules.calendar.verified_from && row.date <= rules.calendar.verified_until, row.date);
    assert.ok(![0, 6].includes(new Date(`${row.date}T00:00:00Z`).getUTCDay()), row.date);
    assert.ok(row.jurisdictions.length > 0 && row.jurisdictions.every((code) => codes.has(code)), row.date);
  });
});

const invalid = [
  ["quarterly regime", { qeDay: "2026-06-30" }, "refused"],
  ["QE day past the calendar", { qeDay: "2027-09-01" }, "refused"],
  ["usual period past the calendar", { qeDay: "2027-08-23" }, "refused"],
  ["item 1 period past the calendar", { qeDay: "2027-08-04", firstContributionToFund: true }, "refused"],
  ["item 2 period past the calendar", { qeDay: "2027-08-20", outOfCycleNextStandardQeDay: "2027-08-27" }, "refused"],
  ["item 3 period past the calendar", { qeDay: "2027-07-01", exceptionalCircumstancesDeterminationDay: "2027-08-10" }, "refused"],
  ["item 4 day past the calendar", { qeDay: "2027-07-01", earlierContributionLatestDueDay: "2027-09-01" }, "refused"],
  ["determination before the calendar", { qeDay: "2026-07-01", exceptionalCircumstancesDeterminationDay: "2026-06-30" }, "refused"],
  ["next standard QE day on the same day", { qeDay: "2026-12-07", outOfCycleNextStandardQeDay: "2026-12-07" }, "refused"],
  ["next standard QE day earlier", { qeDay: "2026-12-07", outOfCycleNextStandardQeDay: "2026-12-01" }, "refused"],
  ["truthy first-contribution string", { qeDay: "2026-07-09", firstContributionToFund: "true" }, "unknown"],
  ["first-contribution number", { qeDay: "2026-07-09", firstContributionToFund: 1 }, "unknown"],
  ["null first contribution", { qeDay: "2026-07-09", firstContributionToFund: null }, "unknown"],
];
for (const value of [undefined, null, "", "2026-02-30", "2026-7-1", "26-07-01", " 2026-07-01", "2026-07-01\n", "2026-07-01T00:00:00Z", "2026/07/01", 20260701, new Date("2026-07-01"), ["2026-07-01"], {}]) {
  const shown = String(value).slice(0, 24);
  invalid.push([`QE day ${shown}`, { qeDay: value }, "unknown"]);
  if (value === undefined) continue;
  for (const key of ["outOfCycleNextStandardQeDay", "exceptionalCircumstancesDeterminationDay", "earlierContributionLatestDueDay"]) {
    invalid.push([`${key} ${shown}`, { qeDay: "2026-07-09", [key]: value }, "unknown"]);
  }
}
for (const [label, input, verdict] of invalid) {
  test(`no calculated date for ${label}`, () => {
    const result = check(input);
    assert.equal(result.verdict, verdict);
    for (const key of dates) assert.equal(result[key], null);
    assert.equal(result.reason_codes.length, result.reasons.length);
  });
}

test("invalid records return a structured result", () => {
  for (const input of [undefined, null, [], 7, "2026-07-01"]) assert.equal(check(input).verdict, "unknown");
});

test("no mutation of the rules through a result", () => {
  const first = check({ qeDay: "2026-12-24" });
  first.sources.push("caller mutation");
  first.limits.length = 0;
  first.holidaysInWindow[0].jurisdictions.length = 0;
  const second = check({ qeDay: "2026-12-24" });
  assert.ok(!second.sources.includes("caller mutation"));
  assert.ok(second.limits.length > 0);
  assert.equal(second.holidaysInWindow[0].jurisdictions.length, 8);
  assert.equal(second.as_of, "2026-11-18");
});
