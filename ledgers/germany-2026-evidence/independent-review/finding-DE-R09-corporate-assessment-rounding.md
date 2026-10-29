# DE-R09: corporate assessment rounding

The frozen `de-corporate-tax` method states the 15% multiplication without the ordinary assessment rounding in KStG §31(1), sentence 2. The cited rule has already been actually read as corporate quote24; no new source acquisition is required.

Official source: https://www.gesetze-im-internet.de/kstg_1977/__31.html . Writer source `U816365676f95809c`, native reader LF7, reader SHA256 `0f17cad845ae999d270ae4cfe0acc0b54b8828885ac3cd017f6f569b2bc874a0`, raw SHA256 `1d6261f3a27fdf78e48767fce5234b13195922f07b70d4186dd01a016d9bf731`.

> Die sich im Zuge der Festsetzung ergebenden einzelnen Körperschaftsteuerbeträge sind jeweils zu Gunsten des Steuerpflichtigen auf volle Euro-Beträge zu runden.

**Option A (recommended):** add the exact bounded assessment step: round each individual assessed corporate-tax amount in the taxpayer's favour to whole euros under §31(1), sentence2. Keep this distinct from a claim to round every underlying base or every surcharge. For a positive assessment, taxable income EUR10,001 ×15%=EUR1,500.15 gives assessed KSt EUR1,500. Both original whole-KSt examples remain byte exact.

**Option B:** retain the multiplication as an intermediate amount and expressly route the final assessment rounding to §31(1), sentence2; do not label the unrounded intermediate final payable tax.

Priority: ordinary finite output-rule correction. No claim about refund rounding, all taxes' common rounding, or portal parity. Independent control saved in `de-corporate-tax-own-controls.json`.
