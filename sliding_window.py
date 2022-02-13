"""
Sliding Window Technique
Dynamic Programming Method
"""


def sliding_window_k_sized(elements, k):
    if len(elements) < k:
        return k
    for i in range(len(elements - k + 1)):
        print(elements[i:i + k])


def sliding_window_all_pairs(elements, k):
    if len(elements) < k:
        return k

    for i in range(len(elements)):
        print(elements[i:i + k])
