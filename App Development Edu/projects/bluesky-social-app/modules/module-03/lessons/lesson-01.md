# Likes and saved posts: Begin with the idea

**Lesson ID:** `bluesky-social-app-03-interactions-lesson-01`  
**Module ID:** `bluesky-social-app-03-interactions`  
**Source focus:** `src/screens/FeedScreen.tsx` → `FeedScreen`

## Purpose and learning objectives

Before reading the excerpt, name the input, the result the user expects, and one assumption the app makes. By the end, explain the behavior and identify what the source does not establish.

## Prerequisites

Basic programming and a way to read the source project.Read the project [README](../../../README.md) and [setup guide](../../../setup-guide.md).

## Progressive explanation

### Beginner explanation

Imagine **Likes and saved posts** as a small part of a phone app: it receives a value or action and helps produce a result. This module’s plain-language model is: A like or bookmark is a personal switch keyed by post ID. Trace each button into its toggle function, then inspect how bookmarkedPosts resolves IDs back into feed records while keeping feed order.

### Step toward the implementation

Before reading the excerpt, name the input, the result the user expects, and one assumption the app makes. The source files for this module are `src/screens/FeedScreen.tsx`, `src/screens/ProfileScreen.tsx`, `src/feed.ts`.

## Source evidence

Excerpt from [`src/screens/FeedScreen.tsx`](../../../../../../App%20Development/bluesky-social-app/src/screens/FeedScreen.tsx); copied from the source, not executed during package refinement. Read surrounding lines for full context.

```tsx
import { topics } from '../data';
import { useFeed } from '../feedContext';
import { filterByTopic, likeCount, MAX_POST_LENGTH } from '../feed';

export default function FeedScreen() {
  const { posts, liked, bookmarks, publish, toggle, toggleBookmark } = useFeed();
  const [draft, setDraft] = useState('');
  const [filter, setFilter] = useState('All');

  function onPublish() {
    if (publish(draft)) setDraft('');
  }

  const visible = filterByTopic(posts, filter);

  return (
    <Screen title="Bluesky" subtitle="A small feed for people building things.">
      <View style={styles.chips}>
        {['All', 'buildinpublic', 'engineering', 'design'].map((topic) => (
          <Pressable key={topic} onPress={() => setFilter(topic)}>
            <Pill label={topic === 'All' ? 'All' : `#${topic}`} tone={filter === topic ? 'brand' : 'default'} />
          </Pressable>
        ))}
      </View>
```

### Read it step by step

1. Find the focus cue `FeedScreen` and identify its arguments or input values.
2. Follow the condition or transformation and identify the returned value or state update.
3. Trace one caller and compare the result with the README claim.
4. Note any local-only, mock, placeholder, or external-service boundary.

## Expected behavior and boundaries

The lesson should produce a source-backed explanation of **Likes and saved posts**. A test or code excerpt establishes only the behavior it covers; it does not prove an external API, device, deployment, or provider works.

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

You began with the module’s plain meaning, traced `FeedScreen` in `src/screens/FeedScreen.tsx`, and identified one limit or testable boundary.

## Knowledge checks

1. What input or action reaches the source focus?
2. What does the code change or return?
3. Which edge case or integration boundary needs verification?

## References

- [Project README](../../../README.md)
- [Setup guide](../../../setup-guide.md)
- [Source file](../../../../../../App%20Development/bluesky-social-app/src/screens/FeedScreen.tsx)
