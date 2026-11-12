# Website and repository delivery

`skills/**` on this repository's `main` branch is the editable source. Merged
changes are ingested by the platform, then served on the website and through
MCP. The platform also runs repository-derived exports. Its current export job does not
write back to `skills/**`.

## Delivery after merge

The [ingest workflow](../.github/workflows/ingest-to-platform.yml) uses
[deliver-to-platform.py](../scripts/deliver-to-platform.py) for pushes, scheduled
catch-up and manual recovery. The production environment retains the ingestion credential;
the job runs only on `main` with read-only repository permissions.

The runner:

1. Collects every changed skill from the complete Git range, without depending
   on file lists in an Actions event or a single Commits API response.
2. Excludes sync-bot authors/committers, templates and index files. Removed source
   skills remain in the plan and are listed explicitly in `deletedPaths`.
3. Groups paths by their last non-merge human writer. A maintainer's merge does
   not replace the writer; a file created only in the merge uses its author.
4. Sends 20 paths per workflow request (the API permits at most 200), with one author and the same requested
   head SHA in every batch.
5. Polls the platform's read-only verifier for every requested path before
   moving to the next batch. Pushes, scheduled sweeps and manual recovery all verify.

Only a complete response containing `match` for every path
passes. Held proposals need action and fail delivery, as do mismatches, failed
or unsettled paths, missing outcomes and unknown states. This does not bypass
any source, accountant or repository review. Independent batches still run
when one fails, and the final job reports failure.

For a withdrawal, `paths` still includes the removed path and `deletedPaths`
names it in both the delivery and verification requests. The platform checks
that the commit belongs to main and that the source is absent both at that
commit and at current main. It unpublishes the exactly bound skill and retires
its canonical serving document, preserving its content, ownership and history.
A matching filename is not sufficient authority to withdraw another skill.
Network and HTTP errors never count as evidence that a source was deleted.
Verification requires confirmed unpublished state and a withdrawal receipt.
Deploy the platform's `deletedPaths` support before enabling this sender change;
an older verifier cannot confirm a withdrawal and the run must remain red.

The mandatory `compare` check enforces version/date integrity. Human source
removals are governed by the mandatory `validate` check's Moved/Not moved record
and the human merge decision; they remain visible as warnings in `compare`.
The former automated exporter (`--mode sync`) still rejects source removal.

Runs share a `queue: max` concurrency group, without cancelling in-progress work.
The workflow checks out current `main` after acquiring the queue. It does not
replay the event's older head when a newer run reached the queue first. GitHub
allows up to 100 pending runs; queue order alone does not prove commit order.
See [GitHub's concurrency contract](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax#concurrency).

The daily 06:17 UTC sweep chooses a seven-day boundary on main's first-parent
history, then examines the entire reachable range. Writing merged recently is
included even when its branch commits have older dates. Repeating a failed
range is safe: already-served documents compare identical, while failed paths
still need verification. Recovery outside that window uses `since_sha`.

A missing ingestion credential fails a non-empty delivery. A failed commit
lookup stops before any request is sent. Redirects are not followed with the
credential. Paths and author names are passed as data, not shell commands.

## Inspect a plan without sending

Run from the repository checkout. This command needs no platform credential
and makes no platform request:

```bash
python3 scripts/deliver-to-platform.py --since <last-delivered-sha> --head HEAD
```

The JSON lists each batch, its exact head SHA, paths and author. The range must
start at an ancestor of the requested head. A shallow checkout needs the missing
history fetched before it can plan that range. The runner rejects shallow
repositories rather than claiming an incomplete plan is complete.

To inspect the same range and batch size as scheduled recovery, without sending:

```bash
python3 scripts/deliver-to-platform.py --lookback-days 7 --head HEAD --batch-size 20
```

For recovery, the existing `workflow_dispatch` input `since_sha` supplies the
last delivered commit. Its delivery and verification use the same runner as a
push. A green notification alone is not proof that a skill is served.

## Derived exports

The platform builds `packages/`, `index.json`, `llms-full.txt` and the generated
AI-client bundles from the repository sources. Contributors edit the sources, not
those generated trees. Updating source delivery does not itself prove that a
later derived export succeeded.

The companion private-platform change replaces its truncated REST collector
with a check of the latest scheduled workflow and its actual delivery step.
Only a fresh successful verified sweep produces its catch-up heartbeat, dated
at the sweep's completion rather than the later monitoring request. It does
not start a second ingestion beside the workflow.

Deploy the public scheduled runner before the private monitoring change, after
existing delivery runs have finished. Verify a scheduled sweep before calling
that deployment complete. These draft changes have not dispatched a live
delivery or backfill. Direct privileged ingestion outside this workflow and
other platform writers still need their own ordering evidence; the workflow
queue does not lock unrelated callers or certify every historical skill.

<details>
<summary>Historical source-writing safeguard, inactive</summary>

The protocol below describes the former platform-to-source writer. Source
writes are currently disabled; retain this contract if that writer is ever
restored. It is not the current contribution or recovery procedure.

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
  "skills/australia/au-gst-bas.md": {
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


</details>

## What this means for contributors

1. Edit `skills/**`; generated files are rebuilt from ingested sources.
2. A merge accepts the contribution. Platform delivery is confirmed separately
   by the complete path verification, not guide presence or an HTTP acknowledgement.
3. Keep `last_updated` and any content version accurate; neither is a
   synchronization token.
4. Set your GitHub username in your accountant profile so merged work can be
   linked to that profile. Attribution does not imply approval.
