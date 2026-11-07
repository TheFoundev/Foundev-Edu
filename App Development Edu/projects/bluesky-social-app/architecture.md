# Architecture — Bluesky Social App

Build a local-first social-feed learning app with publishing, topic filtering, profile views, likes, bookmarks, and resilient persistence.

## Data and behavior map

1. **The feed as a small library** — `src/feed.ts` (`export function canPublish`): Post records, seed fixtures, and pure feed operations. Related files: src/data.ts; src/feed.ts.
2. **From typed text to a post** — `src/feed.ts` (`export function publishPost`): Composer validation, length limits, and immutable insertion. Related files: src/screens/FeedScreen.tsx; src/feed.ts.
3. **Likes and saved posts** — `src/feed.ts` (`export function toggleBookmark`): LikeMap, BookmarkMap, toggles, and the saved-post projection. Related files: src/screens/FeedScreen.tsx; src/screens/ProfileScreen.tsx; src/feed.ts.
4. **One shared feed and its stored snapshot** — `src/store.ts` (`export class FeedStore`): Context state lifecycle, storage adapter, migration defaults, and corrupt data. Related files: src/feedContext.tsx; src/store.ts; src/persistence.ts.
5. **Screens, reusable controls, and app shell** — `App.tsx` (`const TABS`): Tab selection, screen composition, action props, and theme tokens. Related files: App.tsx; src/screens/FeedScreen.tsx; src/screens/DiscoverScreen.tsx; src/screens/ProfileScreen.tsx; src/components.tsx; src/theme.ts.
6. **Test the model and define the network boundary** — `test/feed.test.ts` (`toggleBookmark`): Node test coverage, pure-model boundaries, and absent protocol integration. Related files: test/feed.test.ts; README.md; package.json.
7. **Integrating a coherent social-feed release** — `src/feedContext.tsx` (`toggleBookmark`): End-to-end feature tracing, persistence evidence, and safe demo scope. Related files: App.tsx; src/feedContext.tsx; src/screens/FeedScreen.tsx; src/screens/ProfileScreen.tsx; test/feed.test.ts.

## Runtime boundaries

- Stack: Expo, React Native, TypeScript, AsyncStorage.
- Explicit limits across modules: ['Posts are local sample records; mergeRemotePosts is a helper and does not itself call a network', 'Publishing stores a local post; there is no authenticated AT Protocol write', 'Bookmarks and likes are per-device demo state, not synced account records', 'AsyncStorage is persistent local key/value storage; it is not encrypted account sync', 'The tabs and suggested feeds are local UI; they are not loaded from a Bluesky server', 'No AT Protocol login, moderation, network feed, or remote post creation is implemented', 'The app is a learning implementation, not upstream Bluesky client parity'].
- Source code is the implementation of record; compare each claim with project README and tests.
- Read each lesson’s directly quoted source excerpt and linked source path before changing behavior.
- No application is claimed to have been deployed or connected to production infrastructure.
