"""Array Pair Sum
Given an integer, output all the unique pairs that sum up to a specific k
input pair_sum [1, 2, 3, 4]
target 4
would return 2 pairs: (1, 3) and (2, 2)

pair_sum(array, k)"""


def pair_sum(array, k):
	# Some considerations: null, letters, negative numbers.

	# Check: Problem wants a PAIR of integers. If the array has ONE number, then this array is too small.
	if len(array) < 2:
		return print('Too small!')

	# Creating two sets (unordered tuples / dictionary hybrids)
	# Seen will function has a counter
	#     Seen will hold integers that we have processed
	# Output will hold our pairs that add up to our target
	seen = set()
	output = set()

	# Loop through each element in the array
	for num in array:
		# We are defining a new variable (int), target
		# target will be the specified k value given
		# num will be the element that we are on dependent on the iteration
		# target represents the "other half" of the sum

		target = k - num

		# Check if target, the number we just calculated is in our set, seen
		# If it isn't, let's add the element we are looking at/iterating over right now
		if target not in seen:
			seen.add(num)
		# If target IS in seen, then we have found a pair!
		# After looping again, the new target would have been
		else:
			output.add((target, num))
	print(output)
