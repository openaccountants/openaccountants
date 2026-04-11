# Skill Promotion Playbook — Q3 → Q2 → Q1

How to systematically turn 178 AI-drafted skills into battle-tested production skills.

---

## The bottleneck is not writing. It's verification.

We have 346 skill files. The writing is done. The problem is:

- **Q3 → Q2 requires a human practitioner** in each jurisdiction to read and confirm
- **Q2 → Q1 requires real transaction data** in each jurisdiction to test against

Both of these are scarce resources. The playbook is about how to acquire them efficiently.

---

## Part 1 — Promoting Q3 → Q2 (Practitioner Verification)

### What the practitioner actually does

They receive a skill file and answer one question per section: **"Is this correct for tax year 2025?"**

| Section | What they check | Time estimate |
|---------|----------------|---------------|
| Rates and thresholds | Are these numbers current? | 5 min |
| Form structure / box mapping | Are the form lines correct? | 10 min |
| Filing requirements | Correct deadlines, frequencies, thresholds? | 5 min |
| Computation rules | Does the step-by-step logic produce the right answer? | 15 min |
| Edge cases | Are these correctly resolved? Anything missing? | 10 min |
| Refusal catalogue | Anything dangerous that's missing? | 5 min |
| **Total per skill** | | **~50 min** |

This is a **reading job**, not a writing job. The skill is already written. They just confirm or correct.

### How to find practitioners

#### Channel 1: openaccountants.com contributor programme

- Practitioners sign up, pick their jurisdiction
- They get assigned skills to verify
- In return: public profile, "verified by" credit, visibility to potential clients
- **Target: 5 practitioners in Month 1, 20 by Month 3**

#### Channel 2: Accounting firm partnerships

Approach firms with this pitch:
- "We've written the tax computation logic for [your jurisdiction]. We need a practitioner to confirm it's correct. Takes ~1 hour per skill. Your firm gets credited as the verifier on a public open-source tool used by thousands of freelancers."
- Start with firms in jurisdictions where you already have contacts (Malta, Germany, US, UK)
- **Target: 3 firm partnerships by Month 2**

#### Channel 3: University/academic partnerships

Tax law professors and graduate students can verify skills as part of coursework or research:
- "Compare this AI-drafted tax computation skill against the current statute and official guidance. Document any errors."
- Academic credit potential, publication opportunity
- **Target: 2 university partnerships by Month 3**

#### Channel 4: Paid verification bounties

For high-priority jurisdictions where organic recruitment is slow:
- Pay a licensed practitioner a flat fee per skill verified (e.g., $100–$200 per skill)
- Recruit via Upwork, LinkedIn, or local accounting associations
- **Budget: ~$5,000 covers 25–50 skill verifications**

### Verification workflow

```
1. Practitioner claims a skill on openaccountants.com
2. They receive the skill file + a verification checklist
3. They review each section, marking:
   ✓ Correct as written
   ✗ Error found — with correction and source citation
   ? Uncertain — needs further research
4. They submit their review
5. Errors are corrected in the skill
6. Skill metadata updated: Validated By, Validation Date, credential
7. Skill promoted to Q2
```

### Priority order for Q3 → Q2 verification

Verify the skills that matter most first:

| Priority | Jurisdictions | Why | Skills to verify |
|----------|--------------|-----|-----------------|
| **P1** | UK, Canada, Australia | Largest English-speaking freelancer markets after US | ~15 VAT/GST skills |
| **P2** | Ireland, Singapore, New Zealand | English-speaking, growing freelancer base | ~5 skills |
| **P3** | Spain, Netherlands, Portugal | Large digital nomad / freelancer populations | ~5 skills |
| **P4** | India, Brazil, Mexico | Huge freelancer populations, high demand | ~8 skills |
| **P5** | All remaining EU | EU VAT directive layer already verified, so country skills are faster | ~20 skills |
| **P6** | Rest of world | Long tail — verify as practitioners volunteer | ~125 skills |

### Acceleration tactic: EU VAT skills verify faster

For EU member states, the EU VAT Directive layer is already at Q2. Country-specific VAT skills only need verification of:
- National rates (already in EU TEDB — can be cross-checked mechanically)
- Country-specific box mappings (form structure)
- Country-specific reverse charge rules
- National filing deadlines and thresholds

This means an EU VAT skill verification is ~30 min instead of ~50 min. A single practitioner familiar with EU VAT could verify 3–4 country skills per day.

---

## Part 2 — Promoting Q2 → Q1 (Real-Data Testing)

### What "battle-tested" actually means

A skill is Q1 when it has processed real transactions and produced output that a practitioner would sign. Specifically:

1. **Real bank statement data** (anonymised) was fed to the skill
2. **Every transaction was classified** using the skill's rules
3. **The output was compared** to either:
   - A return prepared manually by a practitioner, OR
   - A return prepared by traditional tax software (Xero Tax, DATEV, etc.)
4. **Discrepancies were investigated** and the skill was corrected
5. **A practitioner reviewed the final output** and confirmed they would sign it

### How to get real data

#### Source 1: Your own practice (Accora clients)

- Malta, US, and any jurisdiction where you already prepare returns
- Use existing client data (with consent) to test skills
- This is how Malta and US federal skills reached Q1
- **Fastest path for jurisdictions you already serve**

#### Source 2: Practitioner partners provide anonymised data

- When a practitioner verifies a skill (Q3→Q2), ask: "Would you be willing to test it against one anonymised client file?"
- Many will say yes — they're already invested in the skill being correct
- Offer to process the data and send them the output for review
- **Builds on the Q2 verification relationship**

#### Source 3: Synthetic test data (partial credit)

For jurisdictions where real data is hard to get:
- Build realistic synthetic transaction sets that cover the main patterns
- Run the skill against them and verify output manually
- This doesn't count as full Q1, but it catches most logic errors
- Mark as **Q1.5** or "tested against synthetic data"

#### Source 4: Open beta with real users

- Launch skills as "unverified" on openaccountants.com
- Users run them against their own data
- Users report errors via the platform
- Each confirmed fix moves the skill closer to Q1
- **Scales verification with usage**

### The Q2 → Q1 testing workflow

```
1. Obtain anonymised transaction data (bank statement CSV, receipt list)
2. Load the skill + workflow base
3. Run classification on every transaction
4. Produce the return / working paper
5. Send to the practitioner who verified (Q2) the skill
6. They compare to what they would have filed
7. Discrepancies logged:
   - CLASSIFICATION ERROR: transaction assigned to wrong line/box
   - RATE ERROR: wrong rate applied
   - THRESHOLD ERROR: threshold check failed
   - EDGE CASE MISS: real-world scenario not covered
   - FORM MAPPING ERROR: amount placed on wrong form line
8. Skill corrected for each discrepancy
9. Re-run with corrections
10. Practitioner confirms: "I would sign this return"
11. Skill promoted to Q1
```

### Priority order for Q2 → Q1 testing

| Priority | Jurisdictions | Data source | Path to Q1 |
|----------|--------------|-------------|------------|
| **P1** | Malta | Accora clients | Already Q1 for IT/SSC/VAT |
| **P1** | US Federal | Accora clients | Already Q1 for bookkeeping/SE |
| **P2** | Germany | Accora or partner | VAT at Q1, need income tax data |
| **P2** | UK | Partner practitioner | High demand, English-speaking |
| **P3** | France, Italy | Partner practitioners | VAT skills at Q2, need real data |
| **P3** | NY, CA | Accora clients (if serving) | State skills at Q2 |
| **P4** | Canada, Australia | Partner practitioners | GST skills at Q3, need verification + data |
| **P5** | All others | Open beta / partners | As practitioners and data become available |

---

## Part 3 — The promotion pipeline (putting it together)

### Month 1–2: Foundation

| Action | Target | Owner |
|--------|--------|-------|
| Launch contributor programme on openaccountants.com | Sign up 5 practitioners | Accora team |
| Verify UK VAT, Canada GST/HST, Australia GST | 3 skills to Q2 | Recruited practitioners |
| Test Germany VAT against 2 more client files | Confirm Q1 | Michael / German partner |
| Build the verification checklist tool on the platform | Practitioners can verify online | Dev team |

### Month 3–4: Scale verification

| Action | Target | Owner |
|--------|--------|-------|
| Verify all P1+P2 consumption tax skills | 20 skills to Q2 | Practitioner network |
| First Q2 → Q1 test for UK and Canada | 2 new Q1 jurisdictions | Partner practitioners |
| Approach 3 accounting firms for partnership | Pipeline for P3–P5 | Accora BD |
| Launch open beta — users test Q3 skills | Error reports flowing in | Platform |

### Month 5–6: Momentum

| Action | Target | Owner |
|--------|--------|-------|
| Verify P3+P4 consumption tax skills | 30 more skills to Q2 | Growing practitioner network |
| Q1 testing for France, Italy, Spain, Netherlands | 4–6 new Q1 jurisdictions | Partners |
| Begin income tax skill verification (start with UK, Canada) | First non-VAT skills to Q2 | Practitioners |
| Paid bounties for hard-to-fill jurisdictions | 10–15 more verifications | Budget |

### By end of Month 6

| Tier | Target count |
|------|-------------|
| Q1 — Battle-tested | 15–20 skills across 8–10 jurisdictions |
| Q2 — Verified | 50–60 skills |
| Q3 — AI-drafted | ~170 skills (decreasing as they promote) |
| Q4 — Stubs | ~60 (being filled by agents + contributors) |

---

## Part 4 — What the user sees

When a skill is loaded on openaccountants.com, the quality tier is visible:

```
┌─────────────────────────────────────────────┐
│  Germany VAT Return (UStVA) v0.1            │
│  ████████████ BATTLE-TESTED                 │
│                                             │
│  Verified by: [Practitioner name], StB      │
│  Tested against: Real client data (3 files) │
│  Last updated: March 2026                   │
│  Tax year: 2025                             │
└─────────────────────────────────────────────┘

┌─────────────────────────────────────────────┐
│  Australia GST (BAS) v0.1                   │
│  ░░░░░░░░░░░░ AI-DRAFTED                    │
│                                             │
│  Verified by: Pending                       │
│  Tested against: Not yet                    │
│  Last updated: April 2026                   │
│  Tax year: 2025                             │
│                                             │
│  ⚠ This skill has not been verified by a    │
│  licensed practitioner. Use with caution.    │
│  Want to verify? openaccountants.com/verify │
└─────────────────────────────────────────────┘
```

---

## Part 5 — The economics

### Cost to verify one skill

| Method | Cost per skill | Time to verify |
|--------|---------------|----------------|
| Volunteer practitioner (contributor programme) | $0 | 1–4 weeks (depends on volunteer availability) |
| University partnership | $0 | 2–8 weeks (academic timelines) |
| Firm partnership | $0 (barter: credit for verification) | 1–2 weeks |
| Paid bounty | $100–$200 | 3–7 days |

### Cost to battle-test one skill

| Method | Cost per skill | Time to test |
|--------|---------------|--------------|
| Own client data (Accora) | $0 | 1–2 days |
| Partner provides data + reviews output | $0–$100 | 3–7 days |
| Paid practitioner test | $200–$500 | 5–10 days |

### Budget scenario: 50 skills verified + 15 battle-tested in 6 months

| Line item | Cost |
|-----------|------|
| 30 volunteer verifications | $0 |
| 20 paid bounty verifications | $3,000 |
| 10 battle-tests via partners | $0–$1,000 |
| 5 paid battle-tests | $1,500 |
| **Total** | **$4,500–$5,500** |

This is remarkably cheap for a global tax computation platform.
