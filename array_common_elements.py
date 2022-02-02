"""Common Elements in Two Sorted Arrays
return the two common elements (as an array) between two sorted arrays of integers
(ascending order)
Example:  The common elements between [1, 3, 4, 6, 7, 9] and [1, 2, 4, 5, 9, 10]
    are [1, 4, 9]
"""


def common_elements(a, b):
    a_index = 0
    b_index = 0

    result = []

    while a_index < len(a) and b_index < len(b):
        if a[a_index] == b[b_index]:
            result.append(a[a_index])
            a_index += 1
            b_index += 2
        elif a[a_index] > b[b_index]:
            b_index += 1
        else:
            a_index += 1
    return result
