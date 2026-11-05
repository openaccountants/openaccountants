# OpenAccountants for Hermes

The OpenAccountants connector as a portable Agent Plugin (agent-plugins.org v1),
which Hermes loads natively: the hosted OpenAccountants connector ships as the
package's MCP server, giving today's figures for 190+ jurisdictions.

## What installs

- `mcp.json` — the connector at https://www.openaccountants.com/api/mcp
  (streamable-http). Hermes registers it as `openaccountants` when the plugin
  is enabled.

The plugin deliberately ships no skills. Every enabled plugin skill adds a row
to the skills index on every turn, so a 2,000-skill bundle would cost tens of
thousands of tokens per request. Install only the skills you need instead:

```bash
# pick jurisdictions by code, one skill by slug, or all, into your Hermes skills
curl -fsSL https://raw.githubusercontent.com/openaccountants/openaccountants/main/agent-skills/install.sh \
  | sh -s -- MT NL DE --to ~/.hermes/skills
```

Browse the full library at https://www.openaccountants.com/skills or in the
repository's `agent-skills/` tree. Hermes loads only each installed skill's
short description and reads the full `SKILL.md` when a task matches.

## Disclosure

- Network calls: the OpenAccountants connector (hosted at
  https://www.openaccountants.com/api/mcp) when the plugin is enabled.
- Shell commands: none. Writes: none at runtime. Credentials: none required.

## Install (Hermes)

Copy this folder to `~/.hermes/plugins/openaccountants/`, then
`hermes plugins enable openaccountants`.
