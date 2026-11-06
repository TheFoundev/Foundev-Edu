# Audited Escrow and Tokenization Contracts

## Overview and purpose

A Solidity suite composes an escrow state machine, ERC20 settlement, ERC721 provenance, access roles, royalties, and a factory.

## Real-world context

Reason about stateful value movement and role-controlled tokenized assets without treating a student project as audited production code.

## Implemented features

Escrow states, partial funding, disputes/timeouts, pull-payment credits; TokenizedAsset roles/provenance/royalties; factory indexes; tests include a reentrancy attacker.

## Source findings and limitations

- The title says audited, but no independent audit report is supplied.
- Passing tests do not establish contract security.
- The .env key is a placeholder; use local/test networks only.

The modules distinguish implemented code from external systems or features that are only described in the README/brief.

## Technology and system requirements

Solidity 0.8.24, Hardhat, TypeScript, ethers.js, OpenZeppelin Contracts. See the repository build files and setup guide for local prerequisites.

## Installation and environment

Follow setup-guide.md and use the project's actual commands. External infrastructure is optional unless a lesson explicitly calls for a disposable test environment.

## Data and persistence

Buyer/seller fund escrow → deadlines/state changes → settlement credits → parties withdraw. Factory creates/indexes instances; token contract tracks asset provenance and royalty balances.

Persistence, external replication, and managed-service behavior are described only where included in source.

## Architecture and testing

See architecture.md. The project contains the following curriculum modules: 12. Follow test commands from the source README; tests do not establish production safety.

## Security and operations

Treat command runners, Docker sockets, cluster credentials, encryption keys, smart contracts, and public endpoints as high-impact boundaries. Use least privilege, test-only credentials, explicit rollback, and cleanup.

## Troubleshooting

Compare README claims with the named source files, inspect logs and test results, and distinguish parser/setup, build, runtime, network, and policy failures.

## Further learning

Use official references in references.json for up-to-date protocol and provider details.
