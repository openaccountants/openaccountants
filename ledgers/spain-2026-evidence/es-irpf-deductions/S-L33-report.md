# S-L33 writer correction

Five supplementary Balearic test fixtures used incorrect 530/650 annual-cap constants. Only their labels, constants and expected results were corrected in `check-ledger.py`. The correct sourced annual caps are 660/900. Results are 332.71 and 453.70 for 184/365 days, 330 for each ordinary payer, and 450 for the enhanced payer. Exact rational calculations independently cross-check these five fixtures.

The focused checker reports 10102 checks, 89 numeric controls and zero failures. Exactly five numeric-control records changed; the other 84 are byte-equivalent as parsed records. Reversing the five exact checker operations reconstructs its preserved predecessor byte-for-byte.

The d633 ledger and current Guide 02b2 remain byte-identical. All source bodies, quotes, 17 section ledgers/builders, old-topic mappings, original oa blocks and actual worked Guide results remain unchanged. In particular, twins 665.42/907.40 and unequal-payment totals 530/580/650 were not altered. No source fetch, Guide edit, Git mutation or broad country/repository check was performed.

Before mutation, the ledger and all 567 then-current non-history support files were copied byte-exact to `history/pre-S-L33-d633`; every saved hash was rechecked. Of those support files, only checker, numeric output, check output, writer status and handover identity metadata changed. New operations/proof/report/manifest files document the correction. Earlier sealed evidence is retained.

This is writer verification for a finite evidence correction, not an independent PASS or country-completion claim.
