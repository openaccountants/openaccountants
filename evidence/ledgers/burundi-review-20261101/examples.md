# Independent recomputation of the sixteen cases

Frozen candidate `124f6a7a00cbf173ddcd91a4c0ee81e5aa0f25bf`; read/recomputed 1 November 2026. Inputs are invented examples, not legal figures. Each applicable rate/regime was separately compared with its Guide's primary sources during the row review. The arithmetic below was recomputed independently of the author's `oa-check` evaluator; the repository checker then also passed all sixteen blocks.

| Guide / case | Independent calculation in BIF | Result and conditions |
|---|---|---|
| Company formation 1 | 1,000,000 capital + 200,000 company fee = 1,200,000 | Correct; chosen fully paid capital remains company property; excludes additional costs. |
| Company formation 2 | 200,000 company fee - 100,000 individual fee = 100,000; 2 SPRL founders - 1 actual founder = 1 | Correct; actual liability/entity choice cannot be made from fees alone. |
| Corporate income 1 | 20,000,000 accounting profit + 1,000,000 fine = 21,000,000 taxable; 30% = 6,300,000; 1% of 120,000,000 = 1,200,000 | Correct; ordinary tax governs; common expense-method omission is F1, not an arithmetic defect. |
| Corporate income 2 | 30% of 6,000,000 = 1,800,000; 1% of 300,000,000 = 3,000,000; each advance 4,000,000 / 4 = 1,000,000; three advances = 3,000,000 | Correct; minimum governs and balance is zero without withholding/credits. |
| Individual income 1 | 5,000,000 / 100 = 50,000 quarterly tax | Correct assuming annual turnover remains within 25m and no special final levy. |
| Individual income 2 | At 25m, annual sum of quarterly 1% = 250,000. At 26m and 10% margin, profit 2,600,000; 30% = 780,000, above minimum 260,000; difference 530,000 | Correct; factual threshold switch is mandatory, not an election. |
| Payroll 1 | Employee pension 450,000 x 4% = 18,000; employer pension 450,000 x 6% = 27,000; employer risk 80,000 x 3% = 2,400. Tax base 500,000 - 18,000 = 482,000; tax 150,000 x 20% + 182,000 x 30% = 84,600 | Correct; cash net 397,400; employer cost 529,400. Actual pension deduction and ordinary civilian regime are explicit; no health/foreign-labor assumptions. |
| Payroll 2 | Principal tax (200,000 - 150,000) x 20% = 10,000; secondary 200,000 x 30% = 60,000; difference 50,000 | Correct; status controls withholding, not a choice. |
| Overview 1 | 1,080,000 + 84,600 + 150,000 = 1,314,600; proposed payment less sum = zero | Correct; assumed outputs require separate tax allocation. |
| Overview 2 | 3 x 22,400 = 67,200; less last-month-only payment 22,400 = underpayment 44,800 | Correct; quarterly INSS frequency independently confirmed. |
| TP 1 | 12m charge - 9m supported price = 3m addback; 20m pre-adjustment profit + 3m = 23m; 30% = 6.9m | Correct; the supported comparator is explicitly hypothetical, no statutory markup asserted; minimum/credit tests remain separate. |
| TP 2 | Ceiling 20m x 30% = 6m; paid 8m + unpaid 1m - permitted 6m = disallowed 3m; if all 9m paid, ceiling still 6m | Correct under the expressly assumed entirely July-governed case; does not resolve annual cutover. |
| VAT 1 | Sales 10m x 18% = output 1.8m; eligible purchases 4m x 18% = input 720k; net 1.08m | Correct assuming actual entitlement, EBMS, verification and traceability conditions. |
| VAT 2 | Old threshold less 30m = 70m headroom; 30m less July threshold 25m = 5m excess; August sales 5m x 18% = 900k output | Correct for reaching the new threshold during July with no earlier independent trigger. This is not the unresolved already-over-threshold-before-July case. |
| Cross-border 1 | 10m gross x 15% = 1.5m withholding; supplier cash 8.5m | Correct assuming resident payer, nonresident service not attributed to PE, no established treaty relief/gross-up; VAT separate. |
| Cross-border 2 | Burundi tax 20m x 30% = 6m. Credit on foreign tax 4m = 4m, domestic balance 2m; on foreign tax 7m credit limited to 6m, balance zero and foreign excess 1m | Correct with stated evidence, rate and no minimum-tax interaction; not an automatic refund. |

No calculation fix was needed. The required tax, filing and evidence corrections in README.md remain material even though the examples recompute.
