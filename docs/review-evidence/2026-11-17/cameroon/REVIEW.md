# Cameroon: independent review and publication evidence

17 November 2026. Research review complete for the source bytes below. This is
not accountant approval, merge authorization or proof of platform delivery.

## Review binding

[PR #2139](https://github.com/openaccountants/openaccountants/pull/2139) source
head `9bc805584335c5e73f44e1b21eac9c947585b6e1` is byte-identical across all
eight Cameroon files to the independently reviewed candidate
`bec2283cf8e3ec05fca2922e43b2a02c0a8efb25` (lane 7, 15 November).
The [complete independent review, per-file reports, ledgers and original-topic
preservation evidence](https://github.com/openaccountants/openaccountants/pull/2139#issuecomment-6926963022)
cover 106 ledger rows, 1,080 original physical nonblank blocks and 110 independent
Decimal outputs. All ten first-pass findings were closed. These completed checks
are reused for identical bytes, not represented as newly performed full checks.
The final pack report SHA256 is
`09acd3949e95faa0ece9cfb7f553333e457bd21fb6a668d6d1daf57c69ef5634`;
its review-manifest SHA256 is
`e3561b2e231d8dcad9970634e4f1368efaca1b73e05582c05dc2a28d1fb1f7ce`.

Source-file SHA256s, relative to `skills/cameroon/`:

| File | SHA256 |
|---|---|
| README.md | `aeb2207777175bb1e1b9357a124f218147631c27ad895d8311e4043554d57b80` |
| cameroon-payroll.md | `bdac9f02d41481482acc1d4d0f4bcbd2ea040fc970d06dee3f4d1f202da200b8` |
| cameroon-social-contributions.md | `8736743bb7e26dafa66546960ef4f861b10e3edd83fabab0951cdb4499092137` |
| cameroon-vat.md | `1d2278acab9a7dd3dffbad9b9b1136c0b0b04fb18bf6888947cf5c462f7940b8` |
| cameroon-corporate-income-tax.md | `ccb02a871fb35aa71407c4b43dc5d7ed31a0c13c6481c6ffbbee9b7c862fcb6c` |
| cameroon-cross-border.md | `c807f590c2bca24a1804b9be011d2ddbbc63ba29ff90bbcc15aeff5748a1edd7` |
| cameroon-income-tax.md | `8b4bf7fda13d468ecbdea88ba982399762381dce4063879714b606c11432f553` |
| cameroon-transfer-pricing.md | `0d553c383378ea9532ad8c6a0597175d344d1db1fd61f6d808cd05adceb8da98` |

The last four passing siblings remain unchanged from main and are not reapproved.
Original human names, historical credit/identifier, approval fields, platform keys,
CTA blocks, calculator quotations, case facts and source-read dates are preserved.

## Actual figures result and source proof

The [exact-head hosted figures job](https://github.com/openaccountants/openaccountants/actions/runs/43940695514/job/133557111411)
checked 60 rows: **four MISS occurrences, zero UNREADABLE**. It exited 1; it did
not pass mechanically. The [17 November independent occurrence dispositions](https://github.com/openaccountants/openaccountants/pull/2139#issuecomment-6945019673)
provide the finite public proof:

| Occurrence | Disposition |
|---|---|
| Payroll 4,800,000 | CGI article 34 explicitly caps the annual 30% professional-expense deduction, separately from compulsory retirement contributions. Original numeral wraps between `4` and `800 000`; retained official text reread. |
| Payroll 60,000 | Decree 2023/00338/PM article 1, French physical page 1, visually reread: `60.000` monthly for other sectors; agriculture `45.000` is separate. Scanned OCR misreads the former. |
| Sources-scope 60,000 | Same source/page/amount; duplicate occurrence in the source-read description. |
| Social 36,270 | Explicitly rejected old floor and held as unconfirmed. No positive current-floor assertion or source proof is claimed. |

Earlier MISSes for 5,040 and 63,000 are absent from this hosted run. Both amounts
are printed on the [official CNPS voluntary page](https://www.cnps.cm/fr/?id=90&option=com_sppagebuilder&view=page)
and recompute at 8.4% of 60,000 and 750,000. Its full operative text was reopened
and read on 17 November. No concatenated-URL checker-bug diagnosis is claimed.

Retained official-source bytes were hash-verified; original reads remain dated
15 November, with separate focused rechecks on 16 and 17 November:

| Official source | SHA256 |
|---|---|
| [CGI 2026 and annexed CNPS decrees](https://www.impots.cm/sites/default/files/documents/CODE%20GENERAL%20DES%20IMPOTS%202026%20SITE%20DGI%20VERSION%20FRANCAISE.pdf) | `374c1d95ba2843dc0d8288cda11b681aed0ebee00bb1730aa9a7d345026025c5` |
| [2023 minimum-wage decree](https://www.spm.gov.cm/site/sites/default/files/dpm_2023-00338_s.pdf) | `2415ed1bcf68acbf8573ccbff0a204eb5244ab643fbf01518ca1c71734706d2a` |
| [2024 State-worker decree](https://www.spm.gov.cm/site/sites/default/files/decree_no_2024_0168.pdf) | `2212fb15f3166705472b1fbb45c038a832fe352f6ae702fc4d054799a655263d` |

## Validation and limits

At the bound source head, [validate and calculator-quotes](https://github.com/openaccountants/openaccountants/actions/runs/43940695514)
and [compare and unit-tests](https://github.com/openaccountants/openaccountants/actions/runs/43940695497)
succeeded. Exact-head local evidence: standards `{}` for all three Guides;
six oa-check blocks, zero failures/missing; all calculator quotations preserved;
strict sync zero errors/warnings/notices. Changed-only validation against fetched
main passed with zero warnings. No full source or unit-suite rerun was performed
merely for this evidence document.

A 17 November isolated integration preview against main
`fe4002fa24814fbefee6f5499f7316f2f3c2a690` had no conflicts, changed only the
four assigned source paths, preserved every Cameroon byte, and passed strict
sync: three Guides, zero errors/warnings/notices. This is preview evidence, not a
new live PR head. The earlier literal tip-to-tip audit failed on unrelated changes
already merged to main; it is not relabelled green. Required hosted checks must
be observed at any resulting PR head before publication.

Full paginated live PR file scopes, including ON HOLD #1336 and #1319, showed no
other Cameroon overlap. This document is a durable public audit record for
maintainer review; no workflow, required check or source Guide was changed.

Mandatory employee/employer pension shares remain separate from employer-only
family and uncapped occupational-risk contributions. Voluntary insurance is the
insured's full 8.4% on an agreed base with actual eligibility confirmation. The
agency voluntary range establishes neither a mandatory employee floor nor a
unilateral payment-frequency election. No pension-benefit entitlement is adopted.

Remaining non-usable holds include monthly withholding/rounding, harmonised levy
calendar, CNPS mandatory floor, detailed excluded costs and special months,
public/foreign schemes, actual VAT/filing portal boxes and individual
supplier/platform/representation/input conditions. Historical names/identifiers
are preserved without inferring approval. Root retains the no-merges-during-
ingestion gate and owns merge/delivery; this record authorizes neither.

Written by Codex. Not reviewed by an accountant.
