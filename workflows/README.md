# OpenAccountants — Guided Tax Workflows

These workflows define structured 6-phase tax advisor experiences. Each file specifies the trigger phrases, the skills to load, the phases to run, and the expected output.

When a user's situation matches a trigger, fetch the relevant jurisdiction bundle (or use the MCP server) and follow the workflow rather than answering from training data.

| Workflow | File | Trigger |
|---|---|---|
| Cross-border / multi-jurisdiction | [cross-border-intake.md](cross-border-intake.md) | Any two-country situation, relocation, exit |
| Australia sole trader | [australia-sole-trader.md](australia-sole-trader.md) | AU freelancer / ABN / sole trader |
| UK self-employed | [uk-self-employed.md](uk-self-employed.md) | UK freelancer / sole trader |
| US self-employed (Schedule C) | [us-schedule-c.md](us-schedule-c.md) | US 1099 / gig worker / sole prop |
| South Africa income tax | [south-africa-income-tax.md](south-africa-income-tax.md) | SA taxpayer, SARS, ITR12 |
| Malta freelancer | [malta-freelancer.md](malta-freelancer.md) | Malta self-employed / part-time |
| Portugal self-employed | [portugal-self-employed.md](portugal-self-employed.md) | Portugal NHR/IFICI / recibos verdes |
| UK capital gains | [uk-capital-gains.md](uk-capital-gains.md) | UK shares, crypto, or property sale |

## How to use via MCP

Each workflow has a corresponding MCP prompt on the live server. Install the MCP connector at [openaccountants.com/connect](https://www.openaccountants.com/connect), then invoke the named prompt with the user's situation as the `situation` argument.

## How to use without MCP

1. Fetch the jurisdiction bundle: `GET https://www.openaccountants.com/api/bundle/<CODE>`
2. Load the bundle as context
3. Follow the 6 phases in the workflow file, applying the skills to the user's numbers
4. End with a professional review handoff
