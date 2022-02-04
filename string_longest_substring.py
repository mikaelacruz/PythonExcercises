"""
Longest Substring
Find the longest substring in a given string s
For example in "abcabccc"
Output is: 3
Explanation: abc is a length of 3
"""


def longest_substring(s):
	max_sub_string = ""  # This variable will keep the longest sub-string
	curr_max_sub_string = ""  # and this is current longest sub-string

	for i in range(len(s)):
		if s[
			i] not in curr_max_sub_string:  # if current  word in s not in curr_max_sub_string, I add this char to
			# curr_max_sub_string
			curr_max_sub_string = curr_max_sub_string + s[i]
		else:  # if I have this char in my curr_max_sub_string
			if len(max_sub_string) < len(
					curr_max_sub_string):  # if length of curr_max_sub_string is bigger than max_sub_string then it
				# becomes new max_sub_string
				max_sub_string = curr_max_sub_string

				while len(curr_max_sub_string) > 0:  # This is the IMPORTANT PART
					if s[i] != curr_max_sub_string[0]:
						curr_max_sub_string = curr_max_sub_string[1::]
					else:
						curr_max_sub_string = curr_max_sub_string[1::]
						curr_max_sub_string = curr_max_sub_string + s[i]
						break
			else:
				while len(curr_max_sub_string) > 0:
					if s[i] != curr_max_sub_string[0]:
						curr_max_sub_string = curr_max_sub_string[1::]
					else:
						curr_max_sub_string = curr_max_sub_string[1::]
						curr_max_sub_string = curr_max_sub_string + s[i]
						break

	if len(max_sub_string) < len(curr_max_sub_string):  # I add this part to make sure my code works properly
		max_sub_string = curr_max_sub_string

	return len(max_sub_string)  # return length of max_sub_string
