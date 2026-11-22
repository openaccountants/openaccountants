// SPDX-License-Identifier: AGPL-3.0-only
// Copyright 2026 Ryan Duguid
import { strict as assert } from 'node:assert';
import { test } from 'node:test';
import { calculateMethodBi, calculatePaygWithholding, grossUpPaygWithholding } from './index.mjs';

const defaultPay = { scopeConfirmed: true, studyLoan: false, period: 'weekly', scale: 2, payDate: '2026-11-20' };

test('uses the payment date to select the tax tables', () => {
  const at = (payDate) => calculatePaygWithholding({ ...defaultPay, payDate, earnings: '1333.45' });
  assert.equal(at('2025-06-30').withholding, '250.00');
  assert.equal(at('2026-06-30').withholding, '250.00');
  assert.equal(at('2026-07-01').withholding, '245.00');
  assert.equal(at('2026-07-01').financialYear, '2026-27');
  assert.equal(at('2027-07-01').verdict, 'refused');
  assert.equal(at('2026-02-30').verdict, 'unknown');
});

test('uses the no-TFN rate on the pay as a whole and discards cents twice', () => {
  const at = (foreignResident) => calculatePaygWithholding({ ...defaultPay, period: 'quarterly', scale: 4, foreignResident, earnings: '1234.56' });
  assert.equal(at(false).withholding, '579.00');
  assert.equal(at(true).withholding, '555.00');
  assert.equal(at(undefined).verdict, 'unknown');
});

test('matches the Schedule 1 examples for Medicare adjustments and offsets', () => {
  assert.equal(calculatePaygWithholding({ ...defaultPay, earnings: '1333.45', medicareChildren: 5 }).withholding, '219.00');
  assert.equal(calculatePaygWithholding({ ...defaultPay, period: 'fortnightly', scale: 5, earnings: '1299.30', taxOffsets: '1645' }).withholding, '23.00');
  assert.equal(calculatePaygWithholding({ ...defaultPay, period: 'monthly', earnings: '5400.33', taxOffsets: '1365' }).withholding, '827.00');
  assert.equal(calculatePaygWithholding({ ...defaultPay, period: 'weekly', earnings: '1', taxOffsets: '1000' }).verdict, 'refused');
});

test('uses year-specific bands for an agreed 53rd or 27th pay', () => {
  for (const [payDate, period, earnings, difference] of [
    ['2026-11-20', 'weekly', '2575', 7], ['2025-11-20', 'weekly', '2575', 6],
    ['2026-11-20', 'fortnightly', '1700', 12], ['2025-11-20', 'fortnightly', '1700', 0],
    ['2026-11-20', 'fortnightly', '7250', 48], ['2025-11-20', 'fortnightly', '7250', 47],
  ]) {
    const input = { ...defaultPay, payDate, period, earnings };
    assert.equal(Number(calculatePaygWithholding({ ...input, extraPay: true }).withholding) - Number(calculatePaygWithholding(input).withholding), difference);
  }
});

test('rounds the study loan component separately and applies the monthly cent rule', () => {
  const loan = { ...defaultPay, studyLoan: true };
  const onWeekly = calculatePaygWithholding({ ...loan, earnings: '2608.36' });
  const onMonthly = calculatePaygWithholding({ ...loan, period: 'monthly', earnings: '5997.33' });
  assert.deepEqual([onWeekly.taxWithholding, onWeekly.studyLoanWithholding, onWeekly.withholding], ['654.00', '193.00', '847.00']);
  assert.deepEqual([onMonthly.taxWithholding, onMonthly.studyLoanWithholding, onMonthly.withholding], ['1131.00', '30.00', '1161.00']);
  assert.equal(calculatePaygWithholding({ ...loan, earnings: '1330', payDate: '2025-09-23' }).verdict, 'refused');
  assert.equal(calculatePaygWithholding({ ...loan, earnings: '1330', payDate: '2025-09-24' }).studyLoanWithholding, '6.00');
});

test('gross-up returns the unique gross or lists every candidate across monthly discontinuities', () => {
  const loan = { ...defaultPay, studyLoan: true };
  const one = grossUpPaygWithholding({ ...loan, netPay: '1761.36' });
  assert.deepEqual([one.grossPay, one.withholding], ['2608.36', '847.00']);
  const several = grossUpPaygWithholding({ ...loan, period: 'monthly', netPay: '4775.33' });
  assert.equal(several.verdict, 'refused');
  assert.deepEqual(several.grossCandidates, ['5884.33', '5893.33']);
  assert.equal(grossUpPaygWithholding({ ...defaultPay, netPay: '1e2' }).verdict, 'unknown');
  assert.equal(grossUpPaygWithholding({ ...defaultPay, netPay: '999999999999' }).verdict, 'refused');
});

test('recalculates Method B(i) per period and adds current pay withholding', () => {
  const payDates = ['2026-09-25', '2026-10-02', '2026-10-09', '2026-10-16', '2026-10-23', '2026-10-30', '2026-11-06', '2026-11-13'];
  const prior = payDates.map((payDate) => ({ payDate, earnings: '1600', backPayment: '100', withheld: '331' }));
  const run = (priorPeriods, rest = {}) => calculateMethodBi({ ...defaultPay, earnings: '1700', priorPeriods, ...rest });
  const tax = run(prior);
  const loan = run(prior.map((period) => ({ ...period, withheld: '371' })), { studyLoan: true });
  assert.deepEqual([tax.backPay, tax.backPayWithholding, tax.currentPayWithholding, tax.withholding], ['800.00', '256.00', '363.00', '619.00']);
  assert.deepEqual([loan.backPayWithholding, loan.currentPayWithholding, loan.withholding], ['376.00', '418.00', '794.00']);
  assert.equal(run([{ ...prior[0], withheld: '400' }]).backPayWithholding, '0.00');
  assert.equal(run([{ ...prior[0], withheld: '300' }]).backPayWithholding, '63.00');
  assert.equal(run([prior[0], prior[0]]).verdict, 'refused');
  assert.equal(run([{ ...prior[0], payDate: '2026-06-30' }]).verdict, 'refused');
});

test('ignores values outside the input contract and requires confirmed declarations', () => {
  const forged = calculatePaygWithholding({ ...defaultPay, earnings: '1333.45', year: 2024, tableYear: 2024 });
  assert.equal(forged.withholding, '245.00');
  assert.equal(calculatePaygWithholding({ ...defaultPay, studyLoan: undefined, earnings: '1000' }).verdict, 'unknown');
  assert.equal(calculatePaygWithholding({ ...defaultPay, period: ['weekly'], earnings: '1000' }).verdict, 'unknown');
});
