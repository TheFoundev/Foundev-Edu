#!/usr/bin/env python3
"""Generate advanced Cloud/DevOps learning packages from supplied source."""

from __future__ import annotations

import json
import re
import shutil
import zipfile
from datetime import datetime, timezone
from pathlib import Path

SOURCE = Path("/home/aziz/foundev/verified-projects-main/06-cloud-devops")
TARGET = Path("/home/aziz/foundev/Mini projects edu/Cloud & Devops")
LIBRARY = Path("/home/aziz/foundev/Foundev-main/Beginner projects modules and assessments/Cloud and Devops")


def mod(title, files, plain, fact, example=None):
    if example is None:
        example = fact
    return {"title": title, "files": files, "plain": plain, "fact": fact, "example": example}


def project(slug, title, description, problem, stack, features, data_flow, gaps, refs, deployment, modules):
    return {"slug": slug, "title": title, "description": description, "problem": problem, "stack": stack,
            "features": features, "data_flow": data_flow, "gaps": gaps, "refs": refs,
            "deployment": deployment, "modules": modules}


PROJECTS = [
    project("audited-escrow-and-tokenization-contracts", "Audited Escrow and Tokenization Contracts",
        "A Solidity suite composes an escrow state machine, ERC20 settlement, ERC721 provenance, access roles, royalties, and a factory.",
        "Reason about stateful value movement and role-controlled tokenized assets without treating a student project as audited production code.",
        ["Solidity 0.8.24", "Hardhat", "TypeScript", "ethers.js", "OpenZeppelin Contracts"],
        "Escrow states, partial funding, disputes/timeouts, pull-payment credits; TokenizedAsset roles/provenance/royalties; factory indexes; tests include a reentrancy attacker.",
        "Buyer/seller fund escrow → deadlines/state changes → settlement credits → parties withdraw. Factory creates/indexes instances; token contract tracks asset provenance and royalty balances.",
        ["The title says audited, but no independent audit report is supplied.", "Passing tests do not establish contract security.", "The .env key is a placeholder; use local/test networks only."],
        [("Solidity docs", "https://docs.soliditylang.org/en/latest/"), ("OpenZeppelin AccessControl", "https://docs.openzeppelin.com/contracts/5.x/access-control"), ("OpenZeppelin utilities", "https://docs.openzeppelin.com/contracts/5.x/api/utils"), ("Hardhat docs", "https://hardhat.org/docs")],
        "Use a local Hardhat node or test network; never use real funds or a production key for this exercise.",
        [
            mod("Roles and Contract Boundaries", "contracts/Escrow.sol; contracts/TokenizedAsset.sol", "A contract is a public rulebook that holds state and permits defined roles to act.", "Escrow distinguishes buyer, seller, and arbiter; TokenizedAsset uses AccessControl roles for minting/auditing and Pausable controls.", "onlyRole(MINTER_ROLE); onlyRole(AUDITOR_ROLE)"),
            mod("Escrow State Machine", "contracts/Escrow.sol", "A state machine is a set of checkpoints; each operation is allowed only at particular checkpoints.", "States: Created, Funded, Disputed, ArbiterDecided, Released, Refunded; invalid transitions revert with custom errors.", "enum State { Created, Funded, Disputed, ArbiterDecided, Released, Refunded }"),
            mod("Native and ERC20 Funding", "contracts/Escrow.sol", "Funding fills a target amount through contributions; partial deposits accumulate until the target is met.", "fund accepts ETH; fundERC20 uses SafeERC20; contributions cannot exceed remainingToFund and completion sets the deadline.", "fund(); fundERC20(contribution); remainingToFund()"),
            mod("Pull Payments and Settlement Credits", "contracts/Escrow.sol", "A pull payment records who may withdraw instead of sending money during each state transition.", "Settlement credits a beneficiary; withdraw transfers credited value under nonReentrant and checks-effects-interactions.", "_settle(...) → _credit(...) → withdraw()"),
            mod("Deadlines and Timeout Paths", "contracts/Escrow.sol", "A deadline is a timer attached to a promise; timeout paths resolve a deal when a party stays silent.", "timeoutRelease and timeoutRefund are separate; refund, cancel, and release each have caller/state requirements.", "timeoutRelease(); timeoutRefund(); cancel()"),
            mod("Dispute and Arbiter Lifecycle", "contracts/Escrow.sol", "A dispute pauses the ordinary path while the assigned arbiter records a ruling.", "raiseDispute opens a window; arbiterRule records a choice; executeRuling applies it; timeoutRefund handles expiry.", "raiseDispute(reason) → arbiterRule(bool) → executeRuling()"),
            mod("ERC721 Provenance and Roles", "contracts/TokenizedAsset.sol", "An NFT token ID is a unique item; provenance records who created or audited it.", "TokenizedAsset extends ERC721, AccessControl, Pausable, ReentrancyGuard; mint stores provenance and recordAudit is role-gated.", "mint(...); recordAudit(tokenId, passed); provenance(tokenId)"),
            mod("Royalty Pool Accounting", "contracts/TokenizedAsset.sol", "A royalty pool is a balance ledger: payments accumulate and an eligible creator later claims the amount.", "payRoyalty transfers configured ERC20 into a token-specific pool; claimRoyalties checks original creator and transfers the claim.", "payRoyalty(tokenId, tokenAmount); claimRoyalties(tokenId)"),
            mod("Factory Creation and Indexing", "contracts/EscrowFactory.sol", "A factory is a deployment desk that creates instances and keeps a searchable catalog.", "createEscrow deploys and indexes instances; escrowAt/getEscrows support lookup and pagination; buyer/seller queries exist.", "createEscrow(...); escrowAt(i); getEscrows(offset, limit)"),
            mod("Events, Errors, and External Calls", "contracts/Escrow.sol; contracts/TokenizedAsset.sol", "Events are receipts for off-chain tools; custom errors make failed operations more specific.", "Contracts emit funding, dispute, settlement, credit, withdrawal, mint, audit, and royalty events and define typed errors.", "emit ContributionReceived(...); error InvalidState(...)"),
            mod("Test Fixtures and Security Tests", "contracts/test/ReentrancyAttacker.sol; test/escrow.spec.ts", "A test attacker calls back during a transfer to test whether a withdrawal can be repeated.", "Hardhat tests cover state transitions, timeouts, ERC20, reentrancy, token roles/pausing/royalties, and factory indexing.", "npm test; test/escrow.spec.ts"),
            mod("Deploy and Audit Limits", "scripts/deploy.ts; hardhat.config.ts; README.md", "A deploy script connects code to a chain; a test report is evidence for tested cases, not a security certification.", "README reports local compile/tests, uses a zero-filled placeholder PRIVATE_KEY, and supplies no independent audit report.", "npm run compile; npx hardhat node; deploy only locally/testnet"),
        ]),
    project("auto-configuring-reverse-proxy-with-service-discovery", "Auto-Configuring Reverse Proxy with Service Discovery",
        "A Go reverse proxy parses a small config, selects healthy backends, and can discover labeled Docker containers.",
        "Understand a service registry, routing, round robin, and the privilege boundary around Docker daemon access.",
        ["Go", "net/http", "httputil", "Docker Engine API"],
        "Line parser, manual health flags, round robin, reverse proxy, Docker list-containers request, label discovery, health route.",
        "Config/Docker API → service registry → healthy backend selection → prefix rewrite → proxy request.",
        ["Parser is a small line parser, not YAML.", "Health is manually marked; there is no active probe loop.", "Docker socket access is powerful and should not be exposed to untrusted users.", "TLS certificate management is absent."],
        [("Go net/http", "https://pkg.go.dev/net/http"), ("Go reverse proxy", "https://pkg.go.dev/net/http/httputil#NewSingleHostReverseProxy"), ("Docker Engine API", "https://docs.docker.com/reference/api/engine/"), ("Docker security", "https://docs.docker.com/engine/security/")],
        "Use test backends locally. Do not expose the Docker socket or Docker TCP API publicly.",
        [
            mod("Service and Instance Models", "proxy.go", "A service is a named doorway with several backend rooms; an instance stores URL and health.", "Service groups instances; Registry holds service map/order guarded by an RWMutex.", "type Service { Name; Instances []*Instance }"),
            mod("Parse the Small Config Format", "proxy.go", "This parser recognizes a few line patterns, like a short checklist rather than general YAML.", "ParseConfig handles services:, - name:, and - http/https lines; rejects instance-before-service and no services.", "strings.HasPrefix(trimmed, \"- name:\")"),
            mod("Health Flags and Round Robin", "proxy.go", "Round robin takes turns among eligible backends and skips those marked unhealthy.", "Mark manually updates Healthy; Pick advances a counter then scans up to all instances; no background health checker exists.", "Pick(service)"),
            mod("Reverse Proxy Path Flow", "proxy.go", "A reverse proxy forwards a request while a client uses one stable address.", "ServeHTTP parses /service/path, selects an instance, removes the prefix, and forwards with NewSingleHostReverseProxy.", "request.URL.Path = \"/\" + strings.Join(parts[1:], \"/\")"),
            mod("Docker Label Discovery", "proxy.go", "The Docker daemon is a host-level control API; discovery asks for containers and uses agreed labels.", "ListContainers calls /containers/json over a Unix socket; discovery reads foundev.service/port/host and filters non-running containers.", "foundev.service; foundev.port; foundev.host"),
            mod("Docker Socket Trust Boundary", "proxy.go; README.md", "Giving a server the Docker socket is like giving it powerful control over the host.", "NewDockerClient defaults to /var/run/docker.sock; the source has no auth around a web-exposed proxy.", "DialContext(..., \"unix\", socket)"),
            mod("Test Routing and Failure Responses", "proxy_test.go", "A temporary test server is a controlled backend that reveals what path the proxy forwards.", "Tests cover config, round robin, manual health, proxy path, /health, unknown service, parser errors, and absent socket.", "httptest.NewServer(...)"),
            mod("Limits of Discovery and Health", "README.md; proxy.go", "Finding an endpoint does not prove that it is ready or safe to receive traffic.", "Discovery runs when called; health is manually marked; no probe loop or TLS manager is implemented.", "Mark(service, instance, healthy) is manual"),
        ]),
    project("chaos-engineering-experiment-platform", "Chaos Engineering Experiment Platform",
        "A Go experiment runner validates actions, applies a fault executor, evaluates hypotheses, records a timeline, and stores results.",
        "Design safe experiments with explicit steady-state hypotheses, controlled actions, recovery, rollback, and evidence.",
        ["Go", "context", "FaultExecutor", "MetricReader"],
        "Validation, dry-run/local executors, static metric reader, pre/post checks, event timeline, rollback, memory/file stores.",
        "Validate → baseline check → apply → wait/recover → verify → persist or abort.",
        ["Local executor may SIGTERM a host process and consume CPU; only use a disposable target.", "Local delay sleeps in Apply and Runner, doubling configured delay.", "Recover is a no-op; killed processes are not restarted.", "Stress magnitude does not scale worker count; static metrics are not Prometheus.", "No Kubernetes/Chaos Mesh API or scheduler is present."],
        [("Chaos Engineering principles", "https://principlesofchaos.org/"), ("Go context", "https://pkg.go.dev/context"), ("Go process signals", "https://pkg.go.dev/os/signal")],
        "DryRunExecutor is the safe default. Do not run local kill/stress against shared or production machines.",
        [
            mod("Experiment and Action Models", "chaos.go", "An experiment is a recipe: a name, optional guardrail hypothesis, and ordered actions.", "Experiment contains namespace/hypothesis/actions; Action has kind, target, duration, magnitude.", "type Experiment struct { Name; Namespace; Hypothesis; Actions }"),
            mod("Validate Actions and Hypotheses", "chaos.go", "Validation checks a plan before it can affect a target.", "Validate allows delay/kill/stress and nonempty targets; hypothesis operators are lt/gt/eq.", "Compare(op, value, threshold)"),
            mod("Executor Interface and Dry Run", "chaos.go", "An executor is a swappable tool for applying and recovering faults; dry-run changes nothing.", "FaultExecutor requires Apply, Recover, Name; nil executor defaults to DryRunExecutor.", "type FaultExecutor interface { Apply; Recover; Name }"),
            mod("Local Fault Effects and Safety", "chaos.go", "Local experiments affect the machine running them unless isolated.", "Local delay sleeps, stress starts busy goroutines, and kill sends SIGTERM to a parsed PID; Recover is empty.", "killProcess(target); LocalExecutor.Recover(...)"),
            mod("Check Steady-State Hypotheses", "chaos.go", "A hypothesis is a guardrail, such as latency staying under a threshold before and after a fault.", "Runner reads MetricReader before actions and after recovery, records checks, and aborts when a check fails.", "checkSteadyState(ctx, experiment, phase)"),
            mod("Runner Timeline and Rollback", "chaos.go", "The runner coordinates events and rollback, similar to an experiment log plus safety controller.", "Run validates, checks baseline, applies actions, waits, recovers, records events, and rolls back actions still marked applied.", "Runner.Run(ctx, experiment)"),
            mod("Store Experiment Results", "chaos.go", "A Store is an interchangeable place to save completed experiment reports.", "MemoryStore keeps results in process; FileStore serializes results to JSON.", "Store.Save(result); Store.List()"),
            mod("Tests and Deterministic Time", "chaos_test.go; chaos.go", "A fake clock lets tests advance time without waiting in real time.", "Tests use fakeClock/recordingExecutor and exercise rollback, failed hypothesis, dry run, and local wait.", "Now and Sleep are injectable"),
            mod("Audit Local Executor Semantics", "chaos.go", "A configured duration should correspond to the observed impact; trace every layer that waits.", "Local delay waits once in Apply and again in Runner; stress magnitude is ignored; kill has no recovery action.", "Runner.sleep(action.Duration) after executor.Apply"),
            mod("Plan Safe Fault Experiments", "README.md; chaos.go", "A hypothesis-first experiment has a measurable healthy baseline, a bounded fault, and an explicit stop/recovery plan.", "Dry run is default; local executor is a host-side demo; scheduler and real infrastructure executor are absent.", "Do not run local kill/stress on shared systems."),
        ]),
    project("cloud-cost-monitoring-dashboard-for-iac", "Cloud Cost Monitoring Dashboard for IaC",
        "A Go command-line/API tool reads a subset of Terraform plan JSON and estimates selected resource costs from hard-coded price tables.",
        "Understand the difference between parsing a plan, applying a simplified price model, and producing a trustworthy cloud bill.",
        ["Go", "Terraform plan JSON", "HTTP JSON"],
        "Plan parser, resource/provider classifier, price tables, per-resource estimates, totals by type/provider, unpriced list, JSON handler.",
        "terraform show JSON → planned_values resources → simplified local estimates → aggregate summary → stdout or a precomputed JSON endpoint.",
        ["ParsePlan traverses root resources and only one child_modules level, not arbitrary nested modules.", "Prices are hard-coded and incomplete; no live cloud pricing or billing data is consulted.", "count=0 defaults to one; database estimate ignores count; S3 storage_gb is a simplified input.", "The HTTP endpoint serves a precomputed summary, not a plan upload/dashboard."],
        [("Terraform JSON format", "https://developer.hashicorp.com/terraform/internals/json-format"), ("Terraform plan", "https://developer.hashicorp.com/terraform/cli/commands/plan"), ("Go encoding/json", "https://pkg.go.dev/encoding/json")],
        "Use synthetic plan JSON. Never treat estimates as an invoice or current cloud pricing; review provider pricing separately.",
        [
            mod("Plans and Planned Values", "main.go; cost.go", "A plan is Terraform's proposed infrastructure outcome; this program reads JSON, it does not run Terraform or create resources.", "main.go uses embedded examplePlan unless -plan is provided; ParsePlan reads planned_values.root_module."),
            mod("Decode Resource Values", "cost.go", "JSON fields arrive as generic maps; the parser extracts type/name/values into Resource records.", "ParsePlan type-asserts root/module resources and stringValue/numberValue convert selected fields."),
            mod("Traverse Modules and Nested Data", "cost.go", "Terraform modules form a tree; collecting one child is not the same as recursively walking descendants.", "childModules reads root child_modules; ParsePlan appends each immediate child's resources but does not recurse."),
            mod("Classify Providers and Resource Types", "cost.go", "Resource type prefixes act like labels that group resources by provider.", "providerOf splits the resource type at the first underscore and returns other when absent."),
            mod("Use the Hard-Coded Price Catalog", "cost.go", "A local rate card is an approximation; prices vary by region, usage, storage, and time.", "instancePrices, googleComputePrices, databasePrices contain fixed sample monthly values."),
            mod("Calculate Estimates and Unknowns", "cost.go", "Every supported resource has a formula; an unpriced resource is reported so a nonzero cost is not mistaken for free.", "EstimateResource handles a few AWS/GCP types; zero monthly estimates are appended to Unpriced."),
            mod("Aggregate and Expose JSON", "cost.go; api.go; main.go", "The program can print one summary or serve a precomputed JSON value; it does not provide a browser dashboard.", "Handler(summary) encodes Summary; main loads plan before ListenAndServe."),
        ]),
    project("cron-dead-man-switch-monitoring", "Cron Dead-Man-Switch Monitoring",
        "A Django heartbeat monitor tracks scheduled jobs, late/down transitions, status endpoints, and alert dispatch.",
        "Understand heartbeat monitoring, simplified schedule parsing, state transitions, authentication, polling, persistence, and notification delivery.",
        ["Python", "Django", "SQLite/PostgreSQL", "HTTP webhooks", "Docker Compose"],
        "Check/Ping/AlertChannel/Alert models, cron-like parser, ping/status and CRUD APIs, token checks, background poller, alert channels.",
        "Scheduled job pings → database/state update → poller evaluates deadline → transition to late/down/up → deduplicated alerts → API/UI status.",
        ["The schedule parser supports a simplified format, not full cron grammar.", "The separate poller must run to detect missed pings; the web process alone is not the scheduler.", "UUID ping URLs are bearer-like secrets; anyone who learns one can spoof a heartbeat.", "Webhook/email delivery and retry guarantees must be checked in core/dispatch.py.", "Production authentication, rate limits, and database operations require operational review."],
        [("Django models", "https://docs.djangoproject.com/en/stable/topics/db/models/"), ("Django management commands", "https://docs.djangoproject.com/en/stable/howto/custom-management-commands/"), ("Django security", "https://docs.djangoproject.com/en/stable/topics/security/"), ("crontab format", "https://man7.org/linux/man-pages/man5/crontab.5.html")],
        "Use a local database and test webhook. Protect ping URLs/tokens; do not launch public monitors without reviewing auth and rate limits.",
        [
            mod("Model Checks, Pings, and Alerts", "core/models.py", "A Check is a monitored job; Ping records a heartbeat; AlertChannel describes destinations and Alert stores sent events.", "Check includes schedule/grace/timeout/status fields; Ping/Alert reference the check."),
            mod("Parse Schedules and Calculate Deadlines", "core/state.py", "A schedule predicts when a job should report next; grace and timeout provide two different late/down boundaries.", "parse_cron/next_occurrence implement a limited grammar; compute_next_scheduled_at and check_deadline_exceeded use the stored schedule."),
            mod("Reason About State Transitions", "core/state.py", "A dead-man switch changes status when expected check-ins do not arrive and returns to healthy on recovery.", "transition_check, should_alert_on_transition, and deadline checks implement new/up/late/down transitions."),
            mod("Receive Heartbeats and Return Status", "core/api.py", "A ping is a request that says a scheduled task ran; a secret UUID in its path identifies the check.", "check_ping handles GET/HEAD/POST; check_status returns the current status JSON."),
            mod("Authenticate Management APIs", "core/api.py", "Read/write management credentials protect CRUD endpoints; the ping UUID is a separate capability.", "authenticate_write_token accepts Bearer or X-API-Token; check_ping is designed for unauthenticated secret URLs."),
            mod("CRUD and Summary Endpoints", "core/api.py", "Management endpoints create, list, update, and delete checks; summary/session endpoints expose reporting data.", "checks_list_create, check_detail, summary, and session are separate view functions."),
            mod("Poller and Alert Dispatch", "core/management/commands/run_poller.py; core/dispatch.py", "A poller is a separate process that periodically evaluates schedules; missed jobs are not found unless it runs.", "run_poller evaluates due checks; dispatch_alert handles configured email/webhook/log channels."),
            mod("Database and Environment Configuration", "config/settings.py; docker-compose.yml", "Local SQLite and configured PostgreSQL are alternative backing stores; compose separates web, poller, and database roles.", "DATABASE_URL, SECRET_KEY, DEBUG, ALLOWED_HOSTS, EMAIL_*, BASE_URL configure deployment."),
            mod("Webhook Reliability and Alert Deduplication", "core/dispatch.py; core/models.py", "Alerts should avoid repeated notifications for the same transition; webhook retry behavior is in the dispatcher, not implied by the model.", "Alert history and channel dispatch are implemented in core/dispatch.py; verify retry and mute semantics before relying on them."),
            mod("Threat Model and Test Boundaries", "core/tests; README.md", "A UUID ping endpoint is convenient for cron but must be protected like a password; tests cannot establish production availability.", "Tests cover parser/state/API/dispatch cases; no public deployment or load test is implied."),
        ]),
    project("decentralized-storage-dapp-on-ipfs", "Decentralized Storage dApp on IPFS",
        "A Node.js project computes raw CIDv1 identifiers and stores bytes in a local content-addressed directory behind an HTTP API.",
        "Distinguish content identifiers and local integrity from IPFS peer discovery, replication, pinning, and UnixFS DAG storage.",
        ["Node.js", "CIDv1", "Multihash", "Local filesystem", "HTTP"],
        "CID/base32 helpers, local store, API server, optional client, static page, and Node tests.",
        "Bytes → SHA-256 multihash + raw codec + CIDv1 + base32 → local file keyed by CID → retrieve and verify.",
        ["README states no IPFS daemon/network is used; storage is local and not replicated/announced.", "Only raw codec/single-block behavior is modeled; real IPFS UnixFS chunking/DAGs can produce different CIDs.", "A CID is generally not the same as a simple whole-file hash.", "No pinning, quotas, or garbage collection."],
        [("IPFS content addressing", "https://docs.ipfs.tech/concepts/content-addressing/"), ("IPFS glossary", "https://docs.ipfs.tech/concepts/glossary/"), ("Node crypto", "https://nodejs.org/api/crypto.html"), ("Node HTTP", "https://nodejs.org/api/http.html")],
        "Use nonsensitive local test content. Do not imply public network upload or deletion; this project stores data locally.",
        [
            mod("Content Addressing in Plain Terms", "src/cid.js; README.md", "A CID is a content-derived label; it says what content is addressed, not where a copy is currently stored.", "cidFromBytes hashes input bytes and assembles a CIDv1 raw-codec value; local addressing does not provide network replication.", "cidFromBytes(content)"),
            mod("Hash Bytes and Build Multihash", "src/cid.js", "The source hashes content using SHA-256 and adds multihash code/length metadata.", "SHA256_MULTIHASH=0x12; MULTIHASH_LENGTH=32."),
            mod("Assemble CIDv1 and Raw Codec", "src/cid.js", "CIDv1 combines a version, codec, multihash, and base encoding; this prototype uses raw codec 0x55.", "CID_VERSION=1; RAW_CODEC=0x55; cidFromBytes(content)."),
            mod("Encode and Decode Base32", "src/cid.js", "Base32 converts binary CID bytes to text; decoding reverses the alphabet/bit grouping.", "base32encode/base32decode use lowercase RFC-style alphabet symbols."),
            mod("Store and Verify Local Content", "src/store.js", "The local store writes bytes under a content-derived identifier and checks identity when retrieving.", "createStore creates directory-backed operations; this is not a distributed IPFS node."),
            mod("HTTP Server and Client Flow", "src/server.js; src/ipfs.js", "The local HTTP API accepts bytes and returns a CID; IpfsClient names the helper but uses the project's HTTP endpoint.", "createIpfsServer injects a store; DEFAULT_API is localhost:5001."),
            mod("Serve the Browser UI", "src/static.js; public/app.js", "A static handler serves files from public while the browser calls local API routes.", "servePublic maps static files/content types from PUBLIC_DIR."),
            mod("Tests and Real-IPFS Limits", "test/ipfs.test.js; src/ipfs.js; README.md", "Tests cover the local client and content APIs, not integration with an IPFS peer network.", "The client only calls a configured node URL; the included app does not provide an IPFS daemon, pinning service, replication, or garbage collection.", "DEFAULT_API = \"http://127.0.0.1:5001\""),
        ]),
    project("distributed-rate-limiter-service", "Distributed Rate Limiter Service",
        "A Go service includes a memory token bucket, Redis fixed-window store, HTTP middleware, trusted-proxy option, and Prometheus text output.",
        "Compare rate-limiting algorithms, shared storage, client identity, failure policy, and observability.",
        ["Go", "HTTP middleware", "Redis RESP subset", "Prometheus text"],
        "Memory token buckets, Redis INCR/PEXPIRE store, key selection, HTTP 429/header middleware, stats exporter, health endpoint.",
        "Request → choose API-key/IP key → Store.Take → allow or 429 → update headers/metrics.",
        ["MemoryStore uses token-bucket refill; RedisStore is a fixed-window INCR/PEXPIRE counter, so the storage backends do not implement identical algorithms.", "RedisStore ignores rate during Take; Sweep is a no-op because Redis TTL handles expiry.", "Store errors fail open in Limiter.AllowAt.", "Stats exposes allowed/blocked counters only for MemoryStore; Redis metrics are missing/zero.", "X-Forwarded-For trust is a global boolean, not a trusted-proxy CIDR list."],
        [("Go net/http", "https://pkg.go.dev/net/http"), ("Redis RESP protocol", "https://redis.io/docs/latest/develop/reference/protocol-spec/"), ("Prometheus exposition", "https://prometheus.io/docs/instrumenting/exposition_formats/"), ("OWASP API Security", "https://owasp.org/www-project-api-security/")],
        "Run locally. Decide whether store outages should fail open or closed before using a limiter for abuse protection.",
        [
            mod("Token Bucket in Plain Terms", "limiter.go; store.go", "A token bucket is a cup that refills at a steady rate; requests spend tokens and burst sets the cup size.", "MemoryStore stores floating tokens and last time, refilling elapsed seconds × rate up to burst."),
            mod("Memory Store Synchronization", "store.go", "A mutex protects shared in-memory bucket counters from simultaneous request handlers.", "Take, Remaining, Sweep, and Counters lock MemoryStore.mu."),
            mod("HTTP Middleware and Rate Headers", "limiter.go; main.go", "Middleware lets allowed requests continue and returns 429 for blocked requests.", "Blocked path sets Retry-After, X-RateLimit-Limit, and X-RateLimit-Remaining."),
            mod("Choose a Request Identity Key", "limiter.go", "A limiter needs a key to decide which requests share a bucket; trusting proxy headers changes who can choose that key.", "KeyFor prefers X-API-Key, then RemoteAddr; first X-Forwarded-For is used only when TrustedProxies is true."),
            mod("Contrast Redis Fixed Window", "store.go", "A fixed window counts requests until a TTL expires; it does not smoothly refill fractional tokens.", "RedisStore increments a key and sets PEXPIRE on count==1; Take compares count to burst and does not use rate."),
            mod("Read the RESP Client", "store.go", "RESP is Redis's length-prefixed command/reply protocol; this project implements only a small subset.", "respClient writes arrays/bulk strings and parses simple, error, integer, and bulk replies."),
            mod("Plan for Store Failure", "limiter.go", "Fail-open means a request is permitted if the store errors; that preserves availability but removes rate protection during the outage.", "AllowAt returns true on Store.Take error; Remaining returns zero on error."),
            mod("Metrics and Expiration", "limiter.go; store.go; main.go", "Metrics are an operational view, and they must reflect the backend actually in use.", "Stats reads Counters only from MemoryStore; RedisStore Sweep returns 0 and relies on key TTL."),
            mod("Tests, Concurrency, and Algorithm Limits", "limiter_test.go; README.md", "Tests should separately check refills, concurrent access, proxy trust, fixed-window boundaries, and store errors.", "TestTheLimiterIsSafeUnderLoad exercises concurrent requests against the in-memory limiter; Redis semantics differ.", "TestTheLimiterIsSafeUnderLoad"),
        ]),
    project("distributed-tracing-and-apm-platform", "Distributed Tracing and APM Platform",
        "A Go in-memory span store groups traces, computes duration/error summaries and service latency percentiles, and exposes JSON handlers.",
        "Understand span relationships and aggregation while distinguishing a custom tracing demo from an interoperable OpenTelemetry backend.",
        ["Go", "net/http", "JSON", "in-memory store"],
        "Span model/store, trace assembly, p50/p95, custom JSON ingestion, stats and trace lookup handlers.",
        "JSON spans → append to memory → group by TraceID → derive root/errors/duration → group by service → calculate percentiles.",
        ["No persistence, sampling, context propagation, or OpenTelemetry SDK/exporter.", "OTLPHandler expects a custom JSON structure and is not mounted in main.go; it is not OTLP JSON/Protobuf compatible.", "Percentile uses floor(p/100*(n-1)) and does not validate p bounds.", "StatsHandler and TraceHandler write JSON without consistent content-type/status helpers."],
        [("OpenTelemetry OTLP specification", "https://opentelemetry.io/docs/specs/otlp/"), ("Go net/http", "https://pkg.go.dev/net/http"), ("Prometheus exposition format", "https://prometheus.io/docs/instrumenting/exposition_formats/")],
        "Treat as an in-memory educational model, not an OTLP receiver or production APM service.",
        [
            mod("Span and Trace Vocabulary", "tracing.go", "A span is one timed operation; a trace groups related spans and parent IDs describe nesting.", "Span carries trace/span/parent IDs, service, operation, start, duration, and status."),
            mod("Store and Concurrency", "tracing.go", "The Store is a shared in-memory notebook; a mutex protects append and copy operations.", "Store.Add locks for append; all returns a copied slice under RLock.", "store.Add(spans...)"),
            mod("Assemble Trace Duration and Root", "tracing.go", "Trace duration spans from the earliest start to latest span end; a root span has no ParentID.", "Traces groups by TraceID and counts status == error."),
            mod("Calculate Latency Percentiles", "tracing.go", "A percentile selects a position from sorted observations; this implementation uses a floor-based nearest-lower index.", "Percentile selects a sorted-value index; Stats converts durations to milliseconds.", "Percentile(values, 95)"),
            mod("Ingest Custom Span JSON", "tracing.go; main.go", "IngestHandler decodes an array of project Span structs; this is custom JSON, not automatically an OTLP payload.", "main mounts /spans to IngestHandler."),
            mod("Audit the OTLP-Labeled Handler", "tracing.go; tracing_test.go; main.go", "Official OTLP JSON uses fields such as traceId/spanId and timeUnixNano; this handler decodes Go field names/fields and is not wired to a route.", "OTLPHandler expects resourceSpans/scopeSpans/spans containing Span-shaped JSON."),
            mod("Query Stats and Trace IDs", "tracing.go; main.go", "Stats groups spans by service; TraceHandler searches assembled trace IDs under /traces/.", "Main registers /stats and /traces/ only when -listen is supplied."),
            mod("Limits and Verification", "tracing.go; tracing_test.go; main.go; README.md", "Unit tests cover the in-memory model and custom handler, not interoperability with an OpenTelemetry Collector.", "OTLPHandler is a local custom handler; the store is memory-backed and main does not mount an official OTLP receiver/exporter.", "func (store *Store) OTLPHandler"),
        ]),
    project("encrypted-configuration-management-in-git", "Encrypted Configuration Management in Git",
        "secretsync is a Python CLI that orchestrates SOPS/age, environment policy, tracked-file scanning, and a hash-chained audit log.",
        "Understand encrypted configuration workflows, key recipients, CI-only decryption policy, audit integrity, rotation, and their trust boundaries.",
        ["Python", "SOPS", "age", "Git", "CI", "optional Ansible"],
        "Config loader/YAML subset, real SOPS/age subprocess wrappers, encrypt/decrypt/rotate CLI, CI policy checks, plaintext scanner, audit chain/checkpoint, Git hooks and CI examples.",
        "Plain config → SOPS encrypt to age recipients → encrypted file committed → CI identity decrypts → audit records and precommit/CI checks verify hygiene.",
        ["SOPS upstream repository is archived; check maintained releases/forks and current binary provenance.", "Decrypt policy is a guard inside this CLI, not an OS sandbox; CI identity can decrypt its authorized environment.", "Audit hash chain is tamper-evident, not tamper-proof; an attacker able to rewrite records and checkpoint can rewrite history.", "Plaintext scanner is pattern-based and can miss secrets; encrypted sample data and local identities must be handled carefully.", "README says Ansible optional; it is not equivalent to external secret management."],
        [("SOPS project repository", "https://github.com/age-sops/sops"), ("age encryption", "https://age-encryption.org/"), ("Git hooks", "https://git-scm.com/book/en/v2/Customizing-Git-Git-Hooks"), ("GitHub Actions secrets", "https://docs.github.com/en/actions/security-for-github-actions/security-guides/using-secrets-in-github-actions")],
        "Use throwaway keys and sample secrets. Never put real secrets in a teaching repository; CI decrypt access must be least-privilege and environment-scoped.",
        [
            mod("Threat Model and Secret Lifecycle", "secretsync/policy.py; README.md", "Ciphertext may be committed, but whoever has an authorized identity can decrypt it; the CI runner is part of the trust boundary.", "authorize_decrypt checks CI identity and marker policy; the README distinguishes stolen clones, compromised CI, shared recipients, and scanner misses.", "authorize_decrypt(context)"),
            mod("Load Environment and Recipient Config", "secretsync/config.py; .sops.yaml", "Configuration maps environments to recipients and policies; parsing/validation decides which keys and files belong to each environment.", "load_config builds EnvKeys, CreationRule, and DecryptPolicy; recipients are validated."),
            mod("Read the Mini-YAML Subset", "secretsync/miniyaml.py", "A small parser supports the project's needed YAML subset, not every YAML feature or the complete SOPS configuration language.", "loads tokenizes/indents and parses scalars, flow lists/maps, sequences, and mappings."),
            mod("Find and Invoke SOPS/Age Tools", "secretsync/sopsbin.py; scripts/fetch_tools.sh", "The wrapper locates external binaries and passes file content and recipient/key settings to them.", "find_tool checks environment/config/path/.tools; sops_encrypt/decrypt call subprocess helpers."),
            mod("Encrypt Files for Recipients", "secretsync/cli.py; secretsync/sopsbin.py", "Encryption converts plaintext into a SOPS document for configured public recipients; public recipient keys are not decryption secrets.", "cmd_encrypt checks configured file/recipients and records an audit action."),
            mod("Authorize CI Decryption", "secretsync/policy.py; secretsync/cli.py", "Decrypt authorization checks CI indicators, run markers, and local-deny policy; this is application policy, not isolation from a compromised runner.", "detect_ci, check_marker, authorize_decrypt determine allow/deny."),
            mod("Rotate Recipients with a Grace Period", "secretsync/cli.py; secretsync/config.py", "Rotation adds new readers while previous recipients remain until the grace-period drop step.", "rotate_env re-encrypts and updates previous_recipients; --drop-previous removes old recipients."),
            mod("Build the Hash-Chained Audit Log", "secretsync/audit.py", "Each audit record hashes a canonical form and links to the prior digest; a separate head checkpoint helps detect tail truncation.", "AuditLog appends JSONL; verify checks chain and head."),
            mod("Scan Tracked Files for Plaintext", "secretsync/plaintext.py; secretsync/check.py", "The scanner applies secret-shaped patterns and exclusions to tracked files; pattern scanning cannot identify every possible secret.", "scan_paths uses configured patterns/globs; run_check combines coverage, ciphertext, audit, and plaintext findings."),
            mod("Use the Pre-Commit and CI Gates", ".githooks/pre-commit; .github/workflows/ci.yml", "Hooks run locally only when installed/configured; CI provides another check but is not a replacement for reviewing trust and permissions.", "README directs git config core.hooksPath .githooks; CI runs tests and example automation."),
            mod("Use the Ansible Example Carefully", "ansible/playbook.yml; ansible/lookup_plugins/secretsync.py", "The playbook/lookup demonstrates automation integration; it adds another execution environment that must receive secrets and identity carefully.", "The project README describes Ansible as an example integration, not required core runtime."),
            mod("Verify and State the Security Limits", "tests/; secretsync/audit.py; secretsync/plaintext.py; README.md", "Tests cover internal policy and tooling paths; they do not prove that every secret is detected or that an entire CI runner is safe.", "AuditLog.verify checks a local hash chain and plaintext scanning uses configured patterns; neither detects every compromise or plaintext secret.", "AuditLog.verify"),
        ]),
    project("encrypted-deduplicated-backup-system", "Encrypted Deduplicated Backup System",
        "A Go prototype chunks data, deduplicates by content hash, encrypts chunks, writes a manifest, and restores files locally.",
        "Understand content-defined chunking, deduplication, key derivation, authenticated encryption, and restore integrity.",
        ["Go", "SHA-256", "PBKDF2-style key derivation", "AES-GCM", "Filesystem"],
        "Content-defined boundaries, chunk hashes, per-chunk encryption, repository manifest, restore path, unit tests.",
        "Input bytes → rolling-hash chunks → chunk ID → encrypted chunk file → manifest → decrypt and concatenate on restore.",
        ["The repository is local; no object-store transport, scheduling, snapshot history, prune, or replication exists.", "Homegrown PBKDF2 and chunking must be reviewed carefully before production use.", "Chunks are stored as separate files, not pack files; backup names/manifest semantics matter.", "A key/secret loss can make encrypted backups unrecoverable."],
        [("Go crypto/aes", "https://pkg.go.dev/crypto/aes"), ("Go crypto/cipher", "https://pkg.go.dev/crypto/cipher"), ("NIST SP 800-38D GCM", "https://csrc.nist.gov/pubs/sp/800/38/d/final"), ("Go crypto/hmac", "https://pkg.go.dev/crypto/hmac")],
        "Use disposable test data only. Do not trust a backup until a restore drill verifies bytes and keys.",
        [
            mod("Chunk and Manifest Model", "repository.go", "A manifest is a recipe that lists encrypted chunk IDs needed to reconstruct a named file.", "ChunkInfo/PutResult/Repository describe chunk metadata and stored content."),
            mod("Password, Salt, and Key Derivation", "repository.go", "A salt makes the derived key unique per repository; a KDF turns a password into key bytes.", "NewSalt, deriveKey, and pbkdf2Key derive a 32-byte key."),
            mod("Content-Defined Chunk Boundaries", "repository.go", "Content-defined chunking chooses boundaries from data content so edits can preserve later chunks better than fixed-size blocks.", "ContentDefined uses rolling hash with min/average/max boundaries."),
            mod("Hash IDs and Deduplication", "repository.go", "A chunk hash acts as a lookup key; identical chunk bytes can reuse a stored chunk.", "chunkID hashes bytes; Put checks chunk presence before writing."),
            mod("Encrypt and Authenticate Chunks", "repository.go", "AES-GCM encrypts bytes and adds an authentication tag so tampering is detected during open.", "seal creates a nonce and stores ciphertext/tag; openSealed authenticates before returning plaintext."),
            mod("Write Repository and Manifest", "repository.go", "Put records a file's chunk list in repository metadata and stores encrypted chunk files under the repository directory.", "Repository.Put returns PutResult; Save serializes repository state."),
            mod("Restore and Verify Content", "repository.go", "Restore loads the manifest, decrypts each referenced chunk, and concatenates them in order.", "OpenRepository loads persisted state; Restore iterates chunk metadata and opens stored chunk bytes."),
            mod("Test Deduplication and Restore Drills", "repository_test.go", "Tests verify chunk boundaries, repeated content deduplication, restoration, and key derivation properties.", "TestBackupDedupAndRestore; TestContentDefinedChunking; TestTheKeyIsDerivedWithASalt."),
            mod("Operational Limits and Recovery", "repository.go; main.go; README.md", "A successful local put is not an off-site backup; production systems need retention, replication, access controls, key custody, and restore drills.", "Restore reads encrypted local chunks; the code has no remote backend, scheduler, retention policy, snapshots, or prune command.", "Restore(name)"),
        ]),
    project("event-streaming-platform-kafka-lite", "Event Streaming Platform (Kafka-lite)",
        "A Java/Kafka clickstream pipeline validates schemas, runs Kafka Streams aggregations, and serves materialized views.",
        "Trace events through schema validation, Kafka topics, stream processing, state stores, and query APIs while distinguishing the local fake registry from a real registry.",
        ["Java", "Apache Kafka 3.7.0", "Kafka Streams", "Schema Registry", "Docker Compose", "JUnit"],
        "Producer, registry client/fake registry, schema validation and DLQ, Kafka Streams topology, windows/sessionization, view server, dashboard.",
        "ClickProducer → clicks topic → schema validation/deserializer → ClicksStreamsApp → aggregates/state stores → ViewServer/dashboard; invalid messages route to DLQ.",
        ["This project uses real Kafka components but has an in-process fake registry option; behavior differs between all-local smoke mode and full Compose stack.", "README describes exactly-once semantics; inspect the actual Streams configuration and transaction guarantees before claiming end-to-end exactly once.", "Dashboard may require serving on the same origin or adjusting fetch URLs; opening the file directly is not the same as serving it.", "Schema registry/client compatibility and Compose health/startup behavior need environment verification."],
        [("Apache Kafka documentation", "https://kafka.apache.org/documentation/"), ("Kafka Streams documentation", "https://kafka.apache.org/documentation/streams/"), ("Confluent Schema Registry", "https://docs.confluent.io/platform/current/schema-registry/index.html"), ("Maven documentation", "https://maven.apache.org/guides/")],
        "Use the local Docker Compose stack. Do not describe fake-registry mode as a production registry or exactly-once guarantees without verifying config.",
        [
            mod("Events, Keys, and Topics", "src/main/java/local/foundev/streams/producer/ClickProducer.java; config/producer.properties", "A topic is an append-only event stream; a message key helps decide which partition receives an event.", "Producer config keys click events by session_id; deterministic event IDs are described in README."),
            mod("Validate Event Schemas", "src/main/java/local/foundev/streams/registry/SchemaRegistryClient.java; src/main/resources/clicks-value.schema.json", "A schema is a contract for event fields; producers/consumers can reject data that does not fit it.", "SchemaRegistryClient calls external registry with bundled-schema fallback; FakeSchemaRegistry is local."),
            mod("Handle Invalid Events and DLQ", "src/main/java/local/foundev/streams/deser/SchemaValidatingDeserializer.java", "A dead-letter queue isolates events that cannot be decoded so they do not silently poison the normal stream.", "README describes violations routed to clicks-dlq; inspect headers and error handler for exact behavior."),
            mod("Build the Kafka Streams Topology", "src/main/java/local/foundev/streams/streams/ClicksStreamsApp.java; config/streams.properties", "A topology is a graph of stream transformations connected to input/output topics.", "Source builds clean-clicks, page-stats, session-stats with state stores and changelog topics."),
            mod("Filter Bots and Aggregate Windows", "src/main/java/local/foundev/streams/streams/ClicksStreamsApp.java", "Windowed aggregation groups events by time intervals; a tumbling window starts a new non-overlapping period.", "README describes regex bot filtering and one-minute tumbling aggregations."),
            mod("Understand Sessionization and State Stores", "src/main/java/local/foundev/streams/streams/ClicksStreamsApp.java", "A session groups nearby events; a state store keeps intermediate data so a stream processor can update aggregates.", "README lists sessionization and changelog-backed state stores."),
            mod("Producer Delivery and Registry Modes", "src/main/java/local/foundev/streams/producer/ClickProducer.java; src/main/java/local/foundev/streams/registry/FakeSchemaRegistry.java; README.md", "A producer may send events continuously or in bursts; fake/local registry mode is a test/development choice.", "CLI subcommands include producer, streams, view, fake-registry, and all-local."),
            mod("Serve Materialized Views", "src/main/java/local/foundev/streams/api/ViewServer.java", "A materialized view is a precomputed answer that avoids recalculating from every raw event on each query.", "ViewServer exposes stats/pages, stats/sessions, top-referrers, and health routes."),
            mod("Dashboard Origin and Data Flow", "src/main/resources/dashboard/index.html; README.md", "A browser can call APIs under its origin; opening a file locally may produce a different origin and fail requests.", "README warns dashboard expects ViewServer same-origin or adjusted fetch URLs."),
            mod("Compose the Stack and Verify Startup", "docker-compose.yml; Dockerfile; tools/verify.sh", "Compose starts broker, registry, producer, stream app, and view server; dependencies and health checks determine readiness.", "README shows full stack and separate local verification gate."),
            mod("Delivery Guarantees and Failure Handling", "src/main/java/local/foundev/streams/streams/StreamsExceptionHandler.java; config/streams.properties", "Exactly-once is a configuration/transaction guarantee with a defined scope; it must not be inferred from the project name.", "README claims/mentions exactly-once; verify actual processing.guarantee and transaction settings in source."),
            mod("Read Tests and Limitations", "src/test/java/local/foundev/streams/registry/SchemaRegistryClientTest.java; README.md", "Tests show behavior under test fixtures but do not establish all deployments or network integrations.", "SchemaRegistryClientTest covers bundled/fake schema resolution; it does not prove a live external Schema Registry integration.", "SchemaRegistryClientTest"),
        ]),
    project("kubernetes-control-plane-for-cloud-resources", "Kubernetes Control Plane for Cloud Resources",
        "A Go prototype models desired resources, validates schemas, plans actions, reconciles a local store, and exposes JSON endpoints.",
        "Understand reconciliation and optimistic resource versions while distinguishing a control-plane simulation from Kubernetes or Crossplane.",
        ["Go", "JSON API", "custom resource model"],
        "Resource model, schema registry, plan/create/update/delete, reconciliation, desired-state Controller, optimistic versioning, optional JSON FileStore, HTTP handlers.",
        "Desired resources → schema validation → plan against current store → reconcile actions → conditions/version updates → JSON API response.",
        ["The project is not a Kubernetes API server or Crossplane provider and contacts no cloud provider.", "Unknown resource kinds pass when no schema is registered.", "README limitation says resources are in memory, but main.go supports an optional -state JSON FileStore; distinguish default and configured paths.", "ResourceVersion is an in-process model, not Kubernetes API-server concurrency."],
        [("Kubernetes controllers", "https://kubernetes.io/docs/concepts/architecture/controller/"), ("Kubernetes custom resources", "https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/"), ("Kubernetes API concepts", "https://kubernetes.io/docs/reference/using-api/api-concepts/"), ("Go JSON", "https://pkg.go.dev/encoding/json")],
        "Run the local Go demo/API only. Do not present its JSON endpoints as Kubernetes-compatible or cloud-provisioning.",
        [
            mod("Resource Specs and Status", "control.go", "A resource has a desired spec and observed status, like a job ticket and its progress card.", "Resource includes Kind, Name, Spec, Status, Conditions, and ResourceVersion."),
            mod("Register and Validate Schemas", "control.go", "A schema is a checklist for required fields and allowed values before a desired resource is accepted.", "SchemaRegistry.Validate checks registered schemas; a kind with no schema is accepted."),
            mod("Plan Desired vs Current State", "control.go", "A plan is a list of differences needed to move actual state toward desired state.", "Plan returns create/update/delete actions and compares specs with sameSpec."),
            mod("Reconcile Actions and Failures", "control.go", "Reconciliation repeatedly applies planned changes and records failures without pretending a cloud provider ran.", "ReconcileWithSchemas validates writes and returns FailedAction details."),
            mod("Use Resource Versions for Stale Writes", "control.go", "A version is a simple concurrency check: reject an update based on an older snapshot instead of overwriting newer state.", "Store.Update requires incoming ResourceVersion to match and increments it on write."),
            mod("Controller Desired State and Generation", "control.go", "The Controller keeps the desired list and a generation number so repeated reconciliation can track changes.", "SetDesired validates and replaces desired resources; Reconcile plans against Store."),
            mod("Persist State with the Optional FileStore", "control.go; main.go", "The default store is in memory; a supplied -state path loads/saves JSON between process starts.", "main.go conditionally loads NewFileStore when state path is nonempty and saves after changes."),
            mod("Expose the JSON Control API", "control.go; main.go", "HTTP endpoints let clients inspect resources, desired state, plans, reconcile, and health.", "Server routes /api/resources, /api/desired, /api/plan, /api/reconcile, /healthz."),
            mod("Separate Simulation from Kubernetes", "README.md; control.go", "A custom-resource-shaped Go struct is not itself a Kubernetes CRD, API server, controller-runtime client, or cloud resource.", "No Kubernetes API server/provider is contacted; status is set by local reconciliation."),
        ]),
    project("lightweight-event-messaging-and-queue-system", "Lightweight Event Messaging and Queue System",
        "A Go in-memory broker partitions topics by key, appends messages, fetches by offset, and tracks one consumer offset.",
        "Understand ordering, partitions, offsets, acknowledgements, retention, and the limitations of a memory-only queue.",
        ["Go", "HTTP JSON API", "in-memory queue"],
        "Topics/partitions, deterministic key partitioning, publish/fetch, consumer cursor/ack/pending, retention trim, HTTP handlers.",
        "Publish(topic,key,payload) → partition/offset → fetch from offset → consumer poll → ack advances cursor → retention trims history.",
        ["All topics/messages/offsets are in memory; restart loses them.", "There are no durable consumer groups, replication, dead-letter queues, or flow control.", "Acknowledgement semantics and retention boundaries are simple prototype behavior, not Kafka/NATS guarantees.", "README says NATS-like concept but implementation is its own Go HTTP API."],
        [("Go net/http", "https://pkg.go.dev/net/http"), ("Apache Kafka concepts", "https://kafka.apache.org/documentation/#intro_concepts_and_terms"), ("NATS concepts", "https://docs.nats.io/nats-concepts/what-is-nats")],
        "Run as a local teaching prototype. Do not use it as a durable production message broker.",
        [
            mod("Message, Topic, and Partition Models", "queue.go", "A topic is a named stream; partitions split a topic into ordered lanes.", "Message carries topic/key/payload/offset/partition; Topic stores partition slices and offsets."),
            mod("Choose a Partition from the Key", "queue.go", "Messages with the same key should map to the same lane so their order is preserved.", "partitionOf(key) hashes key and maps it to the broker's partition count."),
            mod("Publish and Assign Offsets", "queue.go", "An offset is a position within a partition; publishing appends a message and returns its assigned position.", "Broker.Publish obtains/creates Topic, selects partition, increments per-partition offset."),
            mod("Fetch from an Offset", "queue.go", "A consumer asks for messages starting from a position, bounded by a limit.", "Broker.Fetch accepts topic, offset, limit and returns matching messages."),
            mod("Consumer Poll, Ack, and Pending", "queue.go", "A consumer cursor is its current reading position; acknowledgement advances it, while pending counts unacknowledged records.", "Consumer.Poll and Ack track a single offset for that consumer instance."),
            mod("Retention and HTTP API", "queue.go; main.go", "Retention trims old messages in memory; HTTP endpoints expose publish/fetch and demo operations.", "NewBroker(retention); PublishHandler/FetchHandler serve JSON."),
            mod("Durability and Delivery Limits", "queue.go; README.md", "A persistent broker must survive restarts and define replication/consumer-group semantics; this source does not.", "Topic.Messages is an in-memory slice; the queue has no persistence, replication, durable consumer groups, or dead-letter queue.", "Messages []Message"),
        ]),
    project("lightweight-kubernetes-edge-cluster", "Lightweight Kubernetes Edge Cluster",
        "An operations repository provides scripts, K3s configuration, Helm workloads, systemd units, backups, and an offline validation gate.",
        "Plan and review a small HA edge cluster while understanding quorum, node joins, local storage, tokens, and destructive operations.",
        ["K3s", "Kubernetes", "Helm", "systemd", "Linux", "Raspberry Pi/VM"],
        "Preflight and server/agent installation scripts, token helper, verification, uninstall, edge-stateful Helm chart, manifests, systemd health/backup timers, validator and runbook.",
        "Preflight → bootstrap first server/etcd → join control-plane peers and agents → deploy chart → verify → monitor/back up → safe teardown.",
        ["README states no cluster was provisioned; offline validation is not an end-to-end cluster test.", "Control plane requires quorum; node-local local-path volumes are not replicated storage.", "Bootstrap/uninstall commands use sudo and alter hosts; never run without disposable, prepared machines.", "Token helper and environment files contain sensitive cluster credentials; keep them out of logs and Git.", "NetworkPolicy requires a CNI that enforces it; validate on the chosen K3s setup."],
        [("K3s documentation", "https://docs.k3s.io/"), ("Kubernetes cluster architecture", "https://kubernetes.io/docs/concepts/architecture/"), ("Kubernetes NetworkPolicy", "https://kubernetes.io/docs/concepts/services-networking/network-policies/"), ("Helm chart docs", "https://helm.sh/docs/topics/charts/"), ("systemd timers", "https://www.freedesktop.org/software/systemd/man/latest/systemd.timer.html")],
        "This package is for planning and offline review. Provision only disposable hosts after reviewing every privileged script, token, firewall, backup, and uninstall action.",
        [
            mod("Edge Cluster Architecture and Quorum", "k3s/config.yaml; bootstrap/10-install-server.sh; bootstrap/11-install-server-join.sh; docs/ARCHITECTURE.md", "Three control-plane servers form a quorum; an odd server count avoids a tie in majority decisions.", "The server install script configures a first K3s server; the join script adds another server using the shared token and server URL. The config file sets cluster-level K3s options."),
            mod("Preflight Host Requirements", "bootstrap/00-preflight.sh", "Preflight is a checklist before installation: architecture, memory, cgroups, ports, hostname, and swap constraints.", "Preflight script checks host conditions before server/agent actions."),
            mod("Bootstrap the First Server", "bootstrap/10-install-server.sh", "The first server initializes the cluster; TLS SAN names must match how clients reach the API.", "Script installs K3s server with cluster-init and tls-san parameters."),
            mod("Join Additional Servers and Agents", "bootstrap/11-install-server-join.sh; bootstrap/20-install-agent.sh", "Join tokens authorize nodes; control-plane peers and workers use different roles and commands.", "Server join and agent join consume a token file; agent gets node-class label."),
            mod("Handle Tokens and Secret Files", "bootstrap/30-token-helper.sh; .gitignore", "A join token is a credential; store it with restrictive permissions and never echo it to CI logs.", "Helper supports show/rotate, with README emphasizing avoiding terminal-log output."),
            mod("Deploy the Edge Stateful Helm Chart", "helm/edge-stateful", "A Helm chart templates Kubernetes objects; values files customize a deployment without copying every manifest.", "Chart includes StatefulSets, Services, PVC templates, PDB, topology spread, NetworkPolicy, and Pi overrides."),
            mod("Understand Local-Path Storage Limits", "helm/edge-stateful; docs", "Local-path storage lives on a node; it can be persistent across pod restarts but is not replicated across nodes.", "README states node-bound volumes and says durability needs snapshots/application backups."),
            mod("Operate Health and etcd Backups", "systemd/", "A systemd timer periodically runs a service; a health probe and etcd snapshot timer have different operational purposes.", "Project supplies k3s healthcheck and backup service/timer plus retention scripts."),
            mod("Use the Offline Validation Gate", "tools/validate.py", "A static gate checks files and policies without contacting Kubernetes; it cannot prove a live cluster works.", "Validator parses YAML/chart structure and scans secrets/dangling refs/destructive commands."),
            mod("Roll Out, Roll Back, and Verify", "manifests/hello-edge/rollout.yaml; bootstrap/40-verify-cluster.sh", "A rollout status confirms a Deployment update; rollout undo returns to a prior revision, subject to retained history.", "The sample manifest declares a staged Rollout resource; verifier can check nodes, etcd, and local-path state.", "kind: Rollout"),
            mod("Review NetworkPolicy and Failure Modes", "manifests/networkpolicy.example.yaml; docs/TROUBLESHOOTING.md", "Network policies are enforced only if the cluster network plugin supports them; node-level firewall and CNI behavior matter.", "The manifest declares NetworkPolicy rules; the selected K3s CNI must enforce them. Troubleshooting covers cgroup/iptables/hostname/pull fixes.", "kind: NetworkPolicy"),
            mod("Uninstall and Restore Safely", "bootstrap/99-uninstall.sh; README.md", "Teardown scripts can remove a cluster and data; backup restore is a separate recovery process.", "Uninstall is gated by --yes; runbook covers node replacement, token rotation, and snapshot restoration."),
        ]),
    project("message-broker-backend-for-microservices", "Message Broker Backend for Microservices",
        "An Erlang/OTP service accepts orders over HTTP, publishes to RabbitMQ, runs a retryable processing pipeline, and exposes metrics.",
        "Understand supervision, AMQP topology, confirms, consumer acknowledgements, retry ladders, dead letters, and observability.",
        ["Erlang/OTP", "RabbitMQ", "AMQP", "Docker Compose", "Prometheus"],
        "Supervisor tree, connection/topology, publisher confirms/idempotency, consumer prefetch/settlement, order pipeline, retry TTL queues, DLQ, HTTP endpoints, metrics.",
        "HTTP order → publisher/exchange → queue → consumer pipeline → ack/retry/DLQ; broker state and health feed HTTP/metrics endpoints.",
        ["Inventory/payment/fulfillment are deterministic simulations in mbb_order, not real services.", "RabbitMQ topology and Docker Compose must be checked against actual environment; README is detailed but tests are unit-focused.", "Retry TTL ladder can produce delayed retries and duplicate processing; idempotency behavior must be understood.", "Credentials/config must be changed before any exposed broker deployment."],
        [("RabbitMQ AMQP concepts", "https://www.rabbitmq.com/tutorials/amqp-concepts"), ("RabbitMQ confirms", "https://www.rabbitmq.com/docs/confirms"), ("Erlang/OTP supervision", "https://www.erlang.org/doc/system/sup_princ.html"), ("Prometheus exposition", "https://prometheus.io/docs/instrumenting/exposition_formats/")],
        "Run the Compose stack only in a local lab; change example credentials and do not expose the management/broker ports publicly.",
        [
            mod("OTP Application and Supervision", "src/mbb_sup.erl; src/message_broker_backend.app.src", "A supervisor is a caretaker that restarts child processes according to a strategy.", "mbb_sup supervises connection, consumer, metrics, and HTTP workers."),
            mod("Manage AMQP Connection and Reconnect", "src/mbb_connection.erl", "A broker connection is a network session; reconnect logic must recreate channels and topology after a failure.", "Connection module owns connection/channel and re-declares topology after reconnect."),
            mod("Declare Exchanges, Queues, and Bindings", "src/mbb_topology.erl; rabbitmq/", "Topology is the routing map of exchanges, queues, and bindings; declarations should be repeatable.", "Project defines orders exchange, process/retry/DLQ queues, and service queues."),
            mod("Publish with Confirms and Idempotency", "src/mbb_publisher.erl; src/mbb_order.erl", "Publisher confirms tell a producer the broker accepted a message; an idempotency key helps recognize repeated orders.", "Publisher uses confirms and order idempotency key as described by README."),
            mod("Consume with Prefetch and Settlement", "src/mbb_consumer.erl", "Prefetch limits unacknowledged messages; ack says done, retry/requeue or dead-letter handles failures.", "Consumer classifies outcomes and settles deliveries; pipeline returns ok/retry/dead_letter."),
            mod("Process and Classify Orders", "src/mbb_order.erl", "A pipeline is a sequence of business steps; validation errors are terminal while transient backend failures may retry.", "validate → reserve inventory → charge → fulfil; integrations are simulated deterministically."),
            mod("Retry Ladder and Dead-Letter Queue", "src/mbb_topology.erl; src/mbb_consumer.erl; rabbitmq/definitions.json", "A retry queue delays a message before routing it back; a dead-letter queue holds exhausted or terminal failures.", "Retry TTL grows as base × 4^(N-1); x-retry-count and max_retries govern exhaustion."),
            mod("Expose Health, Readiness, and Metrics", "src/mbb_http.erl; src/mbb_metrics.erl", "Liveness means process responds; readiness means dependencies/topology are ready; metrics expose measured counters/histograms.", "README lists /health, /ready, /metrics, /orders."),
            mod("Run and Configure the Broker Stack", "docker-compose.yml; rabbitmq/rabbitmq.conf; prometheus/prometheus.yml", "Compose wires broker, app, and monitoring containers; ports, credentials, and health checks shape local behavior.", "README specifies broker, schema/config, HTTP, and dashboard/run configuration."),
            mod("Test Failure Paths and Duplication", "test/", "Message delivery can be repeated; test retries, idempotency, dead letters, and reconnect behavior rather than assuming one delivery.", "Tests cover order outcomes, metrics, and retries; broker integration should be run separately."),
            mod("Inspect Operational and Security Limits", "src/mbb_order.erl; config/sys.config; README.md", "Credentials, broker access, retry backlogs, and simulated external services affect production readiness.", "The process/1 function uses deterministic inventory and charge functions; they stand in for real network service adapters.", "process(Order)"),
            mod("Build a Safe Local Verification Plan", "README.md; tools/check_erl.py", "A local verification plan separates unit tests, broker integration, and production deployment checks.", "README documents rebar tests, Compose stack, and limitations."),
        ]),
    project("metrics-monitoring-and-alerting-platform", "Metrics Monitoring and Alerting Platform",
        "A Go in-memory time-series store accepts samples, calculates simple window queries, evaluates threshold alerts, and emits Prometheus text.",
        "Understand sample timestamps, windows, rate/sum/average, alert duration, and the limits of a tiny metrics engine.",
        ["Go", "HTTP JSON", "Prometheus text exposition"],
        "Sample store, time-window selection, rate/sum/average, alert rules with for-duration, JSON handlers, Prometheus exporter.",
        "Ingest Sample → store → select window at query time → aggregate → evaluate rule state → JSON or exposition response.",
        ["No PromQL parser or Prometheus scrape integration; samples are pushed into this process.", "Samples are in memory and not persisted.", "Alerts are logged, not delivered to Alertmanager.", "Rate formula and alert pending-duration behavior are the project's simplified semantics, not full Prometheus semantics."],
        [("Prometheus exposition format", "https://prometheus.io/docs/instrumenting/exposition_formats/"), ("Prometheus concepts", "https://prometheus.io/docs/introduction/overview/"), ("Go time", "https://pkg.go.dev/time")],
        "Run locally with synthetic samples. Do not treat the demo as a production monitoring or alerting system.",
        [
            mod("Sample and Label Data Model", "metrics.go", "A sample is a measurement plus labels and time; labels let queries group related series.", "Sample stores metric/name labels/value/timestamp fields."),
            mod("Store and Select a Time Window", "metrics.go", "A time window selects observations near now; old samples outside the window do not contribute.", "windowLocked filters by metric and cutoff time."),
            mod("Calculate Rate", "metrics.go", "A rate estimates change per unit time from samples in a window; this is a simplified calculation.", "rateLocked uses selected sample values/time behavior from source; inspect exact first/last handling."),
            mod("Calculate Sum and Average", "metrics.go", "Sum totals values; average divides total by sample count, with empty-window behavior handled explicitly.", "Store.Sum and Store.Average use windowLocked."),
            mod("Evaluate Alert Rules", "metrics.go", "A threshold is a guardrail; a for-duration requires a condition to persist before producing an alert.", "Evaluate compares rule threshold/for duration and returns Alert records."),
            mod("Expose Prometheus Text", "metrics.go", "Prometheus text is line-oriented samples with HELP/TYPE metadata; emitting text is not the same as implementing PromQL.", "Prometheus(now) generates exposition text; /metrics handler serves it."),
            mod("Use JSON Ingest and Query API", "metrics.go; main.go", "HTTP routes accept/query project-specific JSON and return summaries; they are not Prometheus remote-write or scrape APIs.", "IngestHandler, QueryHandler, and main route registrations."),
        ]),
    project("programmable-ci-cd-engine-with-dagger", "Programmable CI/CD Engine with Dagger",
        "A Go pipeline runner orders steps, hashes inputs/dependencies, caches results, executes host commands, and reports outcomes.",
        "Understand dependency graphs, cache correctness, executor boundaries, retries/timeouts, and secret redaction without mistaking this host runner for Dagger.",
        ["Go", "context", "host process execution", "memory/file cache"],
        "Pipeline/Step model, DAG ordering/cycle checks, digest cache, host/recording executors, retries/timeouts, environment/secret handling, report.",
        "Pipeline definitions → dependency order → content/dependency digests → cache or executor → results/logs.",
        ["Despite project name and listed stack, this implementation does not import or invoke the Dagger SDK/engine; it simulates container steps with host command execution.", "HostExecutor commands run on the machine and are not isolated containers.", "FileCache is local; no remote artifact/cache service exists.", "Secrets are redacted in output by tests but still require careful environment and process handling."],
        [("Dagger Go SDK", "https://docs.dagger.io/reference/sdks/go/"), ("Go os/exec", "https://pkg.go.dev/os/exec"), ("Go context", "https://pkg.go.dev/context")],
        "Run only trusted pipeline definitions in a disposable workspace; host-executed steps can modify the local machine.",
        [
            mod("Model Pipeline Steps and Dependencies", "engine.go", "A pipeline is a set of jobs with dependency edges; a step has a command and execution settings.", "Step contains dependencies, environment, retries, timeout, and secrets; Pipeline contains Steps."),
            mod("Resolve the Dependency Graph", "engine.go", "Topological ordering means a prerequisite runs before the step that depends on it.", "Order rejects unknown dependencies, duplicate names, and cycles."),
            mod("Build Correct Cache Digests", "engine.go", "A cache key must change when a step or its upstream output changes, or stale results can be reused.", "digestOf hashes step content together with dependency digests."),
            mod("Use Memory and File Caches", "engine.go", "A memory cache lasts for one process; a file cache can survive a new engine process on the same disk.", "MemoryCache and FileCache implement Has/Put."),
            mod("Compare Host and Recording Executors", "engine.go", "An executor is the component that performs a step; recording can preview while host execution runs a local command.", "HostExecutor uses os/exec; RecordingExecutor records calls without running them."),
            mod("Run Steps with Retries and Timeouts", "engine.go", "Retries repeat a failed step up to a configured limit; a timeout bounds a command's running time.", "Engine.runStep uses context cancellation and retries, then captures exit code/output."),
            mod("Handle Environment and Secrets", "engine.go; engine_test.go", "Step environment values are passed to commands; secret values should never be printed in logs.", "Tests verify environment delivery and secret redaction."),
            mod("Read Pipeline Files and Reports", "engine.go; main.go", "Pipeline files are serialized configuration; run reports contain status, logs, cache hits, and exit results.", "LoadPipeline/SavePipeline read and write definitions; PrintResults renders results."),
            mod("Distinguish Dagger from This Engine", "engine.go; README.md; go.mod", "Dagger is a containerized programmable build engine; this source runs host commands and has no Dagger SDK dependency.", "HostExecutor.Run invokes the host command executor; the source does not create Dagger containers.", "HostExecutor.Run(ctx, step)"),
        ]),
    project("secrets-management-platform-with-ui", "Secrets Management Platform with UI",
        "A Node.js app derives a key from a master password, encrypts stored values with AES-256-GCM, exposes a token-protected API, and serves a UI.",
        "Understand authenticated encryption, key derivation, file storage, API authorization, audit behavior, and demo deployment limits.",
        ["Node.js", "node:crypto", "AES-256-GCM", "PBKDF2", "HTTP JSON API"],
        "Crypto helper, JSON file SecretStore, single-token API, static UI, node:test suite.",
        "HTTP request with token → SecretStore set/get/delete → PBKDF2-derived key → AES-GCM envelope → JSON file and bounded audit list.",
        ["Default password is change-me when SECRETS_PASSWORD is absent, and the API token is printed to console at startup.", "One API token provides broad access; no role-based access control or key rotation exists.", "Audit history is capped at 200 records and stored beside secrets; it is not an immutable audit system.", "File writes are direct, not an atomic database transaction; no TLS is provided by the basic Node server.", "Read API reveals plaintext to any holder of the API token."],
        [("Node crypto", "https://nodejs.org/api/crypto.html"), ("Node HTTP", "https://nodejs.org/api/http.html"), ("OWASP Cryptographic Storage", "https://cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Storage_Cheat_Sheet.html"), ("OWASP Secrets Management", "https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html")],
        "Use throwaway secrets only on localhost. Set a strong password/token, protect the data file, and do not expose the HTTP service publicly.",
        [
            mod("Threat Model and Secret Boundaries", "src/server.js; README.md", "Encryption at rest protects a stolen data file only while the key/password remains secret; a running server can decrypt requested values.", "The server checks x-api-token for API routes; it has no user roles or key rotation.", "url.pathname.startsWith"),
            mod("Derive a Key from a Password", "src/crypto.js", "PBKDF2 turns a password and salt into key bytes; a salt is stored with the encrypted data and is not itself secret.", "deriveKey uses PBKDF2-SHA256, 120000 iterations, and 32-byte output."),
            mod("Encrypt with AES-GCM", "src/crypto.js", "Authenticated encryption produces ciphertext and a tag; changing ciphertext or tag should cause decryption to fail.", "encrypt uses AES-256-GCM with a random 12-byte IV and returns IV/ciphertext/tag as Base64."),
            mod("Store Envelopes and Audit Records", "src/store.js", "The store saves encrypted envelopes and metadata in a JSON file; the audit list records action/name/time but is bounded.", "SecretStore.set encrypts and saves; record trims audit to last 200 items."),
            mod("Use Set/Get/Delete Operations", "src/store.js", "Set validates names/values, get decrypts a selected entry, list returns names/timestamps, and remove deletes an entry.", "get returns plaintext after decrypt; list never returns secret values."),
            mod("Authorize API Calls", "src/server.js", "An API token is compared before routes; static UI paths are served without the API token.", "API paths require x-api-token; constant-time equal checks equal-length buffers."),
            mod("Review Defaults and HTTP Exposure", "src/server.js; README.md", "A demo default password and console-printed token are unsafe outside localhost; a plain HTTP server has no TLS.", "When SECRETS_PASSWORD absent, main uses change-me; generated TOKEN is logged."),
            mod("Test Crypto and API Behavior", "test/crypto.test.js; test/server.test.js", "Tests check encrypt/decrypt, store operations, authorization, and routes, but do not prove secure deployment or key rotation.", "The Node test cases cover secret round trips, incorrect-password errors, and API authorization; they do not prove deployment hardening.", "test(\"round trips a secret\")"),
            mod("Plan Production Hardening", "README.md; src/store.js", "Production systems need role-scoped access, key rotation/recovery, audit integrity, encrypted backups, rate limiting, and protected transport.", "SecretStore.set writes encrypted envelopes to a local JSON store; the README limits this sample to one API token and no key rotation.", "SecretStore.set(name, value)"),
        ]),
    project("secure-container-registry-with-vulnerability-scanning", "Secure Container Registry with Vulnerability Scanning",
        "A Go model stores image manifests/digests in memory and compares package versions against a small vulnerability catalog.",
        "Understand image manifest identity, semantic versions, package findings, and admission decisions while distinguishing metadata scanning from real image scanning.",
        ["Go", "container manifest metadata", "semantic version parser", "HTTP demo"],
        "Registry push/get, deterministic digest, version parser, vulnerability catalog/scanner, critical finding block decision.",
        "Manifest metadata → digest → registry map → package/version scan → findings → push admission result.",
        ["Images/layers are metadata only; no OCI blobs are stored or served.", "Scanner uses a small hard-coded vulnerability list and does not inspect image layers or OS packages.", "Signing/verification and a real Docker/Trivy/Notary workflow are not implemented.", "README describes an in-memory registry, not a private network registry."],
        [("OCI image manifest", "https://github.com/opencontainers/image-spec/blob/main/manifest.md"), ("Go semver reference", "https://pkg.go.dev/golang.org/x/mod/semver"), ("NIST NVD", "https://nvd.nist.gov/")],
        "Use synthetic package metadata. Do not treat this demo as a vulnerability scanner or security gate for real images.",
        [
            mod("Model Packages, Layers, and Manifests", "registry.go", "A manifest is metadata describing an image; the actual layer bytes are separate content.", "Manifest contains name/tag/packages/layers; Layer metadata and Package versions are Go structs."),
            mod("Compute Deterministic Digests", "registry.go; version.go", "A digest is a hash-derived identifier for manifest content; stable canonical input is needed for reproducibility.", "Digest marshals manifest data and uses HashDigest."),
            mod("Push and Retrieve Registry Entries", "registry.go", "The Registry stores manifests under name/tag keys in memory, then retrieves them by that key.", "Push computes digest and stores map entry; Get reads it."),
            mod("Parse and Compare Versions", "version.go", "Version comparison must compare numeric components, not strings; lexical order misorders values such as 7.9 and 7.88.", "ParseVersion and Version.Less split numeric/prerelease pieces."),
            mod("Represent Findings and Vulnerabilities", "registry.go", "A finding links a package/version to a known vulnerable range and severity.", "DefaultScanner seeds a local vulnerability list and Scan returns Finding objects."),
            mod("Block on Policy Thresholds", "registry.go; main.go", "Scanning identifies matches; policy decides whether findings block a push.", "Blocked checks the configured critical severity threshold."),
            mod("Test Limits of the Scanner", "registry_test.go; registry.go; README.md", "Tests check sample metadata and version rules, not image extraction or a live vulnerability database.", "Registry tests operate on Manifest package metadata; the scanner does not read OCI layer blobs or query a live advisory database.", "DefaultScanner().Scan(manifest)"),
            mod("Plan Real Registry Integration", "registry.go; README.md", "A production registry needs blob storage, authentication, immutable references, scanning updates, and signature verification.", "Registry stores Manifest values in an in-memory map; it has no OCI blob store or durable backend."),
        ]),
    project("self-hosted-git-platform-with-actions-runner", "Self-Hosted Git Platform with Actions Runner",
        "A Go teaching implementation stores Git-like objects, branches and commits, parses a small workflow syntax, and runs host commands.",
        "Understand content-addressed Git objects and workflow scheduling while recognizing that commands execute directly on the host.",
        ["Go", "Git object hashing", "custom workflow parser", "os/exec"],
        "Blob/tree/commit object store, branches/log/diff, JSON save/load, small YAML-like workflow parser, job/step dependency runner.",
        "Files → Git-style objects/commit → branch pointer; workflow text → jobs/steps → dependency gates → host command execution → results.",
        ["Objects are stored in a local JSON state, not packed or served over Git protocol.", "Workflow parser supports only a small syntax subset; it is not full YAML or GitHub Actions.", "Runner executes commands on the host without container isolation; never run untrusted workflow files.", "README's wording that steps are recorded conflicts with tests/implementation showing HostRunner executes them; study source, not that sentence.", "Prebuilt executable files are present in the repository; their provenance is not established by source review, so do not run them blindly."],
        [("Git hash-object", "https://git-scm.com/docs/git-hash-object"), ("Git objects", "https://git-scm.com/book/en/v2/Git-Internals-Git-Objects"), ("Go os/exec", "https://pkg.go.dev/os/exec")],
        "Run only trusted workflow commands in a disposable local repository; there is no sandbox or access control.",
        [
            mod("Git Object Types and Hashing", "repository.go", "Git identifies objects by hashing a header containing object type and content length plus the content bytes.", "gitObjectHash/hashOf build object hash input; tests compare Git-compatible hashes."),
            mod("Build Commits and Branch Pointers", "repository.go", "A commit points to a tree and parent; a branch is a movable name pointing at a commit ID.", "Commit/CommitAs stores objects and updates branch head."),
            mod("Read History, Branches, and Diff", "repository.go", "Log follows commit ancestry; Diff compares file maps between two commits.", "Log, Head, Branches, CreateBranch, Checkout, and Diff provide repository navigation."),
            mod("Save and Load Repository State", "repository.go", "Persistence writes the teaching repository representation to a file; it is not Git packfile storage.", "Save/Load serialize repository state."),
            mod("Parse Workflow Definitions", "repository.go", "The parser recognizes a small indentation-based subset of workflow syntax, not arbitrary YAML.", "ParseWorkflow supports list/key job shapes, run/uses/needs/env fields."),
            mod("Resolve Jobs and Steps", "repository.go", "Dependencies determine which jobs/steps can run; failures block dependent work.", "jobBlocked and stepBlocked check needs/dependencies and prior failures."),
            mod("Run Commands on the Host", "repository.go", "A host runner executes commands through the local shell; it is not an isolated container runner.", "runStep uses process execution and captures output/exit code."),
            mod("Handle Failures and Results", "repository.go", "The runner records step result, skips later steps after failure, and skips dependent jobs.", "Runner.Run returns StepResults with status/output."),
            mod("Test Hashes and Workflow Semantics", "repository_test.go", "Tests compare object hashes/history and exercise parser, runner, failure, and persistence behavior.", "The test suite verifies selected formats and commands, not full Git/Actions compatibility.", "TestTheObjectHashIsTheGitHash"),
            mod("Security and Product Boundaries", "README.md; main.go", "A real hosted Git platform needs authentication, authorization, repository protocol, isolation, and durable storage.", "The CLI entry point starts the local repository/runner; source has no Git server, OAuth, container runner, or multi-user boundary.", "func main()"),
        ]),
    project("tekton-kubernetes-pipeline-engine", "Tekton Kubernetes Pipeline Engine",
        "A Go local runner resolves task dependencies, substitutes parameters, executes commands, handles retries/timeouts/final tasks, and reads directory definitions.",
        "Understand Tekton-like task graphs and execution while distinguishing a local command runner from Tekton CRDs and Pods.",
        ["Go", "context", "os/exec", "YAML-like definitions"],
        "Task/Pipeline structs, DAG resolver, parameter substitution, workspace/results, runner, retry/timeout/finally logic, directory loader.",
        "Definitions → Resolve DAG → substitute params → host-run steps → workspace/results → statuses.",
        ["No Kubernetes API server, Tekton CRDs, Pods, service accounts, or cluster execution are used.", "Commands run on the host; untrusted pipeline definitions can execute arbitrary commands.", "Definitions are Go structs/custom YAML reader rather than Tekton YAML CRDs.", "README's Notes says no retry/timeout/workspace despite earlier features/tests claiming they are implemented; inspect code, which does implement them in the local runner."],
        [("Tekton Tasks", "https://tekton.dev/docs/pipelines/tasks/"), ("Tekton Pipelines", "https://tekton.dev/docs/pipelines/"), ("Tekton retries/finally", "https://tekton.dev/docs/pipelines/pipelines/"), ("Go os/exec", "https://pkg.go.dev/os/exec")],
        "Run only trusted definitions in a disposable workspace. Do not apply as Kubernetes resources; this project executes locally.",
        [
            mod("Task, Step, and Pipeline Models", "engine.go", "A Task groups steps; a Pipeline orders named task instances and their dependencies.", "TaskStep, Task, PipelineTask, Pipeline, TaskStatus are plain Go types."),
            mod("Resolve DAG Dependencies", "engine.go", "A dependency graph is resolved into a topological order; cycles and missing task references prevent execution.", "Resolve detects duplicate tasks, cycles, and unresolved runAfter references."),
            mod("Substitute Task Parameters", "engine.go", "Parameters are placeholders replaced with values before commands run; missing values should fail rather than leave holes.", "Substitute replaces $(params.name) and returns an error for absent parameters."),
            mod("Execute Steps and Capture Results", "engine.go", "Runner executes commands and records output, exit code, and duration; in this project commands run on the host.", "runStep invokes command executor and reads output/result files."),
            mod("Share a Workspace and Read Results", "engine.go", "A workspace is a directory shared by tasks so one task can write a file another task reads.", "runTask creates/uses workspace; readResults collects declared result files."),
            mod("Handle Retries and Timeouts", "engine.go", "Retries repeat a failed task/step; timeouts cancel work after a configured duration.", "Runner/runStep use retry counts, context deadlines, and durations."),
            mod("Run Finally Tasks", "engine.go", "Finally tasks are cleanup/notification tasks intended to execute after the main pipeline regardless of success.", "Runner schedules finally tasks after normal task completion/failure."),
            mod("Load Definitions from Directories", "engine.go; main.go", "A directory loader reads task and pipeline definitions then connects references.", "LoadDefinitionSet reads files and returns pipeline plus task map."),
            mod("Compare the Local Runner with Tekton", "README.md; engine.go", "Tekton executes Task steps as Pods through Kubernetes; this Go engine executes locally and is not a Tekton-compatible controller.", "No Kubernetes client, CRDs, or cluster resources are in source; Runner.Execute delegates to the local command executor.", "runner.Execute(ctx, pipeline, tasks)"),
            mod("Test Execution and Security Limits", "engine.go; engine_test.go; README.md", "Tests cover local command execution, failures, retries, timeout, results, and final tasks; they do not prove a sandbox.", "Host command execution uses exec.CommandContext with the caller's OS permissions; tests use a recording executor for safe cases.", "exec.CommandContext(stepContext, script, \"-c\", command)"),
        ]),
    project("uptime-and-status-monitoring-service", "Uptime and Status Monitoring Service",
        "A Node.js app uses SQLite and scheduled HTTP GET checks to track monitors and alert on status transitions.",
        "Understand monitoring records, polling, transitions, persistence, notification delivery, and the difference between HTTP checks and broader monitoring claims.",
        ["Node.js", "node:sqlite", "HTTP", "node:test"],
        "SQLite database, monitor check function, interval scheduler, transition notifications/webhooks, JSON API, polling dashboard.",
        "Monitor config → scheduled HTTP GET → check result/latency → persisted status/history → transition alert → API/dashboard.",
        ["README claims TCP, DNS, TLS expiry, and content matching in the aspirational brief; implementation notes say checks are HTTP GET only.", "Dashboard polls; no WebSocket push.", "Notifications and multi-node deployment are limited/out of scope; verify exact retry/alert behavior in source.", "SQLite requires a supported Node runtime; runtime version and database feature support must be checked."],
        [("Node.js SQLite", "https://nodejs.org/api/sqlite.html"), ("Node.js timers", "https://nodejs.org/api/timers.html"), ("Node.js HTTP", "https://nodejs.org/api/http.html")],
        "Use local test URLs only. Do not target third-party systems without authorization; configure notification destinations privately.",
        [
            mod("Monitor and Check Data Model", "src/db.js", "A monitor is a saved URL/config; a check is one timestamped observation.", "SQLite schema separates monitors and check history."),
            mod("Perform an HTTP Check", "src/monitor.js", "A checker sends an HTTP GET, measures elapsed time, and classifies response/error.", "checkOnce receives an injectable fetch and returns status/latency/result."),
            mod("Schedule Periodic Checks", "src/monitor.js; src/server.js", "A scheduler repeats checks at intervals; it is not a distributed job queue.", "startScheduler iterates monitors and uses setInterval; timer.unref is used when available."),
            mod("Detect State Changes", "src/monitor.js", "Incident notifications should fire on transitions, not every repeated failed probe.", "previousStatus and notificationsFor compare current/previous status to decide notifications."),
            mod("Send Notifications and Webhooks", "src/monitor.js", "A webhook is an outbound HTTP request to a configured receiver; the project supports notification callbacks.", "notify accepts injectable send function and formats notification payload."),
            mod("Expose API and Static Status Page", "src/server.js; src/static.js; public/", "The server routes API calls and static files; the browser dashboard polls rather than receiving pushed updates.", "createStatusServer and servePublic implement HTTP/static routes."),
            mod("Understand SQLite Persistence", "src/db.js", "SQLite stores local monitoring state on disk, unlike an in-memory-only check list.", "openDatabase creates/uses a SQLite database file and tables."),
            mod("Review Monitoring Scope and Tests", "src/monitor.js; test/", "This source checks HTTP only; it is not a complete uptime suite for TCP, DNS, TLS expiry, or page content.", "The checkOnce function issues HTTP requests; tests cover checks, scheduling, notifications, transitions, and webhook behavior.", "checkOnce(url)"),
        ]),
    project("web3-dapp-frontend-with-wallet-integration", "Web3 dApp Frontend with Wallet Integration",
        "A Node.js static app validates addresses, formats token amounts, encodes ERC20 transfer calldata, and calls an injected EIP-1193 provider.",
        "Understand wallet permissions and transaction construction while recognizing the difference between encoding a call and verifying a token/transaction.",
        ["Node.js", "JavaScript", "Ethereum JSON-RPC", "EIP-1193 provider", "Keccak-256"],
        "Keccak implementation, address helper, decimal-unit conversion, transfer ABI encoder, static page, browser wallet connection and eth_sendTransaction call.",
        "User input → address/amount checks → encode selector/arguments → injected wallet request → wallet approval/sign/broadcast → transaction hash display.",
        ["No contract deployment, on-chain state reader, event listener, or transaction history is implemented.", "The UI checks address shape but does not call EIP-55 checksum validation before encoding.", "No EIP-55 checksum checking is implemented according to README; custom Keccak code needs independent validation before financial use.", "Wallet connection and sending requests require an injected provider; a transaction hash does not mean confirmation/success.", "Only ERC20 transfer calldata is encoded; token contract semantics are not verified."],
        [("EIP-1193 provider API", "https://eips.ethereum.org/EIPS/eip-1193"), ("EIP-55 checksum addresses", "https://eips.ethereum.org/EIPS/eip-55"), ("ERC-20 standard", "https://eips.ethereum.org/EIPS/eip-20"), ("Ethereum ABI specification", "https://docs.soliditylang.org/en/latest/abi-spec.html")],
        "Use a local development chain and test token. Never use a wallet with valuable assets; inspect transaction calldata and chain before signing.",
        [
            mod("Understand Injected Wallet Providers", "public/app.js; src/server.js", "An injected wallet is a browser provider that asks the user to grant accounts and approve transactions.", "connect uses eth_requestAccounts and reads eth_chainId from window.ethereum."),
            mod("Validate Address Shape and Checksum", "src/ethereum.js; src/keccak.js", "A 20-byte hex address shape is different from EIP-55 mixed-case checksum validation.", "isAddress checks 40 hex characters; hasValidChecksum computes Keccak casing; README notes checksum validation limits in UI."),
            mod("Convert Human Units to Base Units", "src/ethereum.js; public/app.js", "Token amounts use integer base units; decimal strings must be scaled without floating point.", "parseUnits accepts digits and optional fraction up to decimals; formatUnits converts BigInt back."),
            mod("Understand Keccak-256 Implementation", "src/keccak.js", "Keccak-256 and standardized SHA3-256 have different padding; cryptographic helper correctness must be validated with known vectors.", "Custom 24-round Keccak-f permutation uses BigInt lanes and rate 136 bytes."),
            mod("Encode ERC20 Transfer Calldata", "src/ethereum.js; public/app.js", "ABI calldata starts with a 4-byte function selector followed by 32-byte encoded arguments.", "TRANSFER_SELECTOR a9059cbb; encodeTransfer pads address and uint256 amount."),
            mod("Construct and Request a Wallet Transaction", "public/app.js", "eth_sendTransaction asks the wallet to handle a transaction; user approval and chain selection matter.", "Request params include from account, token contract address, and data."),
            mod("Inspect Errors and User Safety", "public/app.js; src/ethereum.js", "A returned transaction hash is not proof of mined/confirmed success; wallet rejection and RPC errors must be shown clearly.", "The UI displays hash/error text; it does not wait for receipt confirmation."),
            mod("Review Project Scope and Tests", "src/ethereum.js; test/; README.md", "Tests cover helpers and mocked/provider-facing behavior, not a full dApp or deployed ERC20 contract.", "encodeTransfer builds ERC20 calldata; the source has no contract deployment, event history, on-chain query, or receipt confirmation.", "encodeTransfer(to, amount)"),
        ]),
    project("woodpecker-ci-pipeline-server", "Woodpecker CI Pipeline Server",
        "A Go service parses a small pipeline format, records builds, and can execute commands using a local HostRunner.",
        "Understand a minimal CI server's pipeline parse, build lifecycle, runner boundary, and the dangers of executing repository commands.",
        ["Go", "HTTP", "custom pipeline parser", "os/exec"],
        "Pipeline/Step/Build types, indentation parser, trigger/run/status handlers, HostRunner, in-memory build registry.",
        "HTTP trigger/config → parse pipeline → create build record → run steps → capture outputs/status → list/query build.",
        ["No OAuth/user accounts, queue worker, retries, cancellation, or container isolation.", "HostRunner executes commands on the server machine; do not run untrusted pipelines.", "README says logs are recorded commands but HostRunner captures actual output; reconcile documentation with the selected runner.", "Pipeline syntax is a tiny custom subset, not full Woodpecker YAML."],
        [("Woodpecker CI documentation", "https://woodpecker-ci.org/docs/intro"), ("Go os/exec", "https://pkg.go.dev/os/exec"), ("Go net/http", "https://pkg.go.dev/net/http")],
        "Run only on localhost with trusted test commands. Never expose a host-command runner without authentication, isolation, and authorization.",
        [
            mod("Pipeline and Build Models", "server.go", "A Pipeline is a set of named steps; a Build is one triggered execution record.", "Step/Pipeline/Build types store command, repo/commit, status, and logs."),
            mod("Parse the Pipeline Subset", "server.go", "The parser accepts a deliberately small indentation-based format; it is not a full YAML parser.", "ParsePipeline reads lines and recognizes its supported step shape."),
            mod("Trigger and Record a Build", "server.go; main.go", "Triggering creates a build record before execution; a queue worker is not present.", "Server.Trigger stores Build; main exposes HTTP routes and CLI demo."),
            mod("Execute Steps with HostRunner", "server.go", "HostRunner runs commands on the local machine and captures exit code/output; it does not create containers.", "Runner interface can be replaced in tests; HostRunner uses os/exec."),
            mod("Stop on Failure and Inspect Status", "server.go", "A failed step ends the build path; the result includes step statuses and logs.", "Server.Run updates Build and stops subsequent steps after failure."),
            mod("Serve the HTTP API and Console", "server.go; web/", "HTTP handlers trigger, list, and inspect builds; the web UI is a simple frontend.", "ListHandler and TriggerHandler expose API functionality; frontend/server files are separate."),
            mod("Review Security and Product Scope", "server.go; README.md", "A public pipeline runner that executes commands is a remote-code-execution service and needs strong auth/isolation.", "HostRunner.Run invokes os/exec on the local machine; source has no OAuth/account model, queue, retries, cancellation, or container sandbox.", "func (runner HostRunner) Run"),
        ]),
];

def write_json(path: Path, data) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.rstrip() + "\n", encoding="utf-8")


SOURCE_CODE_EXTENSIONS = {".go", ".sol", ".js", ".ts", ".tsx", ".java", ".py", ".sh", ".tf", ".yaml", ".yml", ".toml", ".json", ".erl", ".hrl", ".ex", ".exs", ".sql", ".html", ".xml", ".rs", ".md"}


def source_excerpt(project, module):
    """Find a short real source excerpt containing a distinctive cue from the authored module example."""
    root = SOURCE / project["slug"]
    paths = [part.strip() for part in module["files"].split(";") if part.strip()]
    files = []
    for rel in paths:
        path = root / rel
        if path.is_file() and path.suffix.lower() in SOURCE_CODE_EXTENSIONS:
            files.append((rel, path))
        elif path.is_dir():
            for child in sorted(path.rglob("*")):
                if child.is_file() and child.suffix.lower() in SOURCE_CODE_EXTENSIONS and child.stat().st_size < 1_000_000:
                    files.append((child.relative_to(root).as_posix(), child))
    cue_text = " ".join((module.get("example", ""), module.get("fact", "")))
    terms = list(dict.fromkeys(re.findall(r"[A-Za-z_][A-Za-z0-9_]{2,}", cue_text)))
    stop = {"The", "This", "That", "README", "Source", "Tests", "Test", "Project", "Project", "No", "Use", "Only", "Do", "Not", "local", "source", "project", "files", "include", "absent", "exists", "implemented", "actual", "current", "return", "status", "the", "and", "not", "with", "from", "or", "if", "else", "true", "false", "for", "error", "config", "handler", "path", "function", "type", "file", "these", "there", "then", "when", "where", "does", "this", "that", "all", "any", "use", "using", "current", "production", "source", "tests", "test", "local", "no", "readme"}
    terms = [term for term in terms if term not in stop or term + "(" in cue_text]
    # Prefer callable/state identifiers over generic words such as URL, API, or ID.
    def cue_priority(term):
        if "_" in term or re.search(r"[a-z][A-Z]", term):
            return 8
        if term + "(" in module.get("example", "") or term + "(" in module.get("fact", ""):
            return 9
        if term[:1].isupper() and any(char.islower() for char in term):
            return 5
        if term.isupper():
            return 1
        return 3 if len(term) >= 8 else 2
    terms.sort(key=lambda t: (cue_priority(t), len(t)), reverse=True)
    ranked = []
    for file_index, (rel, path) in enumerate(files):
        try:
            lines = path.read_text(encoding="utf-8-sig", errors="replace").splitlines()
        except OSError:
            continue
        for line_index, line in enumerate(lines):
            matched = [term for term in terms if re.search(r"(?<![A-Za-z0-9_])" + re.escape(term) + r"(?![A-Za-z0-9_])", line)]
            if not matched:
                continue
            code_line = line.strip()
            executable = bool(code_line) and not code_line.startswith(("//", "#", "*", "/*", "<!--"))
            specificity = sum(5 if ("_" in term or re.search(r"[a-z][A-Z]", term) or term.isupper() or "(" in module.get("example", "") and term + "(" in module.get("example", "")) else 1 for term in matched)
            code_bonus = 8 if path.suffix.lower() != ".md" else -4
            score = specificity + (3 if executable else 0) + code_bonus + max(0, 3 - file_index)
            start = max(0, line_index - 5)
            end = min(len(lines), line_index + 5)
            excerpt = "\n".join(lines[start:end]).strip()
            if len(excerpt) > 1800:
                excerpt = excerpt[:1800]
            for cue in sorted(matched, key=lambda t: (cue_priority(t), len(t)), reverse=True):
                ranked.append((cue_priority(cue) * 10 + score, cue, rel, start + 1, end, excerpt, path.suffix.lower().lstrip(".")))
    if not ranked:
        return None
    ranked.sort(key=lambda item: (item[0], -len(item[5])), reverse=True)
    score, cue, rel, start, end, excerpt, language = ranked[0]
    return {"file": rel, "line_start": start, "line_end": end, "cue": cue, "language": language or "text", "excerpt": excerpt}


def lesson_content(project, module, module_index, lesson_index, objective):
    title = module["title"]
    source = module["files"]
    plain = module["plain"]
    fact = module["fact"]
    excerpt = module["example"]
    code_block = chr(96) * 3 + "text\n" + excerpt + "\n" + chr(96) * 3
    modes = [
        f"Begin with this mental model: {plain} Identify the actual components in {source}.",
        f"Now trace the implementation for {title}. The source finding is: {fact}",
        f"Move from the happy path to operational reasoning: {fact}",
    ]
    steps = [
        "Explain the idea in your own words before inspecting code.",
        f"Open {source} and locate the relevant model, function, or configuration.",
        f"Trace the source finding: {fact}",
        "Predict one normal result and one failure/boundary, then describe safe verification.",
    ]
    return f'''# {objective}

**Lesson ID:** lesson-{lesson_index + 1:02d}  
**Module ID:** module-{module_index + 1:02d}  
**Estimated duration:** 30 minutes

## Purpose and learning objectives

This lesson introduces **{title}** in {project['title']}. Begin with the plain-language model, then move into the source implementation and its operational boundaries.

## Prerequisites

Read the earlier lesson in this module. The project uses {', '.join(project['stack'])}. Follow setup-guide.md and use local or test environments.

## Topic in plain language

{plain}

## Source explanation

{modes[lesson_index]}

This is a source-grounded explanation, not a claim that the whole external platform is implemented. Compare README statements with code and config.

## Step-by-step

{chr(10).join(f'{i}. {step}' for i, step in enumerate(steps, 1))}

## Source excerpt or paraphrase

Source file(s): {source}

{code_block}

Read this with surrounding code. For cryptography, secrets, contracts, and infrastructure, treat the example as educational and verify current official documentation.

## Expected behavior

The source-level finding is: {fact} This content package has not run the application or deployed the infrastructure.

## Practical exercise

Map input → state/data → operation → result. Record one failure mode, a safe test plan, and the evidence that would justify a success claim.

## Common mistakes and debugging

- Treating a project title or feature list as proof the feature is implemented.
- Confusing local simulation with a provider integration.
- Assuming tests establish security or production readiness.
- Running privileged/destructive actions on shared or production systems.
- Logging secrets or committing keys.

## Best practices and security

Use disposable environments, least privilege, bounded inputs, explicit rollback, and credential hygiene. Review network and resource exposure before deployment.

## Summary

You moved from a lay explanation to the exact source behavior and its limits.

## Knowledge check

1. Which source file/function implements the behavior?
2. What data/control path does it follow?
3. What is not implemented or verified?

## References

Use the official links in references.json.
'''


def write_json(path: Path, value) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def write_text(path: Path, value: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(value.rstrip() + "\n", encoding="utf-8")


def lesson_content(project, module, module_index, lesson_index, objective):
    title, source_files, plain, fact, example = (module[k] for k in ("title", "files", "plain", "fact", "example"))
    focus = module.get("_source_focus") or source_excerpt(project, module)
    if focus:
        fence = chr(96) * 4
        code_block = f"**Source:** `{focus['file']}:{focus['line_start']}–{focus['line_end']}`  \n**Focus cue:** `{focus['cue']}`\n\n{fence}{focus['language']}\n{focus['excerpt']}\n{fence}"
    else:
        code_block = f"**Source files:** {source_files}\n\nThe source file map is present, but an excerpt matching the authored focus cue could not be extracted. Review the named function/configuration before teaching this section.\n\nModule's intended source cue: {example}"
    if lesson_index == 0:
        approach = f"Begin with this mental model: {plain} Identify the actual components in {source_files}."
        steps = ["State the idea in your own words before reading code.", f"Open `{focus['file']}` at the cited lines and identify the input and output.", f"Compare the analogy with the implementation: {fact}", "Write one question the analogy does not answer about real deployments."] if focus else ["State the idea in your own words.", f"Inspect the mapped files: {source_files}.", f"Compare the analogy with the implementation: {fact}", "Write one question the analogy does not answer about real deployments."]
    elif lesson_index == 1:
        approach = f"Now trace the implementation for {title}. The source evidence is: {fact}"
        steps = [f"Open `{focus['file']}` and locate `{focus['cue']}`." if focus else f"Open {source_files} and locate the relevant struct/function/configuration.", "Trace values from input to state changes and result.", f"Compare the actual code excerpt with the authored source finding: {fact}", "Separate source behavior from external infrastructure."]
    else:
        approach = f"Move from the happy path to operational reasoning. For this project, {fact}"
        steps = ["Identify a failure, boundary, or unexpected input.", f"Use `{focus['file']}` and the `{focus['cue']}` path to predict behavior: {fact}" if focus else f"Predict the result from source: {fact}", "Describe a safe local/test verification and what evidence to collect.", "State what additional code or infrastructure would be needed before making a production claim."]
    return f'''# {objective}

**Lesson ID:** lesson-{lesson_index + 1:02d}  
**Module ID:** module-{module_index + 1:02d}  
**Estimated duration:** 30 minutes

## Purpose and learning objectives

This lesson introduces **{title}** in {project['title']}. Begin with the plain-language model, then trace the source implementation and examine its operational boundary.

## Prerequisites

Read the earlier lesson in this module. The project uses {', '.join(project['stack'])}. Use a local, simulation, or test environment described in setup-guide.md.

## Topic in plain language

{plain}

## Move from the idea to the source

{approach}

The distinction to keep in view is what the supplied files implement versus what a larger production system would require. The README lists known limitations and source discrepancies.

## Step-by-step

{chr(10).join(f'{i}. {step}' for i, step in enumerate(steps, 1))}

## Source-code walkthrough

**Source file(s):** {source_files}

{code_block}

Read the excerpt in context. Follow the focus cue to its caller or consumer, then state the behavior and one boundary. This copied source excerpt was not executed during content generation. For cryptography, secrets, infrastructure, and smart-contract topics, use official references and treat the package as educational material, not security approval.

## Expected behavior

The code-level finding is: {fact} The original application was not modified or deployed by this content package.

## Practical exercise

Trace one input through the named source. Record the input, validation, state/data change, result, and one failure path. Then design a safe verification plan with the expected result and evidence.

## Common mistakes and debugging

- Treating a README feature list as proof of a real integration.
- Assuming an interface-shaped model is compatible with a provider protocol.
- Confusing passing unit tests with a production guarantee or independent security audit.
- Running destructive host, cluster, contract, or cloud operations against real resources.
- Logging secrets or relying on hard-coded sample credentials.

## Best practices and security

Use disposable environments, least privilege, explicit credential handling, and bounded inputs. For contracts, secrets, infrastructure, and host command runners, inspect the target before execution and separate test from production resources.

## Summary

You moved from a beginner explanation to the actual source behavior and its operational limits. You can cite the file and explain one verification path.

## Knowledge check

1. Which file/function implements the behavior?
2. What data or state changes?
3. What does the source not prove or provide?

## References

Use the official links in references.json.
'''


def exercise_content(project, module_index, module):
    title = module["title"]
    return f'''# Exercise: {title}

**Exercise ID:** exercise-{module_index + 1:02d}  
**Objective:** Demonstrate source comprehension and operational judgment.  
**Difficulty:** Advanced beginner  
**Estimated time:** 45–60 minutes

## Problem

Analyze how {project['title']} implements {title} and create a source-backed explanation or safe local adaptation.

## Requirements

- Cite the source file/function/configuration responsible.
- Diagram the relevant data flow or state transition.
- Identify one failure mode or assumption and a safe verification plan.
- Separate tested behavior, untested behavior, and proposed production work.
- Record security, cost, or operator consequences.

## Constraints

Do not execute untrusted commands with elevated privileges, expose secrets, use real financial assets, or apply infrastructure changes to a shared/production system. Use local fixtures or disposable environments.

## Acceptance criteria

- Claims are supported by source.
- The test plan has explicit inputs, expected output, and evidence.
- Failure paths and security boundaries are addressed.
- No unsupported production-readiness claim is made.
'''


def question_set(project, module_index, module, objectives):
    title, source, fact, example, plain = module["title"], module["files"], module["fact"], module["example"], module["plain"]
    if any(word in " ".join(project["stack"]).lower() for word in ("solidity", "cryptography", "age", "aes")) or "escrow" in project["slug"] or "secret" in project["slug"]:
        myths = ["Passing tests alone proves the system is independently audited and production safe.", "An event log or label is the same as durable, access-controlled state.", "A secret in source or logs remains confidential from repository users."]
        myth_explanations = ["Tests cover specific cases; they are not an independent audit or proof of security.", "An event is an observable record, not by itself durable application state or an access policy.", "Repository files and logs may be visible to users with access; secrets must be protected separately."]
    elif "kubernetes" in " ".join(project["stack"]).lower() or "kubernetes" in project["slug"] or "tekton" in project["slug"]:
        myths = ["A local Go struct automatically registers a Kubernetes CRD and runs as a controller.", "A successful YAML parse proves a cluster accepted and safely applied the resource.", "A local-path volume replicates application data across cluster nodes."]
        myth_explanations = ["A Go struct is only a local type; CRDs/controllers require Kubernetes API registration and a running controller.", "Parsing checks syntax/structure, not cluster admission, permissions, scheduling, or successful reconciliation.", "Local-path volumes are node-local and do not replicate data to other nodes."]
    elif "docker" in " ".join(project["stack"]).lower() or "reverse-proxy" in project["slug"]:
        myths = ["Access to the Docker daemon socket is a harmless read-only permission.", "A health field set to true proves the backend passed an active network probe.", "A host command runner automatically executes commands in a container sandbox."]
        myth_explanations = ["The Docker socket can control the daemon and can effectively grant powerful host access; it is not read-only by default.", "The code has no active probe loop; a stored boolean is only the current manually assigned flag.", "HostExecutor/HostRunner runs commands on the local host unless an isolation layer is explicitly implemented."]
    elif any(word in project["slug"] for word in ("kafka", "broker", "queue", "rate-limiter", "tracing", "metrics")):
        myths = ["An in-memory store survives process restarts and coordinates multiple replicas.", "A protocol-like component name proves wire compatibility with that protocol.", "A successful local unit test proves production delivery and availability guarantees."]
        myth_explanations = ["In-memory state is lost on process restart and is not shared between replicas unless external storage is used.", "Protocol compatibility requires matching wire format and behavior, not just a familiar name or route.", "Unit tests cover selected local cases; they do not prove production reliability, scale, or delivery guarantees."]
    else:
        myths = ["A feature in a README exists even when its source file is absent.", "A local simulation proves behavior matches a production provider integration.", "A metric or UI label proves the remote system is in that state."]
        myth_explanations = ["Documentation may describe intended scope; implementation needs source files that actually provide the feature.", "A simulation exercises local logic, not the provider's API, permissions, network, or runtime behavior.", "A label/value is only as trustworthy as the code path and measurement that produced it."]
    file_distractors = ["README.md by itself", "an unrelated test fixture", "a provider/runtime component absent from the repository"]
    levels = ["basic"] * 3 + ["intermediate"] * 5 + ["advanced"] * 2
    questions, answers = [], []
    for index in range(10):
        lesson_index = 0 if index <= 2 else 1 if index <= 7 else 2
        objective = objectives[lesson_index]
        if index == 0:
            prompt, correct, wrong = f"Which supplied source is primary for {title.lower()}?", source, file_distractors
        elif index == 1:
            prompt, correct, wrong = f"In plain terms, which idea best explains {title.lower()}?", plain, myths
        elif index == 2:
            prompt, correct, wrong = f"Which source finding supports the basic model for {title.lower()}?", fact, myths
        elif index == 3:
            prompt, correct, wrong = f"Where should you trace the implementation of {title.lower()}?", source, file_distractors
        elif index == 6:
            prompt, correct, wrong = f"Which supplied source should be inspected before changing {title.lower()}?", source, file_distractors
        elif index == 4:
            prompt, correct, wrong = f"Which source excerpt or paraphrase illustrates {title.lower()}?", example, myths
        elif index == 7:
            prompt, correct, wrong = f"Which source finding is accurate for {title.lower()}?", fact, myths
        elif index == 5:
            prompt = f"A failure occurs while checking {title.lower()}. Which source finding should guide diagnosis?"
            correct, wrong = fact, myths
        elif index == 8:
            prompt, correct, wrong = f"Which review best connects the basic model and source details in {title.lower()}?", f"Use the model that {plain}, then trace {source}; the source finding is {fact}", myths
        else:
            prompt, correct, wrong = f"After reading the whole module on {title.lower()}, which conclusion combines the source example and its limit?", f"The example is {example}; interpret it with this finding: {fact} Verify the connected component before making a production claim.", myths
        correct_position = (index * 3 + module_index + 1) % 4
        option_texts = [None] * 4
        option_texts[correct_position] = correct
        wrong_iter = iter(wrong)
        for position in range(4):
            if option_texts[position] is None:
                option_texts[position] = next(wrong_iter)
        qid = f"q{module_index + 1}-{index + 1:02d}"
        questions.append({"question_id": qid, "question_text": prompt, "options": [{"option_id": chr(97 + pos), "text": text} for pos, text in enumerate(option_texts)], "difficulty_level": levels[index], "related_learning_objective": objective, "related_lesson_id": f"lesson-{lesson_index + 1:02d}"})
        wrong_explanations = {}
        for position, text in enumerate(option_texts):
            if position == correct_position:
                continue
            if text in myths:
                explanation = myth_explanations[myths.index(text)]
            else:
                explanation = f"This source is not the component identified for the module. Inspect {source}."
            wrong_explanations[chr(97 + position)] = explanation
        if correct == plain:
            explanation = f"This is the module's lay explanation. The implementation source is {source}, where the more specific finding is: {fact} The analogy aids understanding but does not replace the operational limits in the other lessons."
        elif correct == example:
            explanation = f"This excerpt or paraphrase is drawn from {source}. The source finding is: {fact} The other lesson connects this expression to the whole system flow."
        else:
            explanation = f"The relevant source is {source}. It establishes that {fact} The source example is {example} The other lessons place that component in the larger system flow."
        answers.append({"question_id": qid, "correct_option_id": chr(97 + correct_position), "explanation": explanation, "incorrect_option_explanations": wrong_explanations, "concept_tested": title, "related_lesson_id": f"lesson-{lesson_index + 1:02d}", "source_file": source, "supporting_reference": project["refs"][0][1]})
    return {"module_id": f"module-{module_index + 1:02d}", "questions": questions}, {"module_id": f"module-{module_index + 1:02d}", "answers": answers}


def build_package(project):
    base = TARGET / "projects" / project["slug"]
    source_notes = "\n".join(f"- {note}" for note in project["gaps"])
    module_map = "\n".join(f"- **{entry['title']}:** {entry['fact']}" for entry in project["modules"])
    objectives_overall = [
        "Explain the source system's implemented components and limitations",
        "Trace data/control flow through modules and interfaces",
        "Distinguish simulation, local implementation, and external production services",
        "Use tests, logs, and safe experiments to verify claims",
        "Apply security, operational, and failure-mode reasoning",
    ]
    write_json(base / "project.json", {
        "title": project["title"],
        "slug": project["slug"],
        "description": project["description"],
        "problem_solved": project["problem"],
        "target_audience": "Advanced beginner/intermediate Cloud and DevOps learners",
        "technology_stack": project["stack"],
        "difficulty_level": "intermediate",
        "prerequisites": ["Basic programming and terminal use", "Read the project's source tree and setup guide", "Use disposable local/test environments for operational exercises"],
        "learning_outcomes": objectives_overall,
        "estimated_completion_time": f"{len(project['modules']) * 2 + 4}–{len(project['modules']) * 3 + 8} hours",
        "content_schema_version": "1.0.0",
    })
    write_text(base / "prerequisites.md", f"""# Prerequisites

- Working familiarity with the language and tooling in this project: {', '.join(project['stack'])}.
- Basic terminal, Git, and source-code reading skills.
- Infrastructure, cloud, blockchain, and secrets exercises must use disposable or test environments.
- Never commit API keys, private keys, node tokens, passwords, or unencrypted secrets.
- Read the source discrepancy list before following deployment commands.
""")
    write_text(base / "setup-guide.md", f"""# Setup Guide

## Source scope

{project['deployment']}

Inspect the project's README, package/build files, and source before running commands. Some README descriptions refer to broader systems than the included implementation.

## Local setup

Use official tools and versions listed in the repository's build files and references. Prefer local simulations, mock services, test chains, and disposable clusters. Run only the project checks explicitly identified in its README.

## Configuration and credentials

Use environment variables or secret stores for credentials. Do not paste real keys into commands that enter shell history, logs, screenshots, or Git. Check whether a feature uses a local simulation or actual external service.

## Known source gaps

{source_notes}

## Cleanup

Stop local processes and containers, remove disposable state and test resources, revoke temporary credentials, and check cloud/broker/cluster billing before finishing.
""")
    write_text(base / "architecture.md", f"""# Architecture

## Implemented system

{project['features']}

## Data and control flow

{project['data_flow']}

## Module source map

{module_map}

## Boundaries and risks

{source_notes}

This package teaches the checked-in implementation and records gaps between the source and broader platform concepts named by the project. It does not certify security or production readiness.
""")
    write_text(base / "glossary.md", """# Glossary

- **Control plane:** Components that store desired configuration and coordinate changes to managed resources.
- **Data plane:** Components that carry application requests, messages, or user data.
- **Reconciliation:** Repeatedly compare desired and observed state and apply changes to reduce the difference.
- **Idempotency:** Repeating an operation with the same identity should not create unintended duplicate effects.
- **Quorum:** A majority threshold used to make decisions despite some unavailable members.
- **Retry/backoff:** Reattempt a failed operation, often after increasing delays.
- **Dead-letter queue:** A separate destination for messages that cannot be processed normally.
- **Content address:** Identifier derived from data bytes and encoding parameters.
- **KDF:** Key-derivation function that turns a password/secret and salt into key material.
- **Authenticated encryption:** Encryption that also detects modification of ciphertext.
- **Threat model:** A description of assets, attackers, trust boundaries, and failure consequences.
- **SLO/steady-state hypothesis:** A measurable statement about acceptable service behavior.
- **Artifact:** A file or build output passed between workflow steps or stored for later use.
- **Simulation:** A local model that demonstrates logic without contacting the real external service.
- **Least privilege:** Granting only the permissions required for a task.
""")
    write_json(base / "references.json", [{"title": title, "url": url, "type": "official documentation"} for title, url in project["refs"]])
    write_text(base / "README.md", f"""# {project['title']}

## Overview and purpose

{project['description']}

## Real-world context

{project['problem']}

## Implemented features

{project['features']}

## Source findings and limitations

{source_notes}

The modules distinguish implemented code from external systems or features that are only described in the README/brief.

## Technology and system requirements

{', '.join(project['stack'])}. See the repository build files and setup guide for local prerequisites.

## Installation and environment

Follow setup-guide.md and use the project's actual commands. External infrastructure is optional unless a lesson explicitly calls for a disposable test environment.

## Data and persistence

{project['data_flow']}

Persistence, external replication, and managed-service behavior are described only where included in source.

## Architecture and testing

See architecture.md. The project contains the following curriculum modules: {len(project['modules'])}. Follow test commands from the source README; tests do not establish production safety.

## Security and operations

Treat command runners, Docker sockets, cluster credentials, encryption keys, smart contracts, and public endpoints as high-impact boundaries. Use least privilege, test-only credentials, explicit rollback, and cleanup.

## Troubleshooting

Compare README claims with the named source files, inspect logs and test results, and distinguish parser/setup, build, runtime, network, and policy failures.

## Further learning

Use official references in references.json for up-to-date protocol and provider details.
""")
    total_lessons = 0
    total_questions = 0
    for module_index, module in enumerate(project["modules"]):
        module = dict(module)
        module_id = f"module-{module_index + 1:02d}"
        focus = source_excerpt(project, module)
        module["_source_focus"] = focus
        module_sources = [part.strip() for part in module["files"].split(";") if part.strip()]
        objectives = [
            f"Explain {module['title'].lower()} using a plain-language model",
            f"Trace the source implementation for {module['title'].lower()}",
            f"Assess failure and operational limits of {module['title'].lower()}",
        ]
        module_dir = base / "modules" / module_id
        write_json(module_dir / "module.json", {
            "module_id": module_id,
            "title": module["title"],
            "description": f"Progress from an intuitive model to the source implementation and its operational boundary: {module['title']}.",
            "learning_objectives": objectives,
            "prerequisites": [] if module_index == 0 else [f"module-{module_index:02d}"],
            "lesson_ids": ["lesson-01", "lesson-02", "lesson-03"],
            "estimated_duration": "2–3 hours",
            "concepts_covered": [module["plain"], module["fact"]],
            "practical_outcomes": ["Trace the named source component", "Explain at least one operational boundary"],
            "completion_criteria": ["Complete all three lessons and exercise", "Score at least 7/10 on the assessment"],
            "source_files": module_sources,
            "source_code_focus": {"excerpt_file": focus["file"] if focus else None, "symbol_or_search_term": focus["cue"] if focus else module["example"], "line_start": focus["line_start"] if focus else None, "line_end": focus["line_end"] if focus else None},
        })
        for lesson_index, objective in enumerate(objectives):
            write_text(module_dir / "lessons" / f"lesson-{lesson_index + 1:02d}.md", lesson_content(project, module, module_index, lesson_index, objective))
            total_lessons += 1
        write_text(module_dir / "exercises" / f"exercise-{module_index + 1:02d}.md", exercise_content(project, module_index, module))
        assessment, answer_key = question_set(project, module_index, module, objectives)
        write_json(module_dir / "assessment.json", assessment)
        write_json(module_dir / "answer-key.json", answer_key)
        total_questions += len(assessment["questions"])
    final_dir = base / "final-project"
    write_text(final_dir / "requirements.md", f"""# Final Project: Extend and Verify {project['title']}

## Objective

Design and verify a safe extension or correction grounded in the source system: {project['problem']}

## Functional requirements

- Trace the existing request/data/control path and preserve the project's stated core use.
- Address at least one source limitation documented in this package.
- State exact behavior for normal, error, retry, and recovery paths where relevant.
- Provide a testable source-level or integration-level verification plan.

## Non-functional requirements

- Keep credentials and personal data out of source and logs.
- Set explicit resource, timeout, retry, and access boundaries.
- Separate local simulation from real external service behavior.
- Document rollback and cleanup for stateful/infrastructure changes.

## Milestones

1. Inventory modules, source files, dependencies, and trust boundaries.
2. Draw the current data/control flow.
3. Select one extension and write acceptance criteria.
4. Implement or prepare a focused patch in an isolated environment.
5. Verify expected and failure behavior, then document operational limits.

## Deliverables and acceptance criteria

- Source map and architecture diagram or equivalent written flow.
- Working change or precise implementation plan.
- Tests/checks with actual results and any skipped integration tests listed.
- Security/threat review, rollback plan, and cleanup checklist.
- Acceptance: implementation claims match code, error paths are considered, and production readiness is not overstated.

## Testing checklist

- [ ] Test normal input and expected output.
- [ ] Test malformed, missing, stale, or unauthorized input.
- [ ] Test retry, rollback, recovery, or timeout behavior where relevant.
- [ ] Verify persistence and duplicate/replay semantics.
- [ ] Review secrets, network exposure, least privilege, and cleanup.

## Optional extensions

Add production-grade auth, persistent storage, observability, integration tests, or provider support only with an explicit design and threat model.
""")
    write_json(final_dir / "evaluation-rubric.json", {"criteria": [
        {"criterion": "Source-grounded design", "weight": 25, "levels": {"excellent": "Every claim and change maps to actual source", "proficient": "Main architecture is correct", "developing": "Relies on aspirational documentation"}},
        {"criterion": "Correctness and failure handling", "weight": 25, "levels": {"excellent": "Normal and failure/recovery paths are addressed", "proficient": "Main path works", "developing": "Important state or failure cases omitted"}},
        {"criterion": "Verification quality", "weight": 20, "levels": {"excellent": "Reproducible unit and integration evidence is separated", "proficient": "Core behavior is checked", "developing": "No useful evidence"}},
        {"criterion": "Security and operations", "weight": 20, "levels": {"excellent": "Threats, secrets, access, rollback, and cleanup are handled", "proficient": "Major risks considered", "developing": "Unsafe assumptions remain"}},
        {"criterion": "Communication", "weight": 10, "levels": {"excellent": "Simulation, implementation, and production work are clearly separated", "proficient": "Most limits are stated", "developing": "Overstates guarantees"}},
    ]})
    write_text(final_dir / "solution-guide.md", f"""# Mentor Solution Guide

## Source findings

The project implements: {project['features']}

Review known limitations:
{source_notes}

## Review sequence

1. Ask the learner to map the source and identify which external systems are absent.
2. Review the threat/trust boundary and operational failure modes.
3. Check the proposed change against the relevant module and source file.
4. Require separate evidence for unit tests, service integration, and production behavior.
5. Review rollback, secret handling, and cleanup before considering deployment complete.

Do not treat local tests as independent audits, production readiness, or successful provider integration.
""")
    included = sorted(str(path.relative_to(base)) for path in base.rglob("*") if path.is_file() and path.name != "manifest.json")
    write_json(base / "manifest.json", {"project_slug": project["slug"], "content_schema_version": "1.0.0", "package_version": "1.0.0", "generation_timestamp": datetime.now(timezone.utc).isoformat(), "module_count": len(project["modules"]), "lesson_count": total_lessons, "assessment_question_count": total_questions, "included_files": included, "validation_status": "passed_structural_checks_human_review_required"})


def initialize_workspace():
    TARGET.mkdir(parents=True, exist_ok=True)
    for directory in ("projects", "schemas", "tools", "reports", "dist"):
        (TARGET / directory).mkdir(parents=True, exist_ok=True)
    for schema_name in ("project.schema.json", "module.schema.json", "assessment.schema.json"):
        shutil.copy2(LIBRARY / "schemas" / schema_name, TARGET / "schemas" / schema_name)
    module_schema_path = TARGET / "schemas" / "module.schema.json"
    module_schema = json.loads(module_schema_path.read_text(encoding="utf-8"))
    for key in ("source_files", "source_code_focus"):
        if key not in module_schema["required"]:
            module_schema["required"].append(key)
    module_schema["properties"]["source_files"] = {"type": "array", "minItems": 1, "items": {"type": "string"}}
    module_schema["properties"]["source_code_focus"] = {"type": "object", "required": ["excerpt_file", "symbol_or_search_term", "line_start", "line_end"], "properties": {"excerpt_file": {"type": ["string", "null"]}, "symbol_or_search_term": {"type": "string"}, "line_start": {"type": ["integer", "null"]}, "line_end": {"type": ["integer", "null"]}}, "additionalProperties": False}
    write_json(module_schema_path, module_schema)
    write_text(TARGET / "CONTENT_STANDARDS.md", """# Advanced Cloud and DevOps Content Standards

Every module begins with a plain-language model, then follows a cited source-code excerpt, failure cases, and operational boundaries. The source file, line span, and focus cue are recorded in module.json. Student assessments contain ten unique MCQs per module; answer keys remain separate. Content must distinguish simulated behavior from real infrastructure, preserve secrets, and avoid treating tests as production proof.
""")
    write_text(TARGET / "README.md", """# Advanced Cloud and DevOps Learning Library

Twenty-four source-grounded learning packages are in projects/. Each package uses a module count matched to its complexity (six or more), three lessons per module, ten MCQs per module, separate answer keys, exercises, and a final project. ZIPs are in dist/. Run python3 tools/validate_content.py from this directory for structural validation and source-review reports.

The source projects were inspected; this library does not claim to have run their builds, deployed infrastructure, sent transactions, or contacted external APIs. See reports/module-source-audit.md, reports/source-content-audit.md, and package-specific reports for module mappings, source gaps, and human-review items.
""")


def create_archives():
    dist = TARGET / "dist"
    for package in sorted((TARGET / "projects").iterdir()):
        if not package.is_dir():
            continue
        with zipfile.ZipFile(dist / f"{package.name}.zip", "w", zipfile.ZIP_DEFLATED) as archive:
            for item in sorted(package.rglob("*")):
                if item.is_file():
                    archive.write(item, item.relative_to(TARGET))


if __name__ == "__main__":
    initialize_workspace()
    for item in PROJECTS:
        build_package(item)
        print(f"Built {item['slug']} ({len(item['modules'])} modules)")
    create_archives()
