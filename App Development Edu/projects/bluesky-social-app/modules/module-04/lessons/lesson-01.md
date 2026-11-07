# One shared feed and its stored snapshot: Begin with the idea

**Lesson ID:** `bluesky-social-app-04-state-and-persistence-lesson-01`  
**Module ID:** `bluesky-social-app-04-state-and-persistence`  
**Source focus:** `src/feedContext.tsx` → `feedContext`

## Purpose and learning objectives

Before reading the excerpt, name the input, the result the user expects, and one assumption the app makes. By the end, explain the behavior and identify what the source does not establish.

## Prerequisites

Basic programming and a way to read the source project.Read the project [README](../../../README.md) and [setup guide](../../../setup-guide.md).

## Progressive explanation

### Beginner explanation

Imagine **One shared feed and its stored snapshot** as a small part of a phone app: it receives a value or action and helps produce a result. This module’s plain-language model is: Context is the shared clipboard for screens; the store is the filing cabinet. Follow load, state initialization, effects that save changes, and the storage adapter. Inspect defaults for older saves with no bookmarks and malformed values.

### Step toward the implementation

Before reading the excerpt, name the input, the result the user expects, and one assumption the app makes. The source files for this module are `src/feedContext.tsx`, `src/store.ts`, `src/persistence.ts`.

## Source evidence

Excerpt from [`src/feedContext.tsx`](../../../../../../App%20Development/bluesky-social-app/src/feedContext.tsx); copied from the source, not executed during package refinement. Read surrounding lines for full context.

```tsx
type Post,
} from './feed';
import { seedPosts } from './data';

type FeedContextValue = {
  posts: Post[];
  liked: LikeMap;
  bookmarks: BookmarkMap;
  ready: boolean;
  publish: (text: string) => boolean;
  toggle: (postId: string) => void;
  toggleBookmark: (postId: string) => void;
};

const FeedContext = createContext<FeedContextValue | null>(null);

/**
 * Holds the feed and the likes, restores them from storage on start and
 * writes every change back.
 */
export function FeedProvider({ children }: { children: React.ReactNode }) {
  const [posts, setPosts] = useState<Post[]>(seedPosts);
  const [liked, setLiked] = useState<LikeMap>({});
  const [bookmarks, setBookmarks] = useState<BookmarkMap>({});
```

### Read it step by step

1. Find the focus cue `feedContext` and identify its arguments or input values.
2. Follow the condition or transformation and identify the returned value or state update.
3. Trace one caller and compare the result with the README claim.
4. Note any local-only, mock, placeholder, or external-service boundary.

## Expected behavior and boundaries

The lesson should produce a source-backed explanation of **One shared feed and its stored snapshot**. A test or code excerpt establishes only the behavior it covers; it does not prove an external API, device, deployment, or provider works.

## Practical exercise

Complete [`exercise-01.json`](../exercises/exercise-01.json). Add an input or edge case, cite the source, and write the expected result before changing code.

## Common mistakes and debugging

- Inferring feature behavior from the product name or screen alone.
- Skipping the caller, model/state layer, or error path.
- Treating local sample data or a mock response as a real service result.
- Debug by tracing input → validation → transformation → output and then checking the relevant test.

## Best practices and security

Protect credentials and personal data, validate untrusted inputs, request only necessary device permissions, and keep provider/device behavior explicitly unverified until tested in an authorized environment.

## Summary

You began with the module’s plain meaning, traced `feedContext` in `src/feedContext.tsx`, and identified one limit or testable boundary.

## Knowledge checks

1. What input or action reaches the source focus?
2. What does the code change or return?
3. Which edge case or integration boundary needs verification?

## References

- [Project README](../../../README.md)
- [Setup guide](../../../setup-guide.md)
- [Source file](../../../../../../App%20Development/bluesky-social-app/src/feedContext.tsx)
