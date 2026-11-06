# Setup Guide

## Source scope

Use a local development chain and test token. Never use a wallet with valuable assets; inspect transaction calldata and chain before signing.

Inspect the project's README, package/build files, and source before running commands. Some README descriptions refer to broader systems than the included implementation.

## Local setup

Use official tools and versions listed in the repository's build files and references. Prefer local simulations, mock services, test chains, and disposable clusters. Run only the project checks explicitly identified in its README.

## Configuration and credentials

Use environment variables or secret stores for credentials. Do not paste real keys into commands that enter shell history, logs, screenshots, or Git. Check whether a feature uses a local simulation or actual external service.

## Known source gaps

- No contract deployment, on-chain state reader, event listener, or transaction history is implemented.
- The UI checks address shape but does not call EIP-55 checksum validation before encoding.
- No EIP-55 checksum checking is implemented according to README; custom Keccak code needs independent validation before financial use.
- Wallet connection and sending requests require an injected provider; a transaction hash does not mean confirmation/success.
- Only ERC20 transfer calldata is encoded; token contract semantics are not verified.

## Cleanup

Stop local processes and containers, remove disposable state and test resources, revoke temporary credentials, and check cloud/broker/cluster billing before finishing.
