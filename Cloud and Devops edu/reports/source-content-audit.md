# Source-to-Content Audit

Generated: 2026-11-06T14:27:34.201205+00:00

## Scope

Reviewed each package's module source references, source excerpts/findings, student-facing assessment items, answer keys, and the corresponding supplied project files/instructions. Structural checks confirm IDs, lesson links, unique question text, options, answers, manifest counts, and included files. They do not execute mobile apps, Docker images, cloud workflows, or API requests.

## Package Results

| Project | Structure | Modules | Lessons | Questions |
|---|---:|---:|---:|---:|
| audited-escrow-and-tokenization-contracts | PASS | 12 | 36 | 120 |
| auto-configuring-reverse-proxy-with-service-discovery | PASS | 8 | 24 | 80 |
| chaos-engineering-experiment-platform | PASS | 10 | 30 | 100 |
| cloud-cost-monitoring-dashboard-for-iac | PASS | 7 | 21 | 70 |
| cron-dead-man-switch-monitoring | PASS | 10 | 30 | 100 |
| decentralized-storage-dapp-on-ipfs | PASS | 8 | 24 | 80 |
| distributed-rate-limiter-service | PASS | 9 | 27 | 90 |
| distributed-tracing-and-apm-platform | PASS | 8 | 24 | 80 |
| encrypted-configuration-management-in-git | PASS | 12 | 36 | 120 |
| encrypted-deduplicated-backup-system | PASS | 9 | 27 | 90 |
| event-streaming-platform-kafka-lite | PASS | 12 | 36 | 120 |
| kubernetes-control-plane-for-cloud-resources | PASS | 9 | 27 | 90 |
| lightweight-event-messaging-and-queue-system | PASS | 7 | 21 | 70 |
| lightweight-kubernetes-edge-cluster | PASS | 12 | 36 | 120 |
| message-broker-backend-for-microservices | PASS | 12 | 36 | 120 |
| metrics-monitoring-and-alerting-platform | PASS | 7 | 21 | 70 |
| programmable-ci-cd-engine-with-dagger | PASS | 9 | 27 | 90 |
| secrets-management-platform-with-ui | PASS | 9 | 27 | 90 |
| secure-container-registry-with-vulnerability-scanning | PASS | 8 | 24 | 80 |
| self-hosted-git-platform-with-actions-runner | PASS | 10 | 30 | 100 |
| tekton-kubernetes-pipeline-engine | PASS | 10 | 30 | 100 |
| uptime-and-status-monitoring-service | PASS | 8 | 24 | 80 |
| web3-dapp-frontend-with-wallet-integration | PASS | 8 | 24 | 80 |
| woodpecker-ci-pipeline-server | PASS | 7 | 21 | 70 |

## Source Findings and Human Review

### audited-escrow-and-tokenization-contracts
- The project has no independent security audit; tests are not a safety guarantee. Use test networks only, and review the placeholder deployment key.
### auto-configuring-reverse-proxy-with-service-discovery
- Discovery is label-based and health is manually marked; Docker socket access is highly privileged; config parsing is not full YAML.
### chaos-engineering-experiment-platform
- Local delay is applied in both executor and runner, kill recovery is a no-op, and stress magnitude is ignored; isolate any local experiment.
### cloud-cost-monitoring-dashboard-for-iac
- Price tables are hard-coded examples, plan traversal is only one child level, and some cost inputs/defaults are simplified.
### cron-dead-man-switch-monitoring
- Schedule syntax is simplified; the poller must run separately; UUID ping URLs behave as credentials and need protection.
### decentralized-storage-dapp-on-ipfs
- Content store is local rather than connected to IPFS peers; no replication/pinning and no full UnixFS DAG support are implemented.
### distributed-rate-limiter-service
- Memory backend is token bucket but Redis backend is fixed-window; store errors fail open; Redis counters are omitted from exported stats.
### distributed-tracing-and-apm-platform
- The OTLP-labeled handler is custom JSON, is not mounted in main, and is not protocol-compatible with official OTLP payload semantics.
### encrypted-configuration-management-in-git
- SOPS upstream/release status and binary provenance need human review; CI identities can decrypt authorized files; hash-chained audit is tamper-evident, not tamper-proof.
### encrypted-deduplicated-backup-system
- KDF/chunking/encryption are custom code; no remote storage or retention is implemented; verify restored bytes before relying on backups.
### event-streaming-platform-kafka-lite
- Separate fake registry from full Kafka/Schema Registry integration; confirm exactly-once settings and dashboard origin in the deployed stack.
### kubernetes-control-plane-for-cloud-resources
- This is a local control-plane model, not a Kubernetes API server/Crossplane provider; unregistered kinds are accepted and optional FileStore contradicts README memory-only wording.
### lightweight-event-messaging-and-queue-system
- Messages and offsets are in memory; there is no persistence, replication, durable consumer groups, flow control, or DLQ.
### lightweight-kubernetes-edge-cluster
- Bootstrap scripts perform privileged host changes; no cluster was provisioned here; local-path is node-local and NetworkPolicy needs an enforcing CNI.
### message-broker-backend-for-microservices
- Inventory/payment are simulations; review broker credentials, retry/dead-letter behavior, and exposed ports before deployment.
### metrics-monitoring-and-alerting-platform
- This is an in-memory metrics subset, not PromQL or a Prometheus scraper; alerts are logged and not delivered to Alertmanager.
### programmable-ci-cd-engine-with-dagger
- Despite the name, source runs host commands and does not invoke Dagger; only use trusted definitions in a disposable workspace.
### secrets-management-platform-with-ui
- Default password is change-me and the API token is printed at startup; JSON storage/audit is local, mutable, and has no TLS.
### secure-container-registry-with-vulnerability-scanning
- Registry is in-memory metadata; scanner has a small local vulnerability list; image blobs, signing, and verification are absent.
### self-hosted-git-platform-with-actions-runner
- Workflow runner executes host commands without container isolation/auth; README's recorded-step wording conflicts with HostRunner execution; prebuilt binaries have unverified provenance.
### tekton-kubernetes-pipeline-engine
- This is a local Go runner rather than Tekton/Kubernetes; host commands run directly; README's limitation text conflicts with retry/timeout/workspace code.
### uptime-and-status-monitoring-service
- Only HTTP GET checks and polling dashboard are implemented; no TCP/DNS/TLS-expiry/content checks or multi-node guarantee.
### web3-dapp-frontend-with-wallet-integration
- Use only test wallets; no contract deployment or receipt confirmation; custom Keccak/address helpers require independent vectors before financial use.
### woodpecker-ci-pipeline-server
- HostRunner executes commands locally without isolation; no auth/queue/retry/cancel; parser is a limited format rather than full Woodpecker YAML.

## Limits

This validator does not run source builds, containers, cloud deployments, broker stacks, smart contracts, or external services. It checks mapped source files and excerpt cues but cannot certify technical accuracy, production behavior, or current provider/API behavior.
