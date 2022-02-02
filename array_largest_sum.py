"""
Array Largest Sum
Take an array with positive and negative integers and find the maximum sum of the array
"""
def largest_sum(arr):
	# If the length of the array is 0, then the array is too small
	# AKA we need an array to do this with lol
	if len(arr) == 0:
		return print('Too small!')

	# Setting TWO variables max_sum and current_sum to the first element of the array
	max_sum = current_sum = arr[0]

	# Looping through the array starting at the 2nd element until the end of the array
	for num in arr[1:]:
		# current_sum tracker
		# Redefines current_sum. checks what is bigger - current_sum _ num or just num
		current_sum = max(current_sum+num, num)
		# max_sum tracker
		# Redefines max_sum. checks what is bigger - current_sum or max_sum
		# max_sum is what we are after :)
		max_sum = max(current_sum, max_sum)
	return print(max_sum)
