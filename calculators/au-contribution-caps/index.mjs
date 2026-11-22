// SPDX-License-Identifier: AGPL-3.0-only
// Copyright 2026 Ryan Duguid
// Adapted from the author's contribution-caps worksheet in australian-tax-calculators:
// https://github.com/ryanduguid/australian-accounting/tree/main/packages/australian-tax-calculators
// Pure, offline calculation. No clock, network, floating-point money or cap overrides.
import rules from "./rules.json" with { type: "json" };

const moneyPattern = /^(0|[1-9]\d{0,14})(?:\.(\d{1,2}))?$/;

// A non-negative AUD decimal string in cents, otherwise null.
function cents(value) {
  if (typeof value !== "string") return null;
  const match = moneyPattern.exec(value);
  return match ? BigInt(match[1]) * 100n + BigInt((match[2] ?? "").padEnd(2, "0")) : null;
}

const label = (start) => `${start}-${String((start + 1) % 100).padStart(2, "0")}`;

// The first calendar year of an income year written "YYYY-YY", otherwise null.
function yearStart(value) {
  if (typeof value !== "string" || !/^\d{4}-\d{2}$/.test(value)) return null;
  const start = Number(value.slice(0, 4));
  return label(start) === value ? start : null;
}

const formatMoney = (value) => `${value / 100n}.${String(value % 100n).padStart(2, "0")}`;
const smaller = (a, b) => (a < b ? a : b);
const positive = (value) => (value > 0n ? value : 0n);

const capOf = (start) => cents(rules.concessional_caps.amounts[label(start)]);
const firstUnusedYear = yearStart(rules.carry_forward.first_unused_year);
const previousYears = rules.carry_forward.previous_years;
const balanceLimit = cents(rules.carry_forward.total_super_balance_below);

// s 291-20(4) and (5): apply the unapplied unused cap of the 5 years before `start`,
// earliest year first, by no more than `excess`. Returns the total applied.
function applyUnused(pool, start, excess) {
  let applied = 0n;
  for (const entry of pool) {
    if (entry.start < start - previousYears) continue;
    const take = smaller(entry.left, excess - applied);
    entry.left -= take;
    applied += take;
  }
  return applied;
}

// Each earlier year's unused cap after the later earlier years applied it, or a stop.
function history(list, current) {
  const span = `each year from ${label(current - previousYears)} to ${label(current - 1)}`;
  if (list === undefined) {
    return { stop: ["unknown", "earlier_years_missing", `Below a $500,000 total superannuation balance the unused cap carried forward sets the cap (s 291-20(3)): supply earlierYears with ${span}.`] };
  }
  const invalid = { stop: ["unknown", "earlier_years_invalid", `earlierYears must list ${span} once, and may add earlier years back to 2018-19 without a gap: each with incomeYear, concessionalContributions and, where those exceed that year's cap, totalSuperBalanceBeforeYear.`] };
  if (!Array.isArray(list)) return invalid;
  const years = [];
  for (const item of list) {
    const start = yearStart(item?.incomeYear);
    const contributions = cents(item?.concessionalContributions);
    const balance = item?.totalSuperBalanceBeforeYear === undefined ? undefined : cents(item.totalSuperBalanceBeforeYear);
    if (start === null || contributions === null || balance === null) return invalid;
    if (start < firstUnusedYear) {
      return { stop: ["refused", "year_before_2018_19", `${label(start)} is before 2018-19: s 291-20(7) gives no unused cap for it, so leave it out.`] };
    }
    years.push({ start, contributions, balance });
  }
  years.sort((a, b) => a.start - b.start);
  const gapless = years.every((year, i) => year.start === years[0].start + i);
  if (!years.length || !gapless || years[0].start > current - previousYears || years.at(-1).start !== current - 1) return invalid;
  const pool = [];
  for (const year of years) {
    const cap = capOf(year.start);
    if (year.contributions > cap) {
      if (year.balance === undefined) {
        return { stop: ["unknown", "earlier_balance_missing", `${label(year.start)}'s concessional contributions exceed its cap: supply its totalSuperBalanceBeforeYear, which decides whether s 291-20(3)(b) increased that cap.`] };
      }
      if (year.balance < balanceLimit) {
        const from = Math.max(firstUnusedYear, year.start - previousYears);
        if (years[0].start > from) {
          return { stop: ["unknown", "earlier_years_short", `${label(year.start)}'s cap was increased from the unused cap of ${label(from)} onwards (s 291-20(4) and (5)): supply each year from ${label(from)}.`] };
        }
        applyUnused(pool, year.start, year.contributions - cap);
      }
    }
    const unused = positive(cap - year.contributions);
    pool.push({ start: year.start, unused, left: unused });
  }
  return { pool };
}

// Each flag that puts the case outside these rules: its reason code and why.
const exclusions = [
  ["definedBenefitInterest", "defined_benefit_interest", "A defined benefit interest changes what counts as concessional contributions (ITAA 1997 Subdivision 291-C); this calculator does not cover it."],
  ["constitutionallyProtectedFund", "constitutionally_protected_fund", "Contributions to a constitutionally protected fund count differently (ITAA 1997 ss 291-25(4)(a) and 292-90(2)(c)(iv)); this calculator does not cover them."],
  ["earlierBringForwardCoversYear", "bring_forward_later_year", "When an earlier bring forward makes this year its second year, or the third year of a 3-year bring forward, s 292-85(6) or (7) sets the cap from the first year's cap and contributions; this calculator works out only a year whose cap neither subsection determines (s 292-85(3)(d))."],
];

/**
 * @param {object} input
 * @param {string} input.incomeYear A supported income year, e.g. "2026-27".
 * @param {string} input.totalSuperBalanceBeforeYear Total superannuation balance just before the year (at 30 June).
 * @param {string} input.concessionalContributions The year's concessional contributions (s 291-25).
 * @param {string} input.nonConcessionalContributions The year's s 292-90(1)(a) and (aa) amounts, without excess concessional contributions.
 * @param {boolean} input.under75AtAnyTimeInYear s 292-85(3)(c).
 * @param {boolean} input.definedBenefitInterest true is refused.
 * @param {boolean} input.constitutionallyProtectedFund true is refused.
 * @param {boolean} input.earlierBringForwardCoversYear s 292-85(6) or (7) sets this year's cap; true is refused.
 * @param {Array<{incomeYear: string, concessionalContributions: string, totalSuperBalanceBeforeYear?: string}>} [input.earlierYears]
 *   Each of the previous 5 years; required when the balance is below $500,000.
 * @param {boolean} [input.excessConcessionalReleased] Required when the result has excess concessional contributions.
 * @returns {object} JSON-safe result; amounts are decimal strings or null.
 */
export function assessContributionCaps(input) {
  const base = {
    as_of: rules.as_of,
    currency: rules.currency,
    sources: [...rules.sources],
    limits: [...rules.limits],
    incomeYear: null,
    totalSuperBalanceBeforeYear: null,
    concessional: null,
    carryForward: null,
    nonConcessional: null,
  };
  const stop = (verdict, code, reason) => ({ ...base, verdict, reason_codes: [code], reasons: [reason] });
  if (!input || typeof input !== "object" || Array.isArray(input)) {
    return stop("unknown", "invalid_input", "Supply a record with the documented inputs.");
  }
  const current = yearStart(input.incomeYear);
  if (current === null || !rules.supported_years.includes(input.incomeYear)) {
    return stop("refused", "unsupported_year", `Select one of ${rules.supported_years.join(", ")}; no cap is assumed for another year.`);
  }
  for (const [key, code, reason] of exclusions) {
    if (input[key] === true) return stop("refused", code, reason);
    if (input[key] !== false) return stop("unknown", code, `State ${key} as true or false.`);
  }
  if (typeof input.under75AtAnyTimeInYear !== "boolean") {
    return stop("unknown", "age_test", "State under75AtAnyTimeInYear as true or false (s 292-85(3)(c)).");
  }
  const balance = cents(input.totalSuperBalanceBeforeYear);
  const concessional = cents(input.concessionalContributions);
  const nonConcessional = cents(input.nonConcessionalContributions);
  if (balance === null || concessional === null || nonConcessional === null) {
    return stop("unknown", "invalid_money", "Supply totalSuperBalanceBeforeYear, concessionalContributions and nonConcessionalContributions as non-negative AUD decimal strings with at most 2 decimal places; missing is not zero.");
  }

  const belowLimit = balance < balanceLimit;
  let pool = null;
  if (belowLimit || input.earlierYears !== undefined) {
    const found = history(input.earlierYears, current);
    if (found.stop) return stop(...found.stop);
    pool = found.pool;
  }
  const window = pool ? pool.filter((entry) => entry.start >= current - previousYears) : [];
  const carriedIn = window.map((entry) => entry.left);
  const generalCap = capOf(current);
  const increase = belowLimit && concessional > generalCap ? applyUnused(window, current, concessional - generalCap) : 0n;
  const cap = generalCap + increase;
  const excessConcessional = positive(concessional - cap);

  // s 292-90(1)(b): an unreleased excess counts as non-concessional contributions.
  if (excessConcessional > 0n && input.excessConcessionalReleased === true) {
    return stop("refused", "excess_released", "s 292-90(1A) reduces the excess counted as non-concessional contributions by each amount released, divided by 85%; this calculator does not apply a release.");
  }
  if (excessConcessional > 0n && input.excessConcessionalReleased !== false) {
    return stop("unknown", "excess_release_unknown", "The concessional contributions exceed the cap: state excessConcessionalReleased as true or false, since an unreleased excess counts as non-concessional contributions (s 292-90(1)(b)).");
  }
  const generalNonConcessionalCap = BigInt(rules.non_concessional.general_cap_multiple) * generalCap;
  const transferBalanceCap = cents(rules.non_concessional.general_transfer_balance_caps[input.incomeYear]);
  const counted = nonConcessional + excessConcessional;
  // s 292-85(2)(b), then (3)(b), (c) and (e), (4) and (5): the first year cap space sets the multiple.
  const capSpace = transferBalanceCap - balance;
  const multiple = !input.under75AtAnyTimeInYear || capSpace <= generalNonConcessionalCap ? null : capSpace > 2n * generalNonConcessionalCap ? 3n : 2n;
  const bringForwardCap = multiple === null ? null : multiple * generalNonConcessionalCap;
  const triggered = bringForwardCap !== null && counted > generalNonConcessionalCap;
  const nonConcessionalCap = capSpace <= 0n ? 0n : triggered ? bringForwardCap : generalNonConcessionalCap;
  const excessNonConcessional = positive(counted - nonConcessionalCap);

  const findings = [
    [increase > 0n, "carry_forward_applied", "Unused cap of earlier years increases this year's concessional cap (s 291-20(3) to (5))."],
    [excessConcessional > 0n, "excess_concessional", "Concessional contributions exceed the cap available (s 291-20(1)); the excess counts towards the non-concessional cap."],
    [triggered, "bring_forward_triggered", `Non-concessional contributions over the general cap start a ${multiple}-year bring forward period (s 292-85(3) and (5)).`],
    [excessNonConcessional > 0n, "excess_non_concessional", "Non-concessional contributions exceed the cap (s 292-85(2) to (5)); the excess becomes excess non-concessional contributions when the Commissioner determines it (s 292-85(1))."],
  ].filter(([applies]) => applies);
  return {
    ...base,
    verdict: "caps_calculated",
    reason_codes: ["caller_supplied_inputs", ...findings.map(([, code]) => code)],
    reasons: [
      "Every amount and fact is caller-supplied; this calculator has not verified them.",
      ...findings.map(([, , reason]) => reason),
    ],
    incomeYear: input.incomeYear,
    totalSuperBalanceBeforeYear: formatMoney(balance),
    concessional: {
      generalCap: formatMoney(generalCap),
      balanceBelowCarryForwardThreshold: belowLimit,
      unusedCapCarriedIn: pool ? formatMoney(carriedIn.reduce((sum, value) => sum + value, 0n)) : null,
      capIncrease: formatMoney(increase),
      cap: formatMoney(cap),
      contributions: formatMoney(concessional),
      excess: formatMoney(excessConcessional),
      unusedCapThisYear: formatMoney(positive(generalCap - concessional)),
    },
    carryForward: pool && {
      years: window.map((entry, i) => ({
        incomeYear: label(entry.start),
        unusedCap: formatMoney(entry.unused),
        carriedIn: formatMoney(carriedIn[i]),
        appliedThisYear: formatMoney(carriedIn[i] - entry.left),
        remaining: formatMoney(entry.left),
        expiresAtEndOf: label(entry.start + previousYears),
      })),
      expiringAtEndOfYear: formatMoney(window[0].left),
    },
    nonConcessional: {
      generalCap: formatMoney(generalNonConcessionalCap),
      generalTransferBalanceCap: formatMoney(transferBalanceCap),
      contributions: formatMoney(nonConcessional),
      excessConcessionalCounted: formatMoney(excessConcessional),
      contributionsCounted: formatMoney(counted),
      firstYearCapIfBringForwardStarts: bringForwardCap === null ? null : formatMoney(bringForwardCap),
      bringForwardTriggered: triggered,
      bringForwardYears: triggered ? Number(multiple) : null,
      cap: formatMoney(nonConcessionalCap),
      remaining: formatMoney(positive(nonConcessionalCap - counted)),
      excess: formatMoney(excessNonConcessional),
    },
  };
}
