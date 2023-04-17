#!/usr/bin/env python3
"""
Simple helper function
"""

from typing import Tuple
import csv
import math
from typing import List


class Server:
    """
    Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """
        Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Takes in page and page_size and returns the appropriate page of
        the dataset.
        Returns an empty list if the input arguments are out of range
        for the dataset
        """
        assert isinstance(
            page, int) and page > 0, "Argument must be an integer > 0"
        assert isinstance(
            page_size, int) and page_size > 0, "Arg must be an integer > 0"
        # Retrieve the cached data using dataset() method
        dataset = self.dataset()
        # call index_range() to get start and end index using tuple unpacking
        start_index, end_index = index_range(page, page_size)
        if start_index >= page_size:
            return []
        # Return the appropriate slice of the dataset using list slicing
        return dataset[start_index:end_index]


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Takes two integer arguments and returns a tuple of size two containing
    a start index and an end index corresponding to the range of indexes
    to return in a list for those particular pagination parameters
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)
