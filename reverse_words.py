"""
Reverse Words

Given a string of words, reverse all the words

start: "This is the best"
finish: "best the is this"

"""


def reverse_string(s):
	length = len(s)
	spaces = ['']
	i = 0
	words = []

	while i < length:
		if s[i] not in spaces:
			word_start = i

			while i < length and s[i] not in spaces:
				i += 1

			words.append(s[word_start:i])
		i += 1
	return "".join(reversed(s))
