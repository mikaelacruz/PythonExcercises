"""
Sort an unsorted array
Two methods:
1 Selection Sort
2 Counting Sort
"""

import counting_sort


def sort_unsorted_array(array):
    return counting_sort.counting_sort_no_k(array)
