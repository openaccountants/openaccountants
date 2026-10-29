Independent review: 52 figures checked against gesetze-im-internet.de (EStG §§ 3, 6, 8, 19, 19a, 37b, 40, 40b, 52, 100; SvEV §§ 1 to 3; SGB IV §§ 7a, 14; BetrAVG § 1a; SolzG § 4), SVBezGrV 2026, BGBl. 2024 I No. 108, BGBl. 2026 I No. 14, R 8.1(9) LStR and the BMF letters of 3 March 2022, 5 November 2021 and 19 May 2015, plus the BSG decision and hearing report.

Fixed:
- Company cars: added the EUR 60,000 quarter-rate cap for cars bought 2019 to 2023 (§ 52(12) sentence 4; BMF 5 Nov 2021 Rn. 11), the half rate for 2019 to 2021 hybrids (50 g or 40 km, § 6(1) no. 4 sentence 2 no. 2) and for electric cars over the cap bought 2022 to 2024 (no. 4). The table had limited "over the cap" to 2025 to 2030.
- List price rounded down to the full EUR 100 after the quarter or half (R 8.1(9) no. 1 sentence 6 LStR; BMF 5 Nov 2021 Rn. 12). Also added the part-month rule. Removed from Not yet confirmed. Example 1 now uses EUR 64,050 to show the rounding.
- § 37b: EUR 10,000 per recipient a year is a cap (the excess is taxed normally), not a full exclusion; a single gift over EUR 10,000 is excluded in full (§ 37b(1) sentence 3; BMF 19 May 2015 Rn. 21). The calendar year counts for own employees (Rn. 4).
- Staff events: EUR 110 is limited to two events a year, includes VAT, and companions' share counts (§ 19(1) no. 1a sentences 2 to 5).
- § 19a: added the size test (twice the SME turnover and balance-sheet limits, four times headcount, six-year look-back) and the § 19a(4a) employer liability declaration.
- bAV: added the pre-2005 § 40b contracts (§ 52(40)) and the reduction of the § 3 no. 63 limit (§ 52(4) sentence 23); salary sacrifice into a direct promise or Unterstützungskasse is contribution-free only up to 4% (§ 14(1) sentence 2 SGB IV); § 100 changes from 1 Jan 2027 (EUR 360, EUR 1,200, 3% of the ceiling; BRSG II art. 2 no. 2, art. 18(4)). The 2026 figures (EUR 288, 2,575, 30,900, 960) are confirmed as in force for 2026.
- Example 2 changed to EUR 290 a month so it stays within 4%. At EUR 300 the total went over EUR 4,056, so the employer did not save contributions on the whole conversion, and the full 15% top-up the example assumed was not established (§ 1a(1a) BetrAVG: "soweit er ... einspart").
- Added the § 40(2) sentence 1 no. 4 25% rate on travel meal allowances, the § 3 no. 37 end date (§ 52(4) sentence 12), and the rule that directors with no share are always employed (BSG B 12 KR 13/17 R, headnote 1).

Confirmed: EUR 50 limit and voucher rule; § 8(3) 4% and EUR 1,080; 1%, 0.03%, 0.002%; the EUR 100,000 cap from 1 July 2025 and EUR 70,000 cap; the 50 g / 80 km and 60 km hybrid tests; SvEV 2026 values 345/71/137/137, 285, 5.01/4.10, the 1/30 rounding; EUR 60 meal; EUR 25/m2 flat; 30%, 25%, 15%, 20% rates; recreation grants 156/104/52; § 40(1) EUR 1,000; EUR 600, EUR 2,000; pension ceiling EUR 101,400; 8% = EUR 8,112, 4% = EUR 4,056; § 40b EUR 1,752; § 100 2026 figures; 15% top-up; § 7a procedure incl. (4a) to 30 June 2027; BSG 23 July 2026 casting-vote case and EUR 127,833.77; BMF company car letter (salary sacrifice is not a user charge, 180-day rule). Both examples recompute by hand and in check-examples.py.

Still not confirmed: other administrative car rules in R 8.1(9) LStR; staff-event and EUR 60 meal rules in the guidelines beyond the statute; church tax rates on flat taxes; whether a collective agreement can set aside the 15% top-up; the full reasons of the 23 July 2026 BSG judgment; wage tax treatment of the direct promise and Unterstützungskasse routes.

README: kept `partial: {}`. The skill covers all five gaps the old PR partial named: benefits in kind, company cars, § 37b and § 40, employer pensions through the three external routes plus salary sacrifice and § 100, and managing directors. Direct promise and Unterstützungskasse wage tax are a narrow gap, listed in the skill.

Sibling notes (not edited): de-payroll.md line 31 and germany-payroll.md lines 26 and 448 still list benefits in kind, company cars, § 37b/§ 40, employer pensions and managing directors as out of scope with no pointer. They could point to de-payroll-benefits. No figure contradictions found.


Pushed: ecc0b877 on pack/DE-payroll-benefits (review commit 25bcfe14 plus merge of origin/main). Ready to merge as a Source-cited draft: yes.
