import test from "node:test";
import assert from "node:assert/strict";
import { assessActivityStatementDueDate } from "./index.mjs";
import rules from "./rules.json" with { type: "json" };
import paydaySuperRules from "../au-payday-super-timing/rules.json" with { type: "json" };

const check = (input) => assessActivityStatementDueDate(input);
const dates = ["form", "period", "rule", "nominalDueDate", "dueDate", "holidaysPassed"];
const weekday = (iso) => new Date(`${iso}T00:00:00Z`).getUTCDay();
const next = (iso) => new Date(Date.parse(`${iso}T00:00:00Z`) + 86400000).toISOString().slice(0, 10);
const decemberAgent = { form: "monthly", period: "2026-12", concession: "agent" };
const eligibleDecember = { ...decemberAgent, turnoverUpTo10Million: true, reportsGstMonthly: true, deferredGst: false };

test("au-lodgment-deadlines-penalties: 28 February 2027 passes Sunday and WA Labour Day to 2 March", () => {
  const result = check({ form: "quarterly", period: "2026-12" });
  assert.equal(result.verdict, "due_date_calculated");
  assert.equal(result.nominalDueDate, "2027-02-28");
  assert.equal(result.dueDate, "2027-03-02");
  assert.deepEqual(result.holidaysPassed.map((holiday) => holiday.name), ["Labour Day (WA)"]);
  assert.deepEqual(result.reason_codes, ["original", "moved_to_business_day"]);
});

// Nominal dates: ATO, Due dates for lodging and paying your BAS (last updated 17 September 2026); activity
// statements due dates by topic; the BAS agent and registered agent lodgment programs 2026-27 (last updated
// 1 July 2026). Moves: the ATO's weekend and public holiday tables (last updated 1 July 2026).
for (const [form, period, concession, rule, nominalDueDate, dueDate] of [
  ["monthly", "2026-06", "none", "original", "2026-07-21", "2026-07-21"],
  ["monthly", "2026-07", "none", "original", "2026-08-21", "2026-08-21"],
  ["monthly", "2026-08", "none", "original", "2026-09-21", "2026-09-21"],
  ["monthly", "2026-09", "none", "original", "2026-10-21", "2026-10-21"],
  ["monthly", "2026-10", "none", "original", "2026-11-21", "2026-11-23"],
  ["monthly", "2026-11", "none", "original", "2026-12-21", "2026-12-21"],
  ["monthly", "2026-12", "none", "original", "2027-01-21", "2027-01-21"],
  ["monthly", "2027-01", "none", "original", "2027-02-21", "2027-02-22"],
  ["monthly", "2027-02", "none", "original", "2027-03-21", "2027-03-22"],
  ["monthly", "2027-03", "none", "original", "2027-04-21", "2027-04-21"],
  ["monthly", "2027-04", "none", "original", "2027-05-21", "2027-05-21"],
  ["monthly", "2027-05", "none", "original", "2027-06-21", "2027-06-21"],
  ["monthly", "2026-12", "agent", "december_agent", "2027-02-21", "2027-02-22"],
  ["quarterly", "2026-06", "none", "original", "2026-07-28", "2026-07-28"],
  ["quarterly", "2026-09", "none", "original", "2026-10-28", "2026-10-28"],
  ["quarterly", "2027-03", "none", "original", "2027-04-28", "2027-04-28"],
  ["quarterly", "2026-06", "online", "online_concession", "2026-08-11", "2026-08-11"],
  ["quarterly", "2026-09", "online", "online_concession", "2026-11-11", "2026-11-11"],
  ["quarterly", "2027-03", "online", "online_concession", "2027-05-12", "2027-05-12"],
  ["quarterly", "2026-06", "agent", "agent_program", "2026-08-25", "2026-08-25"],
  ["quarterly", "2026-09", "agent", "agent_program", "2026-11-25", "2026-11-25"],
  ["quarterly", "2027-03", "agent", "agent_program", "2027-05-26", "2027-05-26"],
  ["head_company_payg_instalment", "2026-06", "none", "original", "2026-07-21", "2026-07-21"],
  ["head_company_payg_instalment", "2026-09", "none", "original", "2026-10-21", "2026-10-21"],
  ["head_company_payg_instalment", "2026-12", "none", "original", "2027-01-21", "2027-01-21"],
  ["head_company_payg_instalment", "2027-03", "none", "original", "2027-04-21", "2027-04-21"],
]) {
  test(`${form} ${period}, concession ${concession}: due ${dueDate}`, () => {
    const result = check({ ...eligibleDecember, form, period, concession });
    assert.equal(result.verdict, "due_date_calculated");
    assert.equal(result.rule, rule);
    assert.equal(result.nominalDueDate, nominalDueDate);
    assert.equal(result.dueDate, dueDate);
    assert.ok(![0, 6].includes(weekday(result.dueDate)));
    assert.equal(result.reason_codes.includes("moved_to_business_day"), nominalDueDate !== dueDate);
    assert.equal(result.reason_codes.includes("caller_attested_concession"), concession !== "none");
    assert.equal(result.reason_codes.length, result.reasons.length);
    assert.doesNotThrow(() => JSON.stringify(result));
  });
}

test("the December agent date needs each of its conditions stated", () => {
  for (const conditions of [{}, { turnoverUpTo10Million: true, reportsGstMonthly: true }, { turnoverUpTo10Million: "yes", reportsGstMonthly: true, deferredGst: false }]) {
    const result = check({ ...decemberAgent, ...conditions });
    assert.equal(result.verdict, "unknown");
    assert.deepEqual(result.reason_codes, ["december_agent_conditions"]);
    assert.equal(result.dueDate, null);
  }
});

for (const [condition, value] of [["turnoverUpTo10Million", false], ["reportsGstMonthly", false], ["deferredGst", true]]) {
  test(`no 21 February date for a December monthly statement when ${condition} is ${value}`, () => {
    const result = check({ ...eligibleDecember, [condition]: value });
    assert.equal(result.rule, "original");
    assert.equal(result.dueDate, "2027-01-21");
    assert.equal(result.reason_codes[0], "concession_not_applicable");
  });
}

test("no covered statement is due on, or moves across, a day the law and the ATO's tables treat differently", () => {
  const contested = new Set(["2026-09-28", "2026-11-03", "2026-12-24", "2026-12-31"]);
  const periods = [];
  for (let day = Date.UTC(2025, 11, 1); day <= Date.UTC(2027, 5, 1); day = Date.UTC(new Date(day).getUTCFullYear(), new Date(day).getUTCMonth() + 1, 1)) {
    periods.push(new Date(day).toISOString().slice(0, 7));
  }
  let calculated = 0;
  for (const form of ["monthly", "quarterly", "head_company_payg_instalment"]) {
    for (const period of periods) {
      for (const concession of ["none", "online", "agent"]) {
        const result = check({ ...eligibleDecember, form, period, concession });
        if (result.verdict !== "due_date_calculated") continue;
        calculated += 1;
        for (const day = new Date(`${result.nominalDueDate}T00:00:00Z`); day.toISOString().slice(0, 10) <= result.dueDate; day.setUTCDate(day.getUTCDate() + 1)) {
          assert.ok(!contested.has(day.toISOString().slice(0, 10)), `${form} ${period} ${concession}`);
        }
      }
    }
  }
  assert.equal(calculated, 60);
});

test("an omitted concession is none", () => {
  assert.deepEqual(check({ form: "quarterly", period: "2026-09" }), check({ form: "quarterly", period: "2026-09", concession: "none" }));
});

for (const [label, input, dueDate] of [
  ["the online concession on a monthly statement", { form: "monthly", period: "2026-09", concession: "online" }, "2026-10-21"],
  ["the online concession on a December monthly statement", { form: "monthly", period: "2026-12", concession: "online" }, "2027-01-21"],
  ["the agent program on a monthly statement other than December", { form: "monthly", period: "2027-01", concession: "agent" }, "2027-02-22"],
  ["the online concession on quarter 2", { form: "quarterly", period: "2026-12", concession: "online" }, "2027-03-02"],
  ["the agent program on quarter 2", { form: "quarterly", period: "2026-12", concession: "agent" }, "2027-03-02"],
  ["the online concession on a head company's instalment statement", { form: "head_company_payg_instalment", period: "2026-09", concession: "online" }, "2026-10-21"],
  ["the agent program on a head company's instalment statement", { form: "head_company_payg_instalment", period: "2026-12", concession: "agent" }, "2027-01-21"],
]) {
  test(`no later date for ${label}`, () => {
    const result = check(input);
    assert.equal(result.rule, "original");
    assert.equal(result.dueDate, dueDate);
    assert.equal(result.reason_codes[0], "concession_not_applicable");
    assert.ok(!result.reason_codes.includes("caller_attested_concession"));
  });
}

test("the ATO's holiday tables, less the excluded day, reproduce each first business day it gives", () => {
  const listed = new Set(rules.holidays.weekday_holidays.map((holiday) => holiday.date));
  const roll = (iso) => {
    let day = iso;
    while ([0, 6].includes(weekday(day)) || listed.has(day)) day = next(day);
    return day;
  };
  for (const holiday of rules.holidays.weekday_holidays) assert.equal(roll(holiday.date), holiday.ato_first_business_day, holiday.date);
  const [excluded] = rules.holidays.excluded;
  assert.ok(!listed.has(excluded.date));
  assert.notEqual(roll(excluded.date), excluded.ato_first_business_day);
});

test("the holiday rows are sorted, unique weekdays inside the covered span", () => {
  const rows = rules.holidays.weekday_holidays;
  assert.equal(rows.length + rules.holidays.excluded.length, 20);
  rows.forEach((row, index) => {
    assert.ok(index === 0 || rows[index - 1].date < row.date, row.date);
    assert.ok(row.date >= rules.coverage.due_from && row.date <= rules.coverage.due_until, row.date);
    assert.ok(![0, 6].includes(weekday(row.date)), row.date);
  });
});

test("the ATO's list is the Payday Super whole-state calendar plus 3 days the ATO also applies", () => {
  const ours = new Set(rules.holidays.weekday_holidays.map((holiday) => holiday.date));
  const wholeState = paydaySuperRules.calendar.weekday_holidays
    .map((holiday) => holiday.date)
    .filter((date) => date >= rules.coverage.due_from && date <= rules.coverage.due_until);
  for (const date of wholeState) assert.ok(ours.has(date), date);
  assert.deepEqual([...ours].filter((date) => !wholeState.includes(date)), ["2026-11-03", "2026-12-24", "2026-12-31"]);
});

const refusals = [
  ["a monthly period before the span", { form: "monthly", period: "2026-05" }, "outside_program_year"],
  ["the June 2027 monthly statement", { form: "monthly", period: "2027-06" }, "outside_program_year"],
  ["a December 2025 agent date before the span", { ...eligibleDecember, period: "2025-12" }, "outside_program_year"],
  ["quarter 3 2025-26", { form: "quarterly", period: "2026-03" }, "outside_program_year"],
  ["quarter 3 2025-26 through an agent", { form: "quarterly", period: "2026-03", concession: "agent" }, "outside_program_year"],
  ["quarter 4 2026-27", { form: "quarterly", period: "2027-06" }, "outside_program_year"],
  ["quarter 4 2026-27 online", { form: "quarterly", period: "2027-06", concession: "online" }, "outside_program_year"],
  ["quarter 4 2026-27 through an agent, still to be confirmed", { form: "quarterly", period: "2027-06", concession: "agent" }, "outside_program_year"],
  ["a head company's quarter 4 2026-27", { form: "head_company_payg_instalment", period: "2027-06" }, "outside_program_year"],
  ["a quarter ending in August", { form: "quarterly", period: "2026-08" }, "non_standard_quarter"],
  ["a head company's quarter ending in November", { form: "head_company_payg_instalment", period: "2026-11" }, "non_standard_quarter"],
];
for (const value of [undefined, null, "", "2026-13", "2026-00", "2026-9", "26-09", "2026-09-30", " 2026-09", "2026-09\n", 202609, ["2026-09"], {}]) {
  refusals.push([`period ${JSON.stringify(value) ?? "undefined"}`, { form: "quarterly", period: value }, "period"]);
}
for (const value of [undefined, null, "", "Monthly", "annual", "bas", 1, ["monthly"]]) {
  refusals.push([`form ${JSON.stringify(value) ?? "undefined"}`, { form: value, period: "2026-09" }, "form"]);
}
for (const value of [null, "", "Online", "paper", "deferral", true, 1, ["agent"]]) {
  refusals.push([`concession ${JSON.stringify(value)}`, { form: "quarterly", period: "2026-09", concession: value }, "concession"]);
}
for (const [label, input, code] of refusals) {
  test(`no date for ${label}`, () => {
    const result = check(input);
    assert.equal(result.verdict, code === "outside_program_year" || code === "non_standard_quarter" ? "refused" : "unknown");
    assert.deepEqual(result.reason_codes, [code]);
    for (const key of dates) assert.equal(result[key], null);
    assert.equal(result.reason_codes.length, result.reasons.length);
  });
}

test("invalid records return a structured result", () => {
  for (const input of [undefined, null, [], 7, "2026-09"]) assert.deepEqual(check(input).reason_codes, ["invalid_input"]);
});

test("a covered quarter without a published agent date is refused, not guessed", () => {
  const saved = rules.quarterly.agent_program["2026-09"];
  delete rules.quarterly.agent_program["2026-09"];
  try {
    const result = check({ form: "quarterly", period: "2026-09", concession: "agent" });
    assert.equal(result.verdict, "refused");
    assert.deepEqual(result.reason_codes, ["agent_date_unpublished"]);
    assert.equal(result.dueDate, null);
  } finally {
    rules.quarterly.agent_program["2026-09"] = saved;
  }
});

test("no mutation of the rules through a result", () => {
  const first = check({ form: "monthly", period: "2026-11", concession: "none" });
  first.sources.push("caller mutation");
  first.limits.length = 0;
  const christmas = check({ form: "quarterly", period: "2026-12" });
  christmas.holidaysPassed[0].name = "caller mutation";
  assert.ok(!check({ form: "monthly", period: "2026-11" }).sources.includes("caller mutation"));
  assert.ok(check({ form: "monthly", period: "2026-11" }).limits.length > 0);
  assert.equal(check({ form: "quarterly", period: "2026-12" }).holidaysPassed[0].name, "Labour Day (WA)");
  assert.equal(rules.holidays.weekday_holidays[10].name, "Labour Day (WA)");
});
