// SPDX-License-Identifier: AGPL-3.0-only
// Copyright 2026 Ryan Duguid
// Adapted from the author's Australian Accounting PAYG worksheets.
import rules from './rules.json' with { type: 'json' };

const periodWeeks = { weekly: [1n, 1n], fortnightly: [2n, 1n], monthly: [13n, 3n], quarterly: [13n, 1n] };
const priorPayLimits = { weekly: 52, fortnightly: 26, monthly: 11 };
const maximumPay = 100_000_000_000_000n; // cents
const sourceDetails = { as_of: rules.as_of, sources: rules.sources };

function result(verdict, code, reason) {
  return { verdict, reason_codes: [code], reasons: [reason], ...sourceDetails };
}

function amount(value) {
  if (typeof value !== 'string' || value.length > 16) return null;
  const match = /^(0|[1-9]\d{0,12})(?:\.(\d{1,2}))?$/.exec(value);
  if (!match || match[0] !== value) return null;
  const cents = BigInt(match[1]) * 100n + BigInt((match[2] ?? '').padEnd(2, '0'));
  return cents <= maximumPay ? cents : null;
}

function money(cents) {
  return `${cents / 100n}.${String(cents % 100n).padStart(2, '0')}`;
}

function yearOf(date) {
  if (typeof date !== 'string' || date.length !== 10 || !/^\d{4}-\d{2}-\d{2}$/.test(date)) return null;
  const time = Date.parse(`${date}T00:00:00Z`);
  if (!Number.isFinite(time) || new Date(time).toISOString().slice(0, 10) !== date) return null;
  return Number(date.slice(0, 4)) - Number(date.slice(5, 7) < '07');
}

function roundPositive(numerator, denominator) {
  return numerator > 0n ? (numerator + denominator / 2n) / denominator : 0n;
}

function coefficient(decimal) {
  const unsigned = decimal.replace(/^-/, '');
  const [whole, fraction = ''] = unsigned.split('.');
  const scaled = BigInt(whole) * 10_000n + BigInt(fraction.padEnd(4, '0'));
  return decimal.startsWith('-') ? -scaled : scaled;
}

function weeklyEarnings(earnings, period) {
  const [weeks, denominator] = periodWeeks[period];
  const adjusted = period === 'monthly' && earnings % 100n === 33n ? earnings + 1n : earnings;
  return (adjusted * denominator / (weeks * 100n)) * 100n + 99n;
}

function weeklyWithholding(weeklyCents, rows) {
  const [, a, b] = rows.find(([upper]) => upper === null || weeklyCents < BigInt(upper) * 100n);
  return roundPositive(coefficient(a) * weeklyCents - coefficient(b) * 100n, 1_000_000n);
}

function perPeriod(weekly, period) {
  const [weeks, denominator] = periodWeeks[period];
  return roundPositive(weekly * weeks, denominator);
}

function levyAdjustment(weekly, tableYear, scale, children) {
  const { familyThreshold, perChild, [scale]: row } = rules.medicare[tableYear];
  const family = roundPositive((BigInt(familyThreshold) + BigInt(perChild) * children) * 100n, 52n);
  const shadeOut = (family * 5n / 400n) * 100n;
  if (weekly < BigInt(row.threshold) * 100n || weekly >= shadeOut) return 0n;
  const fullRate = scale === 2 ? 2n : 1n;
  if (weekly < BigInt(row.shadeInLimit) * 100n) {
    return roundPositive((weekly - BigInt(row.shadeInBaseCents)) * fullRate * 5n, 10_000n);
  }
  if (weekly < family) return roundPositive(weekly * fullRate, 10_000n);
  return roundPositive((family - (weekly - family) * 4n) * fullRate, 10_000n);
}

function validatePay(input) {
  if (!input || input.scopeConfirmed !== true || typeof input.studyLoan !== 'boolean') {
    return result('unknown', 'scope_unconfirmed', 'Confirm the payment scope and whether a study loan component applies.');
  }
  const { period, scale, payDate, studyLoan, foreignResident, taxOffsets, medicareChildren, extraPay } = input;
  if (typeof period !== 'string' || !Object.hasOwn(periodWeeks, period) || ![1, 2, 3, 4, 5, 6].includes(scale)) {
    return result('unknown', 'invalid_pay_period_or_scale', 'Supply a supported pay period and a confirmed Schedule 1 scale.');
  }
  const year = yearOf(payDate);
  if (!year) return result('unknown', 'invalid_pay_date', 'Supply the actual payment date.');
  if (year < 2024 || year > 2026) return result('refused', 'unsupported_pay_date', 'Use a payment from 1 July 2024 to 30 June 2027.');
  if (scale === 4 ? typeof foreignResident !== 'boolean' : foreignResident !== undefined) {
    return result('unknown', 'invalid_residency', 'Confirm residency for the no-TFN scale only.');
  }
  if (taxOffsets !== undefined && (![2, 5, 6].includes(scale) || amount(taxOffsets) === null)) {
    return result('refused', 'invalid_offset', 'Supply an authorised annual tax offset as a decimal string on scale 2, 5 or 6.');
  }
  if (medicareChildren !== undefined && (![2, 6].includes(scale) || !Number.isSafeInteger(medicareChildren) || medicareChildren < 0)) {
    return result('refused', 'invalid_medicare_adjustment', 'Supply the confirmed number of dependent children for a levy adjustment on scale 2 or 6.');
  }
  if (extraPay !== undefined && (typeof extraPay !== 'boolean' || (extraPay && !['weekly', 'fortnightly'].includes(period)))) {
    return result('refused', 'invalid_extra_pay', 'Use the 53- or 27-pay addition only for weekly or fortnightly earnings when requested.');
  }
  const loan = rules.schedule8[year];
  if (studyLoan && (!loan || payDate < loan.from || scale === 4 || taxOffsets !== undefined || medicareChildren !== undefined || extraPay)) {
    return result('refused', 'unsupported_study_loan_case', 'Check the applicable Schedule 8 date, declaration, scale and adjustments.');
  }
  return { year, tableYear: year === 2026 ? 2026 : 2024, period, scale, payDate, studyLoan, foreignResident, taxOffsets, medicareChildren, extraPay };
}

function withholding(cents, pay) {
  const { period, scale, year, tableYear, foreignResident, taxOffsets, medicareChildren, extraPay, studyLoan } = pay;
  if (scale === 4) {
    const rate = foreignResident ? rules.noTfnRate.foreign : rules.noTfnRate.resident;
    return { tax: (cents / 100n) * BigInt(rate) / 100n, loan: 0n };
  }
  const weekly = weeklyEarnings(cents, period);
  const before = perPeriod(weeklyWithholding(weekly, rules.schedule1[tableYear][scale]), period);
  const offset = taxOffsets === undefined ? 0n : roundPositive(amount(taxOffsets) * BigInt(rules.offsetRates[period]), 100_000n);
  const medicare = medicareChildren === undefined ? 0n : perPeriod(levyAdjustment(weekly, tableYear, scale, BigInt(medicareChildren)), period);
  if (offset + medicare > before) return null;
  const extra = extraPay ? rules.extraPay[tableYear][period].findLast(([from]) => cents >= BigInt(from) * 100n)?.[1] ?? 0 : 0;
  const loanRows = studyLoan ? rules.schedule8[year][scale === 1 ? 'noThreshold' : 'threshold'] : null;
  return {
    tax: before - offset - medicare + BigInt(extra),
    loan: loanRows ? perPeriod(weeklyWithholding(weekly, loanRows), period) : 0n,
  };
}

function amounts(tax, loan) {
  return { taxWithholding: money(tax * 100n), studyLoanWithholding: money(loan * 100n), withholding: money((tax + loan) * 100n) };
}

function calculated(pay, values) {
  return { verdict: 'calculated', ...sourceDetails, financialYear: `${pay.year}-${String(pay.year + 1).slice(-2)}`, ...values };
}

export function calculatePaygWithholding(input) {
  const pay = validatePay(input);
  if (pay.verdict) return pay;
  const earnings = amount(input.earnings);
  if (earnings === null) return result('unknown', 'invalid_earnings', 'Supply gross taxable earnings as a non-negative decimal string.');
  const withheld = withholding(earnings, pay);
  if (!withheld) return result('refused', 'excess_adjustments', 'Reconcile the offsets and levy adjustment with the withholding before applying them.');
  return calculated(pay, amounts(withheld.tax, withheld.loan));
}

export function grossUpPaygWithholding(input) {
  const pay = validatePay(input);
  if (pay.verdict) return pay;
  if (pay.taxOffsets !== undefined || pay.medicareChildren !== undefined || pay.extraPay) {
    return result('refused', 'gross_up_adjustments', 'Use the gross-up only for regular pay with no extra withholding or adjustments.');
  }
  const net = amount(input.netPay);
  if (net === null) return result('unknown', 'invalid_net_pay', 'Supply net pay as a non-negative decimal string.');
  const bound = pay.studyLoan ? 2n * (net / 100n) + 98n : net / 100n + 52n;
  if (net + bound * 100n > maximumPay) return result('refused', 'gross_up_amount_limit', 'The search would exceed the supported gross pay limit.');
  function withheldAt(candidate) {
    const { tax, loan } = withholding(net + candidate * 100n, pay);
    return tax + loan;
  }
  // Whole-dollar withholding is nondecreasing in gross pay. Iteration from
  // zero and a proven upper bound reaches the least and greatest fixed points.
  function settle(candidate) {
    for (let next = withheldAt(candidate); next !== candidate; next = withheldAt(candidate)) candidate = next;
    return candidate;
  }
  const least = settle(0n);
  const greatest = settle(bound);
  const grossAmounts = [];
  for (let candidate = least; candidate <= greatest; candidate++) {
    if (withheldAt(candidate) === candidate) grossAmounts.push(money(net + candidate * 100n));
  }
  if (grossAmounts.length > 1) {
    return { ...result('refused', 'gross_up_not_unique', 'Multiple gross amounts leave this net. Use the gross amount in the pay agreement.'), grossCandidates: grossAmounts };
  }
  const { tax, loan } = withholding(net + least * 100n, pay);
  return calculated(pay, { netPay: money(net), grossPay: grossAmounts[0], ...amounts(tax, loan) });
}

export function calculateMethodBi(input) {
  const pay = validatePay(input);
  if (pay.verdict) return pay;
  if (!Object.hasOwn(priorPayLimits, pay.period) || pay.scale === 4 || pay.taxOffsets !== undefined || pay.medicareChildren !== undefined || pay.extraPay) {
    return result('refused', 'unsupported_method_b_i', 'Use Method B(i) for ordinary weekly, fortnightly or monthly back payments in this scope.');
  }
  if (pay.studyLoan && pay.year === 2025) {
    return result('refused', 'study_loan_schedule_change', 'Reconcile the 2025-26 change in Schedule 8 separately before using Method B(i).');
  }
  const earnings = amount(input.earnings);
  const prior = input.priorPeriods;
  if (earnings === null || !Array.isArray(prior) || prior.length < 1 || prior.length > priorPayLimits[pay.period]) {
    return result('unknown', 'invalid_back_pay_periods', 'Supply current earnings and the affected prior periods.');
  }
  const seen = new Set();
  const periods = [];
  let backPay = 0n;
  let difference = 0n;
  for (const item of prior) {
    const date = item?.payDate;
    const pastEarnings = amount(item?.earnings);
    const increase = amount(item?.backPayment);
    const withheld = amount(item?.withheld);
    if (yearOf(date) !== pay.year || date >= pay.payDate || seen.has(date) || pastEarnings === null || increase === null || increase === 0n || withheld === null || withheld % 100n !== 0n || pastEarnings + increase > maximumPay) {
      return result('refused', 'invalid_affected_period', 'Check the prior payment date, ordinary earnings, back payment and whole-dollar withholding for each distinct period.');
    }
    seen.add(date);
    const updated = withholding(pastEarnings + increase, pay);
    difference += updated.tax + updated.loan - withheld / 100n;
    backPay += increase;
    periods.push({ payDate: date, recalculatedWithholding: money((updated.tax + updated.loan) * 100n) });
  }
  const additional = difference > 0n ? difference : 0n;
  const current = withholding(earnings, pay);
  return calculated(pay, {
    backPay: money(backPay), backPayWithholding: money(additional * 100n),
    currentPayWithholding: money((current.tax + current.loan) * 100n),
    withholding: money((current.tax + current.loan + additional) * 100n), periods,
  });
}
