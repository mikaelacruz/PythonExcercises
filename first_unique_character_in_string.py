"""
First Unique Character in a String
Given a string s, find the first non-repeating character in it and return its index.
If it does not exist, return -1.
"""
import collections
from collections import Counter

# SOLUTION 1

# TIME COMPLEXITY O(N) SINCE WE GO THROUGH THE STRING OF LENGTH N TWO TIMES
# SPACE COMPLEXITY O(1) BECAUSE ENGLISH ALPHABET CONTAINS 26 LETTERS


# s = "leetlovecode"

# builds hash map: character and how often it appears
# uses python built-in collections counter
count = collections.Counter(s)


def first_unique_character_in_string(s):
	for index, letter in enumerate(s):
		if count[letter] == 1:
			print(index)
	# return -1

	counter = Counter(s)
	for i, j in counter.items():
		if j == 1:
			return s.index(i)
		return -1


# The first printed element is the first unique character
# if in a class definition, then just return the index


# SOLUTION 2
# TIME COMPLEXITY O(N)
# SPACE COMPLEXITY O(N)

# build dictionary with seen letters

def first_unique_character_in_string_with_dict(s):
	# EDGE CASES 0, 1, AND ALL SAME ELEMENTS
	if len(s) == 0:
		return -1
	if len(s) == 1:
		return 0
	if len(set(s)) == 1:
		return -1

	seen_letters = {}

	for letters in s:
		seen_letters[letters] = 1 + seen_letters.get(letters, 0)

	for i, letters in enumerate(s):
		if seen_letters[letters] == 1:
			return i
	return -1
