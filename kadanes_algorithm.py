"""
Kadane's Algorithm
Dynamic Programming
"""


def kadanes_algorithm(elements):
    max_sum = curr_sum = elements[0]

    for num in elements[1:]:
        curr_sum = max(curr_sum + num, num)
        max_sum = max(curr_sum, max_sum)
    return max_sum
