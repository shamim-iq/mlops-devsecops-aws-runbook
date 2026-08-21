# Minimal EFK Logging Progress

## Current State

`active` - 2026-08-22. The EFK logging project is scaffolded. No Helm charts or logging resources have been installed.

## Done

- [x] Record requirement to install Elasticsearch, Fluent Bit, and Kibana with Helm.
- [x] Record that retention and data volume must remain minimal.
- [x] Record requirement to verify application logs in Kibana.
- [x] Record owner-only boundary for Helm and cluster changes.

## Remaining

- [ ] Choose Elasticsearch Helm chart and version.
- [ ] Choose Fluent Bit Helm chart and version.
- [ ] Choose Kibana Helm chart and version.
- [ ] Record logging namespace.
- [ ] Define Elasticsearch storage size.
- [ ] Define Elasticsearch replica count.
- [ ] Define retention or cleanup policy.
- [ ] Define resource requests and limits.
- [ ] Define Kibana access method.
- [ ] Owner installs EFK with Helm.
- [ ] Owner verifies logs in Kibana.
- [ ] Owner records EFK cleanup commands.
