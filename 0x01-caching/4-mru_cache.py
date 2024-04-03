#!/usr/bin/env python3
"""MRU Caching module
"""
from collections import deque
BaseCaching = __import__("base_caching").BaseCaching


class MRUCache(BaseCaching):
    """ Class the implements a caching system using the MRU technique
    """
    def __init__(self):
        super().__init__()
        self.keys = deque()

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is None or item is None:
            return

        if (len(self.cache_data) >= BaseCaching.MAX_ITEMS
                and key not in self.cache_data):
            key_removed = self.keys.pop()
            del self.cache_data[key_removed]
            print("DISCARD: {}".format(key_removed))

        self.cache_data[key] = item
        if key in self.keys:
            self.keys.remove(key)
        self.keys.append(key)

    def get(self, key):
        """ Get an item by key
        """
        if key is None or key not in self.cache_data:
            return None
        self.keys.remove(key)
        self.keys.append(key)
        return self.cache_data[key]
