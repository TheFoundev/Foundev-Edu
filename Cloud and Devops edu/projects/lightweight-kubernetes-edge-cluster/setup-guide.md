# Setup Guide

## Source scope

This package is for planning and offline review. Provision only disposable hosts after reviewing every privileged script, token, firewall, backup, and uninstall action.

Inspect the project's README, package/build files, and source before running commands. Some README descriptions refer to broader systems than the included implementation.

## Local setup

Use official tools and versions listed in the repository's build files and references. Prefer local simulations, mock services, test chains, and disposable clusters. Run only the project checks explicitly identified in its README.

## Configuration and credentials

Use environment variables or secret stores for credentials. Do not paste real keys into commands that enter shell history, logs, screenshots, or Git. Check whether a feature uses a local simulation or actual external service.

## Known source gaps

- README states no cluster was provisioned; offline validation is not an end-to-end cluster test.
- Control plane requires quorum; node-local local-path volumes are not replicated storage.
- Bootstrap/uninstall commands use sudo and alter hosts; never run without disposable, prepared machines.
- Token helper and environment files contain sensitive cluster credentials; keep them out of logs and Git.
- NetworkPolicy requires a CNI that enforces it; validate on the chosen K3s setup.

## Cleanup

Stop local processes and containers, remove disposable state and test resources, revoke temporary credentials, and check cloud/broker/cluster billing before finishing.
