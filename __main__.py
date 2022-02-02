import anagram
import array_common_elements
import array_largest_sum
import array_most_frequently_occurring
import array_pair_sum
import array_rotation
import reverse_words

__name__ == '__main__'

s = "23sdafasf"
if s and s.isalpha():
	s = s.replace(' ','').lower()
	print(s)
else:
	print("Error: Nada, boss")
