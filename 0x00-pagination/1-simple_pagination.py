#!/usr/bin/env python3
'''Module containing the index_range function'''
from typing import Tuple
import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    '''Returns a tuple containing the start and end indexes'''
    return ((page - 1) * page_size, page * page_size)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        '''Gets the page from the dataset'''
        assert(type(page) == int and type(page_size) == int)
        assert(page > 0 and page_size > 0)
        start, end = index_range(page, page_size)
        ans = []
        if start >= len(self.dataset()):
            return ans
        ans = self.dataset()
        return ans[start:end]
