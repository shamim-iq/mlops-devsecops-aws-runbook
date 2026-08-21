# MLOps DevOps Runbook

**Owner:** Project owner  
**Date:** 2026-08-22

## Docs Index

| Doc | Purpose |
|-----|---------|
| [Projects Guide](./docs/projects-guide.md) | Project folder conventions - worked README example, one job per file, history in changelog |

## Domain Context

This runbook covers a minimal end-to-end MLOps and DevSecOps demonstration on AWS, built for learning and CV evidence rather than production use. The active project deploys a lightweight scikit-learn model behind a FastAPI prediction API, packages it in Docker, stores the image in Amazon ECR, and runs it on a small CPU-only Amazon EKS worker node. Delivery uses separate CI and CD flows: CI tests, scans, builds, and pushes an image; CD updates a GitOps repository so Argo CD and Argo Rollouts can deploy, validate with Prometheus, promote, or roll back. Git repositories are the source of truth for source code and Kubernetes desired state, AWS Secrets Manager owns runtime/deployment secrets, and AWS IAM with OIDC owns pipeline authentication. Open questions: AWS account and region, CI/CD platform, exact security thresholds, DAST tool, Prometheus analysis thresholds, and the smallest acceptable EKS node shape.

## Domain Rules

- Do not use GPU instances for this project.
- Keep the implementation small enough to complete in one day.
- Keep all public project docs and repository files free of personal details, credentials, account identifiers, local machine paths, and secret-like values.
- Treat INR 500 as a cost-control objective, not a guaranteed invoice ceiling.
- Do not store long-lived AWS access keys in source, pipeline YAML, or local committed files.
- Use OIDC to assume AWS IAM roles from the CI/CD platform.
- Store required credentials in AWS Secrets Manager and retrieve them only when needed.
- Keep CI and CD as separate logical pipelines.
- Gate production deployment with manual approval before the GitOps update.
- Fail the pipeline when configured security thresholds are exceeded.
- Use Argo Rollouts for canary release, Prometheus validation, promotion, and automatic rollback.
- Deploy EFK with Helm and keep retention/data volume minimal.
- Cleanup is mandatory: remove EKS workloads, cluster, node resources, ECR images, S3 artifacts if created, secrets, IAM resources, and leftover networking/security groups after the demonstration.

## Codex Setup

Codex reads this file automatically from the repo root, which is why the conventions live here.

Tool configuration is **not** in this repo. Codex config is per-user and global at `~/.codex/config.toml`, so each collaborator applies it on their own machine. Required for this repo:

```toml
[projects.'<local-runbook-repo>']
trust_level = "trusted"
```

Optional, only if a procedure here dispatches subagents:

```toml
[features]
multi_agent = true
```

Because config is per-user, nobody can configure the repo on anyone else's behalf. New collaborators apply the block above themselves - it belongs in onboarding, not in a setup script.

## Codex Operating Limits

- Codex must never deploy, change, provision, or delete resources in the AWS account.
- Codex is limited to the `<read-only-aws-profile>` AWS profile for AWS inspection only.
- Codex must never use the `<deployment-aws-profile>` AWS profile.
- The owner uses the `<deployment-aws-profile>` AWS profile for resource deployment.
- The owner is responsible for Git add, commit, push, and pull request work.
- Codex must not run `git add`, `git commit`, `git push`, or create pull requests.

## Ownership

Four tiers. A path has exactly one owner.

| Tier | Paths | Rule |
|---|---|---|
| Runbook owner | This file, the portfolio tracker, `scripts/` | Owner edits. Everyone else proposes. |
| Delegated | Each `docs/<area>/` | Its named owner edits. Others report drift, never fix it. |
| Individual | Each `projects/<folder>/` | Its assignee owns it outright. No review. |
| Per-user, unowned | `~/.codex/config.toml` on each machine | Each person owns their own. Never a shared artifact. |

| Path | Owner |
|---|---|
| `AGENTS.md` | Project owner |
| `docs/projects-guide.md` | Project owner |
| `docs/plan.md` | Project owner |
| `projects/2026-08-22_mlops-devsecops-execution-setup/` | Project owner |
| `projects/2026-08-22_gitops-repository-structure/` | Project owner |
| `projects/2026-08-22_model-api-container-build/` | Project owner |
| `projects/2026-08-22_terraform-aws-infrastructure/` | Project owner |
| `projects/2026-08-22_ci-access-and-approval-pipeline/` | Project owner |
| `projects/2026-08-22_argocd-gitops-bootstrap/` | Project owner |
| `projects/2026-08-22_rollouts-prometheus-analysis/` | Project owner |
| `projects/2026-08-22_minimal-efk-logging/` | Project owner |
| `projects/2026-08-22_cd-rollout-promotion-rollback/` | Project owner |
| `projects/2026-08-22_evidence-and-cleanup/` | Project owner |

If you find another owner's docs stale or wrong, document the drift and tell the owner. Do not fix it yourself - they may know something the doc does not say, and a silent cross-area edit means neither of you can trust the file afterwards.

## Project READMEs

`projects/YYYY-MM-DD_name/README.md` is the whole project until it outgrows itself. Write it for yourself returning after two weeks - re-orient, see where things stand, reload the design, act.

Sections in this order. Drop any that has nothing to say.

| Section | Contents |
|---|---|
| Title + lede | 2-4 sentences: what this changes and why it exists. Plain sentences. Enough that you don't reconstruct the problem from scratch. |
| **Owner** | Owner label, plus non-sensitive identifiers such as ticket, epic, or region. Keep emails, cloud account IDs, credentials, and local machine paths out of public docs. |
| **Status** | `active` / `on-hold` / `complete` / `archived`, dated, then what's true now: done, in flight, blocked and on whom. Anything that would bite someone who acted without knowing it goes here. |
| *The core* | The technical model you need in your head, as a paragraph or a small diagram. Name the heading for the genre: **How it works** for a build, **What was done** for finished work, **Root cause** for an incident, **What we found** for an audit. |
| **Next** | The concrete next actions, in order. A complete project still has these. |
| **Files** | Only once other files exist. Say what you'd learn there, not what the file is called. |

Fold "Problem", "Goal", "Constraint", and "Approach" into the lede or the core section. Don't add them as headings.

## When a project outgrows README.md

Start every project as a single `README.md`. Split a file out when its trigger fires, not before.

Canonical names only. A project has one plan, so it is `plan.md` - never `rollout-plan.md` or `implementation-plan.md`. The README says what kind of plan it is.

| Split out | When |
|---|---|
| `design.md` | The core section passes about one screen, or open design questions pile up. |
| `plan.md` | The work has ordered phases or gates - more than **Next** can hold. |
| `decisions.md` | The third decision, or the first reversal. |
| `changelog.md` | **Status** starts accumulating "as of" history. |
| `findings.md` | Evidence outgrows the claims it supports. Audits trip this on day one. |
| `action-log.md` | The first mutating command runs. |
| `approvals.md` | The first action needing human sign-off before it runs. |
| `AGENTS.md` | The project has rules differing from repo defaults. Codex reads the nearest one. |

## Doc Authoring

Write so each fact lands on the first read. Applies to all `docs/` and `projects/` files.

Concision means cutting words that carry nothing. It does not mean cutting the words that carry how facts connect - a reader who parses a dense line twice was saved nothing.

**Accuracy**
- Never infer. State only what's verified.
- Flag uncertainty once, terse, as a blockquote: `> [CONFIRM] <what's unverified>`. Never inline, never repeated. Each flag lives in exactly one file - the topic's home.
- `[CONFIRM]` marks an unverified fact. It does not mark an open question or an unfinished task - those go in **Next**.
- Timestamp data that goes stale: `Verified YYYY-MM-DD`.

**Public safety**
- Never commit personal emails, personal names used as identifiers, local usernames, local absolute paths, cloud account IDs, profile names, access keys, tokens, passwords, private keys, or secret values.
- Use placeholders for sensitive facts: `Project owner`, `Private, not committed`, `<implementation-repository-url>`, `<runbook-repository-url>`, `<local-implementation-repo>`, `<read-only-aws-profile>`, and `<deployment-aws-profile>`.
- Keep credentials in the approved secret store or local uncommitted environment only. Public docs may say where a value belongs, but never include the value.
- Before suggesting a commit or push, scan changed files for personal details and secret-like values.

**Cut**
- Lead with the fact. No throat-clearing, no outros, no "Background"/"Overview" sections, no "Related docs" footers - cross-link inline.
- A section may open with **one** orienting sentence when the heading alone doesn't say why it exists.
- No hedging or softeners. Active voice.
- State scope and decisions once. Other files link, never restate.
- Never write a sentence that restates an adjacent table.

**Keep**
- Causal connectives - because, so, which means, otherwise. These are the reasoning, not filler. Strip them and the doc becomes a list of facts the reader has to re-derive.
- The reason behind a non-obvious choice, in the same breath as the choice.
- An expansion of project jargon at first use per file.

**Sentences**
- One idea per sentence. Split at the semicolon.
- Prose for anything with reasoning, sequence, or cause. Tables for parallel facts.

**Format**
- Tables hold facts of the same shape, one short phrase per cell. If a row needs a "because", it's prose.
- Headings are specific noun phrases.
- A diagram replaces its prose narration. Add only what it can't show: dependencies, timing, failure modes.
- One example per pattern, not three.
- In status and narrative prose, bold only blocked, at-risk, and untracked work - bolding everything marks nothing. Structural labels (table headers, section keys, defined terms) are exempt.

**State versus history**
- State files describe *now*. Keep "done since...", per-person done-lists, and strikethrough-resolved items out of them.
- History goes to `changelog.md`: one dated section per update, append-only, newest first.

## Git

- Branch before committing if you are on the default branch.
- Do not run `git add`, `git commit`, `git push`, or create pull requests. The owner handles staging, commits, pushes, and PRs.
- When Git history work is needed, Codex may suggest a branch name, commit message, or PR description for the owner to apply.

## Structure

```
<repo-root>/
|-- AGENTS.md      # Rules, docs index, ownership. Owner-only. Codex loads this.
|-- docs/          # Stable reference facts that outlive any one project
`-- projects/      # One folder per piece of work: YYYY-MM-DD_project-name/
```

