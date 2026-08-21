# Evidence And Cleanup

This project defines the final proof and teardown work for the demo. It captures CV/demo evidence, plans destruction, removes Kubernetes workloads and add-ons gracefully, destroys demo-owned AWS infrastructure, and verifies that no unwanted billable resources remain.

## Owner

Project owner - AWS account kept private, preferred region `us-east-1`.

## Status

`active` - 2026-08-22. Evidence and cleanup scope is recorded. No deployment evidence, destroy plan, workload cleanup, Terraform destroy, billing check, or resource inventory check has been completed.

## Operating Boundary

Codex must not run `terraform plan -destroy`, remove Kubernetes workloads, run `terraform destroy`, delete AWS resources, or inspect AWS with deployment credentials. The owner performs cleanup with approved deployment access. Codex may help maintain checklists and summarize owner-provided evidence.

## Cleanup Shape

```text
capture demo evidence
  -> owner reviews terraform plan -destroy
  -> owner removes Kubernetes workloads and add-ons
  -> owner runs terraform destroy
  -> owner checks AWS resource inventory
  -> owner checks billing and cost dashboard
```

Cleanup is mandatory because the demo uses temporary AWS infrastructure and has a strict cost-control objective.

> [CONFIRM] Evidence storage location, final cleanup command sequence, resource inventory method, and billing verification evidence are not recorded yet.

## Next

1. Record where screenshots, logs, and command outputs will be stored.
2. Capture CI result evidence.
3. Capture security scan evidence.
4. Capture ECR image evidence.
5. Capture Argo CD sync evidence.
6. Capture rollout promotion evidence.
7. Capture rollback evidence.
8. Capture Kibana/logging evidence.
9. Owner runs `terraform plan -destroy` and reviews resources marked for deletion.
10. Owner removes Kubernetes workloads and add-ons needing graceful teardown.
11. Owner runs `terraform destroy` for demo-owned AWS infrastructure.
12. Owner verifies AWS resource inventory.
13. Owner verifies AWS billing and cost dashboard.

## Files

| File | What you'd learn there |
|---|---|
| [Progress.md](./Progress.md) | Evidence and cleanup work completed and remaining |
| [checklist.md](./checklist.md) | Evidence, destroy, Kubernetes cleanup, billing, and inventory checks |
