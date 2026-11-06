# Architecture

## Implemented system

Preflight and server/agent installation scripts, token helper, verification, uninstall, edge-stateful Helm chart, manifests, systemd health/backup timers, validator and runbook.

## Data and control flow

Preflight → bootstrap first server/etcd → join control-plane peers and agents → deploy chart → verify → monitor/back up → safe teardown.

## Module source map

- **Edge Cluster Architecture and Quorum:** The server install script configures a first K3s server; the join script adds another server using the shared token and server URL. The config file sets cluster-level K3s options.
- **Preflight Host Requirements:** Preflight script checks host conditions before server/agent actions.
- **Bootstrap the First Server:** Script installs K3s server with cluster-init and tls-san parameters.
- **Join Additional Servers and Agents:** Server join and agent join consume a token file; agent gets node-class label.
- **Handle Tokens and Secret Files:** Helper supports show/rotate, with README emphasizing avoiding terminal-log output.
- **Deploy the Edge Stateful Helm Chart:** Chart includes StatefulSets, Services, PVC templates, PDB, topology spread, NetworkPolicy, and Pi overrides.
- **Understand Local-Path Storage Limits:** README states node-bound volumes and says durability needs snapshots/application backups.
- **Operate Health and etcd Backups:** Project supplies k3s healthcheck and backup service/timer plus retention scripts.
- **Use the Offline Validation Gate:** Validator parses YAML/chart structure and scans secrets/dangling refs/destructive commands.
- **Roll Out, Roll Back, and Verify:** The sample manifest declares a staged Rollout resource; verifier can check nodes, etcd, and local-path state.
- **Review NetworkPolicy and Failure Modes:** The manifest declares NetworkPolicy rules; the selected K3s CNI must enforce them. Troubleshooting covers cgroup/iptables/hostname/pull fixes.
- **Uninstall and Restore Safely:** Uninstall is gated by --yes; runbook covers node replacement, token rotation, and snapshot restoration.

## Boundaries and risks

- README states no cluster was provisioned; offline validation is not an end-to-end cluster test.
- Control plane requires quorum; node-local local-path volumes are not replicated storage.
- Bootstrap/uninstall commands use sudo and alter hosts; never run without disposable, prepared machines.
- Token helper and environment files contain sensitive cluster credentials; keep them out of logs and Git.
- NetworkPolicy requires a CNI that enforces it; validate on the chosen K3s setup.

This package teaches the checked-in implementation and records gaps between the source and broader platform concepts named by the project. It does not certify security or production readiness.
