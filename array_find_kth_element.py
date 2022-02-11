"""
Find kth element in an array
1) Find largest kth element in an array
2) Find smallest kth element in an array
"""
from heapq import heapify, heappush, heappop


def find_kth_largest(nums, k):
    heap = []
    heapify(heap)

    for num in nums:
        heappush(heap, num)
        if len(heap) > k:
            heappop(heap)

    return heappop(heap)



# could improve time by incorporating quick select's partitioning method but worst case is O(n^2)
