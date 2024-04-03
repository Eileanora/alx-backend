#!/usr/bin/env python3
"""Fifo Caching module
"""
from collections import deque
BaseCaching = __import__("base_caching").BaseCaching


class FIFOCache(BaseCaching):
    """ Class the implements a caching system using the FIFO technique
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
        return self.cache_data[key]
