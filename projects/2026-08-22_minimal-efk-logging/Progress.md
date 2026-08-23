# Minimal EFK Logging Progress

## Current State

`complete` - 2026-08-23. The owner installed Elasticsearch, Kibana, and Fluent Bit in the `logging` namespace. The one-day retention policy and index template are present, an Elasticsearch query returned `prediction-api` namespace log hits, and all three logging components run together after the owner temporarily scaled the node group to two nodes. Codex did not install Helm charts or change live EKS logging resources.

## Done

- [x] Record requirement to install Elasticsearch, Fluent Bit, and Kibana with Helm.
- [x] Record that retention and data volume must remain minimal.
- [x] Record requirement to verify application logs in Kibana.
- [x] Record owner-only boundary for Helm and cluster changes.
- [x] Choose Elasticsearch and bundled Kibana chart.
- [x] Choose Fluent Bit collector chart.
- [x] Record logging namespace.
- [x] Define Elasticsearch storage size and replica shape.
- [x] Define short retention and cleanup method.
- [x] Define resource requests and limits.
- [x] Define Kibana access method.
- [x] Write owner-run install, verification, and cleanup commands.
- [x] Owner installed Elasticsearch and Kibana with Helm.
- [x] Owner applied the one-day Index Lifecycle Management policy.
- [x] Owner installed Fluent Bit collector with Helm.
- [x] Owner verified `prediction-api` logs in Elasticsearch.
- [x] Owner confirmed Elasticsearch, Kibana, and Fluent Bit run together.

## Remaining

- [ ] Owner verifies the `prediction-api-logs*` data view in Kibana Discover.
- [ ] Owner records non-sensitive EFK evidence.
- [ ] Owner removes EFK resources during cleanup.
- [ ] Owner scales the node group back down during cleanup.
