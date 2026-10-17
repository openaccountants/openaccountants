# Contribute a skill with your AI

**How to use:** copy everything below the line into Claude, ChatGPT or Cursor, replace `{COUNTRY}`, `{JOB}` and `{YOUR NAME}`, and let it work. It needs access to GitHub (the Claude or ChatGPT GitHub connector, or Cursor with `gh` signed in). Read what it wrote before you open the pull request: you are the accountant, it is the typist.

---

You are helping me, {YOUR NAME}, a verified accountant on openaccountants.com, contribute one AI skill (tax rules an AI follows) to the open-source repository github.com/openaccountants/openaccountants. Do these steps in order and show me the file before opening the pull request.

1. Fork `openaccountants/openaccountants` to my GitHub account and create a branch named `skill/{COUNTRY}-{JOB}` (lowercase, hyphens).

2. Read `docs/skill-template.md` and `docs/REPO-LAYOUT.md` in the repository. They are the spec. Follow the frontmatter keys, the category vocabulary and the body section order exactly.

3. Write ONE new skill file for: country {COUNTRY}, job {JOB}. Put it in the right folder: `skills/international/<country-slug>/` for a country, `skills/us-states/<code>/` for a US state, `skills/federal/` for US federal. Look at the existing files in that folder first, match their naming, and do not duplicate a skill that already exists (if one exists, stop and tell me).

4. Required frontmatter: `name`, `description` (80 to 100 words), `jurisdiction` (ISO code, quoted if it is `"NO"`), `category`, `tax_year` as a bare integer, `tier: 2`, `last_updated` set to today's date in `YYYY-MM-DD`. Do not add platform-written keys (`review_status`, `license`, `authored_by`, `trust_label`).

5. Body rules:
   - Every rate, threshold, amount and deadline cites an official source (the tax authority or the legislation) with its link. Fetch the official page and copy the figure from it. If you cannot find an official source for a figure, leave it out and tell me.
   - One sentence near the top saying which tax year or period the figures apply to.
   - A worked example with real numbers that an AI can follow step by step.
   - A self-checks section (what the AI should verify before giving an answer).
   - A disclaimer at the end that this is general reference, not advice.
   - No inline [T1]/[T2]/[T3] tags.

6. Do not edit anything under `packages/`, `agent-skills/`, `plugins/`, or the files `index.json` and `llms-full.txt`. They are generated. Edit only your one file under `skills/`.

7. Show me the full file and wait for my OK.

8. After my OK, commit with the message `Add {COUNTRY} {JOB} skill` and open a pull request against `main` of `openaccountants/openaccountants`. Use the repository's pull request template: one sentence on what the skill covers, the country, my name as the name for attribution, and tick the CLA checkbox and the checklist boxes that are true. Leave boxes you cannot confirm unticked and tell me which.

9. Tell me the pull request link. The `contributor-status` check will look up my GitHub login on openaccountants.com and label the pull request; a maintainer reviews and merges.
