// SPDX-License-Identifier: AGPL-3.0-only
// Copyright 2026 Ryan Duguid
// Adapted from the author's BAS due dates page (ryanduguid.github.io, tools/bas-due-dates) and
// au-fpa-pack's activity statement due dates and holiday list (pyfpa/au/gst.py, public_holidays.yaml).
// Pure, offline calculation. No clock, network or holiday overrides.
import rules from "./rules.json" with { type: "json" };

const msPerDay = 86400000;
const periodPattern = /^(\d{4})-(0[1-9]|1[0-2])$/;
const forms = new Set(["monthly", "quarterly", "head_company_payg_instalment"]);
const concessions = new Set(["none", "online", "agent"]);
const decemberConditions = ["turnoverUpTo10Million", "reportsGstMonthly", "deferredGst"];

const dayNumber = (iso) => Date.parse(`${iso}T00:00:00Z`) / msPerDay;
const ymd = (year, month, day) => Date.UTC(year, month - 1, day) / msPerDay;
const isoDate = (day) => new Date(day * msPerDay).toISOString().slice(0, 10);
const coverFrom = dayNumber(rules.coverage.due_from);
const coverUntil = dayNumber(rules.coverage.due_until);
const holidays = new Map(rules.holidays.weekday_holidays.map((holiday) => [dayNumber(holiday.date), holiday]));

// TAA 1953 s 8AAZMB and Sch 1 s 388-52: the first business day on or after `day` (1970-01-01 was a Thursday).
function businessDayFrom(day) {
  let current = day;
  while ((current + 4) % 7 === 0 || (current + 4) % 7 === 6 || holidays.has(current)) current += 1;
  return current;
}

// The date the law or the 2026-27 program names, before any move, and the rule that names it.
function nominal(form, year, month, concession, decemberEligible) {
  if (form === "monthly") {
    if (month === 12 && concession === "agent" && decemberEligible) {
      const { month: dueMonth, day } = rules.monthly.december_agent;
      return { rule: "december_agent", day: ymd(year + 1, dueMonth, day) };
    }
    const notApplicable = {
      none: null,
      online: "The 2-week online concession does not apply to monthly activity statements.",
      agent: month === 12
        ? "The 21 February date needs up to $10 million annual turnover, monthly GST reporting and no deferred GST registration."
        : "The agent program gives a monthly activity statement a later date only for December.",
    }[concession];
    return { rule: "original", day: ymd(year, month + 1, rules.monthly.due_day), notApplicable };
  }
  if (form === "head_company_payg_instalment") {
    return {
      rule: "original",
      day: ymd(year, month + 1, rules.head_company_payg_instalment.due_day),
      notApplicable: concession === "none" ? null : "A head company's quarterly PAYG instalment activity statement gets neither the online concession nor the agent program date.",
    };
  }
  const key = String(month).padStart(2, "0");
  const original = rules.quarterly.original[key];
  const originalDay = ymd(year + (original.month < month ? 1 : 0), original.month, original.day);
  if (concession === "none") return { rule: "original", day: originalDay };
  if (key === "12") {
    return { rule: "original", day: originalDay, notApplicable: "Quarter 2 already runs to 28 February; neither the online concession nor the agent program gives a later date." };
  }
  if (concession === "online") return { rule: "online_concession", day: originalDay + rules.quarterly.online_concession.days, originalDay };
  const program = rules.quarterly.agent_program[`${year}-${key}`];
  return { rule: "agent_program", day: program === undefined ? null : dayNumber(program), originalDay };
}

/**
 * @param {object} input
 * @param {"monthly"|"quarterly"|"head_company_payg_instalment"} input.form Activity statement kind;
 *   the last is a consolidated group head company's quarterly PAYG instalment activity statement.
 * @param {string} input.period "YYYY-MM": the month, or the last month of a standard quarter.
 * @param {"none"|"online"|"agent"} [input.concession] Caller-attested eligibility for the 2-week
 *   online concession or the registered agent program date; omitted means none.
 * @param {boolean} [input.turnoverUpTo10Million] Required for a December monthly statement with
 *   concession "agent", as are the next 2: annual turnover is up to $10 million.
 * @param {boolean} [input.reportsGstMonthly] GST is reported monthly.
 * @param {boolean} [input.deferredGst] The business is registered for deferred GST.
 * @returns {object} JSON-safe result; dates are "YYYY-MM-DD" strings or null.
 */
export function assessActivityStatementDueDate(input) {
  const base = {
    as_of: rules.as_of,
    program_year: rules.program_year,
    coverage: { dueFrom: rules.coverage.due_from, dueUntil: rules.coverage.due_until },
    sources: [...rules.sources],
    limits: [...rules.limits],
    form: null,
    period: null,
    rule: null,
    nominalDueDate: null,
    dueDate: null,
    holidaysPassed: null,
  };
  const stop = (verdict, code, reason) => ({ ...base, verdict, reason_codes: [code], reasons: [reason] });
  if (!input || typeof input !== "object" || Array.isArray(input)) {
    return stop("unknown", "invalid_input", "Supply a record with the documented inputs.");
  }
  if (!forms.has(input.form)) {
    return stop("unknown", "form", "form must be monthly, quarterly or head_company_payg_instalment.");
  }
  const match = typeof input.period === "string" ? periodPattern.exec(input.period) : null;
  if (!match) return stop("unknown", "period", "Supply the period as YYYY-MM.");
  const concession = input.concession ?? "none";
  if (input.concession === null || !concessions.has(concession)) {
    return stop("unknown", "concession", "concession must be none, online, agent or omitted.");
  }
  const [year, month] = [Number(match[1]), Number(match[2])];
  if (input.form !== "monthly" && month % 3 !== 0) {
    return stop("refused", "non_standard_quarter", "A quarter must end in March, June, September or December; substituted accounting periods are outside scope.");
  }
  const decemberAgent = input.form === "monthly" && month === 12 && concession === "agent";
  if (decemberAgent && !decemberConditions.every((key) => typeof input[key] === "boolean")) {
    return stop("unknown", "december_agent_conditions", "For the December agent date, state turnoverUpTo10Million, reportsGstMonthly and deferredGst as true or false.");
  }
  const decemberEligible = decemberAgent && input.turnoverUpTo10Million && input.reportsGstMonthly && !input.deferredGst;
  const named = nominal(input.form, year, month, concession, decemberEligible);
  const outside = () => stop("refused", "outside_program_year", `This calculator covers due dates from ${rules.coverage.due_from} to ${rules.coverage.due_until}, the span of the ATO's ${rules.program_year} public holiday tables.`);
  // An agent quarter is placed by its original date, so an unlisted quarter outside the span is refused as such.
  const anchor = named.originalDay ?? named.day;
  if (anchor < coverFrom || anchor > coverUntil) return outside();
  if (named.day === null) {
    return stop("refused", "agent_date_unpublished", "The ATO has published no agent program date for this quarter.");
  }
  const due = businessDayFrom(named.day);
  if (due > coverUntil) return outside();

  const reason_codes = [];
  const reasons = [];
  const add = (code, reason) => {
    reason_codes.push(code);
    reasons.push(reason);
  };
  if (named.notApplicable) add("concession_not_applicable", named.notApplicable);
  if (named.rule !== "original") add("caller_attested_concession", "Eligibility for the concession is caller-attested; this calculator has not verified it.");
  add(named.rule, {
    original: "The original due date applies.",
    online_concession: "The 2-week online lodgment concession applies.",
    agent_program: "The 2026-27 agent lodgment program date applies.",
    december_agent: "The agent program's 21 February date for an eligible December monthly business activity statement applies.",
  }[named.rule]);
  if (due !== named.day) add("moved_to_business_day", "The named date is not a business day, so lodgment and payment move to the next business day (TAA 1953 s 8AAZMB and Sch 1 s 388-52).");
  return {
    ...base,
    verdict: "due_date_calculated",
    reason_codes,
    reasons,
    form: input.form,
    period: input.period,
    rule: named.rule,
    nominalDueDate: isoDate(named.day),
    dueDate: isoDate(due),
    holidaysPassed: [...holidays].filter(([day]) => day >= named.day && day < due).map(([, holiday]) => ({ ...holiday })),
  };
}
