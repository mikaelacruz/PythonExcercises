"""
Sort a Dictionary
using list comprehension and sorted method
"""

# Having reverse = True makes in most -> lease
def sort_dictionary(nums):
    new_nums = sorted(nums.items(), key=lambda item: item[1], reverse=True)
    return new_nums
