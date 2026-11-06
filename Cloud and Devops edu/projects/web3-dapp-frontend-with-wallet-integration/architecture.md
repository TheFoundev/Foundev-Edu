# Architecture

## Implemented system

Keccak implementation, address helper, decimal-unit conversion, transfer ABI encoder, static page, browser wallet connection and eth_sendTransaction call.

## Data and control flow

User input → address/amount checks → encode selector/arguments → injected wallet request → wallet approval/sign/broadcast → transaction hash display.

## Module source map

- **Understand Injected Wallet Providers:** connect uses eth_requestAccounts and reads eth_chainId from window.ethereum.
- **Validate Address Shape and Checksum:** isAddress checks 40 hex characters; hasValidChecksum computes Keccak casing; README notes checksum validation limits in UI.
- **Convert Human Units to Base Units:** parseUnits accepts digits and optional fraction up to decimals; formatUnits converts BigInt back.
- **Understand Keccak-256 Implementation:** Custom 24-round Keccak-f permutation uses BigInt lanes and rate 136 bytes.
- **Encode ERC20 Transfer Calldata:** TRANSFER_SELECTOR a9059cbb; encodeTransfer pads address and uint256 amount.
- **Construct and Request a Wallet Transaction:** Request params include from account, token contract address, and data.
- **Inspect Errors and User Safety:** The UI displays hash/error text; it does not wait for receipt confirmation.
- **Review Project Scope and Tests:** encodeTransfer builds ERC20 calldata; the source has no contract deployment, event history, on-chain query, or receipt confirmation.

## Boundaries and risks

- No contract deployment, on-chain state reader, event listener, or transaction history is implemented.
- The UI checks address shape but does not call EIP-55 checksum validation before encoding.
- No EIP-55 checksum checking is implemented according to README; custom Keccak code needs independent validation before financial use.
- Wallet connection and sending requests require an injected provider; a transaction hash does not mean confirmation/success.
- Only ERC20 transfer calldata is encoded; token contract semantics are not verified.

This package teaches the checked-in implementation and records gaps between the source and broader platform concepts named by the project. It does not certify security or production readiness.
