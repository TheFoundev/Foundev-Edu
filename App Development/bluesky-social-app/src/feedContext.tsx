import React, { createContext, useCallback, useContext, useEffect, useMemo, useState } from 'react';
import { feedStore } from './persistence';
import {
  canPublish,
  publishPost,
  toggleLike as toggleLikeState,
  toggleBookmark as toggleBookmarkState,
  type BookmarkMap,
  type LikeMap,
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
  const [ready, setReady] = useState(false);

  useEffect(() => {
    let cancelled = false;

    (async () => {
      const saved = await feedStore.load();
      if (cancelled) return;
      if (saved.posts.length > 0) setPosts(saved.posts);
      if (Object.keys(saved.liked).length > 0) setLiked(saved.liked);
      if (Object.keys(saved.bookmarks).length > 0) setBookmarks(saved.bookmarks);
      setReady(true);
    })();

    return () => {
      cancelled = true;
    };
  }, []);

  // Write the state back whenever it changes, but not before it was loaded.
  useEffect(() => {
    if (!ready) return;
    void feedStore.save({ posts, liked, bookmarks });
  }, [posts, liked, bookmarks, ready]);

  const publish = useCallback((text: string) => {
    if (!canPublish(text)) return false;
    setPosts((current) => publishPost(current, text));
    return true;
  }, []);

  const toggle = useCallback((postId: string) => {
    setLiked((current) => toggleLikeState(current, postId));
  }, []);

  const toggleBookmark = useCallback((postId: string) => {
    setBookmarks((current) => toggleBookmarkState(current, postId));
  }, []);

  const value = useMemo(
    () => ({ posts, liked, bookmarks, ready, publish, toggle, toggleBookmark }),
    [posts, liked, bookmarks, ready, publish, toggle, toggleBookmark],
  );

  return <FeedContext.Provider value={value}>{children}</FeedContext.Provider>;
}

/** The feed state. Throws when it is used outside the provider. */
export function useFeed(): FeedContextValue {
  const value = useContext(FeedContext);
  if (!value) throw new Error('useFeed must be used inside a FeedProvider');
  return value;
}
