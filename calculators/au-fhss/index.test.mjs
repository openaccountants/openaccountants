// SPDX-License-Identifier: AGPL-3.0-only
// Copyright 2026 Ryan Duguid
import { strict as assert } from 'node:assert';
import { test } from 'node:test';
import { estimateFhssRelease, summariseFhssRelease } from './index.mjs';

function contribution(date, amount, kind = 'employer_voluntary', orderWithinDay) {
  return { date, amount, kind, orderWithinDay };
}

function estimate(contributions, overrides = {}) {
  return estimateFhssRelease({
    contributionFactsConfirmed: true,
    determinationRequested: '2026-11-20',
    determinationDate: '2026-11-20',
    contributions,
    personalDeductions: {},
    ...overrides,
  });
}

test('applies the annual limit before 85% and selects the lifetime limit by request date', () => {
  const contributions = [
    contribution('2017-09-01', '16000'), contribution('2018-08-01', '15000'),
    contribution('2019-08-01', '15000'), contribution('2020-08-01', '15000'),
  ];
  const older = estimate(contributions, { determinationRequested: '2022-06-30', determinationDate: '2022-07-01' });
  const later = estimate(contributions, { determinationRequested: '2022-07-01', determinationDate: '2022-07-01' });
  assert.deepEqual(older.contributions.map((line) => line.counted), ['15000.00', '15000.00', '0.00', '0.00']);
  assert.equal(older.concessionalReleasableEstimate, '25500.00');
  assert.deepEqual(later.contributions.map((line) => line.counted), ['15000.00', '15000.00', '15000.00', '5000.00']);
  assert.equal(later.concessionalReleasableEstimate, '42500.00');
});

test('uses an earlier time first and gives a simultaneous after-tax contribution priority', () => {
  const salary = contribution('2026-09-01', '10000', 'employer_voluntary', 1);
  const personal = contribution('2026-09-01', '10000', 'personal', 2);
  const input = { personalDeductions: { '2026-27': '0' } };
  assert.equal(estimate([personal, salary], input).nonConcessionalReleasableEstimate, '5000.00');
  assert.equal(estimate([{ ...personal, orderWithinDay: 1 }, salary], input).nonConcessionalReleasableEstimate, '10000.00');
  assert.equal(estimate([{ ...personal, orderWithinDay: undefined }, salary], input).verdict, 'unknown');
});

test('splits partial personal deductions and preserves the source contribution numbers', () => {
  const output = estimate([
    contribution('2026-07-09', '10000'),
    contribution('2026-08-01', '7000', 'personal'),
    contribution('2026-09-01', '6000', 'personal'),
  ], { personalDeductions: { '2026-27': '10000' } });
  assert.deepEqual(output.contributions.map(({ contribution: row, classification, counted }) => [row, classification, counted]), [
    [2, 'non_concessional', '3000.00'], [1, 'concessional', '10000.00'],
    [2, 'concessional', '2000.00'], [3, 'concessional', '0.00'],
  ]);
  assert.equal(output.concessionalReleasableEstimate, '10200.00');
});

test('compounds each calendar day across quarterly and leap-year boundaries', () => {
  const end = '2024-04-02';
  const output = estimate([contribution('2024-03-31', '15000', 'personal')], {
    determinationRequested: end, determinationDate: end, personalDeductions: { '2023-24': '0' },
  });
  let balance = 15000;
  for (let day = 1; day <= 31; day++) balance *= 1 + 0.0738 / 366;
  for (let day = 1; day <= 2; day++) balance *= 1 + 0.0742 / 366;
  assert.equal(output.associatedEarningsEstimate, `${Math.floor(balance - 15000)}.00`);
});

test('replays the contribution history in GN 2024/1 example 6 as a statutory estimate', () => {
  const contributions = Array.from({ length: 52 }, (_, index) => {
    const month = 6 + index;
    const year = 2020 + Math.floor(month / 12);
    const monthNumber = String(month % 12 + 1).padStart(2, '0');
    return contribution(`${year}-${monthNumber}-15`, '1500');
  });
  const result = estimate(contributions, {
    determinationRequested: '2024-12-01', determinationDate: '2024-12-15',
  });
  assert.equal(result.verdict, 'estimate');
  assert.equal(result.concessionalReleasableEstimate, '42500.00');
  assert.equal(result.associatedEarningsEstimate, '7859.00');
  assert.equal(result.maximumReleaseEstimate, '50359.00');
  assert.equal(result.contributions[39].counted, '500.00');
  assert.equal(result.contributions[40].counted, '0.00');

  const assessment = summariseFhssRelease({
    atoDeterminationConfirmed: true, concessional: '42500', nonConcessional: '0',
    associatedEarnings: '5190', actualReleased: '47690',
  });
  assert.equal(assessment.verdict, 'calculated_from_determination');
  assert.equal(assessment.maximumRelease, '47690.00');
});

test('starts 2017-18 contributions on 1 July and floors earnings per input contribution', () => {
  const early = estimate([contribution('2017-07-01', '10000')], { determinationRequested: '2018-07-01', determinationDate: '2018-07-01' });
  const late = estimate([contribution('2018-06-30', '10000')], { determinationRequested: '2018-07-01', determinationDate: '2018-07-01' });
  assert.equal(early.associatedEarningsEstimate, late.associatedEarningsEstimate);
  const firstYear = 8500 * (1 + 0.0473 / 365) ** 92 * (1 + 0.047 / 365) ** 92
    * (1 + 0.0472 / 365) ** 90 * (1 + 0.0477 / 365) ** 91 * (1 + 0.0496 / 365);
  assert.equal(early.associatedEarningsEstimate, `${Math.floor(firstYear - 8500)}.00`);
  const december = { determinationRequested: '2026-12-01', determinationDate: '2026-12-01', personalDeductions: { '2026-27': '0' } };
  const rows = [contribution('2026-12-01', '3000', 'personal', 1), contribution('2026-12-01', '3000', 'personal', 2)];
  assert.equal(estimate(rows, december).associatedEarningsEstimate, '0.00');
  assert.equal(estimate([contribution('2026-12-01', '6000', 'personal')], december).associatedEarningsEstimate, '1.00');
});

test('requires confirmed facts, exact money, valid dates and complete personal deduction totals', () => {
  assert.equal(estimate([], { contributionFactsConfirmed: false }).verdict, 'unknown');
  assert.equal(estimate([contribution('2026-09-01', '1e2')]).verdict, 'unknown');
  assert.equal(estimate([contribution('2026-02-30', '100')]).verdict, 'unknown');
  assert.equal(estimate([contribution('2026-09-01', '10', 'personal')]).verdict, 'unknown');
  assert.equal(estimate([], { determinationDate: '2027-01-01' }).verdict, 'refused');
  assert.equal(estimate([]).maximumReleaseEstimate, '0.00');
});

test('derives assessment and offset from the stated actual release', () => {
  const inputs = { atoDeterminationConfirmed: true, concessional: '8500', nonConcessional: '2000', associatedEarnings: '500' };
  const partial = summariseFhssRelease({ ...inputs, actualReleased: '8035.17' });
  assert.equal(partial.verdict, 'calculated_from_determination');
  assert.equal(partial.maximumRelease, '11000.00');
  assert.equal(partial.assessableReleased, '6035.17');
  assert.equal(partial.taxOffset, '1810.55');
  assert.equal(summariseFhssRelease({ ...inputs, actualReleased: '1999' }).assessableReleased, '0.00');
  assert.equal(summariseFhssRelease({ ...inputs, actualReleased: '11000.01' }).verdict, 'refused');
  assert.equal(summariseFhssRelease({ ...inputs, atoDeterminationConfirmed: false, actualReleased: '8800' }).verdict, 'unknown');
});
