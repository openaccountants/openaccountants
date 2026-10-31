# Skills register

Generated from the skill tree on 2026-10-31 by `scripts/build-register.py`. One row per skill in `REGISTER.csv`. This file is the summary.

## Totals

- Skills: 2303
- Jurisdictions: 275 (266 countries or states, the rest pseudo-codes)
- Tax year 2026: 960; still 2025: 1212; no year: 126
- Signed by a named accountant (tier 1): 33, in US (21), PH (7), GE (3), CA (1), MY (1)
- Scope: 2058 tax skills (deep-tax shape applies), 89 accounting-pack skills (general template), 156 other (routers, templates, patterns)
- Domain from the README `covered_by`: 100; from the slug: 1266; no tax domain: 937
- Pass all 10 checks: 175 of 2058 tax skills
- Duplicates: 432 skills in 154 (country, domain) cells where the README does not name which skill covers the job

## Pass rate per check

Tax skills only (the deep-tax shape applies to them). One column per check in `REGISTER.csv`; the letters are the order in `scripts/skill_checks.py`.

| | Check | Pass | Fail | Pass rate |
|---|---|---:|---:|---:|
| (a) | `tax_year_current` | 853 | 1205 | 41% |
| (b) | `sources_read_dates` | 485 | 1573 | 24% |
| (c) | `rates_rows_sourced` | 209 | 1849 | 10% |
| (d) | `canonical_headings` | 396 | 1662 | 19% |
| (e) | `two_oa_checks` | 421 | 1637 | 20% |
| (f) | `version_numeric` | 1214 | 844 | 59% |
| (g) | `tier_honest` | 1920 | 138 | 93% |
| (h) | `no_em_dash` | 715 | 1343 | 35% |
| (i) | `not_yet_confirmed` | 480 | 1578 | 23% |
| (j) | `reviewed_on` | 1904 | 154 | 93% |

## By domain

A skill covering two domains counts in both.

| Domain | Skills | Signed |
|---|---:|---:|
| IT-IND | 403 | 5 |
| IT-CORP | 187 | 2 |
| VAT | 299 | 4 |
| SC | 184 | 0 |
| PR | 238 | 2 |
| TP | 58 | 0 |
| XB | 113 | 0 |
| (no tax domain) | 937 | 20 |

## Country by domain

Count of skills in each (country, domain) cell. `*` means at least one is signed by a named accountant; `!` means two or more skills share the cell and the README does not name which one covers it (a duplicate).

| Country | IT-IND | IT-CORP | VAT | SC | PR | TP | XB | All pass | 2026 | Signed | Total |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| US | 37*! | 2! | 4*! |  | 4*! |  | 2! | 0 | 39 | 21 | 103 |
| AU | 7! | 1 | 3! | 1 | 4! | 1 | 4! | 0 | 33 | 0 | 61 |
| CA | 18! | 2! | 1 | 1 | 2! | 1 | 2! | 0 | 5 | 1 | 51 |
| GB | 5! | 1 | 5! | 1 | 2! | 1 | 4! | 13 | 33 | 0 | 35 |
| MT | 6! | 1 | 2! | 1 | 1 | 1 | 1 | 1 | 32 | 0 | 34 |
| DE | 6! | 1 | 2! | 1 | 4! | 1 | 4! | 8 | 30 | 0 | 31 |
| ES | 6! | 2! | 2! | 1 | 2! | 1 | 2! | 21 | 28 | 0 | 30 |
| NL | 4! | 1 | 3! | 1 | 3! | 1 | 1 | 12 | 28 | 0 | 30 |
| FR | 5! | 1 | 1 | 1 | 1 | 1 | 2! | 3 | 22 | 0 | 23 |
| DO | 2! | 1 | 1 | 1 | 2! | 1 | 1 | 0 | 1 | 0 | 22 |
| IN | 5! |  | 2! |  | 1 | 1 | 1 | 0 | 17 | 0 | 22 |
| IT | 1 | 1 | 1 | 2! | 1 | 1 | 1 | 4 | 21 | 0 | 22 |
| ZA | 6! |  | 3! |  |  | 1 | 2! | 0 | 2 | 0 | 20 |
| JP | 3! |  | 2! | 1 | 1 | 1 |  | 0 | 0 | 0 | 19 |
| PK | 3! | 1 | 3! | 1 | 3! |  |  | 0 | 8 | 0 | 19 |
| BD | 3! | 1 | 1 | 2! | 2! |  |  | 0 | 11 | 0 | 18 |
| IE | 3! | 1 | 1 | 1 | 3! | 1 | 3! | 10 | 18 | 0 | 18 |
| PT | 2! | 1 | 2! | 1 | 1 | 1 | 2! | 2 | 18 | 0 | 18 |
| EG | 3! | 1 | 1 | 1 | 2! | 1 |  | 0 | 11 | 0 | 17 |
| KZ | 3! | 1 | 1 | 2! | 2! |  |  | 0 | 11 | 0 | 17 |
| UA | 3! | 1 | 1 | 1 | 1 | 1 | 1 | 3 | 17 | 0 | 17 |
| MA | 4! |  | 1 | 1 | 1 |  |  | 0 | 6 | 0 | 16 |
| US-CA | 4! |  | 1 |  | 1 |  | 1 | 0 | 10 | 0 | 16 |
| US-NY | 6! | 1 | 2! |  | 1 |  | 1 | 0 | 6 | 0 | 16 |
| BE | 3! | 1 | 2! | 1 | 2! | 1 | 1 | 8 | 15 | 0 | 15 |
| GR | 2! | 1 | 2! | 1 | 1 | 1 | 1 | 2 | 15 | 0 | 15 |
| SE | 3! | 1 | 2! | 1 | 1 | 1 | 1 | 0 | 14 | 0 | 15 |
| BR | 4! |  | 1 |  | 1 | 1 |  | 0 | 1 | 0 | 14 |
| CH | 1 | 1 | 2! | 1 | 1 | 1 | 1 | 6 | 14 | 0 | 14 |
| CN | 3! | 1 | 2! | 1 | 1 |  | 1 | 0 | 5 | 0 | 14 |
| FI | 2! | 2! | 1 | 1 | 1 | 1 | 2! | 0 | 14 | 0 | 14 |
| KE | 3! | 1 | 2! |  |  |  | 1 | 0 | 0 | 0 | 14 |
| NG | 4! | 1 | 3! |  | 1 |  |  | 0 | 0 | 0 | 14 |
| RU | 4! |  | 1 | 1 | 1 |  |  | 0 | 14 | 0 | 14 |
| CZ | 2! | 1 | 2! | 2! | 1 | 1 | 1 | 3 | 12 | 0 | 13 |
| ID | 3! | 1 | 1 |  | 2! |  |  | 0 | 1 | 0 | 13 |
| RO | 2! | 1 | 2! | 1 | 1 | 1 | 1 | 2 | 12 | 0 | 13 |
| MX | 3! |  | 1 |  |  | 1 |  | 0 | 0 | 0 | 12 |
| NO | 3! | 1 | 1 | 1 | 1 | 1 | 2! | 0 | 12 | 0 | 12 |
| PL | 2! | 1 | 2! | 1 | 1 | 1 | 1 | 2 | 11 | 0 | 12 |
| SA | 2! | 1 | 1 |  | 1 |  |  | 0 | 0 | 0 | 12 |
| HU | 1 | 1 | 2! | 1 | 1 | 1 | 1 | 5 | 11 | 0 | 11 |
| MM | 3! |  | 3! | 1 | 1 |  |  | 0 | 0 | 0 | 11 |
| NZ | 2! |  | 2! |  |  |  |  | 0 | 10 | 0 | 11 |
| AM | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 10 | 0 | 10 |
| AT | 1 | 1 | 2! | 2! | 1 | 1 | 1 | 3 | 10 | 0 | 10 |
| BA | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 10 | 0 | 10 |
| BG | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 3 | 10 | 0 | 10 |
| DK | 2! | 1 | 2! | 1 | 1 | 1 | 1 | 6 | 9 | 0 | 10 |
| EE | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 3 | 10 | 0 | 10 |
| GG | 1 | 1 | 1 | 1 | 2! | 1 | 1 | 2 | 10 | 0 | 10 |
| HR | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 4 | 10 | 0 | 10 |
| IL | 1 | 1 | 1 |  | 1 |  |  | 0 | 0 | 0 | 10 |
| IS | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 10 | 0 | 10 |
| LK | 2! | 1 | 1 |  | 2! |  |  | 0 | 0 | 0 | 10 |
| LV | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 5 | 10 | 0 | 10 |
| MD | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 6 | 0 | 10 |
| ME | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 10 | 0 | 10 |
| MK | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 10 | 0 | 10 |
| RS | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 3 | 10 | 0 | 10 |
| SG | 1 |  | 2! |  |  | 1 |  | 0 | 3 | 0 | 10 |
| SI | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 3 | 10 | 0 | 10 |
| SK | 1 | 1 | 2! | 1 | 1 | 1 | 1 | 5 | 9 | 0 | 10 |
| US-GA | 2! | 3! | 1 |  | 1 |  |  | 0 | 3 | 0 | 10 |
| AE | 1 | 2! | 2! | 1 | 1 |  |  | 0 | 7 | 0 | 9 |
| CY | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 9 | 0 | 9 |
| LT | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 4 | 8 | 0 | 9 |
| US-MI | 3! | 1 | 1 |  | 1 |  |  | 0 | 0 | 0 | 9 |
| AD | 2! | 1 | 1 | 1 | 1 | 1 | 1 | 4 | 8 | 0 | 8 |
| AL | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 8 | 0 | 8 |
| AR | 1 | 1 | 1 | 1 |  |  |  | 0 | 0 | 0 | 8 |
| AZ | 1 | 1 | 1 | 1 | 1 |  |  | 0 | 0 | 0 | 8 |
| BF | 1 | 1 | 1 | 1 | 1 |  |  | 0 | 0 | 0 | 8 |
| BY | 1 | 1 | 1 | 1 | 1 |  |  | 0 | 0 | 0 | 8 |
| CL | 1 | 1 | 1 | 1 |  |  |  | 0 | 0 | 0 | 8 |
| CO | 1 | 1 | 1 | 1 |  |  |  | 0 | 0 | 0 | 8 |
| EC | 1 | 1 |  | 1 | 1 |  |  | 0 | 0 | 0 | 8 |
| GE | 1* | 1 | 1* | 1 | 1 |  |  | 0 | 0 | 3 | 8 |
| IM | 2! | 1 | 1 | 1 | 1 | 1 | 2! | 0 | 6 | 0 | 8 |
| LU | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 8 | 0 | 8 |
| MC | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 5 | 8 | 0 | 8 |
| MY | 1 | 1* |  |  |  |  |  | 0 | 1 | 1 | 8 |
| QA | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 7 | 8 | 0 | 8 |
| RW | 2! | 1 | 1 | 1 | 1 |  |  | 0 | 0 | 0 | 8 |
| SM | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 8 | 0 | 8 |
| TR | 1 | 1 | 1 | 1 | 1 |  |  | 0 | 0 | 0 | 8 |
| US-TX | 3! |  | 2! |  |  |  |  | 0 | 1 | 0 | 8 |
| UZ | 1 | 1 | 1 | 1 | 1 |  |  | 0 | 0 | 0 | 8 |
| VN | 1 | 1 | 1 | 1 | 1 |  |  | 0 | 2 | 0 | 8 |
| XK | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 5 | 8 | 0 | 8 |
| BM | 1 | 1 | 1 | 1 | 1 |  |  | 0 | 0 | 0 | 7 |
| BN | 1 | 1 | 1 | 1 | 1 |  |  | 0 | 0 | 0 | 7 |
| ET | 1 | 1 | 1 | 1 | 1 |  |  | 0 | 0 | 0 | 7 |
| GH | 1 | 1 | 1 | 1 | 1 |  |  | 0 | 0 | 0 | 7 |
| GT | 1 | 1 |  | 1 | 1 |  |  | 0 | 2 | 0 | 7 |
| HK |  | 1 | 1 |  |  |  |  | 0 | 0 | 0 | 7 |
| HN | 1 | 1 |  | 1 | 1 |  |  | 0 | 1 | 0 | 7 |
| IQ | 1 | 1 | 1 | 1 | 1 |  |  | 0 | 0 | 0 | 7 |
| NI | 1 | 1 |  | 1 | 1 |  |  | 0 | 0 | 0 | 7 |
| PE | 1 | 1 |  | 1 | 1 |  |  | 0 | 2 | 0 | 7 |
| PH | 1* | 1* | 1* |  | 1* |  |  | 0 | 0 | 7 | 7 |
| SN | 1 | 1 | 1 | 1 | 1 |  |  | 0 | 2 | 0 | 7 |
| TH | 1 | 1 | 1 | 1 | 1 |  |  | 0 | 0 | 0 | 7 |
| TN | 1 | 1 | 1 | 1 | 1 |  |  | 0 | 0 | 0 | 7 |
| US-FL | 1 | 1 | 1 |  |  |  |  | 0 | 3 | 0 | 7 |
| US-KS | 1 | 1 | 1 | 1 | 2! | 1 | 1 | 0 | 7 | 0 | 7 |
| US-MA | 1 | 1 | 4! |  | 1 |  |  | 0 | 0 | 0 | 7 |
| US-NC | 2! | 1 | 1 |  | 1 |  |  | 0 | 0 | 0 | 7 |
| UY | 1 | 1 |  | 1 | 1 |  |  | 0 | 0 | 0 | 7 |
| AF | 1 | 1 | 1 | 1 | 1 |  |  | 0 | 0 | 0 | 6 |
| AO | 1 | 1 | 1 | 1 | 1 |  |  | 0 | 0 | 0 | 6 |
| BB | 1 | 1 | 1 | 1 | 1 |  |  | 0 | 0 | 0 | 6 |
| BH | 1 | 1 | 1 | 1 | 1 |  |  | 0 | 0 | 0 | 6 |
| BI | 1 | 1 | 1 | 1 | 1 |  |  | 0 | 0 | 0 | 6 |
| BJ | 1 | 1 | 1 | 1 | 1 |  |  | 0 | 0 | 0 | 6 |
| BS | 1 | 1 | 1 | 1 | 1 |  |  | 0 | 0 | 0 | 6 |
| BT | 1 | 1 | 1 | 1 | 1 |  |  | 0 | 0 | 0 | 6 |
| BW | 1 | 1 | 1 | 1 | 1 |  |  | 0 | 0 | 0 | 6 |
| BZ | 1 | 1 | 1 | 1 | 1 |  |  | 0 | 0 | 0 | 6 |
| CD | 1 | 1 | 1 | 1 | 1 |  |  | 0 | 0 | 0 | 6 |
| CF | 1 | 1 | 1 | 1 | 1 |  |  | 0 | 0 | 0 | 6 |
| CG | 1 | 1 | 1 | 1 | 1 |  |  | 0 | 0 | 0 | 6 |
| CU | 1 | 1 | 1 | 1 | 1 |  |  | 0 | 0 | 0 | 6 |
| CV | 1 | 1 | 1 | 1 | 1 |  |  | 0 | 0 | 0 | 6 |
| CW | 1 | 1 | 1 | 1 | 1 |  |  | 0 | 1 | 0 | 6 |
| DJ | 1 | 1 | 1 | 1 | 1 |  |  | 0 | 0 | 0 | 6 |
| ER | 1 | 1 | 1 | 1 | 1 |  |  | 0 | 0 | 0 | 6 |
| FJ | 1 | 1 | 1 | 1 | 1 |  |  | 0 | 0 | 0 | 6 |
| GM | 1 | 1 | 1 | 1 | 1 |  |  | 0 | 0 | 0 | 6 |
| GN | 1 | 1 | 1 | 1 | 1 |  |  | 0 | 0 | 0 | 6 |
| GQ | 1 | 1 | 1 | 1 | 1 |  |  | 0 | 0 | 0 | 6 |
| GW | 1 | 1 | 1 | 1 | 1 |  |  | 0 | 0 | 0 | 6 |
| GY | 1 | 1 | 1 | 1 | 1 |  |  | 0 | 0 | 0 | 6 |
| HT | 1 | 1 |  |  | 2! |  |  | 0 | 6 | 0 | 6 |
| IR | 1 | 1 | 1 | 1 | 1 |  |  | 0 | 0 | 0 | 6 |
| JM | 1 | 1 |  | 1 | 1 |  |  | 0 | 0 | 0 | 6 |
| JO | 1 | 1 | 1 | 1 | 1 |  |  | 0 | 0 | 0 | 6 |
| KG | 1 | 1 | 1 | 1 | 1 |  |  | 0 | 0 | 0 | 6 |
| KH | 1 | 1 | 1 | 1 | 1 |  |  | 0 | 0 | 0 | 6 |
| KR | 1 |  | 2! | 1 |  |  |  | 0 | 0 | 0 | 6 |
| KW |  | 1 | 1 | 1 | 1 |  |  | 0 | 0 | 0 | 6 |
| KY |  | 1 | 1 | 1 | 1 |  |  | 0 | 0 | 0 | 6 |
| LB | 1 | 1 | 1 | 1 | 1 |  |  | 0 | 0 | 0 | 6 |
| LI | 1 | 1 | 1 | 1 | 1 |  |  | 0 | 0 | 0 | 6 |
| LR | 1 | 1 | 1 | 1 | 1 |  |  | 0 | 0 | 0 | 6 |
| LS | 1 | 1 | 1 | 1 | 1 |  |  | 0 | 0 | 0 | 6 |
| LY | 1 | 1 | 1 | 1 | 1 |  |  | 0 | 0 | 0 | 6 |
| MG | 1 | 1 | 1 | 1 | 1 |  |  | 0 | 0 | 0 | 6 |
| ML | 1 | 1 | 1 | 1 | 1 |  |  | 0 | 0 | 0 | 6 |
| MR | 1 | 1 | 1 | 1 | 1 |  |  | 0 | 0 | 0 | 6 |
| MU | 1 | 1 | 1 | 1 | 1 |  |  | 0 | 0 | 0 | 6 |
| MV | 1 | 1 | 1 | 1 | 1 |  |  | 0 | 0 | 0 | 6 |
| MW | 1 | 1 | 1 | 1 | 1 |  |  | 0 | 0 | 0 | 6 |
| NA | 1 | 1 | 1 | 1 | 1 |  |  | 0 | 0 | 0 | 6 |
| OM | 1 | 1 | 1 | 1 | 1 |  |  | 0 | 0 | 0 | 6 |
| PG | 1 | 1 | 1 | 1 | 1 |  |  | 0 | 0 | 0 | 6 |
| SD | 1 | 1 | 1 | 1 | 1 |  |  | 0 | 0 | 0 | 6 |
| SL | 1 | 1 | 1 | 1 | 1 |  |  | 0 | 0 | 0 | 6 |
| SO | 1 | 1 | 1 | 1 | 1 |  |  | 0 | 0 | 0 | 6 |
| SR | 1 | 1 | 1 | 1 | 1 |  |  | 0 | 0 | 0 | 6 |
| SS | 1 | 1 | 1 | 1 | 1 |  |  | 0 | 0 | 0 | 6 |
| ST | 1 | 1 | 1 | 1 | 1 |  |  | 0 | 0 | 0 | 6 |
| SZ | 1 | 1 | 1 | 1 | 1 |  |  | 0 | 0 | 0 | 6 |
| TD | 1 | 1 | 1 | 1 | 1 |  |  | 0 | 0 | 0 | 6 |
| TG | 1 | 1 | 1 | 1 | 1 |  |  | 0 | 0 | 0 | 6 |
| TJ | 1 | 1 | 1 | 1 | 1 |  |  | 0 | 0 | 0 | 6 |
| TL | 1 | 1 | 1 | 1 | 1 |  |  | 0 | 0 | 0 | 6 |
| TM | 1 | 1 | 1 | 1 | 1 |  |  | 0 | 0 | 0 | 6 |
| TO | 1 | 1 | 1 | 1 | 1 |  |  | 0 | 0 | 0 | 6 |
| TT | 1 | 1 | 1 | 1 | 1 |  |  | 0 | 0 | 0 | 6 |
| TW | 1 | 1 | 1 |  |  |  |  | 0 | 0 | 0 | 6 |
| TZ | 1 |  | 1 | 1 | 2! |  |  | 0 | 2 | 0 | 6 |
| UG | 1 | 1 | 1 | 1 | 1 |  |  | 0 | 0 | 0 | 6 |
| US-CO | 1 |  | 3! |  | 1 |  |  | 0 | 1 | 0 | 6 |
| US-IL | 2! |  | 2! |  | 1 |  |  | 0 | 1 | 0 | 6 |
| US-ND | 2! | 1 | 1 |  | 1 |  |  | 0 | 0 | 0 | 6 |
| US-OH | 1 |  | 2! |  | 1 |  |  | 0 | 4 | 0 | 6 |
| VG |  | 1 | 1 | 1 | 1 |  |  | 0 | 0 | 0 | 6 |
| VU | 1 | 1 | 1 | 1 | 1 |  |  | 0 | 0 | 0 | 6 |
| WS | 1 | 1 | 1 | 1 | 1 |  |  | 0 | 0 | 0 | 6 |
| ZM | 1 | 1 | 1 | 1 | 1 |  |  | 0 | 0 | 0 | 6 |
| ZW | 1 | 1 | 1 | 1 | 1 |  |  | 0 | 0 | 0 | 6 |
| BO | 1 |  |  | 1 | 1 |  |  | 0 | 0 | 0 | 5 |
| CR | 1 |  |  | 1 | 1 |  |  | 0 | 2 | 0 | 5 |
| FO | 1 |  | 1 | 1 | 1 |  | 1 | 0 | 5 | 0 | 5 |
| GA |  | 1 | 1 | 1 | 1 |  |  | 0 | 0 | 0 | 5 |
| GI | 1 | 1 |  | 1 | 1 |  |  | 0 | 5 | 0 | 5 |
| LA |  | 1 | 1 | 1 | 1 |  |  | 0 | 0 | 0 | 5 |
| LC | 1 |  | 2! |  |  |  |  | 0 | 4 | 0 | 5 |
| MN |  | 1 | 1 | 1 | 1 |  |  | 0 | 0 | 0 | 5 |
| MO |  | 1 | 1 | 1 | 1 |  |  | 0 | 0 | 0 | 5 |
| NE |  | 1 | 1 | 1 | 1 |  |  | 0 | 0 | 0 | 5 |
| NP | 1 | 1 | 1 |  | 1 |  |  | 0 | 0 | 0 | 5 |
| SC |  | 1 | 1 | 1 | 1 |  |  | 0 | 0 | 0 | 5 |
| SV | 1 |  |  | 1 | 1 |  |  | 0 | 0 | 0 | 5 |
| US-MN | 1 | 1 | 2! |  | 1 |  |  | 0 | 0 | 0 | 5 |
| US-NJ | 1 |  | 2! |  | 1 |  |  | 0 | 4 | 0 | 5 |
| US-NV |  |  | 2! |  |  |  |  | 0 | 0 | 0 | 5 |
| US-PA | 1 |  | 2! |  | 1 |  |  | 0 | 3 | 0 | 5 |
| US-WA | 1 |  | 2! |  |  |  |  | 0 | 4 | 0 | 5 |
| VE | 1 |  |  | 1 | 1 |  |  | 0 | 0 | 0 | 5 |
| CI | 1 |  | 1 | 1 | 1 |  |  | 0 | 0 | 0 | 4 |
| CM | 1 |  | 1 | 1 | 1 |  |  | 0 | 0 | 0 | 4 |
| DM | 1 | 1 | 1 | 1 | 1 |  |  | 0 | 4 | 0 | 4 |
| DZ | 1 |  | 1 | 1 | 1 |  |  | 0 | 0 | 0 | 4 |
| MZ | 1 |  | 1 | 1 | 1 |  |  | 0 | 0 | 0 | 4 |
| PA | 1 |  |  | 1 | 1 |  |  | 0 | 1 | 0 | 4 |
| PY | 1 |  |  | 1 | 1 |  |  | 0 | 0 | 0 | 4 |
| SH | 3! |  |  |  | 1 |  |  | 0 | 4 | 0 | 4 |
| US-AL | 2! |  | 2! |  |  |  |  | 0 | 0 | 0 | 4 |
| US-AR | 1 |  | 3! |  |  |  |  | 0 | 1 | 0 | 4 |
| US-AZ | 1 |  | 1 |  | 1 |  |  | 0 | 0 | 0 | 4 |
| US-DE | 1 |  |  |  |  |  |  | 0 | 3 | 0 | 4 |
| US-MO | 1 |  | 2! |  | 1 |  |  | 0 | 0 | 0 | 4 |
| US-VA | 1 | 1 | 1 |  | 1 |  |  | 0 | 1 | 0 | 4 |
| US-WI | 1 |  | 2! |  | 1 |  |  | 0 | 1 | 0 | 4 |
| AG |  |  |  | 1 |  |  |  | 0 | 3 | 0 | 3 |
| AW | 1 |  |  | 1 |  |  |  | 0 | 3 | 0 | 3 |
| GD |  |  | 1 | 1 |  |  |  | 0 | 3 | 0 | 3 |
| KM | 1 |  |  |  |  |  |  | 0 | 3 | 0 | 3 |
| MF |  | 1 |  |  |  |  |  | 0 | 3 | 0 | 3 |
| MS |  | 1 |  | 1 | 1 |  | 1 | 0 | 3 | 0 | 3 |
| PR | 1 |  |  |  |  |  |  | 0 | 1 | 0 | 3 |
| SJ | 1 |  |  |  | 1 |  |  | 0 | 3 | 0 | 3 |
| SX | 1 |  |  |  |  |  |  | 0 | 3 | 0 | 3 |
| TC |  |  |  |  |  |  |  | 0 | 3 | 0 | 3 |
| US-CT | 1 |  | 1 |  | 1 |  |  | 0 | 1 | 0 | 3 |
| US-IN |  |  | 2! |  | 1 |  |  | 0 | 0 | 0 | 3 |
| US-KY | 1 |  | 1 |  | 1 |  |  | 0 | 1 | 0 | 3 |
| US-MD | 1 |  | 1 |  | 1 |  |  | 0 | 1 | 0 | 3 |
| US-MS | 1 |  | 2! |  |  |  |  | 0 | 0 | 0 | 3 |
| US-NM | 1 |  | 2! |  |  |  |  | 0 | 0 | 0 | 3 |
| US-OK | 1 |  | 2! |  |  |  |  | 0 | 0 | 0 | 3 |
| US-OR | 1 |  |  |  | 1 |  |  | 0 | 0 | 0 | 3 |
| US-UT | 1 |  | 2! |  |  |  |  | 0 | 0 | 0 | 3 |
| US-WY |  |  | 2! |  |  |  |  | 0 | 0 | 0 | 3 |
| VC |  | 1 | 1 |  |  |  |  | 0 | 3 | 0 | 3 |
| VI | 1 |  |  |  |  |  |  | 0 | 3 | 0 | 3 |
| BL |  |  |  | 1 |  |  |  | 0 | 2 | 0 | 2 |
| CA-AB | 1 |  |  |  |  |  | 1 | 0 | 2 | 0 | 2 |
| GF |  |  | 1 |  |  |  |  | 0 | 2 | 0 | 2 |
| GL |  |  |  |  | 1 |  |  | 0 | 2 | 0 | 2 |
| KN |  |  |  | 2! |  |  |  | 0 | 2 | 0 | 2 |
| PM | 2! |  |  |  |  |  |  | 0 | 1 | 0 | 2 |
| US-DC | 1 |  | 1 |  |  |  |  | 0 | 1 | 0 | 2 |
| US-HI | 1 |  | 1 |  |  |  |  | 0 | 0 | 0 | 2 |
| US-IA | 1 |  | 1 |  |  |  |  | 0 | 0 | 0 | 2 |
| US-ID |  |  | 2! |  |  |  |  | 0 | 0 | 0 | 2 |
| US-LA | 1 |  | 1 |  |  |  |  | 0 | 0 | 0 | 2 |
| US-ME | 1 |  | 1 |  |  |  |  | 0 | 0 | 0 | 2 |
| US-NE | 1 |  | 1 |  |  |  |  | 0 | 0 | 0 | 2 |
| US-NH |  |  |  |  |  |  |  | 0 | 0 | 0 | 2 |
| US-RI | 1 |  | 1 |  |  |  |  | 0 | 0 | 0 | 2 |
| US-SC | 1 |  | 1 |  |  |  |  | 0 | 0 | 0 | 2 |
| US-VT | 1 |  | 1 |  |  |  |  | 0 | 0 | 0 | 2 |
| US-WV | 1 |  | 1 |  |  |  |  | 0 | 0 | 0 | 2 |
| YT |  |  | 1 |  | 1 |  |  | 0 | 2 | 0 | 2 |
| GP |  |  |  |  |  |  |  | 0 | 1 | 0 | 1 |
| MQ |  |  |  |  |  |  |  | 0 | 1 | 0 | 1 |
| RE |  |  |  |  |  |  |  | 0 | 1 | 0 | 1 |
| US-AK |  |  | 1 |  |  |  |  | 0 | 0 | 0 | 1 |
| US-MT | 1 |  |  |  |  |  |  | 0 | 1 | 0 | 1 |
| US-NY-NYC |  |  |  |  |  |  |  | 0 | 0 | 0 | 1 |
| US-SD |  |  | 1 |  |  |  |  | 0 | 0 | 0 | 1 |
| US-TN |  |  | 1 |  |  |  |  | 0 | 0 | 0 | 1 |
| VA |  |  |  |  |  |  |  | 0 | 1 | 0 | 1 |

## Duplicates

Skills that share a (country, domain) cell with another skill and are not named in the pack README's `covered_by`. Fix by naming one in the README or merging the skills.

| Country | Domain | Skill |
|---|---|---|
| AD | IT-IND | `ad-income-tax` |
| AD | IT-IND | `ad-non-resident-income-tax` |
| AE | IT-CORP | `ae-corporate-tax` |
| AE | IT-CORP | `general-uae-corporate-tax-guide` |
| AE | VAT | `ae-vat-return` |
| AE | VAT | `uae-vat` |
| AT | SC | `at-svs-contributions` |
| AT | VAT | `at-vat-return` |
| AT | VAT | `austria-vat-return` |
| AU | IT-IND | `amending-an-individual-income-tax-return-in-australia` |
| AU | IT-IND | `au-amending-individual-income-tax-return-period` |
| AU | IT-IND | `au-capital-gains` |
| AU | IT-IND | `au-capital-gains-2` |
| AU | IT-IND | `au-freelance-intake` |
| AU | IT-IND | `au-individual-return` |
| AU | IT-IND | `au-return-assembly` |
| AU | PR | `au-employment-termination-payments` |
| AU | PR | `au-payroll-tax` |
| AU | PR | `au-working-holiday-makers` |
| AU | PR | `australia-payroll` |
| AU | VAT | `au-gst-bas` |
| AU | VAT | `au-gst-property` |
| AU | VAT | `australia-gst` |
| AU | XB | `au-nonresident-cgt` |
| AU | XB | `au-nonresident-cgt-2` |
| AU | XB | `leaving-australia-residency-the-cgt-departure-choice-and-what-follows-you` |
| AU | XB | `leaving-australia-tax-residency-cgt` |
| BD | IT-IND | `bangladesh-pit` |
| BD | IT-IND | `bd-freelance-intake` |
| BD | IT-IND | `bd-return-assembly` |
| BD | PR | `bd-payroll` |
| BD | SC | `bd-social-contributions` |
| BD | SC+PR | `bd-payroll-social` |
| BE | IT-IND | `be-capital-gains` |
| BE | IT-IND | `be-employee-income-tax` |
| BE | IT-IND | `be-income-tax` |
| BE | PR | `be-payroll-withholding` |
| BE | PR | `belgium-payroll` |
| BE | VAT | `be-vat-return` |
| BE | VAT | `belgium-vat-return` |
| BR | IT-IND | `br-carn-monthly-income-tax-rental-income` |
| BR | IT-IND | `br-freelance-intake` |
| BR | IT-IND | `br-income-tax` |
| BR | IT-IND | `br-return-assembly` |
| CA | IT-CORP | `ab-corporate-tax` |
| CA | IT-CORP | `qc-corporate-tax-co17` |
| CA | IT-IND | `ab-individual-return` |
| CA | IT-IND | `bc-individual-return` |
| CA | IT-IND | `ca-capital-gains` |
| CA | IT-IND | `ca-fed-t1-return` |
| CA | IT-IND | `ca-freelance-intake` |
| CA | IT-IND | `ca-return-assembly` |
| CA | IT-IND | `mb-individual-return` |
| CA | IT-IND | `nb-individual-return` |
| CA | IT-IND | `nl-individual-return` |
| CA | IT-IND | `ns-individual-return` |
| CA | IT-IND | `nt-individual-return` |
| CA | IT-IND | `nu-individual-return` |
| CA | IT-IND | `on-individual-return` |
| CA | IT-IND | `pe-individual-return` |
| CA | IT-IND | `qc-individual-return` |
| CA | IT-IND | `qc-qst-return` |
| CA | IT-IND | `sk-individual-return` |
| CA | IT-IND | `yt-individual-return` |
| CA | PR | `canada-payroll` |
| CA | PR | `nt-payroll-tax` |
| CA | XB | `ca-nonresident-cgt` |
| CA | XB | `leaving-canada-departure-tax` |
| CH | VAT | `ch-vat-return` |
| CH | VAT | `switzerland-vat` |
| CN | IT-IND | `china-pit` |
| CN | IT-IND | `cn-freelance-intake` |
| CN | IT-IND | `cn-return-assembly` |
| CN | VAT | `china-vat` |
| CN | VAT | `cn-vat` |
| CZ | IT-IND | `cz-employee-income-tax` |
| CZ | IT-IND | `cz-income-tax` |
| CZ | SC | `cz-employee-contributions` |
| CZ | SC | `cz-social-health` |
| CZ | VAT | `cz-vat-return` |
| CZ | VAT | `czech-republic-vat-return` |
| DE | IT-IND | `de-capital-gains` |
| DE | IT-IND | `de-employee-income-tax` |
| DE | IT-IND | `de-freelance-intake` |
| DE | IT-IND | `de-income-tax` |
| DE | IT-IND | `de-return-assembly` |
| DE | IT-IND | `de-self-employed-income-tax` |
| DE | PR | `de-payroll` |
| DE | PR | `de-payroll-benefits` |
| DE | PR | `germany-payroll` |
| DE | PR+XB | `de-treaty-withholding-rates` |
| DE | VAT | `de-vat-annual-and-special-schemes` |
| DE | VAT | `germany-vat-return` |
| DE | XB | `de-non-resident-tax` |
| DE | XB | `germany-to-switzerland-cross-border-tax` |
| DK | IT-IND | `dk-capital-gains` |
| DK | IT-IND | `dk-income-tax` |
| DK | VAT | `denmark-vat-return` |
| DK | VAT | `dk-vat-return` |
| DO | IT-IND | `do-capital-gains-tax` |
| DO | IT-IND | `dominican-republic-income-tax` |
| DO | PR | `do-withholding-tax` |
| DO | PR | `dominican-republic-payroll` |
| EG | IT-IND | `eg-freelance-intake` |
| EG | IT-IND | `eg-income-tax` |
| EG | IT-IND | `eg-return-assembly` |
| EG | PR | `eg-payroll` |
| EG | PR | `eg-withholding-tax` |
| ES | IT-CORP | `es-foral-corporate-tax` |
| ES | IT-IND | `es-capital-gains` |
| ES | IT-IND | `es-foral-income-tax` |
| ES | IT-IND | `es-freelance-intake` |
| ES | IT-IND | `es-return-assembly` |
| ES | IT-IND | `es-non-resident-income-tax-irnr-and` |
| ES | PR | `es-foral-payroll` |
| ES | VAT | `spain-vat-return` |
| ES | XB | `es-foral-non-resident-tax` |
| FI | IT-CORP+XB | `fi-corporate-cross-border-tax` |
| FI | IT-IND | `fi-individual-cross-border-residence` |
| FR | IT-IND | `fr-capital-gains` |
| FR | IT-IND | `fr-freelance-intake` |
| FR | IT-IND | `fr-income-tax` |
| FR | IT-IND | `fr-personal-income-tax` |
| FR | IT-IND | `fr-return-assembly` |
| FR | XB | `fr-cross-border` |
| GB | IT-IND | `uk-capital-gains-sa108` |
| GB | IT-IND | `uk-freelance-intake` |
| GB | IT-IND | `uk-income-tax-sa100` |
| GB | IT-IND | `uk-return-assembly` |
| GB | IT-IND | `uk-scottish-income-tax` |
| GB | PR | `uk-payroll` |
| GB | PR | `uk-foreign-tax-and-withholding` |
| GB | VAT | `close-the-uk-vat-quarter-from-xero` |
| GB | VAT | `gb-vat-eu-goods-sellers` |
| GB | VAT | `uk-vat-return` |
| GB | VAT | `vat-returns-for-small-businesses-in-the-uk` |
| GB | VAT | `xero-uk-vat-close` |
| GB | XB | `uk-non-resident-sa109` |
| GB | XB | `uk-to-italy-flat-tax-relocation` |
| GB | XB | `uk-to-uae-relocation-tax` |
| GG | PR | `gg-secondary-pensions` |
| GG | PR | `gg-payroll-social-insurance` |
| GR | IT-IND | `gr-capital-gains` |
| GR | IT-IND | `gr-income-tax` |
| GR | VAT | `gr-vat-return` |
| GR | VAT | `greece-vat-return` |
| HT | PR | `ht-payroll-withholding-and-employer-tax` |
| HT | PR | `ht-service-withholding-and-payment-reporting` |
| HU | VAT | `hu-vat-return` |
| HU | VAT | `hungary-vat-return` |
| ID | IT-IND | `id-freelance-intake` |
| ID | IT-IND | `id-income-tax` |
| ID | IT-IND | `id-return-assembly` |
| ID | PR | `id-payroll-pph21` |
| ID | PR | `id-withholding` |
| IE | IT-IND | `ie-freelance-intake` |
| IE | IT-IND | `ie-income-tax-form11` |
| IE | IT-IND | `ie-return-assembly` |
| IE | PR | `ie-foreign-tax-and-withholding` |
| IE | PR | `ie-payroll` |
| IE | PR+XB | `ie-paye-rental-nonresident` |
| IE | XB | `ie-cross-border` |
| IE | XB | `ie-prsi-cross-border` |
| IM | IT-IND | `im-income-tax` |
| IM | IT-IND | `im-non-resident-income-tax` |
| IM | XB | `im-related-party-uk-treaty` |
| IN | IT-IND | `in-freelance-intake` |
| IN | IT-IND | `in-income-tax` |
| IN | IT-IND | `in-income-tax` |
| IN | IT-IND | `in-return-assembly` |
| IN | IT-IND | `in-tds-freelance` |
| IN | VAT | `in-gst-return` |
| IN | VAT | `india-gst` |
| IT | SC | `it-employer-contributions` |
| IT | SC | `it-inps-contributions` |
| JP | IT-IND | `jp-freelance-intake` |
| JP | IT-IND | `jp-income-tax` |
| JP | IT-IND | `jp-return-assembly` |
| JP | VAT | `japan-consumption-tax` |
| JP | VAT | `jp-consumption-tax` |
| KE | IT-IND | `ke-income-tax` |
| KE | IT-IND | `ke-income-tax-2` |
| KE | IT-IND | `non-resident-rental-income-tax-on-kenyan-property` |
| KE | VAT | `ke-vat-return` |
| KE | VAT | `kenya-vat` |
| KN | SC | `kn-housing-social-development-levy` |
| KN | SC | `kn-social-security-contributions` |
| KR | VAT | `simplified-business-operator-registration-under-vat-act` |
| KR | VAT | `south-korea-vat` |
| KZ | IT-IND | `kz-freelance-intake` |
| KZ | IT-IND | `kz-income-tax` |
| KZ | IT-IND | `kz-return-assembly` |
| KZ | PR | `kz-payroll` |
| KZ | SC | `kz-social-contributions` |
| KZ | SC+PR | `kz-payroll-social` |
| LC | VAT | `lc-imported-services-vat` |
| LC | VAT | `lc-vat` |
| LK | IT-IND | `sri-lanka-capital-gains-tax` |
| LK | IT-IND | `sri-lanka-income-tax` |
| LK | PR | `sri-lanka-payroll` |
| LK | PR | `sri-lanka-withholding-tax` |
| MA | IT-IND | `ma-freelance-intake` |
| MA | IT-IND | `ma-income-tax` |
| MA | IT-IND | `ma-return-assembly` |
| MA | IT-IND | `morocco-income-tax` |
| MM | IT-IND | `mm-income-tax` |
| MM | IT-IND | `myanmar-personal-income-tax-2` |
| MM | IT-IND | `myanmar-personal-income-tax-4` |
| MM | VAT | `mm-vat-gst` |
| MM | VAT | `myanmar-vat-gst` |
| MM | VAT | `myanmar-vat-gst-2` |
| MT | IT-IND | `how-to-submit-capital-gain-taxes-in-malta` |
| MT | IT-IND | `malta-income-tax` |
| MT | IT-IND | `mt-capital-gains` |
| MT | IT-IND | `mt-freelance-intake` |
| MT | IT-IND | `mt-return-assembly` |
| MT | IT-IND | `mt-vat3-quarterly-return-malta` |
| MT | VAT | `malta-vat-return` |
| MT | VAT | `mt-reverse-charge-vat-services-received-from` |
| MX | IT-IND | `mx-freelance-intake` |
| MX | IT-IND | `mx-income-tax` |
| MX | IT-IND | `mx-return-assembly` |
| NG | IT-IND | `ng-freelance-intake` |
| NG | IT-IND | `ng-income-tax` |
| NG | IT-IND | `ng-personal-income-tax` |
| NG | IT-IND | `ng-return-assembly` |
| NG | VAT | `ng-vat` |
| NG | VAT | `ng-vat-return` |
| NG | VAT | `nigeria-vat` |
| NL | IT-IND | `nl-freelance-intake` |
| NL | IT-IND | `nl-income-tax` |
| NL | IT-IND | `nl-income-tax-special-groups` |
| NL | IT-IND | `nl-return-assembly` |
| NL | PR | `netherlands-payroll` |
| NL | PR | `nl-dividend-withholding` |
| NL | PR | `nl-payroll-tax` |
| NL | VAT | `netherlands-vat-return` |
| NL | VAT | `nl-vat-registration` |
| NL | VAT | `nl-vat-return` |
| NO | IT-IND | `no-capital-gains` |
| NO | IT-IND | `no-income-tax` |
| NO | IT-IND | `no-individual-residence` |
| NO | XB | `norway-to-switzerland-wealth-tax-exit` |
| NZ | IT-IND | `nz-capital-gains` |
| NZ | IT-IND | `nz-income-tax-ir3` |
| NZ | VAT | `new-zealand-gst` |
| NZ | VAT | `nz-gst-return` |
| PK | IT-IND | `pk-freelance-intake` |
| PK | IT-IND | `pk-income-tax` |
| PK | IT-IND | `pk-return-assembly` |
| PK | PR | `pk-payroll` |
| PK | PR | `pk-payroll-eobi` |
| PK | PR | `pk-withholding-tax` |
| PK | VAT | `pakistan-sales-tax` |
| PK | VAT | `pk-sales-tax-federal` |
| PK | VAT | `pk-sales-tax-services` |
| PL | IT-IND | `pl-capital-gains` |
| PL | IT-IND | `pl-income-tax` |
| PL | VAT | `pl-vat-return` |
| PL | VAT | `poland-vat-return` |
| PM | IT-IND | `pm-company-income-tax` |
| PM | IT-IND | `pm-personal-income-tax-2025` |
| PT | IT-IND | `pt-income-tax` |
| PT | IT-IND | `pt-return-assembly` |
| PT | VAT | `portugal-vat-return` |
| PT | VAT | `pt-vat-return` |
| PT | XB | `pt-cross-border` |
| PT | XB | `pt-foreign-source-treaties` |
| RO | IT-IND | `ro-employee-income-tax` |
| RO | IT-IND | `ro-income-tax` |
| RO | VAT | `ro-vat-return` |
| RO | VAT | `romania-vat-return` |
| RU | IT-IND | `ru-freelance-intake` |
| RU | IT-IND | `ru-income-tax` |
| RU | IT-IND | `ru-return-assembly` |
| RU | IT-IND | `ru-self-employed-npd` |
| RW | IT-IND | `rw-income-tax` |
| RW | IT-IND | `rwanda-income-tax` |
| SA | IT-IND | `sa-freelance-intake` |
| SA | IT-IND | `sa-return-assembly` |
| SE | IT-IND | `se-capital-gains` |
| SE | IT-IND | `se-employee-income-tax` |
| SE | IT-IND | `se-income-tax` |
| SE | VAT | `se-vat-return` |
| SE | VAT | `sweden-vat-return` |
| SG | VAT | `sg-gst-return` |
| SG | VAT | `singapore-gst` |
| SH | IT-IND | `sh-company-income-tax` |
| SH | IT-IND | `sh-individual-tax-residence` |
| SH | IT-IND | `sh-personal-income-tax` |
| SK | VAT | `slovakia-vat-registration-4-7-7a` |
| SK | VAT | `slovakia-vat-return` |
| TZ | PR | `tanzania-payroll` |
| TZ | PR | `tanzania-withholding-tax` |
| UA | IT-IND | `ua-freelance-intake` |
| UA | IT-IND | `ua-return-assembly` |
| US | IT-CORP | `us-1120-corporation-return-schedule-ordinary-business` |
| US | IT-CORP | `us-corporate-extension-form-7004-and-the` |
| US | IT-IND | `us-1099-k-and-payment-processors` |
| US | IT-IND | `us-amended-return-form-1040-including-capital` |
| US | IT-IND | `us-capital-gains` |
| US | IT-IND | `us-education-credits-8863` |
| US | IT-IND | `us-estate-gift-706-709` |
| US | IT-IND | `us-fbar-and-fatca-8938` |
| US | IT-IND | `us-federal-income-tax-return-1040` |
| US | IT-IND | `us-federal-return-assembly` |
| US | IT-IND | `us-foreign-earned-income-2555` |
| US | IT-IND | `us-foreign-tax-credit-1116` |
| US | IT-IND | `us-form-1040-individual-income-tax-return` |
| US | IT-IND | `us-form-1040-individual-return` |
| US | IT-IND | `us-form-1040-individual-return` |
| US | IT-IND | `us-form-1041-trust-and-estate-income` |
| US | IT-IND | `us-form-1065-partnership` |
| US | IT-IND | `us-form-1120-c-corp` |
| US | IT-IND | `us-form-5471-cfc-information` |
| US | IT-IND | `us-form-5472-foreign-owned-us` |
| US | IT-IND | `us-gilti-fdii-beat` |
| US | IT-IND | `us-irs-collections-and-controversy` |
| US | IT-IND | `us-multi-state-residency-and-allocation` |
| US | IT-IND | `us-pl-86-272-income-tax-nexus` |
| US | IT-IND | `us-pl-86-272-income-tax-nexus` |
| US | IT-IND | `us-pte-state-matrix` |
| US | IT-IND | `us-r-and-d-section-174-and-41` |
| US | IT-IND | `us-section-1031-like-kind-exchange` |
| US | IT-IND | `us-section-1202-qsbs` |
| US | IT-IND | `us-secure-2-and-retirement-updates` |
| US | IT-IND | `us-self-employed-health-insurance` |
| US | IT-IND | `us-self-employed-retirement` |
| US | IT-IND | `us-state-bonus-depreciation-conformity-matrix` |
| US | IT-IND | `us-state-estimated-tax-safe-harbors-matrix` |
| US | IT-IND | `us-state-formation-matrix` |
| US | IT-IND | `us-state-new-hire-reporting-matrix` |
| US | IT-IND | `us-tax-return-review-supporting-documents-findings` |
| US | IT-IND+PR | `us-form-941-940-payroll` |
| US | IT-IND+PR | `us-state-payroll-matrix` |
| US | PR | `us-form-941-940-payroll` |
| US | PR | `us-state-payroll-matrix` |
| US | VAT | `no-sales-tax-states` |
| US | VAT | `us-sales-tax` |
| US | VAT | `us-sales-tax-nexus-50-state-matrix` |
| US | VAT | `us-sales-tax-nexus-50-state-matrix` |
| US | XB | `us-expatriation-exit-tax` |
| US | XB | `us-nonresident-cgt` |
| US-AL | IT-IND | `al-income-tax` |
| US-AL | IT-IND | `alabama-income-tax` |
| US-AL | VAT | `al-sales-tax` |
| US-AL | VAT | `alabama-sales-tax` |
| US-AR | VAT | `ar-sales-tax` |
| US-AR | VAT | `arizona-sales-tax` |
| US-AR | VAT | `arkansas-sales-tax` |
| US-CA | IT-IND | `ca-540-individual-return` |
| US-CA | IT-IND | `ca-income-tax` |
| US-CA | IT-IND | `us-ca-freelance-intake` |
| US-CA | IT-IND | `us-ca-return-assembly` |
| US-CO | VAT | `co-sales-tax` |
| US-CO | VAT | `colorado-sales-tax` |
| US-CO | VAT | `connecticut-sales-tax` |
| US-GA | IT-CORP | `ga-corporate-and-ptet` |
| US-GA | IT-CORP | `georgia-corporate-income-tax-returns-form-600` |
| US-GA | IT-CORP | `georgia-pass-through-entity-returns-form-700-partnership-and-form-600s-s-corporation` |
| US-GA | IT-IND | `ga-income-tax` |
| US-GA | IT-IND | `georgia-individual-tax-return-form-500` |
| US-ID | VAT | `id-sales-tax` |
| US-ID | VAT | `idaho-sales-tax` |
| US-IL | IT-IND | `il-estimated-tax` |
| US-IL | IT-IND | `il-income-tax` |
| US-IL | VAT | `il-sales-tax` |
| US-IL | VAT | `illinois-sales-tax` |
| US-IN | VAT | `in-sales-tax` |
| US-IN | VAT | `indiana-sales-tax` |
| US-KS | PR | `ks-payroll` |
| US-KS | PR | `ks-social-contributions` |
| US-MA | VAT | `ma-sales-tax` |
| US-MA | VAT | `maine-sales-tax` |
| US-MA | VAT | `maryland-sales-tax` |
| US-MA | VAT | `massachusetts-sales-tax` |
| US-MI | IT-IND | `mi-detroit-individual-return` |
| US-MI | IT-IND | `mi-income-tax` |
| US-MI | IT-IND | `mi-return-assembly` |
| US-MN | VAT | `minnesota-sales-tax` |
| US-MN | VAT | `mn-sales-tax` |
| US-MO | VAT | `missouri-sales-tax` |
| US-MO | VAT | `mo-sales-tax` |
| US-MS | VAT | `mississippi-sales-tax` |
| US-MS | VAT | `ms-sales-tax` |
| US-NC | IT-IND | `nc-income-tax` |
| US-NC | IT-IND | `nc-return-assembly` |
| US-ND | IT-IND | `nd-income-tax` |
| US-ND | IT-IND | `nd-return-assembly` |
| US-NJ | VAT | `new-jersey-sales-tax` |
| US-NJ | VAT | `nj-sales-tax` |
| US-NM | VAT | `new-mexico-sales-tax` |
| US-NM | VAT | `nm-sales-tax` |
| US-NV | VAT | `nevada-sales-tax` |
| US-NV | VAT | `nv-sales-tax` |
| US-NY | IT-IND | `ny-estimated-tax` |
| US-NY | IT-IND | `ny-income-tax` |
| US-NY | IT-IND | `ny-it-201-resident-return` |
| US-NY | IT-IND | `nyc-ubt` |
| US-NY | IT-IND | `us-ny-freelance-intake` |
| US-NY | IT-IND | `us-ny-return-assembly` |
| US-NY | VAT | `new-york-sales-tax` |
| US-NY | VAT | `ny-sales-tax` |
| US-OH | VAT | `oh-sales-tax` |
| US-OH | VAT | `ohio-sales-tax` |
| US-OK | VAT | `ok-sales-tax` |
| US-OK | VAT | `oklahoma-sales-tax` |
| US-PA | VAT | `pa-sales-tax` |
| US-PA | VAT | `pennsylvania-sales-tax` |
| US-TX | IT-IND | `tx-franchise-tax` |
| US-TX | IT-IND | `us-tx-freelance-intake` |
| US-TX | IT-IND | `us-tx-return-assembly` |
| US-TX | VAT | `texas-sales-tax` |
| US-TX | VAT | `tx-sales-tax` |
| US-UT | VAT | `ut-sales-tax` |
| US-UT | VAT | `utah-sales-tax` |
| US-WA | VAT | `wa-sales-tax` |
| US-WA | VAT | `washington-sales-tax` |
| US-WI | VAT | `wi-sales-tax` |
| US-WI | VAT | `wisconsin-sales-tax` |
| US-WY | VAT | `wy-sales-tax` |
| US-WY | VAT | `wyoming-sales-tax` |
| ZA | IT-IND | `capital-gains-tax-rate-tables-2023-to-2027` |
| ZA | IT-IND | `income-tax-rate-tables-by-year-of-assessment-2023-to-2027` |
| ZA | IT-IND | `za-capital-gains` |
| ZA | IT-IND | `za-capital-gains-tables` |
| ZA | IT-IND | `za-income-tax` |
| ZA | IT-IND | `za-income-tax-tables` |
| ZA | VAT | `south-africa-vat` |
| ZA | VAT | `za-vat-return` |
| ZA | VAT+XB | `cancelling-a-vat-registration-and-the-exit-vat-charge` |
| ZA | XB | `leaving-south-africa-tax-emigration` |
