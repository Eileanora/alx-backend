#!/usr/bin/env python3
"""LIFO Caching module
"""
BaseCaching = __import__("base_caching").BaseCaching


class LIFOCache(BaseCaching):
    """ Class the implements a caching system using the LIFO technique
    """
    def __init__(self):
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.keys.remove(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            key_removed = self.keys.pop()
            del self.cache_data[key_removed]
            print("DISCARD: {}".format(key_removed))

        self.cache_data[key] = item
        self.keys.append(key)

    def get(self, key):
        """ Get an item by key
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
