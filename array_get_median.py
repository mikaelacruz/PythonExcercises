"""
Get Median of Array

Method gets the median of an array
"""


def get_median(nums):
    median = len(nums) / 2

    if len(nums) % 1 == 1:
        average_median = ((nums[int(median)] + nums[int(median - 1)]) / 2)
        return average_median
    else:
        average_median = len(nums) / 2
        return average_median
