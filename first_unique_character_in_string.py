
def first_unique_character_in_string(s):
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

def first_unique_character_in_string_with_enumerate(s):
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



def unique_character_in_string_with_builtins(s):
	# If the string is not empty
	if s:
		# Get rid of whitespaces and lower cases
		s = s.replace(' ', '').lower()
	else:
		return False
	# Create a set
	characters = set()

	# For every letter in the s,
	#   If the letter is already in our set, then it is NOT unique
	#       If it is not in our set, then it IS unique, so add it!
	for letter in s:
		if letter in characters:
			return False
		else:
			characters.add(letter)
	return True


def non_repeating_element(s):
	# Similar methods to above, but iterative without enumerating

	# If the string is not empty, replace the whitespace and
	#    make all lower cases
	if s:
		s = s.replace(' ', '').lower()

	# Dictionary to track key:value pair for each character in the string
	char_count = ()

	# Iterate over every character in the string
	# IF we have a character in our dictionary already,
	#    then add the additional occurrence AKA NOT a unique letter smh
	# Otherwise, add that letter to the dictionary
	for c in s:
		if c in char_count:
			char_count[c] += 1
		else:
			char_count[c] = 1

	# Same vibe as before
	# Iterate over every character in the list
	# Only the character with 1 occurrence (1 in the char_count) is unique
	# The first character will be returned ONLY THE FIRST ONE!
	for c in s:
		if char_count[c] == 1:
			return c
	# Looks like there were no uniques and we'll be returning None :(
	return None


def non_repeating_elements(s):
	"""
	Non Repeating Elements
	Similar to First Unique Character in String, but will return ALL the elments that are unique
	Taking inspiration from above, let's get started
	"""

	# If the string is not empty, replace the whitespace and
	#    make all lower cases
	if s:
		s = s.replace(' ', '').lower()

	# Iterate over every character in the string
	# IF we have a character in our dictionary already,
	#    then add the additional occurrence AKA NOT a unique letter smh
	# Otherwise, add that letter to the dictionary
	for c in s:
		if c in char_count:
			char_count[c] += 1
		else:
			char_count[c] = 1

	# Creating new variable all_unqiues, an empty list
	# This will store our unique values that we will return at the end
	all_uniques = []

	# We will sort the dictionary so that the values control the order of the keys
	# We will be using .items and lambda to do this
	# All lambda is doing is MAKING IT HAPPEN
	#    We want x (the key) to be in the 2nd position now, AKA our dictionary to be
	#        sorted by the VALUE and not the key
	# This will compare each index position of each tuple because remember we have a list
	#     and if we have a key and a value that's going to be separated by a comma in the list
	#     not like the dictionary where it they have :
	y = sorted(char_count.items(), key = lambda x: x[1])
	# y should look something like this now
	# y = [ ( 'i', 1 ), ( 's', 1 ) , ( 'a', 2 ), ( 'l', 2 ), ( 'p', 4 ), ( 'e', 4 )]
	#        item1        item2         item3       item4      item5       item6
	#      item[1] = 1 (2nd position of the pair) AKA the value
	#      y [0][1] = 1 (first pair, 2nd position of the pair) AKA the value
	# iterate through every item in y
	for item in y:
		if item[1] == y[0][1]:
			all_uniques.append(item)

	# Return all_uniques list :) all our unique values will be in this list
	return all_uniques
