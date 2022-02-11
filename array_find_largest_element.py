"""
Find the largest element in an array
"""


def array_find_largest_element(array) -> int:
    max_element = array[0]
    for i in range(1, len(array)):
        if array[i] > max_element:
            max_element = array[i]
    return max_element
