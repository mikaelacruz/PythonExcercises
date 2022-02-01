"""CONTAINS DUPLICATION

Given an integer array nums, return TRUE if any value appears at least twice in the array,
return FALSE if every element is distinct
"""
# Input
nums = [ 1, 2, 3, 1]
counted_dict = {}

# Looping through the input array/list
for num in nums:
# If the element is in the counted dict
    if num in counted_dict:
# Then we have a duplicate!!
# Returning True
        return True
    # Else, this element is new and we add it to the counted dict
    else:
        counted_dict[num] = 1
# We didn't find any duplicates at all :(
return False

# Output
# Should be TRUE
