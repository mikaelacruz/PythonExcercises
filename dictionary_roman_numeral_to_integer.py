"""Roman Numeral to Integer
Given a Roman Numeral, convert it to an integer
"""
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
