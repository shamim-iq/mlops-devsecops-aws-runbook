# Projects Guide

Conventions for `projects/`. The README section shape and the file-growth triggers live in [AGENTS.md](../AGENTS.md) because they have to apply without being looked up. This doc holds the worked example and the conventions that only matter once a project spans several files.

## Folder naming

```
projects/YYYY-MM-DD_project-name/
```

The date is when the project opened, not when it ships.

## Status vocabulary

| Status | Meaning |
|---|---|
| `active` | In progress. |
| `on-hold` | Paused, expected to resume. Say what would restart it. |
| `complete` | Done. Leave the folder in place. |
| `archived` | No longer relevant. Say why, so nobody reopens the question. |

The status line carries the word, a date, and the current state in one or two sentences:

> `active` - 2026-09-14. Design locked. Deploy blocked on API keys, waiting on the platform team.

## Worked README

Shape only. Substitute your own domain.

````markdown
# Frontend / Backend Separation

The frontend is its own repo, but it ships *inside* the backend container: the build
output is copied in, committed, and baked into the image. A CSS change therefore needs
a backend image build and a full deploy.

This project breaks that coupling so the frontend deploys on its own. The catch is that
the public hostname has to stay single, so the split happens behind that hostname rather
than at DNS.

## Owner

Project owner - Epic PROJ-318 (due 2026-10-31)

## Status

`active` - 2026-09-30. Direction re-locked on path-based routing after the CDN approach
was dropped (decision #6). Route map verified, design and rollout rewritten. No infra
has changed yet.

## How it works

The load balancer gets a set of path rules above the existing host-header rule. Paths on
a static allowlist go to a new nginx service; everything else falls through to the
backend exactly as it does today.

```text
DNS (unchanged) -> load balancer (unchanged listener, cert, WAF)
    |-- p2-p7 static path allowlist -> static-web (nginx)
    `-- p10   host header only      -> backend - API, forms, webhooks
```

Routing by allowlist with the backend as the default means an unmatched path keeps
working, so a missed pattern degrades to today's behaviour instead of 404ing. Rollback
is deleting the static rules, because the backend still carries its embedded copy.

The CDN was the earlier plan. It was dropped because it would have moved DNS, cert, and
WAF at the same time as the split.

Full routing table and build chain: [design.md](./design.md).

## Next

1. Move the legacy static assets into the frontend repo.
2. Add the Dockerfile, nginx config, and deploy workflows.
3. Build the static-web module and land the listener rules in dev.
4. Resolve POST parity for the three auth routes (design.md, open #3).

## Files

| File | What you'd learn there |
|---|---|
| [findings.md](./findings.md) | How the frontend is built, served, and routed today - verified, with sources |
| [design.md](./design.md) | The full path allowlist, nginx behaviour per route, the four open decisions |
| [plan.md](./plan.md) | Per-environment rollout and the gates between dev, staging, and prod |
| [decisions.md](./decisions.md) | Why the CDN was dropped, why the allowlist defaults to the backend |
| [changelog.md](./changelog.md) | Dated history, newest first |
````

Note what the **Files** table does: each row says what you'd learn, so you can pick a file without opening three. A row reading "the decision log" is worth nothing - you knew that from the filename.

## Density: what to fix

A real line from a project design doc:

> ~30 static path patterns verified (explicit allowlist - no wildcards; one test route and the REST API are dynamic); the service module needs a small multi-rule extension (5 values per condition).

Rewritten:

> The load balancer routes about 30 explicit static paths to nginx. Wildcards don't work, because they would also catch the test route, which the backend renders dynamically. A condition holds at most 5 values, so 30 paths means 6 rules - the service module builds only one today and needs extending.

Same facts, roughly the same length. The difference is that the second version states the causal links the first leaves you to infer: *why* no wildcards, *why* six rules. Density that hides reasoning isn't concision, it's deferred work.

## One job per file

Each file answers one question. State a fact once; every other file links to it.

| File | Question it answers |
|---|---|
| `README.md` | What is this, where does it stand, what's next |
| `design.md` | How does the target actually work |
| `plan.md` | In what order, behind which gates |
| `decisions.md` | Why this way and not the other way |
| `findings.md` | What's actually true today, verified |
| `changelog.md` | What happened, when |

## Tracked vs local-only

Keep the **tracked** repo lean - the consolidated files above. Granular working detail you want for your own reference (scratch notes, per-ticket action logs, dated evidence dumps, throwaway scripts) can be kept **local-only, never pushed**, via this clone's `.git/info/exclude` - a personal ignore file that is itself never tracked:

```
# .git/info/exclude  (local to this clone; no remote footprint)
/projects/YYYY-MM-DD_project/tickets/
/projects/YYYY-MM-DD_project/scratch-notes.md
```

Those paths stay on disk and editable, but never appear as untracked and can't be accidentally committed. When local detail matters to others, **fold its substance up** into the tracked files rather than pushing the raw detail.

- Back up anything local-only **outside the repo** if losing the clone would lose it.
- `.git/info/exclude` is **per-clone**: re-add it after a fresh clone.

## History versus state

State files describe *now*. History goes to `changelog.md`: one dated section per update, append-only, newest first. Sub-headings as needed - done, canceled or re-created, new, handoffs and status changes, blockers resolved.

## Lists, not run-ons

One bullet per work item. Never chain items inside a sentence with separators. A table cell holds a short phrase; multi-clause narrative belongs in prose or a detail file.

## Ticket references

First use per file gets the number plus a 2-4 word label: `199 (dev QA)`. Bare number after that. One range style: `258-262`. Don't mix `210/211` and `210-211` for the same set.

## Flags

`[CONFIRM]` marks a fact you have not verified. It does not mark an open question, an unfinished task, or a process gap - a governance step that demonstrably never happened is a verified finding, so it belongs in **Next** or `findings.md`, not behind a flag.

No blocker or finding ID schemes (B1, B2...) unless the IDs are renumbered on every update, because gaps read as missing data.
