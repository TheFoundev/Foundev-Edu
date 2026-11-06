# Architecture

## Implemented system

Escrow states, partial funding, disputes/timeouts, pull-payment credits; TokenizedAsset roles/provenance/royalties; factory indexes; tests include a reentrancy attacker.

## Data and control flow

Buyer/seller fund escrow → deadlines/state changes → settlement credits → parties withdraw. Factory creates/indexes instances; token contract tracks asset provenance and royalty balances.

## Module source map

- **Roles and Contract Boundaries:** Escrow distinguishes buyer, seller, and arbiter; TokenizedAsset uses AccessControl roles for minting/auditing and Pausable controls.
- **Escrow State Machine:** States: Created, Funded, Disputed, ArbiterDecided, Released, Refunded; invalid transitions revert with custom errors.
- **Native and ERC20 Funding:** fund accepts ETH; fundERC20 uses SafeERC20; contributions cannot exceed remainingToFund and completion sets the deadline.
- **Pull Payments and Settlement Credits:** Settlement credits a beneficiary; withdraw transfers credited value under nonReentrant and checks-effects-interactions.
- **Deadlines and Timeout Paths:** timeoutRelease and timeoutRefund are separate; refund, cancel, and release each have caller/state requirements.
- **Dispute and Arbiter Lifecycle:** raiseDispute opens a window; arbiterRule records a choice; executeRuling applies it; timeoutRefund handles expiry.
- **ERC721 Provenance and Roles:** TokenizedAsset extends ERC721, AccessControl, Pausable, ReentrancyGuard; mint stores provenance and recordAudit is role-gated.
- **Royalty Pool Accounting:** payRoyalty transfers configured ERC20 into a token-specific pool; claimRoyalties checks original creator and transfers the claim.
- **Factory Creation and Indexing:** createEscrow deploys and indexes instances; escrowAt/getEscrows support lookup and pagination; buyer/seller queries exist.
- **Events, Errors, and External Calls:** Contracts emit funding, dispute, settlement, credit, withdrawal, mint, audit, and royalty events and define typed errors.
- **Test Fixtures and Security Tests:** Hardhat tests cover state transitions, timeouts, ERC20, reentrancy, token roles/pausing/royalties, and factory indexing.
- **Deploy and Audit Limits:** README reports local compile/tests, uses a zero-filled placeholder PRIVATE_KEY, and supplies no independent audit report.

## Boundaries and risks

- The title says audited, but no independent audit report is supplied.
- Passing tests do not establish contract security.
- The .env key is a placeholder; use local/test networks only.

This package teaches the checked-in implementation and records gaps between the source and broader platform concepts named by the project. It does not certify security or production readiness.
