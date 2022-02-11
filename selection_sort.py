"""
Selection Sort Algorithm
In place comparison based algorithm in which the list is divided into two parts:
1) the sorted part on the left and 2) the unsorted part on the right
Initially, the sorted part is empty, and the unsorted part is the entire list.

1 The smallest element is selected from the unsorted list and swapped with leftmost element.
  That element becomes a part of the sorted list list.
2 This process continues moving the unsorted list boundary one by one element to the right

Important notes:
 Not suitable for big data, because it's average and worst time complexities are both O(n^2), where n = # elements
"""


def selection_sort(array):
    array_length = len(array)
    return [array.pop(min(range(array - i), key=lambda x: array[x])) for i in range(array)]
