// SPDX-License-Identifier: AGPL-3.0-only
// Copyright 2026 Ryan Duguid
// Adapted from the author's payday-super-checker deadline engine:
// https://github.com/ryanduguid/australian-accounting/tree/main/packages/payday-super-checker
// Pure, offline calculation. No clock, network or holiday overrides.
import rules from "./rules.json" with { type: "json" };

const msPerDay = 86400000;
const datePattern = /^(\d{4})-(\d{2})-(\d{2})$/;

// Days since 1970-01-01 for a valid YYYY-MM-DD string, otherwise null.
function dayNumber(value) {
  if (typeof value !== "string") return null;
  const match = datePattern.exec(value);
  if (!match) return null;
  const time = Date.UTC(Number(match[1]), Number(match[2]) - 1, Number(match[3]));
  return new Date(time).toISOString().slice(0, 10) === value ? time / msPerDay : null;
}

const isoDate = (day) => new Date(day * msPerDay).toISOString().slice(0, 10);
const regimeStart = dayNumber(rules.regime_start);
const calendarStart = dayNumber(rules.calendar.verified_from);
const calendarEnd = dayNumber(rules.calendar.verified_until);
const holidays = new Map(rules.calendar.weekday_holidays.map((holiday) => [dayNumber(holiday.date), holiday]));

// SGAA s 6(1): not a Saturday or Sunday (1970-01-01 was a Thursday) and not a whole-state holiday.
const isBusinessDay = (day) => (day + 4) % 7 !== 0 && (day + 4) % 7 !== 6 && !holidays.has(day);

// The count-th business day after `day`, or null when the count passes the verified calendar.
function businessDaysAfter(day, count) {
  let current = day;
  for (let found = 0; found < count; ) {
    current += 1;
    if (current > calendarEnd) return null;
    if (isBusinessDay(current)) found += 1;
  }
  return current;
}

/**
 * @param {object} input
 * @param {string} input.qeDay Day the qualifying earnings were paid, "YYYY-MM-DD".
 * @param {boolean} [input.firstContributionToFund] s 18C(2) item 1, caller-supplied.
 * @param {string} [input.outOfCycleNextStandardQeDay] s 18C(2) item 2: the first standard QE day
 *   after an out-of-cycle QE day under LI 2026/20, caller-supplied.
 * @param {string} [input.exceptionalCircumstancesDeterminationDay] s 18C(2) item 3: the day a
 *   determination covering the employer and this QE day was made, caller-supplied.
 * @param {string} [input.earlierContributionLatestDueDay] s 18C(2) item 4: the latest due day of an
 *   earlier eligible contribution made and applied for an earlier QE day, caller-supplied.
 * @returns {object} JSON-safe result; dates are "YYYY-MM-DD" strings or null.
 */
export function assessPaydaySuperTiming(input) {
  const base = {
    as_of: rules.as_of,
    sources: [...rules.sources],
    limits: [...rules.limits],
    calendar: { verifiedFrom: rules.calendar.verified_from, verifiedUntil: rules.calendar.verified_until },
    qeDay: null,
    periods: null,
    latestReceiptDay: null,
    governingRule: null,
    holidaysInWindow: null,
  };
  const stop = (verdict, code, reason) => ({ ...base, verdict, reason_codes: [code], reasons: [reason] });
  if (!input || typeof input !== "object" || Array.isArray(input)) {
    return stop("unknown", "invalid_input", "Supply a record with the documented inputs.");
  }
  const qe = dayNumber(input.qeDay);
  if (qe === null) return stop("unknown", "qe_day_missing", "Supply the QE day as YYYY-MM-DD.");
  if (qe < regimeStart) {
    return stop("refused", "quarterly_regime", "Qualifying earnings paid before 1 July 2026 fall under the quarterly due dates, not Payday Super.");
  }
  const first = input.firstContributionToFund;
  if (first !== undefined && typeof first !== "boolean") {
    return stop("unknown", "first_contribution", "firstContributionToFund must be true, false or omitted.");
  }
  const optionalDay = (key) => (input[key] === undefined ? undefined : dayNumber(input[key]));
  const next = optionalDay("outOfCycleNextStandardQeDay");
  const determination = optionalDay("exceptionalCircumstancesDeterminationDay");
  const earlier = optionalDay("earlierContributionLatestDueDay");
  if (next === null || determination === null || earlier === null) {
    return stop("unknown", "invalid_date", "Supply each optional date as YYYY-MM-DD or omit it.");
  }
  if (next !== undefined && next <= qe) {
    return stop("refused", "next_standard_qe_day", "The next standard QE day must be after the out-of-cycle QE day.");
  }
  const horizon = () => stop("refused", "calendar_horizon", `Every day counted must lie within the verified business-day calendar, ${rules.calendar.verified_from} to ${rules.calendar.verified_until}.`);
  if ([qe, next, determination, earlier].some((day) => day !== undefined && (day < calendarStart || day > calendarEnd))) return horizon();

  const candidates = [["usual_period", businessDaysAfter(qe, 7)]];
  if (first) candidates.push(["item_1", businessDaysAfter(qe, 20)]);
  if (next !== undefined) candidates.push(["item_2", businessDaysAfter(next, 7)]);
  if (determination !== undefined) {
    const ownPeriod = businessDaysAfter(qe, 20);
    const afterDetermination = businessDaysAfter(determination, 20);
    candidates.push(["item_3", ownPeriod === null || afterDetermination === null ? null : Math.max(ownPeriod, afterDetermination)]);
  }
  if (earlier !== undefined) candidates.push(["item_4", earlier]);
  if (candidates.some(([, day]) => day === null)) return horizon();

  // The latest day of any applicable period; a tie keeps the earlier-listed rule.
  let [governingRule, due] = candidates[0];
  for (const [rule, day] of candidates) if (day > due) [governingRule, due] = [rule, day];
  const holidaysInWindow = [...holidays]
    .filter(([day]) => day > qe && day <= due)
    .map(([, holiday]) => ({ ...holiday, jurisdictions: [...holiday.jurisdictions] }));
  return {
    ...base,
    verdict: "latest_receipt_day_calculated",
    reason_codes: ["caller_supplied_inputs", governingRule],
    reasons: [
      "The QE day and every extension are caller-supplied; this calculator has not verified them.",
      governingRule === "usual_period"
        ? "The usual period of 7 business days governs."
        : `s 18C(2) ${governingRule.replace("_", " ")} gives the latest day; establish its conditions before relying on it.`,
    ],
    qeDay: input.qeDay,
    periods: Object.fromEntries(candidates.map(([rule, day]) => [rule, isoDate(day)])),
    latestReceiptDay: isoDate(due),
    governingRule,
    holidaysInWindow,
  };
}
