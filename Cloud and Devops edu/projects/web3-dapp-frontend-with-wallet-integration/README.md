# Web3 dApp Frontend with Wallet Integration

## Overview and purpose

A Node.js static app validates addresses, formats token amounts, encodes ERC20 transfer calldata, and calls an injected EIP-1193 provider.

## Real-world context

Understand wallet permissions and transaction construction while recognizing the difference between encoding a call and verifying a token/transaction.

## Implemented features

Keccak implementation, address helper, decimal-unit conversion, transfer ABI encoder, static page, browser wallet connection and eth_sendTransaction call.

## Source findings and limitations

- No contract deployment, on-chain state reader, event listener, or transaction history is implemented.
- The UI checks address shape but does not call EIP-55 checksum validation before encoding.
- No EIP-55 checksum checking is implemented according to README; custom Keccak code needs independent validation before financial use.
- Wallet connection and sending requests require an injected provider; a transaction hash does not mean confirmation/success.
- Only ERC20 transfer calldata is encoded; token contract semantics are not verified.

The modules distinguish implemented code from external systems or features that are only described in the README/brief.

## Technology and system requirements

Node.js, JavaScript, Ethereum JSON-RPC, EIP-1193 provider, Keccak-256. See the repository build files and setup guide for local prerequisites.

## Installation and environment

Follow setup-guide.md and use the project's actual commands. External infrastructure is optional unless a lesson explicitly calls for a disposable test environment.

## Data and persistence

User input → address/amount checks → encode selector/arguments → injected wallet request → wallet approval/sign/broadcast → transaction hash display.

Persistence, external replication, and managed-service behavior are described only where included in source.

## Architecture and testing

See architecture.md. The project contains the following curriculum modules: 8. Follow test commands from the source README; tests do not establish production safety.

## Security and operations

Treat command runners, Docker sockets, cluster credentials, encryption keys, smart contracts, and public endpoints as high-impact boundaries. Use least privilege, test-only credentials, explicit rollback, and cleanup.

## Troubleshooting

Compare README claims with the named source files, inspect logs and test results, and distinguish parser/setup, build, runtime, network, and policy failures.

## Further learning

Use official references in references.json for up-to-date protocol and provider details.
