# Setup guide — BlueWallet

## Source location and tools

The editable source copy is `../../../projects/bluewallet/`. Keep this educational package separate from that app tree. Follow the source README and do not copy secrets into the client.

### JavaScript / Expo projects

Install a supported Node.js release and npm, then open the project directory and run `npm install`. Start with `npm start`; use Expo Go or the supported platform target described by that project. Run `npm test` for its test script and `npm run typecheck` where the package defines it. On Windows use `npm.cmd` if the PowerShell execution policy blocks `npm.ps1`.

### SwiftUI projects

On macOS, install Xcode and the XcodeGen tool if the README specifies it. In the project directory run `xcodegen generate`, open the generated project, and run its XCTest scheme in an iOS simulator. There is no claim that these commands were run in this package-generation environment.

## Project-specific configuration

- Check the project README before configuring any provider. Optional endpoints must be user-controlled and compatible.
- Peyara defaults to loopback, logging-only behavior. Do not enable network binding or real input except in a trusted isolated lab; it has no TLS or authentication.
- Rocket.Chat runs offline without an endpoint. A configured endpoint must be a real `wss://` endpoint; client-side `EXPO_PUBLIC_` values are public and must never contain secrets.
- BlueWallet is not a functioning wallet: it has no signing/keys and displays a placeholder address. Never use real funds.
- COVID Alert checks and symptom scores are simulations/informational only, not public-health or medical advice.

## Test and evidence record

Record the command, operating system, tool versions, result, and failures in your project log. A unit test using fakes is evidence for only that isolated behavior; it does not prove real API, network, native permission, UI, or deployment behavior.

## Troubleshooting

- If dependencies are absent, install only within the app source directory and follow its lockfile.
- If Node tests cannot compile TypeScript, verify that dependencies and local TypeScript are installed; do not substitute an unrecorded test result.
- If an iOS build tool is missing, use a Mac with Xcode. A YAML project spec by itself is not a built app.
- For connection failures, inspect the URL scheme, server version, network reachability, and actual server logs. Do not loosen security controls to make a demo appear connected.
