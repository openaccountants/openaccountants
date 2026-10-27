# Yemen general sales tax: source/editorial review

22 October 2026. Local unpublished draft; no professional attestation or complete country coverage.

Independent reviewer: review_gi_minimum. Full review at SHA256 `095d978cd19f9ddae46b27656db6687808223871cdef681523065f7b934ca1eb` found no material rate or computational error, but required explicit notification and payment **before** diversion or sale under Decision 164/2020. Writer fixed the sequence.

Writer also added Decision 1/2006 article 1, PDF page 3, establishing the historical YER50 million regulatory threshold. Reviewer independently checked that addition and the procedural fix; delta review passed at SHA256 `2c64770871ab75b6a3b4febe430faab30eb389e052a65ae6fce1a711a0572858`.

Both examples recompute: output tax YER100,000; net payable YER70,000 with eligible paid inputs or YER100,000 without recovery. These checks do not establish transaction eligibility.

Remaining substantive gaps: current threshold and amendment chain, administration-specific territorial application, full schedules, refund procedures including Decision 164/2020 regulation 90(b)(VIII), supply valuation/timing and detailed compliance. No nationwide current-law certification.

Targeted schema and two example checks passed before the regulatory-threshold addition. Aggregate checks follow the local commit; this record does not predeclare their result.

Post-commit checks at `e4a928e`: changed-only schema passed for 54 Guides (58 changed paths), with the existing Gibraltar 2024 freshness warning; 103 executable example blocks passed with zero missing; sync audit passed for 58 source files with zero errors/warnings; whitespace check passed. No push or publication performed.
