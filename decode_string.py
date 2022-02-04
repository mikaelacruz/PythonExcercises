"""
Decode String
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4].


"""
stack = []

cur_token, cur_number = '', 0

for char in s:

    if char == '[':
        # meet start symbol '['
        # save current token and current number into stack
        stack.append((cur_token, cur_number))

        # clear cur_token for new symbol in [ ]
        cur_token = ''

        # clear cur_number for new number in [ ]
        cur_number = 0

    elif char == ']':
        # meet ending symbol ']'
        # pop previous token and repeat times of current token from stack
        prev_token, repeat_times = stack.pop()

        # update current token with specified repeat times
        cur_token = prev_token + cur_token * repeat_times

    elif char.isdigit():

        # update current number
        cur_number = cur_number * 10 + int(char)

    else:

        # update current token
        cur_token += char

return cur_token
