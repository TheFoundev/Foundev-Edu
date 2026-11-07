# Architecture — Rocket.Chat Mobile

Build a channel/message mobile demo with a small DDP client, typed mapping, persistent offline state, and an explicit endpoint configuration boundary.

## Data and behavior map

1. **Channels and messages as typed records** — `src/chat.ts` (`export type Channel`): Channel/ChatMessage models, seeded data, and unread display. Related files: src/chat.ts; src/data.ts; src/screens/ChannelsScreen.tsx.
2. **A client opens a socket and speaks DDP messages** — `src/chat.ts` (`export class DdpClient`): Socket abstraction, connect/session, method IDs, ping/pong, timeout and close. Related files: src/chat.ts; test/chat.test.ts.
3. **Map server-shaped data and manage channels/messages** — `src/chat.ts` (`export function toMessages`): toChannels/toMessages, filtering, unread counts, optimistic append. Related files: src/chat.ts; src/screens/ChatScreen.tsx; src/screens/ChannelsScreen.tsx.
4. **Make offline mode explicit and reject placeholders** — `src/chat.ts` (`export function isConfiguredChatEndpoint`): EXPO_PUBLIC_CHAT_URL, secure WebSocket validation, `.example` rejection, idle status. Related files: src/chat.ts; src/chatContext.tsx; test/chat.test.ts.
5. **Hydrate local chat state and coordinate shared actions** — `src/store.ts` (`export class ChatStore`): AsyncStorage adapter, load/save effects, context actions, and optimistic state. Related files: src/store.ts; src/chatContext.tsx.
6. **Connect channels, messages, and profile UI** — `src/screens/ChatScreen.tsx` (`export default function ChatScreen`): Tab shell, selected channel, offline banner, reconnect control, shared components, and status rendering. Related files: App.tsx; src/screens/ChatScreen.tsx; src/screens/ChannelsScreen.tsx; src/screens/ProfileScreen.tsx; src/components.tsx; src/theme.ts.
7. **Test protocol edges and plan a compatible server demo** — `test/chat.test.ts` (`fakeSocket`): Fake socket assertions, endpoint test cases, dependency and provider review. Related files: test/chat.test.ts; package.json; README.md.

## Runtime boundaries

- Stack: Expo, React Native, TypeScript, AsyncStorage, WebSocket, Rocket.Chat DDP demo client.
- Explicit limits across modules: ['Seed rows are local demo content and do not prove a server account exists', 'The app-specific methods channels.list, chat.sendMessage, and chat.getMessages are not verified Rocket.Chat method names; DDP method calls are marked deprecated in current Rocket.Chat documentation', 'Method names and response shapes are a demo contract; confirm them against the target server version', 'Only a compatible real wss endpoint should be configured; no server was tested here', 'Local chat persistence is not end-to-end encrypted server sync', 'The app has no login, push notification integration, or upstream client parity', 'Current Rocket.Chat docs recommend REST by default and mark DDP method calls deprecated; the custom method names in this source have not been verified against a server'].
- Source code is the implementation of record; compare each claim with project README and tests.
- Read each lesson’s directly quoted source excerpt and linked source path before changing behavior.
- No application is claimed to have been deployed or connected to production infrastructure.
