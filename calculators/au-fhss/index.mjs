// SPDX-License-Identifier: AGPL-3.0-only
// Copyright 2026 Ryan Duguid
// Adapted from the author's Australian Accounting FHSS worksheet.
import rules from './rules.json' with { type: 'json' };

const millisecondsPerDay = 86_400_000;
const moneyPattern = /^(0|[1-9]\d{0,14})(?:\.(\d{1,2}))?$/;
const annualLimit = 1_500_000n;
const isRecord = (value) => value !== null && typeof value === 'object' && !Array.isArray(value);
const min = (left, right) => left < right ? left : right;

function cents(value) {
  if (typeof value !== 'string' || value.length > 18) return null;
  const match = moneyPattern.exec(value);
  if (!match || match[0] !== value) return null;
  return BigInt(match[1]) * 100n + BigInt((match[2] ?? '').padEnd(2, '0'));
}

function money(value) {
  return `${value / 100n}.${String(value % 100n).padStart(2, '0')}`;
}

function parseDate(value) {
  if (typeof value !== 'string' || value.length !== 10 || !/^\d{4}-\d{2}-\d{2}$/.test(value)) return null;
  const milliseconds = Date.parse(`${value}T00:00:00Z`);
  if (!Number.isFinite(milliseconds) || new Date(milliseconds).toISOString().slice(0, 10) !== value) return null;
  const calendarYear = Number(value.slice(0, 4));
  const month = Number(value.slice(5, 7));
  return { day: milliseconds / millisecondsPerDay, year: calendarYear - Number(month < 7) };
}

function yearLabel(year) {
  return `${year}-${String((year + 1) % 100).padStart(2, '0')}`;
}

function invalid(verdict, code, reason) {
  return { verdict, reason_codes: [code], reasons: [reason], as_of: rules.as_of, sources: rules.sources };
}

function parseContributions(items, determinationDay) {
  if (!Array.isArray(items) || items.length > 1_000) return null;
  const firstDay = parseDate(rules.first_contribution_date).day;
  const pieces = [];
  const sequencedDays = new Map();
  for (const [index, item] of items.entries()) {
    if (!isRecord(item) || !['personal', 'employer_voluntary'].includes(item.kind)) return null;
    const date = parseDate(item.date);
    const amount = cents(item.amount);
    if (!date || date.day < firstDay || date.day > determinationDay || amount === null || amount === 0n) return null;
    const sequence = item.orderWithinDay;
    const hasSequence = sequence !== undefined;
    if (hasSequence && (!Number.isSafeInteger(sequence) || sequence < 0)) return null;
    if (sequencedDays.has(date.day) && !(sequencedDays.get(date.day) && hasSequence)) return null;
    sequencedDays.set(date.day, hasSequence);
    pieces.push({ index, ...date, date: item.date, sequence: sequence ?? 0, amount, personal: item.kind === 'personal' });
  }
  return pieces.sort((left, right) => left.day - right.day || left.sequence - right.sequence || left.index - right.index);
}

function splitPersonal(pieces, deductions) {
  if (!isRecord(deductions)) return null;
  const totalByYear = new Map();
  for (const piece of pieces.filter((piece) => piece.personal)) {
    totalByYear.set(piece.year, (totalByYear.get(piece.year) ?? 0n) + piece.amount);
  }
  const remainingAfterTax = new Map();
  const mixedYears = new Set();
  if (Object.keys(deductions).length !== totalByYear.size) return null;
  for (const [year, total] of totalByYear) {
    const key = yearLabel(year);
    const deducted = Object.hasOwn(deductions, key) ? cents(deductions[key]) : null;
    if (deducted === null || deducted > total) return null;
    remainingAfterTax.set(year, total - deducted);
    if (deducted > 0n && deducted < total) mixedYears.add(year);
  }

  const parts = [];
  for (const piece of pieces) {
    if (!piece.personal) {
      parts.push({ ...piece, concessional: true });
      continue;
    }
    const afterTax = min(remainingAfterTax.get(piece.year), piece.amount);
    remainingAfterTax.set(piece.year, remainingAfterTax.get(piece.year) - afterTax);
    if (afterTax > 0n) parts.push({ ...piece, amount: afterTax, concessional: false });
    const deducted = piece.amount - afterTax;
    if (deducted > 0n) parts.push({ ...piece, amount: deducted, concessional: true });
  }

  function orderWithinYear(left, right) {
    const hasMixedPersonal = mixedYears.has(left.year);
    if (hasMixedPersonal && left.concessional !== right.concessional) return Number(left.concessional) - Number(right.concessional);
    return left.day - right.day || left.sequence - right.sequence
      || Number(left.concessional) - Number(right.concessional) || left.index - right.index;
  }
  return parts.sort((left, right) => left.year - right.year || orderWithinYear(left, right));
}

function earningsFactor(start, end) {
  let numerator = 1n;
  let denominator = 1n;
  for (const [index, annualRateBasisPoints] of rules.sic_annual_basis_points.entries()) {
    const quarter = 2 + index;
    const calendarYear = 2017 + Math.floor(quarter / 4);
    const firstMonth = (quarter % 4) * 3;
    const firstDay = Date.UTC(calendarYear, firstMonth, 1) / millisecondsPerDay;
    if (firstDay > end) break;
    const nextQuarter = Date.UTC(calendarYear, firstMonth + 3, 1) / millisecondsPerDay;
    if (nextQuarter <= start) continue;
    const days = BigInt(Math.min(end + 1, nextQuarter) - Math.max(start, firstDay));
    const daysInYear = BigInt((Date.UTC(calendarYear + 1, 0, 1) - Date.UTC(calendarYear, 0, 1)) / millisecondsPerDay);
    const dailyDenominator = daysInYear * 10_000n;
    numerator *= (dailyDenominator + BigInt(annualRateBasisPoints)) ** days;
    denominator *= dailyDenominator ** days;
  }
  return { numerator: numerator - denominator, denominator: denominator * 10_000n };
}

function countContributions(parts, lifetimeLimit, lastDay) {
  const yearly = new Map();
  const earningsByContribution = new Map();
  const rows = [];
  let totalCounted = 0n;
  let concessional = 0n; // hundredths of one cent after the 85% factor
  let nonConcessional = 0n;
  for (const part of parts) {
    const usedInYear = yearly.get(part.year) ?? 0n;
    const counted = min(part.amount, min(annualLimit - usedInYear, lifetimeLimit - totalCounted));
    yearly.set(part.year, usedInYear + counted);
    totalCounted += counted;
    const earningsBase = counted * (part.concessional ? 85n : 100n);
    if (part.concessional) concessional += earningsBase;
    else nonConcessional += counted;
    if (earningsBase > 0n) {
      const start = part.year === 2017 ? rules.first_contribution_date : `${part.date.slice(0, 7)}-01`;
      const entry = earningsByContribution.get(part.index) ?? { start, base: 0n };
      entry.base += earningsBase;
      earningsByContribution.set(part.index, entry);
    }
    rows.push({ contribution: part.index + 1, date: part.date, classification: part.concessional ? 'concessional' : 'non_concessional', counted: money(counted) });
  }
  const factors = new Map();
  let earnings = 0n;
  for (const { start, base } of earningsByContribution.values()) {
    if (!factors.has(start)) factors.set(start, earningsFactor(parseDate(start).day, lastDay));
    const factor = factors.get(start);
    earnings += base * factor.numerator / factor.denominator * 100n;
  }

  const concessionalCents = (concessional + 50n) / 100n;
  return {
    annualContributionLimit: money(annualLimit),
    lifetimeContributionLimit: money(lifetimeLimit),
    totalContributionsCounted: money(totalCounted),
    concessionalReleasableEstimate: money(concessionalCents),
    nonConcessionalReleasableEstimate: money(nonConcessional),
    associatedEarningsEstimate: money(earnings),
    maximumReleaseEstimate: money(concessionalCents + nonConcessional + earnings),
    contributions: rows,
  };
}

export function estimateFhssRelease(input) {
  if (!isRecord(input) || input.contributionFactsConfirmed !== true) {
    return invalid('unknown', 'contribution_facts_unconfirmed', 'Confirm the supplied dates, classifications, contribution eligibility and personal deductions.');
  }
  const requested = parseDate(input.determinationRequested);
  const determined = parseDate(input.determinationDate);
  if (!requested || !determined || requested.day > determined.day) {
    return invalid('unknown', 'invalid_determination_dates', 'Supply valid request and determination dates in order.');
  }
  if (requested.day < parseDate(rules.first_request_date).day || determined.day > parseDate(rules.latest_sic_date).day) {
    return invalid('refused', 'unsupported_determination_date', 'Check the documented determination dates and published interest rates.');
  }
  const pieces = parseContributions(input.contributions, determined.day);
  if (!pieces) return invalid('unknown', 'invalid_contributions', 'Supply valid dated rows and explicit sequence for rows on the same date.');
  const parts = splitPersonal(pieces, input.personalDeductions);
  if (!parts) return invalid('unknown', 'invalid_deductions', 'Confirm a deduction total, including an explicit zero, for each year with personal contributions.');

  const lifetimeLimit = requested.day < parseDate('2022-07-01').day ? 3_000_000n : 5_000_000n;
  return {
    verdict: 'estimate', as_of: rules.as_of, sources: rules.sources, limits: rules.limits,
    ...countContributions(parts, lifetimeLimit, determined.day),
  };
}

export function summariseFhssRelease(input) {
  if (!isRecord(input) || input.atoDeterminationConfirmed !== true) {
    return invalid('unknown', 'ato_determination_unconfirmed', 'Use the stated ATO determination and actual released amount.');
  }
  const concessional = cents(input.concessional);
  const nonConcessional = cents(input.nonConcessional);
  const earnings = cents(input.associatedEarnings);
  const actual = cents(input.actualReleased);
  if ([concessional, nonConcessional, earnings, actual].includes(null)) {
    return invalid('unknown', 'invalid_determination_amount', 'Supply exact non-negative Australian dollar amounts as decimal strings.');
  }
  const maximum = concessional + nonConcessional + earnings;
  if (actual > maximum) return invalid('refused', 'release_above_maximum', 'Reconcile the released amount with the determination before using it.');
  const assessable = actual > nonConcessional ? actual - nonConcessional : 0n;
  return {
    verdict: 'calculated_from_determination',
    as_of: rules.as_of,
    sources: rules.sources,
    maximumRelease: money(maximum),
    assessableReleased: money(assessable),
    taxOffset: money((assessable * 30n + 50n) / 100n),
  };
}
