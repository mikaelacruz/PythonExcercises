"""Roman Numeral to Integer
Given a Roman Numeral, convert it to an integer

# input string
s = "MCDLXXIX"

# Creating a roman dictionary of 13 symbols mapping an integer to str
roman_dict = {
	'I': 1,
	'V': 5,
	'X': 10,
	'L': 50,
	'C': 100,
	'D': 500,
	'M': 1000,
	'IV': 4,
	'IX': 9,
	'XL': 40,
	'XC': 90,
	'CD': 400,
	'CM': 900
	}

count = 0
i = 0

# while the index is less than the length of the string
while i < len(s):
	# if at least 2 characters remain and substring(i, i+1) is in roman_dict
	if i < len(s) - 1 and s[i:i + 2] in roman_dict:
		count += roman_dict[s[i:i + 2]]
		i += 2
	else:
		count += roman_dict[s[i]]
		i += 1
print(count)
################################################################################################
First Unique Character in a String
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

# SOLUTION 1

# TIME COMPLEXITY O(N) SINCE WE GO THROUGH THE STRING OF LENGTH N TWO TIMES
# SPACE COMPLEXITY O(1) BECAUSE ENGLISH ALPHABET CONTAINS 26 LETTERS


s = "leetlovecode"
# builds hash map: character and how often it appears
# uses python built-in collections counter
count = collections.Counter(s)

for index, letter in enumerate(s):
	if count[letter] == 1:
		print(index)
#return -1

counter = Counter(s)
for i, j in counter.items():
	if j==1:
		return s.index(i)
	return -1

# The first printed element is the first unique character
# if in a class definition, then just return the index


# SOLUTION 2
# TIME COMPLEXITY O(N)
# SPACE COMPLEXITY O(N)

# build dictionary with seen letters

seen_letters = {}
for letters in s:
	seen_letters[letters] = 1+ seen.get(letters,0)

for i, letters in enumerate(s):
	if seen_letters[letters] == 1:
		return i
return -1



# EDGE CASES 0, 1, AND ALL SAME ELEMENTS
    if len(s) == 0: return -1
    if len(s) == 1: return 0
    if len(set(s)) == 1: return -1

################################################################################################

CONTAINS DUPLICATION

Given an integer array nums, return TRUE if any value appears at least twice in the array,
return FALSE if every element is distinct

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
"""
