# Setup Guide

## Source scope

Run only trusted workflow commands in a disposable local repository; there is no sandbox or access control.

Inspect the project's README, package/build files, and source before running commands. Some README descriptions refer to broader systems than the included implementation.

## Local setup

Use official tools and versions listed in the repository's build files and references. Prefer local simulations, mock services, test chains, and disposable clusters. Run only the project checks explicitly identified in its README.

## Configuration and credentials

Use environment variables or secret stores for credentials. Do not paste real keys into commands that enter shell history, logs, screenshots, or Git. Check whether a feature uses a local simulation or actual external service.

## Known source gaps

- Objects are stored in a local JSON state, not packed or served over Git protocol.
- Workflow parser supports only a small syntax subset; it is not full YAML or GitHub Actions.
- Runner executes commands on the host without container isolation; never run untrusted workflow files.
- README's wording that steps are recorded conflicts with tests/implementation showing HostRunner executes them; study source, not that sentence.
- Prebuilt executable files are present in the repository; their provenance is not established by source review, so do not run them blindly.

## Cleanup

Stop local processes and containers, remove disposable state and test resources, revoke temporary credentials, and check cloud/broker/cluster billing before finishing.
