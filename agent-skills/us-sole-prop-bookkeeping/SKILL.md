---
name: us-sole-prop-bookkeeping
description: "Classify a US sole proprietor's or single-member LLC's 2026 bank, card and payment processor transactions into the lines of the 2026 Schedule C (Form 1040), from statements alone or with receipts. Holds the bank and processor pattern library (Chase, Wells Fargo, Mercury, Stripe, PayPal, Square, SaaS, travel, fuel, government payments, personal items), the 2026 line map (16a mortgage, 16b vehicle loan, 16c other interest, 27a Form 7205 only, 27b other expenses from Part V), the 50% meals and 0% entertainment rules, section 274(d) substantiation, the 2026 standard mileage rates (72.5 cents to 30 June, 76 cents from 1 July), the de minimis safe harbor, the USD 2,000 Form 1099-NEC threshold for 2026 payments, conservative defaults, ambiguity questions and the working paper layout. Trigger on \"categorize my transactions\", \"Schedule C bookkeeping\", \"which line does this go on\", \"is this deductible for my business\", \"bank statement to Schedule C\". Feeds us-schedule-c-and-se-computation. Feder"
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/us-sole-prop-bookkeeping"
  jurisdiction: "US"
  tax_year: "2026"
  last_updated: "2026-11-13"
---

# US sole proprietor bookkeeping into Schedule C, tax year 2026

> **Source-cited draft.** Built from the 2026 Schedule C (Form 1040), IRS Notice 2026-10 and the IRS standard mileage rates page, Rev. Proc. 2025-32, Treas. Reg. 1.263(a)-1(f) and Notice 2015-82, Public Law 119-21 and 26 U.S.C. 162, 262, 274, 280F and 6050W, read on 2026-11-13. No accountant has reviewed it. All outputs must be reviewed by a qualified tax professional before filing.

**Answer first.** Every business deposit and payment is put on one 2026 Schedule C line or excluded. Processor payouts (Stripe, PayPal, Square) are not revenue: line 1 is the gross the customer paid, and the processor fee goes to line 27b with the other Part V expenses. Line 27a is only the energy efficient commercial buildings deduction (Form 7205). Interest is split three ways on the 2026 form: 16a mortgage, 16b vehicle loan (business share), 16c other. Meals with a documented business purpose are 50% (line 24b), entertainment is 0%. Taxes on income, owner draws, personal items and the owner's health insurance and retirement contributions never go on Schedule C. When a fact is missing, the default is the conservative one (exclude, or 0% business use) and the client is asked.

## Scope and who this is for

In scope: transaction classification for tax year 2026 for one individual's Schedule C business: a sole proprietor, or a single-member LLC disregarded for federal tax, on the cash method unless the client uses accrual.

| Field | Detail |
| --- | --- |
| Form | Schedule C (Form 1040) 2026, Profit or Loss From Business |
| Return | 2026 Form 1040, due 15 April 2027 (15 October 2027 on extension) |
| Currency | USD |
| Key law | Internal Revenue Code; Public Law 119-21 (4 July 2025) |

Out of scope, and where it goes:

| Topic | Skill |
| --- | --- |
| Net profit, home office method and Schedule SE | `us-schedule-c-and-se-computation` |
| Section 179, bonus depreciation and the vehicle depreciation caps | `us-section-179-and-bonus-depreciation` |
| Issuing Forms 1099-NEC to contractors | `us-1099-nec-issuance` |
| Forms 1099-K received from processors and marketplaces | `us-1099-k-and-payment-processors` |
| Owner's health insurance (Schedule 1) | `us-self-employed-health-insurance` |
| Owner's retirement contributions (Schedule 1) | `us-self-employed-retirement` |
| QBI | `us-qbi-deduction` |
| Payroll returns for employees | `us-form-941-940-payroll` |
| Hiring the owner's children, accountable plans | `us-hiring-your-children-and-accountable-plans` |
| Capital assets, crypto | `us-capital-gains` |
| Whole-return order | `us-federal-return-assembly` |

## Ask the client first

**Minimum:** the full-year 2026 statement (CSV, PDF or pasted) for every account the business uses, 1 January to 31 December 2026. Any US bank works (Chase Business, Wells Fargo Business, Bank of America Business, Capital One Spark, Mercury, Relay, Novo, Bluevine and others). With no statement at all, stop.

**Recommended:** every Form 1099-NEC, 1099-MISC and 1099-K received; the 2025 Schedule C and Form 4562 (depreciation, vehicle method, home office method carried forward); receipts for single expenses over USD 75; card statements where business spending runs through a card.

**Ideal:** a contemporaneous mileage log; home office measurements; the invoice register; W-9s from contractors; Forms 1095 for health insurance.

If only statements are available, proceed and put this in the reviewer note: "This working paper was produced from bank statements alone. The reviewer must verify: (a) all 1099 income is captured, (b) prior-year depreciation elections are carried forward, (c) the vehicle method chosen in the first year of use is honoured, and (d) section 274(d) substantiation exists for travel, meals, gifts and listed property."

Infer from the data first; ask only what the data cannot answer:

| Fact | Inference from the data | Question if it cannot be inferred |
| --- | --- | --- |
| Entity | DBA or the owner's name means sole proprietor; "LLC" means a single-member LLC; several owners suggests a partnership | "Are you a sole proprietor, single-member LLC, partnership, S corporation or C corporation?" |
| Accounting method | Most sole proprietors use cash | "Do you use the cash or accrual method?" |
| Principal activity | Counterparty mix and 1099 descriptions | "What does the business do?" (for the business code on line B) |
| EIN or SSN | Not inferable | "Does the business have an EIN, or do you use your SSN?" |
| Prior year return | Not inferable | "Can you send the 2025 Schedule C and Form 4562?" |
| Home office | Residential address and no office rent | "Is part of your home used regularly and only for the business? Square feet of that area and of the home?" |
| Vehicle | Fuel and repair charges | "Which vehicle, which method (standard mileage or actual), business miles 1 January to 30 June and 1 July to 31 December 2026, and is there a log?" |
| Employees | Gusto or ADP charges, regular payments to individuals | "Do you have W-2 employees?" |
| Inventory | Wholesale supplier payments | "Do you sell physical products and keep inventory?" |
| Health insurance | Premium payments | "Do you pay your own health insurance, and could you join a spouse's employer plan in any month?" |

## The method, step by step

### Rates, bands and thresholds

| Item | Amount, 2026 | Source |
| --- | --- | --- |
| Standard mileage rate, business, 1 January to 30 June 2026 | 72.5 cents a mile | [IRS Notice 2026-10](https://www.irs.gov/pub/irs-drop/n-26-10.pdf) |
| Standard mileage rate, business, 1 July to 31 December 2026 | 76 cents a mile | [IRS standard mileage rates](https://www.irs.gov/tax-professionals/standard-mileage-rates) |
| Business meals, deductible share | 50% | [26 U.S.C. 274(n)(1)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partIX-sec274.htm) |
| Entertainment, deductible share | 0% | [26 U.S.C. 274(a)(1)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partIX-sec274.htm) |
| Business gifts, deductible per recipient per year | USD 25 | [26 U.S.C. 274(b)(1)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partIX-sec274.htm) |
| De minimis safe harbor per item or invoice, no applicable financial statement (raised from the regulation's USD 500) | USD 2,500 | [IRS Notice 2015-82](https://www.irs.gov/pub/irs-drop/n-15-82.pdf) |
| De minimis safe harbor per item or invoice, with an applicable financial statement | USD 5,000 | [Treas. Reg. 1.263(a)-1(f)(1)(i)(D)](https://www.ecfr.gov/current/title-26/section-1.263(a)-1) |
| Form 1099-NEC and 1099-MISC base threshold, payments made after 31 December 2025 | USD 2,000 | [Rev. Proc. 2025-32](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| Form 1099-K from a payment app or marketplace: both tests | more than USD 20,000 and more than 200 transactions | [Public Law 119-21, section 70432](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm) |
| Gross receipts test (small business inventory and cash method rules) | USD 32,000,000 average over the prior 3 years | [Rev. Proc. 2025-32](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| Heavy vehicle line for the passenger car depreciation caps | over 6,000 pounds gross vehicle weight | [26 U.S.C. 280F(d)(5)(A)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partIX-sec280F.htm) |

Section 179, bonus depreciation and the 2026 passenger car depreciation caps are in `us-section-179-and-bonus-depreciation`; the home office rate and cap are in `us-schedule-c-and-se-computation`. There is no 100% restaurant meal deduction in 2026: the temporary rule for 2021 and 2022 has expired and was not renewed.

### Step 1: the 2026 Schedule C line map

| Line | Content |
| --- | --- |
| 1 | Gross receipts or sales |
| 2 | Returns and allowances |
| 4 | Cost of goods sold (Part III, line 42) |
| 6 | Other income (including fuel tax credits or refunds) |
| 8 | Advertising |
| 9 | Car and truck expenses |
| 10 | Commissions and fees |
| 11 | Contract labor |
| 12 | Depletion |
| 13 | Depreciation and section 179 (Form 4562) |
| 14 | Employee benefit programs (employees, not the owner) |
| 15 | Insurance (other than health) |
| 16a | Interest: mortgage paid to banks |
| 16b | Interest: vehicle loan (business share) |
| 16c | Interest: other |
| 17 | Legal and professional services |
| 18 | Office expense |
| 19 | Pension and profit-sharing plans (employees only) |
| 20a | Rent or lease: vehicles, machinery, equipment |
| 20b | Rent or lease: other business property |
| 21 | Repairs and maintenance |
| 22 | Supplies |
| 23 | Taxes and licenses |
| 24a | Travel |
| 24b | Deductible meals (50% applied) |
| 25 | Utilities |
| 26 | Wages (less employment credits) |
| 27a | Energy efficient commercial buildings deduction (attach Form 7205) only |
| 27b | Other expenses, listed in Part V and totalled on line 48 (bank charges, merchant fees, software, cloud hosting) |
| 30 | Business use of home (computed in `us-schedule-c-and-se-computation`) |

Source: [Schedule C (Form 1040) 2026](https://www.irs.gov/pub/irs-pdf/f1040sc.pdf).

### Step 2: read the statement and strip out what is not business

- **Chase Business CSV:** columns `Details, Posting Date, Description, Amount, Type, Balance, Check or Slip #`; dates MM/DD/YYYY; debits negative. `ORIG CO NAME:STRIPE TRANSFER` is a Stripe payout; `CHASE CREDIT CRD AUTOPAY` paying a personal card is an owner draw; `GUSTO` or `ADP` is payroll (wages line 26, employer taxes line 23); `ONLINE TRANSFER TO CHK...` is an internal transfer.
- **Wells Fargo Business CSV:** columns `Date, Amount, *, Check Number, Description`; `PURCHASE AUTHORIZED ON MM/DD [COUNTERPARTY] CARD XXXX` is a card purchase; `BILL PAY` names the payee; `WIRE TYPE:WIRE IN` may be a client payment.
- **Mercury CSV:** columns `Date, Description, Amount, Status, Bank Description, Running Balance`; dates YYYY-MM-DD; processor payouts are labelled.
- **Internal transfers** between the owner's accounts: exclude.
- **Card payments from the business account:** paying a personal card is an owner draw; paying a business card is a debt payment, and the card's individual charges are what get classified.
- **Duplicates:** a purchase on the card statement and the lump card payment on the bank statement are one expense; classify the card line only.
- **Owner draws and personal use:** exclude.
- **Refunds, returns, credits, reversals, chargebacks:** a customer refund goes to line 2; a vendor refund reduces the original expense line.

### Step 3: apply the pattern library

Match the counterparty by case-insensitive substring, most specific pattern first. If nothing matches, go to step 4.

**Banks**

| Pattern | Treatment | Line |
| --- | --- | --- |
| CHASE, JPMORGAN CHASE, WELLS FARGO, WFBNA, BANK OF AMERICA, BOA, BOFA | Service charges, wire and overdraft fees: bank charges | 27b |
| CAPITAL ONE | Fees: bank charges; keep separate from Capital One card purchases | 27b |
| MERCURY, RELAY, NOVO, BLUEVINE | Fintech bank fees | 27b |
| INTEREST INCOME, INT EARNED | Usually Schedule B interest, not Schedule C; flag | 6 or exclude |
| LOAN, BUSINESS LOAN, LINE OF CREDIT | Proceeds are not income and principal is not deductible; interest only | 16c |

**Payment processors**

| Pattern | Treatment | Line |
| --- | --- | --- |
| STRIPE TRANSFER, STRIPE PAYOUT | Exclude the payout; take gross sales from the dashboard to line 1 | none |
| PAYPAL TRANSFER, PAYPAL INST XFER | Same as Stripe | none |
| SQUARE, SQ *, SQUAREUP | Same; Square deposits are net of fees | none |
| VENMO BUSINESS, VENMO CASHOUT | Same; gross is revenue | none |
| STRIPE FEE, PAYPAL FEE, SQ FEE | Merchant processing fees | 27b |

If only statements are available, processor deposits are net. The working paper says: "Revenue from [processor] is reported net of fees. The reviewer must take gross revenue from the [processor] dashboard and add the fees back to line 1 and to line 27b."

**Software and cloud**

| Pattern | Treatment | Line |
| --- | --- | --- |
| AWS, AMAZON WEB SERVICES | Cloud hosting | 27b |
| GOOGLE WORKSPACE, GOOGLE CLOUD, GOOGLE *GSUITE | Software subscriptions | 27b |
| MICROSOFT 365, MSFT *OFFICE, AZURE | Software or hosting | 27b |
| ADOBE, ADOBE *CREATIVE, SLACK, NOTION, GITHUB, JETBRAINS, FIGMA, CANVA, DROPBOX | Software subscriptions | 27b |
| ZOOM, ZOOM.US | Software (or line 25 if treated as telecom); default software | 27b |
| MAILCHIMP, CONVERTKIT, CONSTANT CONTACT | Email marketing | 8 |
| HUBSPOT | Marketing use line 8, general CRM 27b; default 27b | 27b |
| QUICKBOOKS, INTUIT *QB, XERO, FRESHBOOKS, WAVE | Accounting software | 27b |

**Office and coworking**

| Pattern | Treatment | Line |
| --- | --- | --- |
| WEWORK, REGUS, IWG, SPACES, INDUSTRIOUS | Coworking rent | 20b |
| OFFICE RENT, COMMERCIAL LEASE | Office lease | 20b |

**Communication**

| Pattern | Treatment | Line |
| --- | --- | --- |
| VERIZON, VZ WIRELESS, AT&T, ATT, T-MOBILE, TMOBILE, GOOGLE FI | Phone, business share only; a shared personal line goes to step 4 | 25 |
| COMCAST, XFINITY, SPECTRUM, CHARTER | Internet, business share only | 25 |

**Insurance**

| Pattern | Treatment | Line |
| --- | --- | --- |
| STATE FARM, GEICO, PROGRESSIVE, ALLSTATE, USAA (auto) | Personal auto cover: exclude; a business vehicle on actual costs puts the business share on line 9 | 9 or none |
| HARTFORD, HISCOX, NEXT INSURANCE, THIMBLE, GENERAL LIABILITY, E&O, PROFESSIONAL LIABILITY | Business insurance | 15 |
| WORKERS COMP | Workers' compensation for employees | 15 |
| HEALTH INSURANCE, BLUE CROSS, AETNA, UNITED HEALTH, CIGNA, KAISER | Owner's health cover: exclude; Schedule 1 via `us-self-employed-health-insurance` | none |

**Meals**

| Pattern | Treatment | Line |
| --- | --- | --- |
| Any named restaurant | 50% if business purpose and attendees are documented | 24b |
| UBER EATS, DOORDASH, GRUBHUB, POSTMATES | Same substantiation as a restaurant | 24b |
| STARBUCKS, DUNKIN, coffee shops | 50% only if a client or business contact was present; solo coffee is personal | 24b or none |
| ENTERTAINMENT, CONCERTS, SPORTS TICKETS | Entertainment: not deductible | none |

The only 100% food items are de minimis workplace snacks and coffee (section 132(e)) and meals for the employer's convenience (section 119).

**Travel**

| Pattern | Treatment | Line |
| --- | --- | --- |
| UNITED, DELTA, AMERICAN AIRLINES, SOUTHWEST, JETBLUE, ALASKA AIR, FRONTIER, SPIRIT | Airfare on a trip primarily for business; split off personal days | 24a |
| MARRIOTT, HILTON, HYATT, IHG, BEST WESTERN, HOLIDAY INN | Business lodging; business days only | 24a |
| AIRBNB (as a guest) | Business lodging; hosting income is a rental, see refusals | 24a |
| HERTZ, ENTERPRISE, NATIONAL, AVIS, BUDGET | Rental car while travelling | 24a |
| UBER, LYFT out of town | Ground transport while travelling; local rides are line 9 or commuting | 24a |
| AMTRAK | Train fare while travelling | 24a |

**Vehicle**

| Pattern | Treatment | Line |
| --- | --- | --- |
| SHELL, CHEVRON, BP, EXXON, MOBIL, SUNOCO, MARATHON, SPEEDWAY, WAWA | Fuel: only with the actual-cost method and a documented business share; included in the mileage rate otherwise | 9 |
| JIFFY LUBE, VALVOLINE, MIDAS, PEP BOYS, AUTOZONE, O'REILLY, CARWASH | Repairs and parts: same rule as fuel | 9 |
| PARKING, PARKWHIZ, SPOTHERO | Business parking, deductible on top of the mileage rate; commuting parking is not | 9 |
| TOLL, EZPASS, SUNPASS, IPASS | Business tolls, deductible on top of the mileage rate; commuting tolls are not | 9 |
| AUTO LOAN, car finance company | Interest only, business share | 16b |

**Professional services**

| Pattern | Treatment | Line |
| --- | --- | --- |
| CPA, ACCOUNTING, TAX PREPARATION, ENROLLED AGENT | Business return and books; personal return prep is not deductible; allocate a combined bill | 17 |
| ATTORNEY, LAW OFFICE, LEGAL SERVICES, ESQ | Business legal matters only | 17 |
| BOOKKEEPER, BOOKKEEPING SERVICE | Bookkeeping | 17 |
| CONSULTANT, CONSULTING | Advice line 17, operational work line 11; default 17 | 17 |
| LEGALZOOM, INCFILE, NORTHWEST REGISTERED AGENT | Formation and registered agent | 17 |

**Contractors**

| Pattern | Treatment | Line |
| --- | --- | --- |
| FIVERR, UPWORK, TOPTAL | Platform contractor payments; the platform reports, so usually no 1099-NEC from the client | 11 |
| Individuals paid for services | Contract labor; flag for a 1099-NEC if paid USD 2,000 or more in 2026 by non-card, non-platform means | 11 |

Payments by card or through a payment settlement entity are reported on Form 1099-K by the processor and are left off Form 1099-NEC. Zelle, ACH, wire, check, cash and personal Venmo are not; the business issues the 1099-NEC. Details: `us-1099-nec-issuance`. Source: [26 U.S.C. 6050W](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap61-subchapA-partIII-subpartB-sec6050W.htm).

**Government**

| Pattern | Treatment | Line |
| --- | --- | --- |
| IRS, UNITED STATES TREASURY, EFTPS, US TREASURY, USATAXPYMT | Federal income, self-employment and estimated tax: exclude | none |
| FTB, FRANCHISE TAX BOARD, STATE TAX PAYMENT, STATE ESTIMATED TAX | State income tax: exclude (Schedule A, see `us-federal-income-tax-return-1040` for the cap) | none |
| EDD, EMPLOYMENT DEVELOPMENT, state unemployment | Employer unemployment tax line 23; employee withholding passed through: exclude | 23 or none |
| BUSINESS LICENSE, CITY LICENSE, COUNTY LICENSE | Licences and permits | 23 |
| SECRETARY OF STATE, SOS FILING | LLC annual fee, registration | 23 |
| SALES TAX REMITTANCE | Exclude if sales tax was kept out of line 1; line 23 if it was included in line 1 | 23 or none |

**Personal (exclude)**

| Pattern | Treatment |
| --- | --- |
| NETFLIX, HULU, DISNEY+, HBO MAX, PARAMOUNT+ | Personal streaming |
| SPOTIFY, APPLE MUSIC, PANDORA | Personal music (background music at business premises, documented, could be 27b) |
| GYM, PLANET FITNESS, EQUINOX, LA FITNESS, ORANGETHEORY | Personal fitness |
| GROCERY, WHOLE FOODS, TRADER JOE, COSTCO | Personal groceries |
| TARGET, WALMART | Personal unless the receipt shows business supplies |
| AMAZON (unspecified) | Step 4, default personal |
| CLOTHING, NORDSTROM, ZARA, H&M, GAP | Personal unless a uniform or protective gear unsuitable for everyday wear |
| MORTGAGE, RENT (home) | Personal; any home office goes through line 30 |
| Home utilities | Personal; any home office goes through line 30 |
| MEDICAL, PHARMACY, CVS, WALGREENS | Personal medical |
| CHARITABLE, DONATION, TITHE | Schedule A, not Schedule C (a sponsorship with advertising value can be line 8) |
| VENMO, ZELLE, CASH APP (personal transfers) | Personal transfers |
| CHILD CARE, DAYCARE, TUITION | Personal (a dependent care credit may apply) |

### Step 4: rules for clear data

1. **Revenue (line 1).** All business receipts, cash method unless accrual applies: client payments, 1099-NEC and 1099-K amounts, cash and barter, tips. Gross up processor deposits. Line 1 should be at least the total of the 1099s received. Source: [Schedule C (Form 1040) 2026](https://www.irs.gov/pub/irs-pdf/f1040sc.pdf).
2. **Capital or expense.** An item over the de minimis amount per invoice or item is capitalized and goes to Form 4562 (line 13); at or under it, expense it on line 18 or 22 if the annual election is made on the return. The acquisition date (binding contract or order date, not the bank date) decides the bonus rate; take the rate from `us-section-179-and-bonus-depreciation`. Section 179 is income-limited; bonus is not. Record both options for the reviewer.
3. **Home office.** Regular and exclusive use, and principal place of business or a place to meet clients or a separate structure. No measurements, no deduction. The method and the figures are in `us-schedule-c-and-se-computation`.
4. **Vehicle (line 9).** Standard mileage: business miles in each half of 2026 times that half's rate, plus business parking and tolls. Actual costs: fuel, repairs, insurance, registration, lease and depreciation times the business-use share, with the passenger car caps. A vehicle used with actual costs and MACRS depreciation in its first business year cannot switch to the standard rate; one that started on the standard rate can switch to actual costs (straight-line depreciation). Without a contemporaneous log (date, destination, purpose, miles) the deduction is nil under section 274(d). Commuting is never deductible, except trips from a home office that is the principal place of business.
5. **Meals (line 24b).** 50%, with the amount, date, place, business purpose and the business relationship of those present. Entertainment 0%.
6. **Travel (line 24a).** Away from the tax home overnight, primarily for business: fares, lodging, car hire, local transport, tips, laundry, and meals at 50%. Mixed domestic trips: transport in full if primarily business, lodging and meals for business days only. Foreign trips over 7 days with 25% or more personal days need an allocation. Source: [IRS Publication 463](https://www.irs.gov/pub/irs-pdf/p463.pdf).
7. **Contract labor (line 11).** Payments for services by non-employees; flag the Form 1099-NEC duty at USD 2,000 for 2026 payments.
8. **Insurance (line 15).** Liability, professional, workers' compensation, business property and cyber cover. Not personal auto, home, health or life.
9. **Taxes and licenses (line 23).** Business licences, permits, business taxes that are not income taxes, the employer share of FICA and FUTA, property tax on business assets.
10. **Interest (lines 16a to 16c).** Business mortgage 16a; business share of vehicle loan interest 16b; other business interest 16c. The personal car loan interest deduction on Schedule 1-A is not Schedule C; interest already deducted on Schedule C cannot be claimed there.
11. **Rent (lines 20a, 20b).** Vehicle and equipment leases 20a; office, coworking and other property 20b.
12. **Advertising (line 8).** Online ads, print, business cards, website build and hosting, domains, SEO, email marketing, trade show stands, promotional items. Political spending and lobbying are not deductible (section 162(e)); client gifts above USD 25 per recipient per year are not deductible.
13. **Supplies and office (lines 18, 22).** Office and admin items line 18; materials used in delivering the work line 22.
14. **Inventory.** With average gross receipts at or under the 2026 gross receipts test amount, the small business rule lets inventory be treated as non-incidental materials and supplies, deducted when used or sold.
15. **Hobby risk.** A net loss is flagged. The presumption of profit motive is met with profit in 3 of 5 years (section 183(d)).
16. **Never on Schedule C:** federal and state income tax payments; owner draws; owner's health insurance (Schedule 1) and retirement contributions (Schedule 1); any personal expense (section 262); charitable gifts; commuting; political contributions; government fines and penalties (section 162(f)); everyday clothing; personal loan and card payments. Sources: [26 U.S.C. 162](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partVI-sec162.htm), [26 U.S.C. 262](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partIX-sec262.htm), [26 U.S.C. 183](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partVI-sec183.htm).

### Step 5: what to ask when the data is not enough

| Ambiguity | Why the statement is not enough | Default | Question |
| --- | --- | --- | --- |
| Fuel and vehicle charges | Vehicle, method, business share and log are unknown | 0% business use | "Which vehicle, standard mileage or actual costs, business miles in each half of 2026, and do you keep a log?" |
| Home utilities, insurance, mortgage | Office existence, size and exclusive use are unknown | 0% | "Is there an area used regularly and only for the business? Its square feet, and the home's?" |
| Restaurants and food delivery | Business purpose and attendees are unknown | Personal | "For each meal: who was there, and what was the business purpose?" |
| Shared phone or home internet | Business share is unknown | 0% | "Is this a dedicated business line, or shared? If shared, what share is business?" |
| AMAZON, AMZN, AMZN MKTP | The product is rarely shown | Personal | "Please check the order history and tell me which orders were business items and what they are used for." |
| ATM and cash withdrawals | Use is unknown | Owner draw | "What was the cash spent on? Any receipts?" |
| Mixed subscriptions (Adobe, Microsoft, Apple, Google) | Business and personal use mix | Business if in the software list above, else personal | "Is this used mainly for the business? If mixed, what share?" |
| Flight and hotel spanning a weekend | Business and personal days are unknown | Exclude the trip | "How many days were business, how many personal, and what was the purpose?" |

### Step 6: the working paper

**Sheet "Transactions":** A date; B counterparty as on the statement; C description; D amount (debits negative); E Schedule C line; F gross amount; G deductible amount (after the 50% meals limit or business-use share); H section 274(d) substantiation (yes, no, not needed); I default applied (Y/N); J question for the client; K reviewer attention reason; L notes.

**Sheet "Schedule C Summary":** one row per line, summing column G by line with `=SUMIFS(Transactions!G:G, Transactions!E:E, "<line>")`, for lines 1, 2, 4, 6, 8 to 15, 16a, 16b, 16c, 17, 18, 20a, 20b, 21 to 23, 24a, 24b, 25, 26, 27a and 27b.

**Sheet "Return Form":** line 7 = (line 1 − line 2 − line 4) + line 6; line 28 = lines 8 to 27b; line 29 = line 7 − line 28; line 30 from `us-schedule-c-and-se-computation`; line 31 = line 29 − line 30. A loss is flagged for hobby and at-risk review.

**Sheet "Asset Register":** description, date acquired, date placed in service, cost, recovery period, convention, method, section 179 amount, bonus rate, current-year depreciation, acquisition-date flag, notes.

**Format:** blue for values from the statement, black for formulas, green for cross-sheet references, yellow fill for rows where a default was applied. Recalculate before delivery (for example `soffice --headless --convert-to xlsx --outdir <dir> <file>.xlsx`), reopen, and fix any formula error before presenting it.

## Boundary and exception table

| Situation | Treatment |
| --- | --- |
| Processor payout on the statement | Exclude the payout; line 1 is gross, fee line 27b |
| Software, bank or merchant fees | Line 27b (Part V), never line 27a |
| Vehicle loan interest | Business share on line 16b (new line on the 2026 form); other interest 16c |
| Solo coffee while working at home | Personal |
| Meal while travelling overnight on business | 50%, line 24b |
| Asset ordered before 20 January 2025, placed in service in 2026 | The old phase-down bonus rate applies; see `us-section-179-and-bonus-depreciation` |
| Item of USD 2,400 with no applicable financial statement | Can be expensed if the de minimis election is made |
| Vehicle over 6,000 pounds | Passenger car caps do not apply; section 179 SUV limit does (sibling skill) |
| Contractor paid USD 1,900 by Zelle in 2026 | Under the USD 2,000 threshold: no 1099-NEC |
| Contractor paid USD 2,500 by Zelle in 2026 | 1099-NEC due from the business |
| Contractor paid by card or through a payment platform | Reported on Form 1099-K by the processor; no 1099-NEC |
| Sales tax included in line 1 | Remittance on line 23 |
| Health insurance paid from the business account | Exclude from Schedule C; Schedule 1 |
| Personal card paid from the business account | Owner draw |

### Defaults when a fact is missing

| Missing fact | Default |
| --- | --- |
| Business share of vehicle, home office, phone or internet | 0% |
| Business or personal | Personal |
| Business purpose of a meal | Personal |
| Business or personal travel day | Personal |
| Acquisition date of an asset near 20 January 2025 | The earlier date (lower bonus rate) |
| Cost basis of an asset | No depreciation |
| Recovery period | The longest plausible |
| Employee or contractor | Contractor (line 11) with a classification flag |
| Payee's entity type | Assume a 1099-NEC is needed |
| Amazon purchase with no description | Personal |
| Cash withdrawal | Owner draw |
| Processor fee: per transaction or subscription | Merchant fee, line 27b |

### Red flags for the reviewer

| Flag | Level |
| --- | --- |
| Single transaction of USD 5,000 or more | High |
| Vehicle business use claimed without a mileage log | High |
| Meals above 20% of gross receipts | High |
| Contractor paid USD 2,000 or more in 2026 without a W-9 or 1099 status | Medium |
| Home office claimed without measurements | Medium |
| More than 5 defaults applied across the return | Medium |
| Schedule C net loss (hobby and at-risk questions) | Low |
| Line 1 below the 1099-NEC and 1099-K totals | Medium |

## Worked cases

Six classification lines from a freelance developer's 2026 Chase Business Checking statement:

| Date | Counterparty | USD | Line | Default? | Question |
| --- | --- | --- | --- | --- | --- |
| 01/15/2026 | STRIPE TRANSFER | +4,827.50 | excluded payout | Y | Gross sales and fees from the Stripe dashboard |
| 02/01/2026 | GITHUB INC | −19.00 | 27b software | N | none |
| 03/12/2026 | THE CAPITAL GRILLE | −187.42 | 24b at 50%, or personal | Y | Who was present, and the business purpose? |
| 01/22/2026 | APPLE STORE (MacBook) | −3,499.00 | 13, Form 4562 (over USD 2,500) | Y | Order date, and section 179 or bonus? |
| 04/08/2026 | SHELL OIL | −62.18 | 9 at 0%, or excluded | Y | Vehicle, method, business share, log? |
| 06/15/2026 | IRS USATAXPYMT | −5,000.00 | excluded, personal tax | N | none |

**Case 1: grossing up a Stripe payout, and a client meal.** The Stripe dashboard shows January sales of USD 5,000 and fees of USD 172.50, paid out as USD 4,827.50. The client confirms the Capital Grille dinner was with a prospective client, to discuss a contract.

Line 1 gets USD 5,000 (not the USD 4,827.50 deposit), and line 27b gets the USD 172.50 fee; profit is unchanged, but line 1 now matches the Form 1099-K. Line 24b gets 50% of USD 187.42 = USD 93.71.

```oa-check
name: Processor gross-up and meals limit (2026)
inputs:
  payout: 4827.50
  fees: 172.50
  meal: 187.42
steps:
  - line_1: payout + fees
  - line_27b_fees: fees
  - net_effect: line_1 - line_27b_fees - payout
  - line_24b: meal * 0.50
expected:
  line_1: 5000.00
  line_27b_fees: 172.50
  net_effect: 0
  line_24b: 93.71
```

**Case 2, a decision: standard mileage or actual costs for a car first used in 2026?** The car was driven 18,000 miles in 2026, of which 12,500 were business miles with a log: 6,000 from 1 January to 30 June and 6,500 from 1 July to 31 December. Fuel, insurance, repairs and registration cost USD 6,500, and first-year depreciation (inside the passenger car cap) would be USD 5,000.

Standard: 6,000 x 72.5 cents + 6,500 x 76 cents = USD 4,350 + USD 4,940 = USD 9,290. Actual: (USD 6,500 + USD 5,000) x 12,500 / 18,000 = USD 7,986.11. Standard mileage gives USD 1,303.89 more, and parking and tolls are added under either method. Choosing the standard rate in the first year also keeps the option to move to actual costs later; choosing actual costs with accelerated depreciation now would lock the car out of the standard rate. Recommend standard mileage.

```oa-check
name: Standard mileage against actual costs (2026)
inputs:
  miles_h1: 6000
  miles_h2: 6500
  total_miles: 18000
  running_costs: 6500
  depreciation: 5000
steps:
  - business_miles: miles_h1 + miles_h2
  - standard: miles_h1 * 0.725 + miles_h2 * 0.76
  - actual: (running_costs + depreciation) * business_miles / total_miles
  - standard_advantage: standard - actual
expected:
  business_miles: 12500
  standard: 9290.00
  actual: 7986.11
  standard_advantage: 1303.89
```

## When to refuse or refer

If one of these triggers, stop and give the message.

| Code | Trigger | Message |
| --- | --- | --- |
| R-US-PARTNERSHIP | Partners, a partnership agreement, Form 1065, K-1s, an LLC with more than one member | "This covers sole proprietors and single-member LLCs only. A partnership files Form 1065; see `us-form-1065-partnership` or a CPA or EA." |
| R-US-RENTAL | Rental income, landlord activity, Schedule E, rental properties, Airbnb hosting | "Rental income normally goes on Schedule E, which this skill does not cover. Please use a CPA or EA." |
| R-US-CRYPTO | Trading, DeFi, NFTs, mining, staking, token swaps | "Digital assets need basis tracking and Form 8949; see `us-capital-gains` or a specialist." |
| R-US-EMPLOYEES | W-2 employees, payroll, Forms 941 or 940 | "Wages (line 26) and employer taxes (line 23) are classified here, but payroll filings are not; see `us-form-941-940-payroll`." |
| R-US-SCORP | S corporation election, Form 2553 or 1120-S, officer salary | "An S corporation files Form 1120-S, not Schedule C; see `us-s-corp-election-decision` or `us-form-1120-s-s-corporation-return`." |
| R-US-CCORP | C corporation, Form 1120, dividends from the owner's corporation | "A C corporation files Form 1120; see `us-form-1120-c-corp`." |
| R-US-FARMING | Farming, crops, livestock, Schedule F | "Farm income goes on Schedule F. Please use a CPA or EA." |
| R-US-DEPLETION | Oil and gas royalties, mineral rights, timber | "Depletion under sections 611 to 613 is outside this skill." |
| R-US-FOREIGN-INCOME | Foreign accounts, FBAR, Form 8938, Form 2555 | "Foreign income and account reporting is outside this skill; see `us-fbar-and-fatca-8938`." |
| R-US-ESTATE-TRUST | Estate, trust, Form 1041 | "Fiduciary returns are outside this skill. Please use a CPA or attorney." |

## Filing and payment

The working paper feeds Schedule C, which is attached to the 2026 Form 1040 due **15 April 2027** (15 October 2027 with Form 4868; an extension does not extend payment). The 2026 Forms 1099-NEC the business must issue are due to contractors and the IRS by 1 February 2027 (31 January falls on a Sunday); see `us-1099-nec-issuance`. Hand the Schedule C summary, the asset register and the reviewer note to `us-schedule-c-and-se-computation`.

## Completion checklist

- Every transaction has a line or an exclusion reason.
- Processor deposits grossed up; line 1 at least the 1099 totals, or the gap explained.
- Bank, software and merchant fees on line 27b; line 27a used only for Form 7205.
- Interest split between 16a, 16b and 16c.
- Meals at 50% with substantiation; entertainment excluded.
- Mileage split between the two 2026 rates, with a log.
- Assets over the de minimis amount on the asset register with acquisition dates.
- Contractors paid USD 2,000 or more by non-card means flagged for a 1099-NEC.
- Owner's health insurance, retirement, income taxes and draws excluded.
- Defaults and questions listed for the client; reviewer note written.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| Schedule C (Form 1040) 2026. Read for lines 1 to 31, the new 16a, 16b (vehicle loan) and 16c split, line 27a (Form 7205) and Part V to line 48 and 27b. | https://www.irs.gov/pub/irs-pdf/f1040sc.pdf | 2026-11-13 |
| IRS Notice 2026-10. Read for the 72.5 cents business rate from 1 January 2026 (library quote). | https://www.irs.gov/pub/irs-drop/n-26-10.pdf | 2026-11-13 |
| IRS standard mileage rates page. Read for the 76 cents business rate from 1 July 2026 (library quote). | https://www.irs.gov/tax-professionals/standard-mileage-rates | 2026-11-13 |
| Rev. Proc. 2025-32. Read for the $2,000 information return threshold for payments after 31 December 2025 and the $32,000,000 gross receipts test (library quotes). | https://www.irs.gov/pub/irs-drop/rp-25-32.pdf | 2026-11-13 |
| Public Law 119-21. Read for section 70432, the Form 1099-K thresholds of more than $20,000 and more than 200 transactions (library quote). | https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm | 2026-11-13 |
| Treas. Reg. 1.263(a)-1 (eCFR). Read for (f), the de minimis safe harbor: $5,000 with an applicable financial statement, $500 in the regulation text without one. | https://www.ecfr.gov/current/title-26/section-1.263(a)-1 | 2026-11-13 |
| 26 U.S.C. 274 (govinfo). Read for (a) entertainment, (b) the $25 gift limit, (d) substantiation and (n) the 50% meals limit. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partIX-sec274.htm | 2026-11-13 |
| 26 U.S.C. 280F (govinfo). Read for (d)(5)(A), the 6,000 pound line. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partIX-sec280F.htm | 2026-11-13 |
| 26 U.S.C. 6050W (govinfo). Read for payment settlement entities and card transactions reported on Form 1099-K. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap61-subchapA-partIII-subpartB-sec6050W.htm | 2026-11-13 |
| 26 U.S.C. 162, 183 and 262 (govinfo). Read for ordinary and necessary expenses, (e) lobbying, (f) fines, the hobby presumption and personal expenses. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partVI-sec162.htm | 2026-11-13 |
| IRS Notice 2015-82. Read for the increase of the no-AFS de minimis amount from $500 to $2,500. | https://www.irs.gov/pub/irs-drop/n-15-82.pdf | 2026-11-13 |
| IRS Publication 463 (for 2025 returns, the latest on the site). Read for travel, gifts and car expenses, including foreign trip allocation and the log. | https://www.irs.gov/pub/irs-pdf/p463.pdf | 2026-11-13 |

Not yet confirmed: the 2026 Instructions for Schedule C were not published when read, so line contents come from the 2026 form itself; Publication 463 read is the latest edition on the site, not a 2026 edition; the 1 February 2027 Form 1099-NEC date is the 31 January rule moved for the weekend and should be checked against the 2026 Form 1099-NEC instructions.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-13. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `us-sole-prop-bookkeeping` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/us-sole-prop-bookkeeping. If neither is available, confirm every figure against the official source pages cited above before relying on it.
