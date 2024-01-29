#!/usr/bin/env python3
'''Module containing the index_range function'''
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    '''Returns a tuple containing the start and end indexes'''
    return ((page - 1) * page_size, page * page_size)
