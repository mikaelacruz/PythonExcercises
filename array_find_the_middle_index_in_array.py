"""
Find the Middle Index in Array same as find the pivot index
Given a 0-indexed integer array nums, find the leftmost middleIndex
(i.e., the smallest amongst all the possible ones).

A middleIndex is an index where
nums[0] + nums[1] + ... + nums[middleIndex-1] == nums[middleIndex+1] + nums[middleIndex+2] + ... + nums[nums.length-1].

If middleIndex == 0, the left side sum is considered to be 0.
Similarly, if middleIndex == nums.length - 1, the right side sum is considered to be 0.

Return the leftmost middleIndex that satisfies the condition, or -1 if there is no such index.



Example 1:

Input: nums = [2,3,-1,8,4]
Output: 3
Explanation: The sum of the numbers before index 3 is: 2 + 3 + -1 = 4
The sum of the numbers after index 3 is: 4 = 4
Example 2:

Input: nums = [1,-1,4]
Output: 2
Explanation: The sum of the numbers before index 2 is: 1 + -1 = 0
The sum of the numbers after index 2 is: 0
Example 3:

Input: nums = [2,5]
Output: -1
Explanation: There is no valid middleIndex.


Constraints:

1 <= nums.length <= 100
-1000 <= nums[i] <= 1000

#############################################
SOLUTION

Approach #1: Prefix Sum [Accepted]
Intuition and Algorithm

We need to quickly compute the sum of values to the left and the right of every index.

Let's say we knew S as the sum of the numbers, and we are at index i.
If we knew the sum of numbers leftsum that are to the left of index i,
then the other sum to the right of the index would just be S - nums[i] - leftsum.

As such, we only need to know about leftsum to check whether an index is a pivot index in constant time.
Let's do that: as we iterate through candidate indexes i, we will maintain the correct value of leftsum.

Complexity Analysis

Time Complexity: O(N)O(N), where NN is the length of nums.

Space Complexity: O(1)O(1), the space used by leftsum and S.
"""


def middle_index(nums):
    s = sum(nums)
    left_sum = 0
    for i, x in enumerate(nums):
        if left_sum == (s - left_sum - x):
            return i
        left_sum += x
    return -1
