#!/usr/bin/env python3
"""LFU Caching module
"""
from heapq import heapify, heappop
BaseCaching = __import__("base_caching").BaseCaching


class LFUCache(BaseCaching):
    """ Class the implements a caching system using the LFU technique
    """
    def __init__(self):
        super().__init__()
        self.keys = []
        heapify(self.keys)
        self.keys_freq = {}

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is None or item is None:
            return
        self.keys_freq[key] = self.keys_freq[key] + 1 if key in self.keys_freq else 1

        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            _, least_freq_key = heappop(self.keys)
            del self.cache_data[least_freq_key]
            del self.keys_freq[least_freq_key]
            print("DISCARD: {}".format(least_freq_key))

    def get(self, key):
        """ Get an item by key
        """
        if key is None or key not in self.cache_data:
            return None
        self.keys_freq[key] += 1
        return self.cache_data[key]
