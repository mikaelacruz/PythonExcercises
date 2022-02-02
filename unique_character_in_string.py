"""Unique Characters in a String
Two methods to check for unique characters in a string
1) Uses built-in Python method
2) Iterates through
"""


def unique_characters_in_string_builtin(s):
	# Get rid of spaces in the string s and make all lowercase
	s = s.replace(' ', '')
	# Returns the Boolen True or False
	#     If the lengths of the strings are the same
	return len(set(s)) == len(s)


def unique_characters_in_string(s):
	# Check if te string is not empty
	#    if not empty,
	#        then take out whitespaces and make them all lower case
	#    else
	#        return False bc we got nothing good here fam
	if s:
		s = s.replace(' ', '').lower()
	else:
		return False

	# Creating a variable characters as a set
	# Set is a python built in data structure that is unordered, unchangeable, and can only have
	#      NO DUPLICATES so it's perfect for us here
	characters = set()

	# Iterating through the string s, going through each letter in our string s
	for letter in s:
		# If the letter in our string is already in the set characters, then oops gotta duplicate
		#     So we return False and say goodbye b
		if letter in characters:
			return False
		# However, if the letter is NOT in the set characters, we add it there because it's new!
		else:
			characters.add(letter)
	# If we made it this far, we had no issues and we return True bb!
	return True
