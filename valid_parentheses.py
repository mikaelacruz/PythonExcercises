"""
Valid Parentheses
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.


Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false


Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.

"""


def valid_parentheses(s):
    # stack to keep track of opening brackets
    stack = []
    top_element = ""

    # dictionary for keeping track of key:val pairs aka the brack pairs :)
    pairs = {")": "(", "}": "{", "]": "["}

    # for every bracket in the expression
    for char in s:
        # if the character is a closing bracket
        if char in pairs:
            # if stack is non empty,
            # pop the topmost element from the stack
            # else
            # assign a dummy value of "#" to the top_element variable
            if stack:
                top_element = stack.pop()
            else:
                top_element = "#"

            # if the pair for the opening bracket in our dictionary
            #    and the top element from teh stack don't match return False
            if pairs(char) != top_element:
                return False
            else:
                stack.append(char)
        # else we have an opening bracket, simply push it onto the stack
        else:
            stack.append(char)
    # in the end, if the stack is empty, then we have a valid expression
    # the stack won't be empty for cases like ((((((
    return not stack
