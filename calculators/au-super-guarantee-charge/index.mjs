// SPDX-License-Identifier: AGPL-3.0-only
// Copyright 2026 Ryan Duguid
// Adapted from the author's SGC and Payday Super calculator on ryanduguid.github.io:
// https://github.com/ryanduguid/ryanduguid.github.io/blob/20b7d885510a764a62f63493ef7b07965435ead8/assets/sgc-payday.mjs
// Pure, offline calculation. No clock, network, floating-point money or rate overrides.
import rules from "./rules.json" with { type: "json" };
import { assessPaydaySuperTiming } from "../au-payday-super-timing/index.mjs";

const msPerDay = 86400000;
const datePattern = /^(\d{4})-(\d{2})-(\d{2})$/;
const moneyPattern = /^(0|[1-9]\d{0,14})(?:\.(\d{1,2}))?$/;
const ratePattern = /^(0|[1-9]\d?)(?:\.(\d{1,2}))?$/;

// Days since 1970-01-01 for a valid YYYY-MM-DD string, otherwise null.
function dayNumber(value) {
  if (typeof value !== "string") return null;
  const match = datePattern.exec(value);
  if (!match) return null;
  const time = Date.UTC(Number(match[1]), Number(match[2]) - 1, Number(match[3]));
  return new Date(time).toISOString().slice(0, 10) === value ? time / msPerDay : null;
}

const isoDate = (day) => new Date(day * msPerDay).toISOString().slice(0, 10);
const daysInYear = (day) => {
  const year = new Date(day * msPerDay).getUTCFullYear();
  return year % 4 === 0 && (year % 100 !== 0 || year % 400 === 0) ? 366n : 365n;
};

// A non-negative AUD decimal string in cents, otherwise null.
function cents(value) {
  if (typeof value !== "string") return null;
  const match = moneyPattern.exec(value);
  return match ? BigInt(match[1]) * 100n + BigInt((match[2] ?? "").padEnd(2, "0")) : null;
}

// An annual percentage string such as "11.51" in hundredths of 1%, above nil, otherwise null.
function hundredths(value) {
  if (typeof value !== "string") return null;
  const match = ratePattern.exec(value);
  const rate = match ? BigInt(match[1]) * 100n + BigInt((match[2] ?? "").padEnd(2, "0")) : 0n;
  return rate > 0n ? rate : null;
}

const formatMoney = (value) => `${value / 100n}.${String(value % 100n).padStart(2, "0")}`;
// numerator / denominator, both non-negative, to the nearest whole unit, half up.
const roundHalfUp = (numerator, denominator) => (2n * numerator + denominator) / (2n * denominator);
const min = (a, b) => (a < b ? a : b);

const qeFrom = dayNumber(rules.qe_days.from);
const qeTo = dayNumber(rules.qe_days.to);
const latestAssessment = dayNumber(rules.latest_assessment_day);
const maximumBase = cents(rules.maximum_contributions_base["2026-27"]);
const quarters = rules.notional_earnings.gic_quarters.map((quarter) => ({
  from: dayNumber(quarter.from),
  to: dayNumber(quarter.to),
  rate: hundredths(quarter.annual_percent),
}));
const tableEnd = quarters[quarters.length - 1].to;
const uplift = rules.administrative_uplift;
const timingKeys = ["qeDay", "firstContributionToFund", "outOfCycleNextStandardQeDay", "exceptionalCircumstancesDeterminationDay", "earlierContributionLatestDueDay"];

/**
 * @param {object} input
 * @param {string} input.qeDay Day the qualifying earnings were paid, "YYYY-MM-DD", 1 July 2026 to 30 June 2027.
 * @param {boolean} [input.firstContributionToFund] s 18C(2) item 1, as for au-payday-super-timing.
 * @param {string} [input.outOfCycleNextStandardQeDay] s 18C(2) item 2, as for au-payday-super-timing.
 * @param {string} [input.exceptionalCircumstancesDeterminationDay] s 18C(2) item 3, as for au-payday-super-timing.
 * @param {string} [input.earlierContributionLatestDueDay] s 18C(2) item 4, as for au-payday-super-timing.
 * @param {"general"|"norfolk_island_transitional"|"mixed"} input.sgRateSchedule
 *   Caller-confirmed classification of the QE day under Payday Super Act Sch 1 item 189.
 * @param {string} input.qualifyingEarnings Qualifying earnings paid to or for the employee on the QE day (s 17A(2)).
 * @param {string} input.earlierQualifyingEarningsThisYear Qualifying earnings from this employer earlier in 2026-27 (s 10A(6)).
 * @param {string} input.onTimeContributions Eligible contributions applied to this QE day under s 18C(1).
 * @param {{receivedDay: string, amount: string}[]} input.lateContributions Eligible contributions received in the
 *   late period and applied to this QE day under s 18D(2), each with the day the fund received it; [] when none.
 * @param {string} [input.assessmentDay] Day the assessment is made; required when the base shortfall is above nil.
 * @param {boolean} [input.noCommissionerInitiatedAssessmentOrEstimate] Reg 13C applies; required with a shortfall.
 * @param {string} [input.voluntaryDisclosureLodgedDay] Day a voluntary disclosure statement was lodged (reg 13D).
 * @param {string} [input.assumedGicAnnualPercent] Annual GIC rate assumed for days after the published table.
 * @returns {object} JSON-safe estimate; money is decimal strings, dates "YYYY-MM-DD", or null.
 */
export function assessSuperGuaranteeCharge(input) {
  const base = {
    as_of: rules.as_of,
    currency: rules.currency,
    sources: [...rules.sources],
    limits: [...rules.limits],
    rounding: rules.rounding,
    qeDay: null,
    latestReceiptDay: null,
    governingRule: null,
    sgAmount: null,
    baseShortfall: null,
    lateContributionsApplied: null,
    lateContributionsNotApplied: null,
    finalShortfall: null,
    notionalEarningsDays: null,
    notionalEarningsTo: null,
    assumedGicDays: null,
    notionalEarnings: null,
    upliftPercent: null,
    administrativeUplift: null,
    chargeBeforeChoiceLoading: null,
  };
  const stop = (verdict, code, reason) => ({ ...base, verdict, reason_codes: [code], reasons: [reason] });
  if (!input || typeof input !== "object" || Array.isArray(input)) {
    return stop("unknown", "invalid_input", "Supply a record with the documented inputs.");
  }
  const timing = assessPaydaySuperTiming(Object.fromEntries(timingKeys.filter((key) => key in input).map((key) => [key, input[key]])));
  if (timing.verdict !== "latest_receipt_day_calculated") return { ...base, verdict: timing.verdict, reason_codes: timing.reason_codes, reasons: timing.reasons };
  const qe = dayNumber(input.qeDay);
  if (qe > qeTo) {
    return stop("refused", "maximum_contributions_base", "Only QE days from 1 July 2026 to 30 June 2027 are covered: the maximum contributions base for a later year was not published on the check date.");
  }
  const due = dayNumber(timing.latestReceiptDay);
  const timed = { ...base, qeDay: input.qeDay, latestReceiptDay: timing.latestReceiptDay, governingRule: timing.governingRule };
  const fail = (verdict, code, reason) => ({ ...timed, verdict, reason_codes: [code], reasons: [reason] });

  const schedule = Object.hasOwn(input, "sgRateSchedule") ? input.sgRateSchedule : undefined;
  if (schedule === "norfolk_island_transitional" || schedule === "mixed") {
    return fail("refused", "norfolk_island_transition", "Review the QE day under Payday Super Act Sch 1 item 189. This worksheet only covers general-rate earnings.");
  }
  if (schedule !== "general") {
    return fail("unknown", "sg_rate_schedule", "Confirm sgRateSchedule as general, norfolk_island_transitional or mixed using Sch 1 item 189 and the QE day evidence.");
  }

  const earnings = cents(input.qualifyingEarnings);
  const earlier = cents(input.earlierQualifyingEarningsThisYear);
  const onTime = cents(input.onTimeContributions);
  if (earnings === null || earlier === null || onTime === null) {
    return fail("unknown", "invalid_money", 'Supply qualifyingEarnings, earlierQualifyingEarningsThisYear and onTimeContributions as non-negative AUD decimal strings with at most 2 decimal places; "0" when there is none, as missing is not zero.');
  }
  if (earnings === 0n) return fail("unknown", "nil_earnings", "Supply the qualifying earnings paid on the QE day, above nil.");
  if (!Array.isArray(input.lateContributions)) {
    return fail("unknown", "late_contributions", "Supply lateContributions as a list of { receivedDay, amount }, or [] when there are none.");
  }
  const late = [];
  for (const entry of input.lateContributions) {
    const day = entry && typeof entry === "object" ? dayNumber(entry.receivedDay) : null;
    const amount = entry && typeof entry === "object" ? cents(entry.amount) : null;
    if (day === null || amount === null || amount === 0n) {
      return fail("unknown", "late_contributions", "Each late contribution needs receivedDay as YYYY-MM-DD and an amount above nil as an AUD decimal string.");
    }
    if (day <= due) {
      return fail("refused", "received_on_time", `A contribution received by ${timing.latestReceiptDay} is on time: include it in onTimeContributions.`);
    }
    late.push({ day, amount });
  }
  late.sort((a, b) => a.day - b.day);

  // s 10A(6): earnings past the year's maximum contributions base count only to it; s 17A(2): 12% of them.
  const counted = min(earnings, maximumBase > earlier ? maximumBase - earlier : 0n);
  const sgAmount = roundHalfUp(counted * BigInt(rules.charge_percentage), 100n);
  const baseShortfall = sgAmount > onTime ? sgAmount - onTime : 0n;
  const amounts = { ...timed, sgAmount: formatMoney(sgAmount), baseShortfall: formatMoney(baseShortfall) };
  if (baseShortfall === 0n) {
    return {
      ...amounts,
      lateContributionsApplied: "0.00",
      lateContributionsNotApplied: formatMoney(late.reduce((total, entry) => total + entry.amount, 0n)),
      finalShortfall: "0.00",
      notionalEarningsDays: 0,
      assumedGicDays: 0,
      notionalEarnings: "0.00",
      administrativeUplift: "0.00",
      chargeBeforeChoiceLoading: "0.00",
      verdict: "no_shortfall",
      reason_codes: ["caller_attested_inputs", counted === 0n ? "maximum_contributions_base_reached" : "on_time_contributions_cover"],
      reasons: [
        "Every amount, date and answer is caller-attested; this calculator has not verified them.",
        counted === 0n
          ? "Earlier qualifying earnings in 2026-27 have reached the maximum contributions base, so the SG amount is nil (s 10A(6))."
          : "On-time contributions cover the SG amount, so there is no base shortfall and no SG charge for this QE day before any choice loading (ss 16B(1) and 18C).",
      ],
    };
  }
  const stopWith = (verdict, code, reason) => ({ ...amounts, verdict, reason_codes: [code], reasons: [reason] });
  const assessment = dayNumber(input.assessmentDay);
  if (assessment === null) return stopWith("unknown", "assessment_day", "Supply the day the assessment is made as YYYY-MM-DD: the late period ends the day before it.");
  if (assessment <= due || assessment > latestAssessment) {
    return stopWith("refused", "assessment_day", `The assessment day must be after ${timing.latestReceiptDay}, the last day for an on-time contribution, and no later than ${rules.latest_assessment_day}.`);
  }
  if (late.some((entry) => entry.day >= assessment)) {
    return stopWith("refused", "received_after_assessment", "A contribution the fund receives on or after the assessment day is not in the late period: leave it out.");
  }
  const flag = input.noCommissionerInitiatedAssessmentOrEstimate;
  if (typeof flag !== "boolean") {
    return stopWith("unknown", "regulation_13c", "State noCommissionerInitiatedAssessmentOrEstimate as true or false (reg 13C).");
  }
  let disclosure = null;
  if (input.voluntaryDisclosureLodgedDay !== undefined) {
    disclosure = dayNumber(input.voluntaryDisclosureLodgedDay);
    if (disclosure === null || disclosure < qe || disclosure >= assessment) {
      return stopWith("refused", "voluntary_disclosure", `A voluntary disclosure statement counts only if lodged from the QE day to ${isoDate(assessment - 1)}, before the day of the assessment (s 33(2)(a), reg 13D); omit it otherwise.`);
    }
  }

  // s 18D(2): late contributions apply in the order received, never below nil.
  let finalShortfall = baseShortfall;
  let cleared = null;
  for (const entry of late) {
    finalShortfall -= min(entry.amount, finalShortfall);
    if (finalShortfall === 0n && cleared === null) cleared = entry.day;
  }
  const lateTotal = late.reduce((total, entry) => total + entry.amount, 0n);
  const applied = baseShortfall - finalShortfall;

  // s 19A: each day from the day after the due day while the final shortfall is above nil, counting the receipt day of
  // the contribution that clears it, to the day before the assessment.
  const lastDay = cleared === null ? assessment - 1 : cleared;
  let assumed = null;
  if (lastDay > tableEnd) {
    assumed = hundredths(input.assumedGicAnnualPercent);
    if (assumed === null) {
      return stopWith("unknown", "assumed_gic_rate", `The late period runs past ${isoDate(tableEnd)}, the last published GIC quarter: supply assumedGicAnnualPercent, such as "11.51".`);
    }
  }
  let grown = baseShortfall;
  let scale = 1n;
  for (let day = due + 1; day <= lastDay; day += 1) {
    const rate = day > tableEnd ? assumed : quarters.find((quarter) => day >= quarter.from && day <= quarter.to)?.rate;
    if (rate === undefined) return stopWith("refused", "gic_rate", `No GIC rate is held for ${isoDate(day)}.`);
    const whole = 10000n * daysInYear(day);
    grown *= whole + rate;
    scale *= whole;
  }
  const notional = roundHalfUp(grown - baseShortfall * scale, scale);

  let percent = uplift.percent - (flag ? uplift.no_commissioner_initiated_assessment_reduction : 0);
  if (disclosure !== null) {
    const dayOfPeriod = disclosure - qe + 1;
    percent -= uplift.voluntary_disclosure.find((row) => row.lodged_by_day === null || dayOfPeriod <= row.lodged_by_day).reduction;
  }
  percent = Math.max(0, percent);
  const upliftAmount = roundHalfUp((finalShortfall + notional) * BigInt(percent), 100n);
  const days = lastDay - due;
  const assumedDays = assumed === null ? 0 : lastDay - Math.max(due, tableEnd);
  return {
    ...amounts,
    lateContributionsApplied: formatMoney(applied),
    lateContributionsNotApplied: formatMoney(lateTotal - applied),
    finalShortfall: formatMoney(finalShortfall),
    notionalEarningsDays: days,
    notionalEarningsTo: isoDate(lastDay),
    assumedGicDays: assumedDays,
    notionalEarnings: formatMoney(notional),
    upliftPercent: percent,
    administrativeUplift: formatMoney(upliftAmount),
    chargeBeforeChoiceLoading: formatMoney(finalShortfall + notional + upliftAmount),
    verdict: "charge_estimated",
    reason_codes: ["caller_attested_inputs", assumed === null ? "published_gic_rates" : "assumed_gic_rate"],
    reasons: [
      "Every amount, date and answer is caller-attested; this calculator has not verified them.",
      assumed === null
        ? "Every day of notional earnings uses a published GIC rate."
        : `${assumedDays} days of notional earnings use the assumed GIC rate of ${input.assumedGicAnnualPercent}% a year: recompute when the ATO publishes the rate.`,
    ],
  };
}
