# Peyara Remote Mouse

Turn a phone into a wireless touchpad and keyboard.

> Turns a phone into a wireless mouse and keyboard for a computer using a small WebSocket relay.

## Overview

An original, self-contained implementation of the **Peyara Remote Mouse** concept, built for the Foundev portfolio. It has two halves:

- an **Expo app** with a connect screen, a touchpad and a keyboard,
- a **Node relay** that receives the events of the phone and drives the cursor of the computer with `robotjs`.

The protocol, the backoff of the reconnects and the settings of the app live in small modules with no imports, so both halves are covered by tests that run without a phone, without a network and without a React Native runtime.

## Features

- Connect screen that remembers the address of the relay on the device
- Touchpad with drag-to-move, left and right click, and scroll
- Keyboard screen that sends typed text and the special keys
- Automatic reconnect with a growing delay (1s, 2s, 4s, … up to 30s, five tries) and a visible status
- Relay that maps every event to a real action: move, click, scroll, type and key press
- The relay keeps working without `robotjs`: the actions are logged instead of performed
- 41 tests over the relay configuration, protocol, connection, settings and relay behavior

## Stack

`Node.js; Expo; React; React Native; TypeScript`
The stack is Node.js + Expo + React + React Native + TypeScript. The relay is a separate small Node process that only needs `ws`.

## Run

```bash
npm install
npm start          # the app: scan the QR code with Expo Go, or press w for web
npm run relay      # the relay, on the computer
```

The relay defaults to `ws://127.0.0.1:8765` with desktop input disabled. For a trusted LAN demo, start the relay with `HOST=0.0.0.0`, `ALLOW_NETWORK_LISTEN=true`, and (only if you want real mouse/keyboard control) `ENABLE_REAL_INPUT=true`; set the computer's LAN address in the app. Use PowerShell environment syntax on Windows, for example `$env:HOST='0.0.0.0'`. The relay has no TLS or client authentication, so do not expose it to the internet or an untrusted network.

## Structure

```text
peyara-remote-mouse/
├── App.tsx                 tab shell
├── src/protocol.ts          the events, their validation and the relay URL
├── src/connection.ts        the websocket, the status and the reconnect backoff
├── src/settings.ts          the settings store (key/value interface)
├── src/persistence.ts       the only module that imports AsyncStorage
├── src/data.ts              the shared store the screens read
├── src/screens/             one file per screen
├── src/components.tsx       small shared UI pieces
├── src/theme.ts             colours and spacing
├── test/                    the tests of the app
└── server/
    ├── relay.js             the logic of the relay (no ws, no robotjs)
    ├── index.js             the websocket server
    └── test/relay.test.js   the tests of the relay
```

## Testing

```bash
npm test           # the app and the relay
npm run test:app   # only the app
npm run test:relay # only the relay
npm run typecheck  # tsc --noEmit
```

The suite covers the protocol (every event type, the validation of a bad message, the encoding and the relay URL), the connection (the status changes, the backoff, the give-up after the last try, the manual disconnect), the settings (the last address, a corrupt value, the clearing) and the relay (the mapping of every event to a robotjs call, the fallback without robotjs, the counters).

## Notes and limitations

- The phone sends small JSON messages over a local WebSocket; the relay drives the cursor when `robotjs` is installed and logs the actions otherwise.
- Install `robotjs` in `server/` to move the real cursor; it is optional and may need build tools.
- Safe relay defaults bind only to loopback and log events; network binding requires the explicit `ALLOW_NETWORK_LISTEN=true` acknowledgement.
- Real desktop input is off by default and requires `ENABLE_REAL_INPUT=true` plus a working optional `robotjs` installation.
- For a phone-to-computer demo, both devices must be on the same trusted network. There is no pairing, authentication, or TLS, so do not expose the relay to the internet or an untrusted network.
- The touchpad sensitivity defaults to 1.5; configure `SENSITIVITY` from greater than 0 through 10 in the relay environment.

## License

MIT. See `LICENSE`.
