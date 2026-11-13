# Publish an approved hosted Registry entry

Publishing is manual and requires Michael's approval of the exact manifest and hash.
The workflow only runs from this repository's main branch when Michael dispatches it.
It publishes the hosted listing only. It does not publish the Python package.

The canonical input is `src/lib/mcp/server.json` in the private website repository.
The public `mcp/server.json` version must match it. The descriptions may use different
truthful wording. No version is copied into the publishing workflow.

After showing Michael the old and new entry and recording his approval, from the
website checkout, dispatch the approved file and its approved SHA256:

```sh
gh workflow run publish-mcp-registry.yml --repo openaccountants/openaccountants --ref main \
  -F manifest_json=@src/lib/mcp/server.json \
  -f approved_sha256="$APPROVED_MANIFEST_SHA256"
```

The workflow checks the hash, hosted identity, public version, endpoint, description
and actual live MCP version before publishing. It uses publisher v1.8.9 from the
official release with a pinned SHA256, then runs schema validation. GitHub's short-lived
repository identity authenticates to the Registry; no PAT or copied login is used.
There is no push, tag or scheduled publishing trigger.

Verify the official latest entry, then rerun the private website's Registry/tool check:
`https://registry.modelcontextprotocol.io/v0.1/servers/io.github.openaccountants%2Fopenaccountants/versions/latest`.

The Registry currently documents that interactive GitHub device login cannot prove
organization ownership. Use this manual GitHub Actions flow for the organization's
listing. See [Registry authentication](https://github.com/modelcontextprotocol/registry/blob/main/docs/modelcontextprotocol-io/authentication.mdx)
and [GitHub Actions publishing](https://github.com/modelcontextprotocol/registry/blob/main/docs/modelcontextprotocol-io/github-actions.mdx).
