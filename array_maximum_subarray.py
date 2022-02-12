"""
Maximum Subarray
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum
and return its sum.

A subarray is a contiguous part of an array.

Possible solutions!
1) Dynamic Programming 2) Divide and Conquer

Let's do Dynamic Programming - Kadane's Algorithm.

Leetcode states, "Whenever you have a question that asks for the maximum or minimum of anything,
consider using dynamic programming!"

For this problem, we need to focus on one thing: Where the largest sum array begins.
Example 1:
If we have an example of nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
We can see the subarray could not be the first 3 elements, because the overall sum would always
    subtract from the total. There, the subarray either starts at the first 4, or somewhere further right.

Example 2:
nums = [-2, 100000000000, -3, 4, -1, 2, 1, -5, 4]
We can see that our conclusion from Example 1 wouldn't fit this case.

Overall conclusion from Example 1 and Example 2: We need a GENERAL way to figure out when
                                                 a part of the array is worth keeping.


How about: Any subarray whose sum is positive is worth keeping?
Let's try that. (I'll also upload my hand drawn notes to this repo as a pdf)
"""

def maximum_subarray(nums):
    # Initialize our variables using the first element
    # This is because we already know we are comparing elements - why not start with the first?
    # current_subarray_sum will be the sum of all the elements in subarray we are looking at
    # max_subarray_sum will be the final output of the subarray sum
    #    We will continuously update max_subarray_sum as we iterate through
    # current_subarray will be the actual subarray that contains the elements we are collection

    current_subarray_sum = max_subarray_sum = nums[0]

    for num in nums[1:]:
        current_subarray_sum = max(num, current_subarray_sum + num)
        max_subarray_sum = max(max_subarray_sum, current_subarray_sum)
    return max_subarray_sum
