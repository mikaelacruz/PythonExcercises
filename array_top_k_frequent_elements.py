"""
Top K Frequent Elements
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any
order.



Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]


Constraints:

1 <= nums.length <= 105
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.

"""


def topKFrequent(nums, k):
    count = {}
    max_items = []
    max_count = 0

    for i in nums:
        if i not in count:
            count[i] = 1
        else:
            count[i] += 1

    sorted_count = sorted(count.items(), key=lambda item: item[1], reverse=True)

    most_frequent = []

    for i in range(0, k):
        most_frequent.append(sorted_count[i][0])

    return most_frequent
