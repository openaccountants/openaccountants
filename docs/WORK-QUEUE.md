# Work queue

Since 14 Nov 2026, work between Michael's AI workers goes through GitHub issues on this
repository, not through Michael pasting briefs between chats.

| Label | Who picks it up |
|---|---|
| `owner:claude` | Claude (the data2 chat for the US and the platform, the world chat for other countries) |
| `owner:codex` | Codex (ChatGPT) |
| `owner:grok` | Grok Bot |
| `owner:michael` | Michael: only what is truly his (a send, a person's name, money) |
| `owner:ryan`, `owner:jeff` | Ryan Duguid (Australia, source reachability), Jeff Watts |
| `owner:open` | Anyone |

## How it works

1. **Opening a job.** One issue per job, from the "Work item" template: the job, the scope
   (folders, files, what not to touch), and the brief and checks. One owner label.
2. **Starting.** At the start of every session a worker lists its open issues:
   `gh issue list -R openaccountants/openaccountants --label owner:<me> --state open`.
   Before starting, it comments "Started" so nobody else takes it.
3. **Finishing.** The result is a PR whose body says `Closes #<issue>`; merging closes the
   issue. A finding for another worker (a wrong figure found in a live test, a file outside
   your scope) is a new issue with that worker's label.
4. **Nothing waits on Michael** unless the label is `owner:michael`.

Merging follows `docs/AUTOMATED-REVIEW.md` ("Figure check").
