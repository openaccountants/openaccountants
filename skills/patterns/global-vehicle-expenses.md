---
name: global-vehicle-expenses
description: >
  Vehicle expense deduction rules across the top 10 jurisdictions for freelancers and
  self-employed individuals. Covers per-kilometre/mileage rates, actual cost methods,
  logbook requirements, business-use caps, and common mistakes.
version: 0.1
category: patterns
depends_on: []
---

# Global Vehicle Expense Pattern Library v0.1

## What this file is

**Functional role:** Vehicle expense deduction rules and calculation methods by jurisdiction
**Status:** Active reference data

Vehicle expenses are a high-audit-risk category because the line between business and personal use is inherently blurred. Every jurisdiction requires some method of distinguishing business trips from personal trips. This file provides the rules, rates, and logbook requirements for the top 10 jurisdictions.

---

## The fundamental rule

> **Commuting is NOT a business trip.**
>
> Travel from home to your regular place of work is commuting. It is personal, and it is NOT deductible in ANY jurisdiction (though Germany has a partial commute allowance, the Entfernungspauschale, which is technically a reduction in taxable income rather than a business expense).
>
> Business trips include: travel to client sites, travel to meetings, travel to temporary workplaces, travel between business locations, travel to the bank/post office for business errands.

---

## Vehicle expense rules by jurisdiction

### United States

| Method | Rate/Formula | Log required? | Business use cap | Citation |
|---|---|---|---|---|
| **Standard mileage rate** | **70 cents per mile** (2025, IRS announced rate — verify annually) | Yes. Must maintain a contemporaneous mileage log: date, destination, business purpose, miles driven. | No personal miles can be claimed. Must have records to substantiate business vs. personal split. | IRS Rev. Proc. (annual); IRC Section 274(d) |
| **Actual expense method** | Total actual vehicle costs (gas, oil, tires, repairs, insurance, registration, depreciation/lease payments) multiplied by (business miles / total miles). | Yes. Same log requirement. Also need all receipts for actual expenses. | Depreciation limits (luxury auto caps): Section 280F. Year 1: $12,400 (2025, verify). Bonus depreciation may increase first-year limit. | IRC Section 162; Section 280F |

**Key notes — US:**
- You must choose one method for the tax year. Once you use actual expenses for a vehicle, you CANNOT switch to standard mileage rate for that vehicle in future years (with limited exceptions).
- You CAN switch from standard mileage to actual in a later year, but depreciation will be computed using the standard mileage depreciation component.
- If you use the standard mileage rate, you CANNOT also deduct gas, repairs, insurance, etc. separately. Parking and tolls ARE deductible on top of the standard rate.
- The log must be "contemporaneous" — the IRS does not accept logs reconstructed at year-end. Write it down at the time of each trip.
- Vehicles used less than 50% for business cannot use MACRS accelerated depreciation (must use straight-line).

---

### United Kingdom

| Method | Rate/Formula | Log required? | Business use cap | Citation |
|---|---|---|---|---|
| **Simplified mileage rate** | First 10,000 business miles: **45p per mile**. Above 10,000 miles: **25p per mile**. | Yes. Must maintain a mileage log with date, destination, purpose, and miles. | Only business miles claimed. Personal miles excluded. | ITTOIA 2005 s94B; HMRC Simplified Expenses |
| **Actual cost method** | Total actual costs (fuel, insurance, servicing, repairs, road tax, MOT, depreciation/capital allowances) multiplied by business-use percentage. | Yes. Need a mileage log to determine business-use percentage AND receipts for all costs. | Must apportion between business and personal. | ITTOIA 2005 s34; CAA 2001 for capital allowances |

**Key notes — UK:**
- The simplified mileage rates are generous for the first 10,000 miles but drop significantly after that. For expensive cars with high running costs, actual may be better after 10,000 miles.
- Once you use actual costs for a particular vehicle, you CANNOT switch to simplified mileage for that vehicle. You CAN switch from simplified to actual (but not back).
- Capital allowances (not depreciation — UK uses capital allowances): Annual Investment Allowance (AIA) on the business-use proportion. Electric vehicles: 100% first-year allowance.
- VAT: fuel VAT can be reclaimed on the business proportion. Alternatively, use the HMRC fuel scale charge.
- Motorcycles: 24p per mile (flat rate, no tiering).
- Bicycles: 20p per mile.

---

### Germany

| Method | Rate/Formula | Log required? | Business use cap | Citation |
|---|---|---|---|---|
| **Entfernungspauschale (commute allowance)** | **30 cents per km** for one-way distance (first 20 km). **38 cents per km** from km 21 onward. Only for commute to primary workplace. | No log required for commute — only the distance. | Only counts actual working days. Maximum one trip per working day. | EStG Section 9 Abs. 1 Satz 3 Nr. 4 |
| **Fahrtenbuch (logbook) for business trips** | Actual total vehicle costs (fuel, insurance, tax, depreciation, repairs, garage) multiplied by (business km / total km). | Yes. **Extremely strict logbook** (Fahrtenbuch): each trip must record date, departure/arrival location, route, purpose, km reading at start and end. Must be bound or electronic (BMF-approved format). | Only the business-trip proportion. Commute is separately handled by Entfernungspauschale. | EStG Section 4 Abs. 5 Nr. 6 |
| **1% rule (company car / Privatnutzung)** | If using the car for both business and personal: add 1% of the car's gross list price per month as taxable benefit. Plus 0.03% x list price x km for commute. | No logbook required. | Simplification: you avoid the logbook but accept a deemed private-use addition. | EStG Section 6 Abs. 1 Nr. 4 Satz 2 |

**Key notes — Germany:**
- The Entfernungspauschale is unique: it is a commute allowance, not a business-trip deduction. Most countries disallow commute deductions entirely.
- Important: the Entfernungspauschale is for one-way distance only (not round trip), but you claim it for each working day.
- The Fahrtenbuch requirements are among the strictest in the world. Missing entries, gaps, or inconsistencies can cause the entire logbook to be rejected, resulting in the 1% rule being applied instead.
- The 1% rule often results in a HIGHER taxable amount than the Fahrtenbuch for expensive cars with low private use. Run both calculations.
- For self-employed: if business use is less than 10%, the vehicle is "private" and you can only deduct individual business trips at 30c/km (same as Entfernungspauschale rate). If 10-50%: you choose between Fahrtenbuch and 30c/km. If >50%: the vehicle is "business" and either Fahrtenbuch or 1% rule applies.
- Electric vehicles: 1% rule uses only 25% of list price (for list prices up to EUR 70,000), making it very favorable.

---

### Australia

| Method | Rate/Formula | Log required? | Business use cap | Citation |
|---|---|---|---|---|
| **Cents per km method** | **88 cents per km** (2024-25 income year — verify annually) | No detailed log required. Must be able to show how you calculated business km (reasonable estimate accepted). | Maximum **5,000 business km** per vehicle per year = **AUD 4,400 max deduction**. | ITAA 1997 s28-25; ATO rates |
| **Logbook method** | Actual total vehicle costs multiplied by business-use percentage (determined by a 12-week representative logbook sample). | Yes. Must keep a **12-week logbook** (continuous period). The logbook is valid for 5 years unless circumstances change materially. Must keep all receipts. | No km cap. Business-use percentage from the logbook applies to total costs including depreciation. | ITAA 1997 Div 28; ATO logbook rules |

**Key notes — Australia:**
- The cents-per-km method is capped at 5,000 km. If you drive more than 5,000 business km, you MUST use the logbook method to claim beyond the cap.
- The logbook only needs to be kept for 12 continuous weeks, but it must be representative of your usual travel pattern. Do not keep it during an atypical period (e.g., a holiday month with no business driving).
- Once you have a valid logbook, you apply the business-use percentage for up to 5 years. You must keep a new logbook if your driving pattern changes significantly (e.g., you get a new client across town).
- The ATO is known for data-matching vehicle claims against other records. Overclaiming is a top audit target.
- Depreciation: effective life of a car is 8 years. Instant asset write-off for assets under the threshold (check current small business threshold).
- Fuel tax credits: NOT available for private vehicles — only for heavy vehicles, machinery, and certain business vehicles off-road.

---

### Canada

| Method | Rate/Formula | Log required? | Business use cap | Citation |
|---|---|---|---|---|
| **Per-km rate (CRA prescribed)** | First 5,000 business km: **70 cents per km**. Each additional km: **64 cents per km**. (2025 rates — verify annually. Yukon/NWT/Nunavut: add 4c/km.) | Yes. Must maintain a logbook: date, destination, purpose, km driven. | Only business km. Must separate business and personal use with a log. | CRA Motor Vehicle Expenses guide (T4002); Income Tax Regulations s7306 |
| **Actual cost method** | Total actual costs (fuel, insurance, maintenance, licence, interest on car loan, CCA/depreciation) multiplied by (business km / total km). | Yes. Same logbook. Also keep all receipts. | CCA (capital cost allowance) limits: Class 10 vehicle max cost is **CAD 37,000** (2025 — verify). Passenger vehicle interest deduction capped at **CAD 300/month**. Lease costs capped at **CAD 1,050/month**. | CRA T4002; ITR s7307; Class 10/10.1 |

**Key notes — Canada:**
- The per-km rate is ONLY for calculating the deductible amount. You still need a logbook.
- The CCA (depreciation) limits are designed to prevent deductions on luxury vehicles. If your car costs more than CAD 37,000, the excess cost is not depreciable.
- If business use is less than 50%, you may face additional restrictions on CCA recapture.
- GST/HST: if registered, you can claim input tax credits (ITCs) on the business portion of vehicle expenses. But if the vehicle is used less than 90% for business, ITCs are limited.
- The CRA audits vehicle claims frequently. A detailed contemporaneous logbook is essential.

---

### Spain

| Method | Rate/Formula | Log required? | Business use cap | Citation |
|---|---|---|---|---|
| **IRPF (income tax)** | Vehicle costs are generally **NOT deductible** for autonomos unless you are in a profession where a vehicle is essential (commercial agents, transport, delivery, taxi, sales representatives). | N/A for most. If eligible: yes, logbook needed. | For most autonomos: **0% deductible** for IRPF. | LIRPF art. 22; Reglamento IRPF art. 21 |
| **IVA (VAT)** | **50% of IVA** on vehicle purchase and expenses is deductible (presumed 50% business use). Can claim 100% if you prove 100% business use (very difficult). | Must keep purchase invoices. | 50% IVA deduction cap unless full business use proven. | LIVA art. 95.Tres.2 |

**Key notes — Spain:**
- Spain is uniquely restrictive on vehicle expenses. For income tax (IRPF), most self-employed individuals (autonomos) CANNOT deduct vehicle costs at all. The Tribunal Supremo has consistently held that a vehicle used for mixed purposes is not "exclusively" related to the activity.
- The exception: certain professions where a vehicle is integral (agentes comerciales, taxistas, transportistas, repartidores). Even then, the burden of proof is on the taxpayer.
- For IVA: the law presumes 50% business use, so you can deduct 50% of the IVA on fuel, repairs, insurance, and the vehicle purchase. This is automatic — no logbook needed.
- In practice, many Spanish autonomos simply do not claim vehicle expenses for IRPF and claim the 50% IVA.

---

### Italy

| Method | Rate/Formula | Log required? | Business use cap | Citation |
|---|---|---|---|---|
| **Statutory percentage** | Vehicle expenses are deductible at **20% of actual costs** for self-employed professionals. Fuel, insurance, repairs, depreciation — all at 20%. | Keep all receipts and invoices. No formal logbook, but recommended. | Depreciation base capped at **EUR 18,075.99** for cars. Fuel deductible at 20%. | TUIR art. 164 (DPR 917/1986) |
| **Agenti di commercio (commercial agents)** | **80% of actual costs** deductible. | Same record-keeping. | Depreciation base capped at **EUR 25,822.84**. | TUIR art. 164.1.b |

**Key notes — Italy:**
- The 20% cap is regardless of actual business use. Even if you use the car 90% for business, you can only deduct 20% of costs (unless you are an agente di commercio).
- IVA (VAT): 40% of IVA on vehicle costs is deductible (for non-agents). 100% for agents and certain transport activities.
- The depreciation cap (EUR 18,075.99) means that if your car cost EUR 50,000, you depreciate as if it cost EUR 18,075.99, and then you apply the 20% rule to that depreciation amount.
- Tolls (pedaggi) and parking: 20% deductible (same rule).
- Electronic invoicing (fatturazione elettronica) required for all vehicle-related expenses.

---

### Netherlands

| Method | Rate/Formula | Log required? | Business use cap | Citation |
|---|---|---|---|---|
| **Actual costs only** | Total actual costs (fuel, insurance, road tax, depreciation, maintenance, financing costs) minus private-use adjustment. | Yes. Must maintain a logbook (rittenadministratie) if claiming more than incidental business use. | If private use > 500 km/year: must add back a deemed private-use amount (bijtelling) — 22% of catalogue value per year for most cars, 16% for zero-emission. | Wet IB 2001; Belastingdienst km-administratie |
| **No per-km allowance** | The Netherlands does NOT offer a per-km deduction rate for self-employed. | N/A. | N/A. | |

**Key notes — Netherlands:**
- The Netherlands has no simplified per-km rate for zelfstandigen (self-employed). You must use actual costs.
- If the vehicle is on your business balance sheet (ondernemingsvermogen): deduct all costs, but add back a bijtelling (deemed private use) if private use exceeds 500 km/year.
- The bijtelling for 2025 is 22% of the car's catalogue value (new price including BPM and VAT) per year. For zero-emission (electric): 16% up to EUR 30,000 of value, 22% above that.
- If the vehicle is NOT on your business balance sheet (privebelangvermogen): you can claim EUR 0.23/km for business trips (this is the employee reimbursement rate, sometimes used by IB-ondernemers). But this requires a logbook.
- The logbook must be very detailed: each trip with date, departure, destination, route, purpose, and odometer readings. The Belastingdienst frequently audits logbooks and rejects them for inconsistencies.

---

### India

| Method | Rate/Formula | Log required? | Business use cap | Citation |
|---|---|---|---|---|
| **Actual costs only** | Actual fuel, maintenance, insurance, depreciation costs attributable to business use. | Must keep receipts and demonstrate business nexus. No formal logbook format prescribed. | Must show business nexus. Presumptive scheme (44ADA) does not allow separate vehicle claims. | IT Act 1961, Section 37(1); Section 44ADA |
| **Depreciation** | Cars: 15% WDV (written-down value) per year. Commercial vehicles: 30% WDV. | Keep asset register. | Depreciation applies only to the business-use portion. | IT Act 1961, Section 32; CBDT depreciation table |

**Key notes — India:**
- Under the presumptive scheme (Section 44ADA, for professionals with receipts up to INR 75 lakh), 50% of gross receipts is deemed profit and you cannot separately claim vehicle expenses.
- Under non-presumptive (ITR-3): actual expenses are deductible, but you must maintain books of account and demonstrate the business connection.
- No per-km allowance exists for self-employed. Employees receive exemptions for car perquisites, but that does not apply to freelancers.
- GST input credit on car purchase: generally NOT available for passenger vehicles (blocked credit under Section 17(5) of the CGST Act), except for specific businesses (driving schools, transport services, dealers).
- Fuel: GST input credit on petrol/diesel is blocked.

---

### Malta

| Method | Rate/Formula | Log required? | Business use cap | Citation |
|---|---|---|---|---|
| **Proportional to business use** | Actual fuel, insurance, licence fees, repairs, depreciation — proportioned by business-use percentage. | Must keep fuel receipts and a business-use log or estimate. | Must be proportional. No formal cap, but IRD reviews reasonableness. | ITA Cap. 123; IRD practice |
| **Capital allowances** | Wear and tear allowance: typically 20% per year on cost (5-year write-off for motor vehicles). | Keep purchase documentation. | Applied to total cost, then proportioned by business-use percentage. | ITA Cap. 123; subsidiary legislation |

**Key notes — Malta:**
- Malta has no simplified per-km mileage rate. You must use actual costs proportioned by business use.
- Fuel receipts are essential. The IRD will request them on audit.
- A reasonable estimate of business-use percentage (e.g., 60% business, 40% personal) is accepted if supportable, but a trip log strengthens the claim significantly.
- VAT: 18% VAT on vehicle purchase is NOT reclaimable for passenger cars (blocked). VAT on fuel, repairs, and maintenance: reclaimable on the business-use proportion.
- Registration tax and annual licence fees: proportioned like other vehicle costs.
- Company cars: a fringe benefit value is added to the employee/director's income.

---

## Summary comparison table

| Jurisdiction | Per-km/mile rate available? | Rate | Cap on simplified | Logbook required? | Key restriction |
|---|---|---|---|---|---|
| **US** | Yes | 70c/mile | No mile cap (but actual expenses may be better) | Yes (strict) | Must choose method; luxury auto depreciation caps |
| **UK** | Yes | 45p/25p per mile | No cap | Yes | Cannot switch back from actual to simplified |
| **Germany** | Only for commute (30c/38c per km) | 30c/km commute; Fahrtenbuch for business trips | Commute only; business trips = actual | Yes (extremely strict Fahrtenbuch) | Fahrtenbuch can be rejected entirely for errors |
| **Australia** | Yes | 88c/km | 5,000 km/year | 12-week sample logbook (for logbook method) | Cents-per-km capped at 5,000 km |
| **Canada** | Yes | 70c/64c per km | No km cap | Yes | Depreciation/lease caps on expensive vehicles |
| **Spain** | No | N/A | N/A | N/A | Vehicle generally NOT deductible for IRPF |
| **Italy** | No | N/A | N/A | Receipts (no logbook) | Statutory 20% cap regardless of actual use |
| **Netherlands** | No (EUR 0.23/km for employees only) | N/A | N/A | Yes (strict) | No per-km for self-employed; bijtelling for private use |
| **India** | No | N/A | N/A | Keep receipts | Presumptive scheme (44ADA) covers all expenses |
| **Malta** | No | N/A | N/A | Fuel receipts required | Must demonstrate business nexus |

---

## Common mistakes

1. **Claiming commute as business travel.** Home to regular workplace is commuting in every jurisdiction (Germany's Entfernungspauschale is a partial income reduction, not a business expense deduction). Travel from your office to a client IS business travel.

2. **No logbook at all.** The US, UK, Canada, Germany, Netherlands, and Australia all require some form of log. Claiming vehicle expenses without a log is the fastest way to lose the deduction on audit. Write it down at the time — do not reconstruct at year-end.

3. **Claiming 100% business use.** Unless the vehicle is truly never used personally (very rare for a freelancer), claiming 100% business use is a red flag. A credible business-use percentage for most freelancers is 40-70%.

4. **Ignoring the Spain/Italy restrictions.** Many freelancers in Spain and Italy assume vehicle costs are fully deductible (like in the US or UK). They are not. Spain generally disallows IRPF deduction for most autonomos. Italy caps at 20% for professionals.

5. **Using the wrong rate year.** Per-km/mile rates change annually. Always verify the rate for the specific tax year you are filing. Using a prior year's rate is an error.

6. **Double-counting parking and tolls.** In the US, parking and tolls are deductible ON TOP of the standard mileage rate. In other jurisdictions, they may be included in the actual-cost calculation. Do not claim them twice.

7. **Forgetting the electric vehicle advantages.** Many jurisdictions offer more favorable treatment for electric vehicles: Germany's 25% list price for 1% rule, Australia's FBT exemption, UK's 100% first-year allowance, Netherlands' lower bijtelling rate. Check if EV-specific rules apply.

---

## Disclaimer

This file provides general guidance for vehicle expense deductions. Rates, caps, and logbook requirements change annually. Always verify against the relevant tax authority's current publications and rate announcements. This is not tax advice. A qualified professional should review all vehicle expense claims before filing.
