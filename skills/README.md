# Skills

**Looking for a country? Start here: each country has its own folder.**

| Folder | What is in it |
|---|---|
| [`<country>/`](./) | One folder per country. Each has a README naming the skill for each tax |
| [us/federal/](us/federal/) | United States federal skills |
| [us/states/](us/states/) | United States, one folder per state |
| [eu/](eu/) | European Union rules that every member state shares |
| [global/](global/) | Skills that belong to no one place: cross-border rules, methods, accounting standards, industries, software |
| [research/](../evidence/research/) | Evidence behind country reviews. Not skills |

## How the folders work

Every skill lives under a place. Look for it in this order.

1. **A country.** If a skill is about one country, it is in that country's folder, for example `malta/` or `germany/`. That includes the country's intake and return-assembly files. The United States is split into `us/federal/` and `us/states/<state>/`, and Canada's provinces sit inside `canada/`.
2. **A region.** Rules that the whole European Union shares are in `eu/`.
3. **Global.** Everything that is not about one country or region is in `global/`:

| Folder | What is in it |
|---|---|
| [global/cross-border/](global/cross-border/) | Rules that span two or more countries, with treaty tables in `treaty-corridors/` |
| [global/methods/](global/methods/) | How the work is done: the workflow base for each kind of task, and the router that picks the skills to load |
| [global/audit/](global/audit/) | How a statutory audit is run |
| [global/financial-reporting/](global/financial-reporting/) | Accounting standards, with `ifrs/` and `us-gaap/` |
| [global/industries/](global/industries/) | Industry-specific skills, such as construction, banking or content creators |
| [global/integrations/](global/integrations/) | How to read exports from software and payment platforms, such as Xero or Stripe |
| [global/expense-patterns/](global/expense-patterns/) | How common vendors on a bank statement are usually classified |
| [global/planning-tools/](global/planning-tools/) | Deadlines, thresholds and planning checks that work across countries |

**Folder = place, label = domain + job.** The folder says where a skill applies. Its `domain:` (from [docs/domains.yml](../docs/domains.yml)) and its job (the file name) say what it does. IFRS and ISA skills are global, under `global/financial-reporting/` and `global/audit/`.

When a file moves between folders its name stays the same, so its slug does not change. Every move is listed in [docs/PATH-MOVES.md](../docs/PATH-MOVES.md).
