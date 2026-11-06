# Architecture

## Implemented system

Line parser, manual health flags, round robin, reverse proxy, Docker list-containers request, label discovery, health route.

## Data and control flow

Config/Docker API → service registry → healthy backend selection → prefix rewrite → proxy request.

## Module source map

- **Service and Instance Models:** Service groups instances; Registry holds service map/order guarded by an RWMutex.
- **Parse the Small Config Format:** ParseConfig handles services:, - name:, and - http/https lines; rejects instance-before-service and no services.
- **Health Flags and Round Robin:** Mark manually updates Healthy; Pick advances a counter then scans up to all instances; no background health checker exists.
- **Reverse Proxy Path Flow:** ServeHTTP parses /service/path, selects an instance, removes the prefix, and forwards with NewSingleHostReverseProxy.
- **Docker Label Discovery:** ListContainers calls /containers/json over a Unix socket; discovery reads foundev.service/port/host and filters non-running containers.
- **Docker Socket Trust Boundary:** NewDockerClient defaults to /var/run/docker.sock; the source has no auth around a web-exposed proxy.
- **Test Routing and Failure Responses:** Tests cover config, round robin, manual health, proxy path, /health, unknown service, parser errors, and absent socket.
- **Limits of Discovery and Health:** Discovery runs when called; health is manually marked; no probe loop or TLS manager is implemented.

## Boundaries and risks

- Parser is a small line parser, not YAML.
- Health is manually marked; there is no active probe loop.
- Docker socket access is powerful and should not be exposed to untrusted users.
- TLS certificate management is absent.

This package teaches the checked-in implementation and records gaps between the source and broader platform concepts named by the project. It does not certify security or production readiness.
