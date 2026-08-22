# Website ↔ repo sync

The platform database (openaccountants.com) is the operational source for
website guide content. This repository is its public projection, and merged
external changes to `skills/**` must be ingested back into the platform before
the next outbound export.

> **Current limitation:** automated repository-to-platform ingestion has not
> shipped. A maintainer must run and verify the private platform ingest after
> every merge that changes `skills/**`. Public GitHub Actions run after a push;
> they can detect a stale export but cannot undo or prevent one.

## Outbound (platform → repo), daily

A scheduled job in the separate, private platform repository renders published
guides using the same serving code as the website:

- `skills/**` is rendered per guide (`skills.github_path` in the platform DB).
- An existing guide edited by an accountant is committed under that
  accountant's name (git author); the committer is
  `openaccountants-sync[bot]`.
- Derived trees — `packages/`, `index.json`, `llms-full.txt` — are regenerated
  in the same run and committed by the bot. **Never edit them in a PR.**
- Frontmatter uses `reviewed_by` plus `review_status` (`current` |
  `pending_review`). The legacy `verified_by` key is removed on rewrite.

The exporter must not use the platform database's timestamp, `last_updated`, or
content `version` as its concurrency decision. Those fields describe content;
they do not prove that the platform ingested the current repository blob.

## Inbound (repo → platform)

Once successfully ingested, merged pull requests touching `skills/**` replace
or create the corresponding platform guide and retain the pull-request author's
attribution. A substantive edit supersedes any professional review of the
previous text and therefore sets the guide back to `pending_review` until it is
reviewed again.

Until automated ingestion ships, the maintainer sequence is:

1. Identify every changed `skills/**` path in the merge commit.
2. Pause outbound writes for those paths.
3. Run the private ingest tool against the exact merge commit.
4. Verify that the complete body and frontmatter were stored atomically, prior
   review was invalidated when appropriate, and the merge's Git blob hash was
   recorded for each path.
5. Resume outbound sync only after that verification succeeds.

If ingestion fails or cannot be verified, keep the affected paths quarantined;
do not allow an older platform record to replace them.

## Required private-platform integrity contract (not deployed here)

The durable guard is optimistic concurrency per guide. The platform sync state
must record:

- `last_repo_blob_sha`: the Git blob hash of the exact source guide most
  recently imported or exported successfully; and
- `content_revision`: a platform-controlled, monotonically increasing integer.

The private database must enforce `content_revision` monotonicity in the same
transaction that stores the guide. The public script can validate only that a
supplied revision has the expected basic shape; the Git blob is the concurrency
token it can independently compare.

Before changing an existing `skills/**` file, the exporter fetches the current
`main` tip and compares that file's blob hash with `last_repo_blob_sha`:

- Match: the platform may render the candidate, subject to metadata checks.
- Mismatch, but rendered content already equals the repository: treat this as
  idempotent state repair and adopt the current blob without rewriting it.
- Any other mismatch: abort the source-writing phase, report a conflict, and
  require ingestion or human resolution. Never use last-writer-wins.

The rendered frontmatter must also pass the repository's strict YAML parser.
The preflight rejects malformed YAML, duplicate keys, non-mapping roots,
non-list `depends_on` values, and known string fields that YAML 1.1 would
coerce to another type (for example, unquoted `jurisdiction: NO` becomes the
boolean `false`).

The exporter must also abort on a non-fast-forward push and retry from a fresh
fetch. Body, frontmatter, content revision, and imported Git blob must be stored
in one transaction so a stale body cannot be combined with newer metadata.

### Private exporter preflight

After rendering into a clean worktree based on the fetched `main`, the platform
job creates a temporary provenance JSON file. It contains public paths and
revision tokens only — never credentials, database identifiers, or guide text:

```json
{
  "skills/international/australia/au-gst-bas.md": {
    "expected_repo_blob": "0123456789abcdef0123456789abcdef01234567",
    "content_revision": 42
  }
}
```

For a genuinely new path, `expected_repo_blob` is `null`. The private job then
runs, before committing or pushing:

```bash
python3 -m pip install -r scripts/requirements-validation.txt
python3 scripts/check-sync-integrity.py \
  --base origin/main \
  --worktree \
  --mode sync \
  --provenance "$RUNNER_TEMP/openaccountants-sync-provenance.json"
```

Strict sync mode fails on a blob conflict, missing or malformed provenance,
invalid or ambiguous YAML frontmatter, backwards `last_updated` or numeric
`version`, loss of an ordered numeric version, a newly inconsistent body-heading
version, and an unversioned body rewrite. It always stops on a source-guide
deletion or rename; a maintainer must perform any approved migration through a
separate controlled process.

### Public audit

The `Sync Integrity` workflow compares pull-request revisions and each push to
`main`. It flags an aggregate bot-authored commit that rewrites an existing
source guide, and a `main` push fails if a guide body changes without advancing
its date or version. Correct accountant attribution remains a private-exporter
responsibility; the public check narrowly identifies the known aggregate
sync-bot identity. A failed post-push check is an alarm after `main` changed; it
cannot roll back or prevent the write.

## Deployment and repository controls

This public repository supplies the preflight implementation, tests, workflow,
and protocol. It does **not** install the command in the private platform job,
change the bot from direct pushes to pull requests, or configure GitHub branch
rules. `CODEOWNERS` identifies reviewers but is not an enforcement mechanism on
its own. At the time this contract was added, `main` had no branch-protection
rule or repository ruleset.

Maintainers should deploy the remaining controls in this order:

1. Integrate strict CAS preflight into the private exporter and exercise it in
   dry-run mode against the current `main` tip.
2. Change the exporter to push a sync branch and open a pull request instead of
   writing directly to `main`.
3. Add a `main` ruleset that requires pull requests, code-owner review, and the
   exact job contexts `guard-derived-trees`, `validate`, `unit-tests`, and
   `compare`; block force pushes and branch deletion. GitHub's UI may display
   these as `Workflow name / job name`. Retain the repository's operational CLA
   check as a separate required context, confirming its exact name in Settings.
4. Do not grant the sync bot a broad bypass. Keep any emergency bypass limited,
   human-controlled, and auditable.
5. Verify one complete round trip — platform v1, merged repository v2, inbound
   v2 ingest, then an outbound render that leaves v2 unchanged.

Enabling blocking rules before the bot uses branches would only break the
scheduled job. Leaving the direct-push bot exempt would preserve the stale-write
path this contract is intended to close.

## What this means for contributors

1. Edit `skills/**` only; generated files are rebuilt by the platform sync.
2. A merge accepts the repository contribution. Platform publication is
   complete only after the maintainer confirms inbound ingestion.
3. `last_updated` must never move backwards. Bump `version` on substantive
   changes when the guide has that field, but do not treat either value as a
   synchronization token.
4. Set your GitHub username in your accountant profile on openaccountants.com
   so platform edits can be attributed to your GitHub account.
