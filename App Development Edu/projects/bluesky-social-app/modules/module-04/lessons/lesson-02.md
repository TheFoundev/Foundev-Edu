# One shared feed and its stored snapshot: Trace the source

**Lesson ID:** `bluesky-social-app-04-state-and-persistence-lesson-02`  
**Module ID:** `bluesky-social-app-04-state-and-persistence`  
**Source focus:** `src/feedContext.tsx` → `feedContext`

## Purpose and learning objectives

Open `src/feedContext.tsx` and locate `feedContext`. Read the signature, guards, transformation, and return/state update in that order. By the end, explain the behavior and identify what the source does not establish.

## Prerequisites

Complete the previous lesson in this module. Read the project [README](../../../README.md) and [setup guide](../../../setup-guide.md).

## Progressive explanation

### Beginner explanation

In everyday terms, the code path behind **One shared feed and its stored snapshot** is like following one item through a workshop: locate the input, see what changes, then find the output. Context is the shared clipboard for screens; the store is the filing cabinet. Follow load, state initialization, effects that save changes, and the storage adapter. Inspect defaults for older saves with no bookmarks and malformed values.

### Step toward the implementation

Open `src/feedContext.tsx` and locate `feedContext`. Read the signature, guards, transformation, and return/state update in that order. The source files for this module are `src/feedContext.tsx`, `src/store.ts`, `src/persistence.ts`.

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
