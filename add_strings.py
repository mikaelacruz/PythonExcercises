"""
Add Strings
Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.

You must solve the problem without using any built-in library for handling large integers (such as BigInteger).
You must also not convert the inputs to integers directly.



Example 1:

Input: num1 = "11", num2 = "123"
Output: "134"
Example 2:

Input: num1 = "456", num2 = "77"
Output: "533"
Example 3:

Input: num1 = "0", num2 = "0"
Output: "0"


Constraints:

1 <= num1.length, num2.length <= 104
num1 and num2 consist of only digits.
num1 and num2 don't have any leading zeros except for the zero itself.
"""
def add_strings(num_1, num_2):

    # empty result structure
    result = []

    # start from carry = 0
    carry = 0

    # sets pointers for the end of each string
    point_1 = len(num_1) - 1
    point_2 = len(num_2) - 1

    # loop over strings from beginning to end of string using point_1 and point_2
    while point_1 >= 0 or point_2 >= 0:
        # set x1 and x2 equal to a digit from a respective string if reached the beginning of num_1 and num_2
        # otherwise, x1 and x2 = 0
        x1 = ord(num_1[point_1]) - ord('0') if point_1 >= 0 else 0
        x2 = ord(num_2[point_2]) - ord('0') if point_2 >= 0 else 0
        # compute the current value and update carry
        value = (x1 + x2 + carry) % 10
        carry = (x1 + x2 + carry) // 10
        # append the current value to the result
        result.append(value)
        point_1 -= 1
        point_2 -= 1
        # now both strings are done, if the carry is STILL non zero, append to the result
    if carry:
        result.append(carry)
    return ''.join(str(x) for x in result[::-1])
