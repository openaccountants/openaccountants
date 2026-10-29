# DE-R12: trade-tax apportionment uses statutory wages, not all pay

`de-trade-tax` LF107 supplies a multi-municipality computation using wages paid at each establishment but omits the ordinary §31 wage adjustments. The cited own source already quotes these complete rules. In particular, trainee remuneration and one-off profit-based remuneration are excluded; other remuneration above EUR50,000 per employee is excluded. Overtime and Sunday/holiday/night supplements count regardless of income-tax treatment. The separate EUR25,000 working-owner amount for non-legal-person businesses remains unchanged. This is a material ordinary input-base condition, not a request for every special apportionment industry.

Official source https://www.gesetze-im-internet.de/gewstg/__31.html . B source DEB146/GT.ownerwages, actual reader `germany-ledger-writer-B-2026-10-29/readers/DEB146.txt`, literalLF7–11, reader SHA256 `2f305a64620e8172d7d6a3a2e56110d809ce1669d14bff861f0687697b90bd3b`. These five paragraphs were actually independently read in full while verifying trade quote26. §31(4) states:

> Nach dem Gewinn berechnete einmalige Vergütungen (z. B. Tantiemen, Gratifikationen) sind nicht anzusetzen. Das Gleiche gilt für sonstige Vergütungen, soweit sie bei dem einzelnen Arbeitnehmer 50.000 Euro übersteigen.

**Option A (recommended):** use qualifying statutory wages under §31, explicitly supply the common exclusions/per-person50,000 ceiling and supplement inclusion, then the existing §29 full1,000 rounding/key. Keep the25,000 owner addition and existing special-industry referral. Add the input questions needed for the wage base.

**Option B:** withdraw the unqualified wages-paid computation and explicitly refer the unsupplied §31 wage-base branch. This leaves the ordinary multi-establishment computation incomplete, so A is preferable.

Separating fictional control, ordinary company/two establishments/no trainee, profit-based bonus or other complication: A has one employee paid EUR100,000 and B one employee paid EUR50,000. The statutory wage base is EUR50,000 each, so a EUR1,000 base amount splits EUR500/EUR500, not two-thirds/one-third. No new common euro rounding or municipal-rate assumption is inferred. The original two single-municipality examples remain exact.
