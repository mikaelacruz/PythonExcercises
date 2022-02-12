"""
Median of Two Sorted Arrays

Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).



Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.


Constraints:

nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106



Solution:
1) Must merge two arrays together
2) Find median

Runtime: 80 ms, faster than 96.21% of Python3 online submissions for Median of Two Sorted Arrays.
Memory Usage: 14.5 MB, less than 41.24% of Python3 online submissions for Median of Two Sorted Arrays.
I took a rather easy approach.
First generate a sorted list of the two input lists combined,
then find the middle one (or middle two, and take the average of those).
But you don't need to sort all of it, you just need to sort until you hit the middle.
"""


def find_median_two_sorted_arrays(nums1, nums2):
    # Get the lengths of both lists
    l1, l2 = len(nums1), len(nums2)
    # Determine the middle
    middle = (l1 + l2) / 2

    # EDGE CASE:
    # If we only have 1 value (e.g. [1], []), return nums1[0] if the length of
    # that list is greater than the length of l2, otherwise return nums2[1]
    if middle == 0.5:
        return float(nums1[0]) if l1 > l2 else float(nums2[0])

    # Initialize 2 pointers
    x = y = 0
    # Initialize 2 values to store the previous and current value (in case of an even
    # amount of values, we need to average 2 values)
    cur = prev = 0
    # Determine the amount of loops we need. If the middle is even, loop that amount + 1:
    # eg: [1, 2, 3, 4, 5, 6]        6 values, middle = 3, loops = 3+1
    #            ^  ^
    #            |  +-- cur
    #            +----- prev
    # If the middle is odd, loop that amount + 0.5
    # eg: [1, 2, 3, 4, 5]           5 values, middle = 2.5, loops = 2.5+0.5
    #            ^
    #            +--- cur
    loops = middle + 1 if middle % 1 == 0 else middle + 0.5

    # Walk forward the amount of loops
    for _ in range(int(loops)):
        # Store the value of cur in prev
        prev = cur
        # If the x pointer is equal to the amount of elements of nums1 (l1 == len(nums1))
        if x == l1:
            # Store nums2[y] in cur, 'cause we hit the end of nums1
            cur = nums2[y]
            # Move the y pointer one ahead
            y += 1
            # If the y pointer is equal to the amount of elements of nums2 (l2 == len(nums2))
        elif y == l2:
            # Store nums1[x] in cur, 'cause we hit the end of nums2
            cur = nums1[x]
            # Move the x pointer one ahead
            x += 1
            # If the value in nums1 is bigger than the value in nums2
        elif nums1[x] > nums2[y]:
            # Store nums2[y] in cur, because it's the lowest value
            cur = nums2[y]
            # Move the y pointer one ahead
            y += 1
            # If the value in nums2 is bigger than the value in nums1
        else:
            # Store nums1[x] in, because it's the lowest value
            cur = nums1[x]
            # Move the x pointer one ahead
            x += 1

    # If middle is even
    if middle % 1 == 0.0:
        # Return the average of the cur + prev values (which will return a float)
        return (cur + prev) / 2
    # If middle is odd
    else:
        # Return the cur value, as a float
        return float(cur)
