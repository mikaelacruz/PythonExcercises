"""Anagram problem
Given two strings, check if they are anagrams.
An anagram is when two strings can be written using the exact same letters,
	so you can get a different phrase or word.

For example, "public relations" is an anagram for "crap built on lies".
Another example, "clint eastwood" is an anagram of "old west action".

Note: ignore spaces and capitalization. So, "d go" is an anagram of "God".

"""


def anagram(string, string2):
	# First, we will remove the whitespaces and the upper case letters from each string
	string = string.replace(' ', '').lower()
	string2 = string2.replace(' ', '').lower()

	# Check if the length of two strings match
	# Anagrams must have the same letters, thus the same length
	# If not, then the method will return False
	if len(string) != len(string2):
		return False

	# Initiate an empty dictionary, Count
	# We will keep a count of each letter in each string here
	count = {}

	# We will loop through each letter in string
	# For every letter in string,
	# IF the letter is already in the dictionary,
	#    then add 1 to that letter key
	# Else, then just add the letter to the dictionary
	for letter in string:
		if letter in count:
			count[letter] += 1
		else:
			count[letter] = 1

	# Do the reverse for string2
	# This is because, if the letters match, then count will go down to 0
	# We are counting up in string's loop
	# then counting down in string2's loop
	for letter in string2:
		if letter in count:
			count[letter] -= 1
		else:
			count[letter] = 1

	# We will loop through count to make sure that every letter
	# has been matched aka subtracted aka 0
	# No letters should be left over
	for k in count:
		if count[k] != 0:
			return False
	# If there are no letters that are left over, we return True
	# These two strings, string and string2, are anagrams!
	return True
