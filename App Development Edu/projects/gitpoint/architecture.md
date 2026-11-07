# Architecture — GitPoint

Build a GitHub-oriented repository and issue browser with API mapping, search/filtering, cached state, and clear authentication limits.

## Data and behavior map

1. **Repositories and issues as typed records** — `src/github.ts` (`export type Repo`): Repository/issue shapes, response mapping, sample data, and sort fields. Related files: src/github.ts; src/data.ts.
2. **Make and interpret GitHub API requests** — `src/github.ts` (`export class GitHubClient`): Fetch client, request paths, headers, response mapping, GitHubError, and rate-limit headers. Related files: src/github.ts; test/github.test.ts.
3. **Turn a list into useful repository and issue views** — `src/github.ts` (`export function searchRepos`): Search fields, date ordering, state filters, and list rendering. Related files: src/github.ts; src/screens/ReposScreen.tsx; src/screens/IssuesScreen.tsx.
4. **Keep a last-known view when storage or network fails** — `src/store.ts` (`export class CacheStore`): Cache keys, load/save, corrupt data, provider startup, and fallback state. Related files: src/store.ts; src/githubContext.tsx; test/github.test.ts.
5. **Connect the app shell to repository and issue screens** — `src/githubContext.tsx` (`export function GitHubProvider`): Context lifecycle, tabs, profile/repository/issue states, and reusable controls. Related files: App.tsx; src/githubContext.tsx; src/screens/ReposScreen.tsx; src/screens/IssuesScreen.tsx; src/screens/ProfileScreen.tsx; src/components.tsx; src/theme.ts.
6. **Verify API logic and plan safe integration** — `test/github.test.ts` (`fakeFetch`): Mock response evidence, test script, public API boundary, and token risk. Related files: test/github.test.ts; package.json; README.md.

## Runtime boundaries

- Stack: Expo, React Native, TypeScript, GitHub REST API, AsyncStorage.
- Explicit limits across modules: ['Seed data is a fallback/demo and should not be confused with live account data', 'Authentication, token storage, pagination breadth, and current provider quotas need review before production use', 'Filtering the current dataset is not the same as server-side search across all GitHub', 'Cached repository/issue data can be stale and is not evidence of a current provider response', 'The UI does not reproduce every capability or policy of the upstream GitPoint app', 'Do not put a personal access token in a client bundle or commit it into source'].
- Source code is the implementation of record; compare each claim with project README and tests.
- Read each lesson’s directly quoted source excerpt and linked source path before changing behavior.
- No application is claimed to have been deployed or connected to production infrastructure.
