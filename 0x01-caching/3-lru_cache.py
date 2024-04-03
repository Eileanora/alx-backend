#!/usr/bin/env python3
"""LRU Caching module
"""
from collections import deque
BaseCaching = __import__("base_caching").BaseCaching


class LRUCache(BaseCaching):
    """ Class the implements a caching system using the LRU technique
    """
    def __init__(self):
        super().__init__()
        self.keys = deque()

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is None or item is None:
            return

        self.cache_data[key] = item

        # check if it was there before to mark it as used
        if key in self.keys:
            self.keys.remove(key)
        self.keys.append(key)

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            key_removed = self.keys.popleft()
            del self.cache_data[key_removed]
            print("DISCARD: {}".format(key_removed))

    def get(self, key):
        """ Get an item by key
        """
        if key is None or key not in self.cache_data:
            return None
        self.keys.remove(key)
        self.keys.append(key)
        return self.cache_data[key]
