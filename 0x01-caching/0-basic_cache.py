#!/usr/bin/env python3
"""BaseCache Module
"""
BaseCaching = __import__("base_caching").BaseCaching


class BasicCache(BaseCaching):
    """ Basic Cache module
    """
    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
