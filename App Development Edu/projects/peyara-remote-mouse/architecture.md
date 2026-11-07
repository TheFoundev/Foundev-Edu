# Architecture — Peyara Remote Mouse

Build a phone touchpad and keyboard plus a WebSocket relay, with validated messages, reconnect logic, storage, and safe-by-default relay settings.

## Data and behavior map

1. **Agree on a small language of remote-control events** — `src/protocol.ts` (`export function decodeMessage`): Event union, JSON encoding, decoding, bounds, and unknown-event rejection. Related files: src/protocol.ts; server/relay.js; test/protocol.test.ts.
2. **Turn gestures and text into protocol messages** — `src/screens/TouchpadScreen.tsx` (`PanResponder.create`): PanResponder deltas, click/scroll actions, text and key events. Related files: src/screens/TouchpadScreen.tsx; src/screens/KeyboardScreen.tsx; src/data.ts.
3. **Connect, report status, and retry carefully** — `src/connection.ts` (`export class RelayConnection`): Socket lifecycle, connection snapshots, exponential delay, max retry, and manual disconnect. Related files: src/connection.ts; src/data.ts; test/connection.test.ts.
4. **Remember the relay address with a storage seam** — `src/settings.ts` (`export async function loadSettings`): Host validation, settings key, AsyncStorage adapter, and load/save flow. Related files: src/settings.ts; src/persistence.ts; src/screens/ConnectScreen.tsx.
5. **Map validated events to host actions under explicit controls** — `server/config.js` (`function readConfig`): Loopback default, bind acknowledgement, port/sensitivity validation, opt-in robotjs, event mapping. Related files: server/config.js; server/relay.js; server/index.js; server/test/config.test.js.
6. **Debug one event from finger to cursor** — `server/relay.js` (`function createRelay`): End-to-end protocol path, fallback logging, and evidence from isolated tests. Related files: src/data.ts; src/connection.ts; server/index.js; server/relay.js; server/test/relay.test.js.
7. **Operate the relay without exposing a control port** — `server/index.js` (`new WebSocketServer`): Safe defaults, trusted LAN warning, robotjs native dependency, and shutdown/review. Related files: server/config.js; server/index.js; README.md.
8. **Deliver a tested phone-to-host demo** — `src/data.ts` (`export function connect`): Integration checklist, UI feedback, observable connection state, demonstration, and safe teardown. Related files: App.tsx; src/protocol.ts; src/connection.ts; src/components.tsx; src/theme.ts; server/config.js; test/connection.test.ts.

## Runtime boundaries

- Stack: Expo, React Native, TypeScript, Node.js, WebSocket, optional robotjs.
- Explicit limits across modules: ['Validation narrows malformed input but does not authenticate a sender', 'Only the relay can control the host; the mobile UI itself does not perform desktop input', 'Retry logic does not add TLS, pairing, or authentication to the relay', 'A LAN address is private configuration; only connect to a relay you trust', 'There is no TLS or client authentication; network use remains unsafe on untrusted networks', 'The test suite does not prove the phone and host can reach each other on a real network', 'No pairing, TLS, client authentication, or internet-safe deployment is included', 'Do not operate the unauthenticated relay outside a controlled trusted environment'].
- Source code is the implementation of record; compare each claim with project README and tests.
- Read each lesson’s directly quoted source excerpt and linked source path before changing behavior.
- No application is claimed to have been deployed or connected to production infrastructure.
