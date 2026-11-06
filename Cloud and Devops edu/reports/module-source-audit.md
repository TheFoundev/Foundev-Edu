# Module-to-source audit

Modules audited: 221

Every module is mapped to source files and a code focus. Validation checks source-file existence, excerpt citations, focus-cue presence, and plain-language-before-code progression. Human review remains necessary for semantic correctness.

## audited-escrow-and-tokenization-contracts

- **Roles and Contract Boundaries** — `contracts/TokenizedAsset.sol` → `TokenizedAsset` (lines 19–28); mapped: `contracts/Escrow.sol`, `contracts/TokenizedAsset.sol`.
- **Escrow State Machine** — `contracts/Escrow.sol` → `ArbiterDecided` (lines 345–354); mapped: `contracts/Escrow.sol`.
- **Native and ERC20 Funding** — `contracts/Escrow.sol` → `fund` (lines 217–226); mapped: `contracts/Escrow.sol`.
- **Pull Payments and Settlement Credits** — `contracts/Escrow.sol` → `withdraw` (lines 370–379); mapped: `contracts/Escrow.sol`.
- **Deadlines and Timeout Paths** — `contracts/Escrow.sol` → `cancel` (lines 301–310); mapped: `contracts/Escrow.sol`.
- **Dispute and Arbiter Lifecycle** — `contracts/Escrow.sol` → `raiseDispute` (lines 318–327); mapped: `contracts/Escrow.sol`.
- **ERC721 Provenance and Roles** — `contracts/TokenizedAsset.sol` → `ReentrancyGuard` (lines 19–28); mapped: `contracts/TokenizedAsset.sol`.
- **Royalty Pool Accounting** — `contracts/TokenizedAsset.sol` → `tokenAmount` (lines 204–213); mapped: `contracts/TokenizedAsset.sol`.
- **Factory Creation and Indexing** — `contracts/EscrowFactory.sol` → `getEscrows` (lines 79–88); mapped: `contracts/EscrowFactory.sol`.
- **Events, Errors, and External Calls** — `contracts/Escrow.sol` → `ContributionReceived` (lines 239–248); mapped: `contracts/Escrow.sol`, `contracts/TokenizedAsset.sol`.
- **Test Fixtures and Security Tests** — `test/escrow.spec.ts` → `reentrancy` (lines 368–377); mapped: `contracts/test/ReentrancyAttacker.sol`, `test/escrow.spec.ts`.
- **Deploy and Audit Limits** — `hardhat.config.ts` → `PRIVATE_KEY` (lines 8–17); mapped: `scripts/deploy.ts`, `hardhat.config.ts`, `README.md`.

## auto-configuring-reverse-proxy-with-service-discovery

- **Service and Instance Models** — `proxy.go` → `Registry` (lines 217–226); mapped: `proxy.go`.
- **Parse the Small Config Format** — `proxy.go` → `HasPrefix` (lines 53–62); mapped: `proxy.go`.
- **Health Flags and Round Robin** — `proxy.go` → `Pick` (lines 91–100); mapped: `proxy.go`.
- **Reverse Proxy Path Flow** — `proxy.go` → `Join` (lines 149–158); mapped: `proxy.go`.
- **Docker Label Discovery** — `proxy.go` → `ListContainers` (lines 212–221); mapped: `proxy.go`.
- **Docker Socket Trust Boundary** — `proxy.go` → `DialContext` (lines 174–183); mapped: `proxy.go`, `README.md`.
- **Test Routing and Failure Responses** — `proxy_test.go` → `NewServer` (lines 30–39); mapped: `proxy_test.go`.
- **Limits of Discovery and Health** — `proxy.go` → `Mark` (lines 71–80); mapped: `README.md`, `proxy.go`.

## chaos-engineering-experiment-platform

- **Experiment and Action Models** — `chaos.go` → `Actions` (lines 23–32); mapped: `chaos.go`.
- **Validate Actions and Hypotheses** — `chaos.go` → `Compare` (lines 139–148); mapped: `chaos.go`.
- **Executor Interface and Dry Run** — `chaos.go` → `DryRunExecutor` (lines 419–428); mapped: `chaos.go`.
- **Local Fault Effects and Safety** — `chaos.go` → `Recover` (lines 226–235); mapped: `chaos.go`.
- **Check Steady-State Hypotheses** — `chaos.go` → `checkSteadyState` (lines 448–457); mapped: `chaos.go`.
- **Runner Timeline and Rollback** — `chaos.go` → `Run` (lines 412–421); mapped: `chaos.go`.
- **Store Experiment Results** — `chaos.go` → `Save` (lines 306–315); mapped: `chaos.go`.
- **Tests and Deterministic Time** — `chaos_test.go` → `recordingExecutor` (lines 143–152); mapped: `chaos_test.go`, `chaos.go`.
- **Audit Local Executor Semantics** — `chaos.go` → `sleep` (lines 359–368); mapped: `chaos.go`.
- **Plan Safe Fault Experiments** — `chaos.go` → `executor` (lines 419–428); mapped: `README.md`, `chaos.go`.

## cloud-cost-monitoring-dashboard-for-iac

- **Plans and Planned Values** — `main.go` → `ParsePlan` (lines 32–41); mapped: `main.go`, `cost.go`.
- **Decode Resource Values** — `cost.go` → `stringValue` (lines 110–119); mapped: `cost.go`.
- **Traverse Modules and Nested Data** — `cost.go` → `childModules` (lines 89–98); mapped: `cost.go`.
- **Classify Providers and Resource Types** — `cost.go` → `providerOf` (lines 170–179); mapped: `cost.go`.
- **Use the Hard-Coded Price Catalog** — `cost.go` → `instancePrices` (lines 138–147); mapped: `cost.go`.
- **Calculate Estimates and Unknowns** — `cost.go` → `EstimateResource` (lines 130–139); mapped: `cost.go`.
- **Aggregate and Expose JSON** — `main.go` → `Handler` (lines 40–49); mapped: `cost.go`, `api.go`, `main.go`.

## cron-dead-man-switch-monitoring

- **Model Checks, Pings, and Alerts** — `core/models.py` → `Ping` (lines 41–50); mapped: `core/models.py`.
- **Parse Schedules and Calculate Deadlines** — `core/state.py` → `parse_cron` (lines 28–37); mapped: `core/state.py`.
- **Reason About State Transitions** — `core/state.py` → `should_alert_on_transition` (lines 135–144); mapped: `core/state.py`.
- **Receive Heartbeats and Return Status** — `core/api.py` → `check_status` (lines 90–99); mapped: `core/api.py`.
- **Authenticate Management APIs** — `core/api.py` → `check_ping` (lines 32–41); mapped: `core/api.py`.
- **CRUD and Summary Endpoints** — `core/api.py` → `checks_list_create` (lines 112–121); mapped: `core/api.py`.
- **Poller and Alert Dispatch** — `core/management/commands/run_poller.py` → `dispatch_alert` (lines 3–12); mapped: `core/management/commands/run_poller.py`, `core/dispatch.py`.
- **Database and Environment Configuration** — `config/settings.py` → `DATABASE_URL` (lines 53–62); mapped: `config/settings.py`, `docker-compose.yml`.
- **Webhook Reliability and Alert Deduplication** — `core/dispatch.py` → `Alert` (lines 5–14); mapped: `core/dispatch.py`, `core/models.py`.
- **Threat Model and Test Boundaries** — `core/tests/test_alerts.py` → `dispatch` (lines 1–8); mapped: `core/tests`, `README.md`.

## decentralized-storage-dapp-on-ipfs

- **Content Addressing in Plain Terms** — `src/cid.js` → `cidFromBytes` (lines 44–53); mapped: `src/cid.js`, `README.md`.
- **Hash Bytes and Build Multihash** — `src/cid.js` → `SHA256_MULTIHASH` (lines 64–73); mapped: `src/cid.js`.
- **Assemble CIDv1 and Raw Codec** — `src/cid.js` → `CID_VERSION` (lines 61–70); mapped: `src/cid.js`.
- **Encode and Decode Base32** — `src/cid.js` → `base32encode` (lines 70–75); mapped: `src/cid.js`.
- **Store and Verify Local Content** — `src/store.js` → `createStore` (lines 2–11); mapped: `src/store.js`.
- **HTTP Server and Client Flow** — `src/server.js` → `createIpfsServer` (lines 15–24); mapped: `src/server.js`, `src/ipfs.js`.
- **Serve the Browser UI** — `src/static.js` → `servePublic` (lines 22–27); mapped: `src/static.js`, `public/app.js`.
- **Tests and Real-IPFS Limits** — `src/ipfs.js` → `DEFAULT_API` (lines 5–14); mapped: `test/ipfs.test.js`, `src/ipfs.js`, `README.md`.

## distributed-rate-limiter-service

- **Token Bucket in Plain Terms** — `store.go` → `MemoryStore` (lines 48–57); mapped: `limiter.go`, `store.go`.
- **Memory Store Synchronization** — `store.go` → `MemoryStore` (lines 58–67); mapped: `store.go`.
- **HTTP Middleware and Rate Headers** — `limiter.go` → `RateLimit` (lines 125–134); mapped: `limiter.go`, `main.go`.
- **Choose a Request Identity Key** — `limiter.go` → `RemoteAddr` (lines 96–105); mapped: `limiter.go`.
- **Contrast Redis Fixed Window** — `store.go` → `RedisStore` (lines 242–251); mapped: `store.go`.
- **Read the RESP Client** — `store.go` → `respClient` (lines 217–226); mapped: `store.go`.
- **Plan for Store Failure** — `limiter.go` → `AllowAt` (lines 45–54); mapped: `limiter.go`.
- **Metrics and Expiration** — `store.go` → `RedisStore` (lines 261–270); mapped: `limiter.go`, `store.go`, `main.go`.
- **Tests, Concurrency, and Algorithm Limits** — `limiter_test.go` → `TestTheLimiterIsSafeUnderLoad` (lines 51–60); mapped: `limiter_test.go`, `README.md`.

## distributed-tracing-and-apm-platform

- **Span and Trace Vocabulary** — `tracing.go` → `Span` (lines 40–49); mapped: `tracing.go`.
- **Store and Concurrency** — `tracing.go` → `Add` (lines 47–56); mapped: `tracing.go`.
- **Assemble Trace Duration and Root** — `tracing.go` → `TraceID` (lines 89–98); mapped: `tracing.go`.
- **Calculate Latency Percentiles** — `tracing.go` → `Percentile` (lines 124–133); mapped: `tracing.go`.
- **Ingest Custom Span JSON** — `main.go` → `IngestHandler` (lines 25–34); mapped: `tracing.go`, `main.go`.
- **Audit the OTLP-Labeled Handler** — `tracing.go` → `scopeSpans` (lines 147–156); mapped: `tracing.go`, `tracing_test.go`, `main.go`.
- **Query Stats and Trace IDs** — `main.go` → `traces` (lines 37–43); mapped: `tracing.go`, `main.go`.
- **Limits and Verification** — `tracing.go` → `OTLPHandler` (lines 138–147); mapped: `tracing.go`, `tracing_test.go`, `main.go`, `README.md`.

## encrypted-configuration-management-in-git

- **Threat Model and Secret Lifecycle** — `secretsync/policy.py` → `authorize_decrypt` (lines 4–13); mapped: `secretsync/policy.py`, `README.md`.
- **Load Environment and Recipient Config** — `secretsync/config.py` → `DecryptPolicy` (lines 15–24); mapped: `secretsync/config.py`, `.sops.yaml`.
- **Read the Mini-YAML Subset** — `secretsync/miniyaml.py` → `mappings` (lines 118–127); mapped: `secretsync/miniyaml.py`.
- **Find and Invoke SOPS/Age Tools** — `secretsync/sopsbin.py` → `sops_encrypt` (lines 17–26); mapped: `secretsync/sopsbin.py`, `scripts/fetch_tools.sh`.
- **Encrypt Files for Recipients** — `secretsync/cli.py` → `cmd_encrypt` (lines 290–299); mapped: `secretsync/cli.py`, `secretsync/sopsbin.py`.
- **Authorize CI Decryption** — `secretsync/policy.py` → `authorize_decrypt` (lines 4–13); mapped: `secretsync/policy.py`, `secretsync/cli.py`.
- **Rotate Recipients with a Grace Period** — `secretsync/cli.py` → `previous_recipients` (lines 606–615); mapped: `secretsync/cli.py`, `secretsync/config.py`.
- **Build the Hash-Chained Audit Log** — `secretsync/audit.py` → `AuditLog` (lines 21–30); mapped: `secretsync/audit.py`.
- **Scan Tracked Files for Plaintext** — `secretsync/check.py` → `scan_paths` (lines 120–129); mapped: `secretsync/plaintext.py`, `secretsync/check.py`.
- **Use the Pre-Commit and CI Gates** — `.github/workflows/ci.yml` → `runs` (lines 4–13); mapped: `.githooks/pre-commit`, `.github/workflows/ci.yml`.
- **Use the Ansible Example Carefully** — `ansible/playbook.yml` → `Ansible` (lines 1–6); mapped: `ansible/playbook.yml`, `ansible/lookup_plugins/secretsync.py`.
- **Verify and State the Security Limits** — `tests/test_audit.py` → `AuditLog` (lines 6–15); mapped: `tests/`, `secretsync/audit.py`, `secretsync/plaintext.py`, `README.md`.

## encrypted-deduplicated-backup-system

- **Chunk and Manifest Model** — `repository.go` → `ChunkInfo` (lines 204–213); mapped: `repository.go`.
- **Password, Salt, and Key Derivation** — `repository.go` → `NewSalt` (lines 44–53); mapped: `repository.go`.
- **Content-Defined Chunk Boundaries** — `repository.go` → `ContentDefined` (lines 101–110); mapped: `repository.go`.
- **Hash IDs and Deduplication** — `repository.go` → `chunkID` (lines 206–215); mapped: `repository.go`.
- **Encrypt and Authenticate Chunks** — `repository.go` → `openSealed` (lines 239–248); mapped: `repository.go`.
- **Write Repository and Manifest** — `repository.go` → `PutResult` (lines 203–212); mapped: `repository.go`.
- **Restore and Verify Content** — `repository.go` → `OpenRepository` (lines 187–196); mapped: `repository.go`.
- **Test Deduplication and Restore Drills** — `repository_test.go` → `TestContentDefinedChunking` (lines 6–15); mapped: `repository_test.go`.
- **Operational Limits and Recovery** — `repository.go` → `Restore` (lines 228–237); mapped: `repository.go`, `main.go`, `README.md`.

## event-streaming-platform-kafka-lite

- **Events, Keys, and Topics** — `src/main/java/local/foundev/streams/producer/ClickProducer.java` → `event` (lines 47–56); mapped: `src/main/java/local/foundev/streams/producer/ClickProducer.java`, `config/producer.properties`.
- **Validate Event Schemas** — `src/main/java/local/foundev/streams/registry/SchemaRegistryClient.java` → `SchemaRegistryClient` (lines 9–18); mapped: `src/main/java/local/foundev/streams/registry/SchemaRegistryClient.java`, `src/main/resources/clicks-value.schema.json`.
- **Handle Invalid Events and DLQ** — `src/main/java/local/foundev/streams/deser/SchemaValidatingDeserializer.java` → `dlq` (lines 23–32); mapped: `src/main/java/local/foundev/streams/deser/SchemaValidatingDeserializer.java`.
- **Build the Kafka Streams Topology** — `src/main/java/local/foundev/streams/streams/ClicksStreamsApp.java` → `stats` (lines 29–38); mapped: `src/main/java/local/foundev/streams/streams/ClicksStreamsApp.java`, `config/streams.properties`.
- **Filter Bots and Aggregate Windows** — `src/main/java/local/foundev/streams/streams/ClicksStreamsApp.java` → `regex` (lines 17–26); mapped: `src/main/java/local/foundev/streams/streams/ClicksStreamsApp.java`.
- **Understand Sessionization and State Stores** — `src/main/java/local/foundev/streams/streams/ClicksStreamsApp.java` → `state` (lines 13–22); mapped: `src/main/java/local/foundev/streams/streams/ClicksStreamsApp.java`.
- **Producer Delivery and Registry Modes** — `src/main/java/local/foundev/streams/producer/ClickProducer.java` → `producer` (lines 1–5); mapped: `src/main/java/local/foundev/streams/producer/ClickProducer.java`, `src/main/java/local/foundev/streams/registry/FakeSchemaRegistry.java`, `README.md`.
- **Serve Materialized Views** — `src/main/java/local/foundev/streams/api/ViewServer.java` → `ViewServer` (lines 160–169); mapped: `src/main/java/local/foundev/streams/api/ViewServer.java`.
- **Dashboard Origin and Data Flow** — `src/main/resources/dashboard/index.html` → `ViewServer` (lines 57–66); mapped: `src/main/resources/dashboard/index.html`, `README.md`.
- **Compose the Stack and Verify Startup** — `tools/verify.sh` → `verification` (lines 1–7); mapped: `docker-compose.yml`, `Dockerfile`, `tools/verify.sh`.
- **Delivery Guarantees and Failure Handling** — `src/main/java/local/foundev/streams/streams/StreamsExceptionHandler.java` → `processing` (lines 7–16); mapped: `src/main/java/local/foundev/streams/streams/StreamsExceptionHandler.java`, `config/streams.properties`.
- **Read Tests and Limitations** — `src/test/java/local/foundev/streams/registry/SchemaRegistryClientTest.java` → `SchemaRegistryClientTest` (lines 10–19); mapped: `src/test/java/local/foundev/streams/registry/SchemaRegistryClientTest.java`, `README.md`.

## kubernetes-control-plane-for-cloud-resources

- **Resource Specs and Status** — `control.go` → `ResourceVersion` (lines 87–96); mapped: `control.go`.
- **Register and Validate Schemas** — `control.go` → `SchemaRegistry` (lines 154–163); mapped: `control.go`.
- **Plan Desired vs Current State** — `control.go` → `sameSpec` (lines 128–137); mapped: `control.go`.
- **Reconcile Actions and Failures** — `control.go` → `FailedAction` (lines 261–270); mapped: `control.go`.
- **Use Resource Versions for Stale Writes** — `control.go` → `ResourceVersion` (lines 87–96); mapped: `control.go`.
- **Controller Desired State and Generation** — `control.go` → `SetDesired` (lines 340–349); mapped: `control.go`.
- **Persist State with the Optional FileStore** — `main.go` → `NewFileStore` (lines 85–94); mapped: `control.go`, `main.go`.
- **Expose the JSON Control API** — `control.go` → `Server` (lines 402–411); mapped: `control.go`, `main.go`.
- **Separate Simulation from Kubernetes** — `control.go` → `Kubernetes` (lines 19–28); mapped: `README.md`, `control.go`.

## lightweight-event-messaging-and-queue-system

- **Message, Topic, and Partition Models** — `queue.go` → `Message` (lines 71–80); mapped: `queue.go`.
- **Choose a Partition from the Key** — `queue.go` → `partitionOf` (lines 56–65); mapped: `queue.go`.
- **Publish and Assign Offsets** — `queue.go` → `Broker` (lines 31–40); mapped: `queue.go`.
- **Fetch from an Offset** — `queue.go` → `Broker` (lines 92–101); mapped: `queue.go`.
- **Consumer Poll, Ack, and Pending** — `queue.go` → `Consumer` (lines 139–148); mapped: `queue.go`.
- **Retention and HTTP API** — `queue.go` → `NewBroker` (lines 30–39); mapped: `queue.go`, `main.go`.
- **Durability and Delivery Limits** — `queue.go` → `Messages` (lines 19–28); mapped: `queue.go`, `README.md`.

## lightweight-kubernetes-edge-cluster

- **Edge Cluster Architecture and Quorum** — `bootstrap/10-install-server.sh` → `K3s` (lines 71–80); mapped: `k3s/config.yaml`, `bootstrap/10-install-server.sh`, `bootstrap/11-install-server-join.sh`, `docs/ARCHITECTURE.md`.
- **Preflight Host Requirements** — `bootstrap/00-preflight.sh` → `agent` (lines 18–27); mapped: `bootstrap/00-preflight.sh`.
- **Bootstrap the First Server** — `bootstrap/10-install-server.sh` → `K3s` (lines 71–80); mapped: `bootstrap/10-install-server.sh`.
- **Join Additional Servers and Agents** — `bootstrap/20-install-agent.sh` → `agent` (lines 84–93); mapped: `bootstrap/11-install-server-join.sh`, `bootstrap/20-install-agent.sh`.
- **Handle Tokens and Secret Files** — `bootstrap/30-token-helper.sh` → `rotate` (lines 36–45); mapped: `bootstrap/30-token-helper.sh`, `.gitignore`.
- **Deploy the Edge Stateful Helm Chart** — `helm/edge-stateful/templates/networkpolicy.yaml` → `NetworkPolicy` (lines 25–34); mapped: `helm/edge-stateful`.
- **Understand Local-Path Storage Limits** — `helm/edge-stateful/Chart.yaml` → `application` (lines 1–8); mapped: `helm/edge-stateful`, `docs`.
- **Operate Health and etcd Backups** — `systemd/scripts/k3s-healthcheck.sh` → `healthcheck` (lines 11–20); mapped: `systemd/`.
- **Use the Offline Validation Gate** — `tools/validate.py` → `structure` (lines 180–189); mapped: `tools/validate.py`.
- **Roll Out, Roll Back, and Verify** — `manifests/hello-edge/rollout.yaml` → `kind` (lines 6–15); mapped: `manifests/hello-edge/rollout.yaml`, `bootstrap/40-verify-cluster.sh`.
- **Review NetworkPolicy and Failure Modes** — `manifests/networkpolicy.example.yaml` → `NetworkPolicy` (lines 24–33); mapped: `manifests/networkpolicy.example.yaml`, `docs/TROUBLESHOOTING.md`.
- **Uninstall and Restore Safely** — `bootstrap/99-uninstall.sh` → `snapshot` (lines 10–19); mapped: `bootstrap/99-uninstall.sh`, `README.md`.

## message-broker-backend-for-microservices

- **OTP Application and Supervision** — `src/mbb_sup.erl` → `mbb_sup` (lines 8–17); mapped: `src/mbb_sup.erl`, `src/message_broker_backend.app.src`.
- **Manage AMQP Connection and Reconnect** — `src/mbb_connection.erl` → `Connection` (lines 157–166); mapped: `src/mbb_connection.erl`.
- **Declare Exchanges, Queues, and Bindings** — `src/mbb_topology.erl` → `exchange` (lines 234–243); mapped: `src/mbb_topology.erl`, `rabbitmq/`.
- **Publish with Confirms and Idempotency** — `src/mbb_publisher.erl` → `idempotency` (lines 1–7); mapped: `src/mbb_publisher.erl`, `src/mbb_order.erl`.
- **Consume with Prefetch and Settlement** — `src/mbb_consumer.erl` → `dead_letter` (lines 231–240); mapped: `src/mbb_consumer.erl`.
- **Process and Classify Orders** — `src/mbb_order.erl` → `inventory` (lines 1–8); mapped: `src/mbb_order.erl`.
- **Retry Ladder and Dead-Letter Queue** — `src/mbb_consumer.erl` → `max_retries` (lines 11–20); mapped: `src/mbb_topology.erl`, `src/mbb_consumer.erl`, `rabbitmq/definitions.json`.
- **Expose Health, Readiness, and Metrics** — `src/mbb_http.erl` → `orders` (lines 100–109); mapped: `src/mbb_http.erl`, `src/mbb_metrics.erl`.
- **Run and Configure the Broker Stack** — `prometheus/prometheus.yml` → `configuration` (lines 1–5); mapped: `docker-compose.yml`, `rabbitmq/rabbitmq.conf`, `prometheus/prometheus.yml`.
- **Test Failure Paths and Duplication** — `test/mbb_metrics_tests.erl` → `metrics` (lines 1–8); mapped: `test/`.
- **Inspect Operational and Security Limits** — `src/mbb_order.erl` → `process` (lines 39–48); mapped: `src/mbb_order.erl`, `config/sys.config`, `README.md`.
- **Build a Safe Local Verification Plan** — `tools/check_erl.py` → `stack` (lines 111–120); mapped: `README.md`, `tools/check_erl.py`.

## metrics-monitoring-and-alerting-platform

- **Sample and Label Data Model** — `metrics.go` → `Sample` (lines 53–62); mapped: `metrics.go`.
- **Store and Select a Time Window** — `metrics.go` → `windowLocked` (lines 38–47); mapped: `metrics.go`.
- **Calculate Rate** — `metrics.go` → `rateLocked` (lines 69–78); mapped: `metrics.go`.
- **Calculate Sum and Average** — `metrics.go` → `windowLocked` (lines 38–47); mapped: `metrics.go`.
- **Evaluate Alert Rules** — `metrics.go` → `Evaluate` (lines 134–143); mapped: `metrics.go`.
- **Expose Prometheus Text** — `metrics.go` → `Prometheus` (lines 158–167); mapped: `metrics.go`.
- **Use JSON Ingest and Query API** — `metrics.go` → `QueryHandler` (lines 199–208); mapped: `metrics.go`, `main.go`.

## programmable-ci-cd-engine-with-dagger

- **Model Pipeline Steps and Dependencies** — `engine.go` → `Steps` (lines 35–44); mapped: `engine.go`.
- **Resolve the Dependency Graph** — `engine.go` → `Order` (lines 312–321); mapped: `engine.go`.
- **Build Correct Cache Digests** — `engine.go` → `digestOf` (lines 334–343); mapped: `engine.go`.
- **Use Memory and File Caches** — `engine.go` → `MemoryCache` (lines 242–251); mapped: `engine.go`.
- **Compare Host and Recording Executors** — `engine.go` → `RecordingExecutor` (lines 196–205); mapped: `engine.go`.
- **Run Steps with Retries and Timeouts** — `engine.go` → `runStep` (lines 360–369); mapped: `engine.go`.
- **Handle Environment and Secrets** — `engine.go` → `environment` (lines 26–35); mapped: `engine.go`, `engine_test.go`.
- **Read Pipeline Files and Reports** — `engine.go` → `PrintResults` (lines 433–442); mapped: `engine.go`, `main.go`.
- **Distinguish Dagger from This Engine** — `engine.go` → `Run` (lines 160–169); mapped: `engine.go`, `README.md`, `go.mod`.

## secrets-management-platform-with-ui

- **Threat Model and Secret Boundaries** — `src/server.js` → `startsWith` (lines 28–37); mapped: `src/server.js`, `README.md`.
- **Derive a Key from a Password** — `src/crypto.js` → `deriveKey` (lines 55–60); mapped: `src/crypto.js`.
- **Encrypt with AES-GCM** — `src/crypto.js` → `ciphertext` (lines 29–38); mapped: `src/crypto.js`.
- **Store Envelopes and Audit Records** — `src/store.js` → `SecretStore` (lines 82–87); mapped: `src/store.js`.
- **Use Set/Get/Delete Operations** — `src/store.js` → `get` (lines 48–57); mapped: `src/store.js`.
- **Authorize API Calls** — `src/server.js` → `token` (lines 28–37); mapped: `src/server.js`.
- **Review Defaults and HTTP Exposure** — `src/server.js` → `SECRETS_PASSWORD` (lines 80–89); mapped: `src/server.js`, `README.md`.
- **Test Crypto and API Behavior** — `test/crypto.test.js` → `test` (lines 2–11); mapped: `test/crypto.test.js`, `test/server.test.js`.
- **Plan Production Hardening** — `src/store.js` → `set` (lines 32–41); mapped: `README.md`, `src/store.js`.

## secure-container-registry-with-vulnerability-scanning

- **Model Packages, Layers, and Manifests** — `registry.go` → `Manifest` (lines 69–78); mapped: `registry.go`.
- **Compute Deterministic Digests** — `version.go` → `HashDigest` (lines 121–129); mapped: `registry.go`, `version.go`.
- **Push and Retrieve Registry Entries** — `registry.go` → `Get` (lines 69–78); mapped: `registry.go`.
- **Parse and Compare Versions** — `version.go` → `ParseVersion` (lines 18–27); mapped: `version.go`.
- **Represent Findings and Vulnerabilities** — `registry.go` → `DefaultScanner` (lines 98–107); mapped: `registry.go`.
- **Block on Policy Thresholds** — `registry.go` → `Blocked` (lines 137–146); mapped: `registry.go`, `main.go`.
- **Test Limits of the Scanner** — `registry.go` → `Scan` (lines 115–124); mapped: `registry_test.go`, `registry.go`, `README.md`.
- **Plan Real Registry Integration** — `registry.go` → `Registry` (lines 34–43); mapped: `registry.go`, `README.md`.

## self-hosted-git-platform-with-actions-runner

- **Git Object Types and Hashing** — `repository.go` → `hashOf` (lines 60–69); mapped: `repository.go`.
- **Build Commits and Branch Pointers** — `repository.go` → `CommitAs` (lines 79–88); mapped: `repository.go`.
- **Read History, Branches, and Diff** — `repository.go` → `CreateBranch` (lines 148–157); mapped: `repository.go`.
- **Save and Load Repository State** — `repository.go` → `Save` (lines 213–222); mapped: `repository.go`.
- **Parse Workflow Definitions** — `repository.go` → `ParseWorkflow` (lines 301–310); mapped: `repository.go`.
- **Resolve Jobs and Steps** — `repository.go` → `jobBlocked` (lines 522–531); mapped: `repository.go`.
- **Run Commands on the Host** — `repository.go` → `runStep` (lines 502–511); mapped: `repository.go`.
- **Handle Failures and Results** — `repository.go` → `Runner` (lines 468–477); mapped: `repository.go`.
- **Test Hashes and Workflow Semantics** — `repository_test.go` → `TestTheObjectHashIsTheGitHash` (lines 43–52); mapped: `repository_test.go`.
- **Security and Product Boundaries** — `main.go` → `main` (lines 17–26); mapped: `README.md`, `main.go`.

## tekton-kubernetes-pipeline-engine

- **Task, Step, and Pipeline Models** — `engine.go` → `PipelineTask` (lines 222–231); mapped: `engine.go`.
- **Resolve DAG Dependencies** — `engine.go` → `runAfter` (lines 106–115); mapped: `engine.go`.
- **Substitute Task Parameters** — `engine.go` → `Substitute` (lines 232–241); mapped: `engine.go`.
- **Execute Steps and Capture Results** — `engine.go` → `runStep` (lines 240–249); mapped: `engine.go`.
- **Share a Workspace and Read Results** — `engine.go` → `readResults` (lines 254–263); mapped: `engine.go`.
- **Handle Retries and Timeouts** — `engine.go` → `runStep` (lines 260–269); mapped: `engine.go`.
- **Run Finally Tasks** — `engine.go` → `Runner` (lines 314–323); mapped: `engine.go`.
- **Load Definitions from Directories** — `engine.go` → `LoadDefinitionSet` (lines 377–386); mapped: `engine.go`, `main.go`.
- **Compare the Local Runner with Tekton** — `engine.go` → `Execute` (lines 175–184); mapped: `README.md`, `engine.go`.
- **Test Execution and Security Limits** — `engine.go` → `CommandContext` (lines 287–296); mapped: `engine.go`, `engine_test.go`, `README.md`.

## uptime-and-status-monitoring-service

- **Monitor and Check Data Model** — `src/db.js` → `monitors` (lines 3–12); mapped: `src/db.js`.
- **Perform an HTTP Check** — `src/monitor.js` → `checkOnce` (lines 1–7); mapped: `src/monitor.js`.
- **Schedule Periodic Checks** — `src/monitor.js` → `setInterval` (lines 104–113); mapped: `src/monitor.js`, `src/server.js`.
- **Detect State Changes** — `src/monitor.js` → `previousStatus` (lines 119–125); mapped: `src/monitor.js`.
- **Send Notifications and Webhooks** — `src/monitor.js` → `notification` (lines 96–105); mapped: `src/monitor.js`.
- **Expose API and Static Status Page** — `src/server.js` → `servePublic` (lines 2–11); mapped: `src/server.js`, `src/static.js`, `public/`.
- **Understand SQLite Persistence** — `src/db.js` → `openDatabase` (lines 84–89); mapped: `src/db.js`.
- **Review Monitoring Scope and Tests** — `src/monitor.js` → `checkOnce` (lines 114–123); mapped: `src/monitor.js`, `test/`.

## web3-dapp-frontend-with-wallet-integration

- **Understand Injected Wallet Providers** — `public/app.js` → `eth_chainId` (lines 31–40); mapped: `public/app.js`, `src/server.js`.
- **Validate Address Shape and Checksum** — `src/ethereum.js` → `hasValidChecksum` (lines 72–81); mapped: `src/ethereum.js`, `src/keccak.js`.
- **Convert Human Units to Base Units** — `src/ethereum.js` → `BigInt` (lines 57–66); mapped: `src/ethereum.js`, `public/app.js`.
- **Understand Keccak-256 Implementation** — `src/keccak.js` → `BigInt` (lines 31–40); mapped: `src/keccak.js`.
- **Encode ERC20 Transfer Calldata** — `src/ethereum.js` → `TRANSFER_SELECTOR` (lines 1–9); mapped: `src/ethereum.js`, `public/app.js`.
- **Construct and Request a Wallet Transaction** — `public/app.js` → `account` (lines 55–64); mapped: `public/app.js`.
- **Inspect Errors and User Safety** — `public/app.js` → `receipt` (lines 57–66); mapped: `public/app.js`, `src/ethereum.js`.
- **Review Project Scope and Tests** — `src/ethereum.js` → `encodeTransfer` (lines 60–69); mapped: `src/ethereum.js`, `test/`, `README.md`.

## woodpecker-ci-pipeline-server

- **Pipeline and Build Models** — `server.go` → `Pipeline` (lines 118–127); mapped: `server.go`.
- **Parse the Pipeline Subset** — `server.go` → `ParsePipeline` (lines 81–90); mapped: `server.go`.
- **Trigger and Record a Build** — `server.go` → `Trigger` (lines 118–127); mapped: `server.go`, `main.go`.
- **Execute Steps with HostRunner** — `server.go` → `HostRunner` (lines 141–150); mapped: `server.go`.
- **Stop on Failure and Inspect Status** — `server.go` → `Server` (lines 165–174); mapped: `server.go`.
- **Serve the HTTP API and Console** — `server.go` → `ListHandler` (lines 227–236); mapped: `server.go`, `web/`.
- **Review Security and Product Scope** — `server.go` → `HostRunner` (lines 147–156); mapped: `server.go`, `README.md`.

