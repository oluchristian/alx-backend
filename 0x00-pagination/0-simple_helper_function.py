#!/usr/bin/env python3
""" a function that takes two integer arguments page and page_size
"""


def index_range(page, page_size):
    """prints the start and end index of a page
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)
