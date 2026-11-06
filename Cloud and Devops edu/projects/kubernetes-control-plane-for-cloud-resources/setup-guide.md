# Setup Guide

## Source scope

Run the local Go demo/API only. Do not present its JSON endpoints as Kubernetes-compatible or cloud-provisioning.

Inspect the project's README, package/build files, and source before running commands. Some README descriptions refer to broader systems than the included implementation.

## Local setup

Use official tools and versions listed in the repository's build files and references. Prefer local simulations, mock services, test chains, and disposable clusters. Run only the project checks explicitly identified in its README.

## Configuration and credentials

Use environment variables or secret stores for credentials. Do not paste real keys into commands that enter shell history, logs, screenshots, or Git. Check whether a feature uses a local simulation or actual external service.

## Known source gaps

- The project is not a Kubernetes API server or Crossplane provider and contacts no cloud provider.
- Unknown resource kinds pass when no schema is registered.
- README limitation says resources are in memory, but main.go supports an optional -state JSON FileStore; distinguish default and configured paths.
- ResourceVersion is an in-process model, not Kubernetes API-server concurrency.

## Cleanup

Stop local processes and containers, remove disposable state and test resources, revoke temporary credentials, and check cloud/broker/cluster billing before finishing.
