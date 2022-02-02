"""Array Rotation
Given two arrays (assume no duplicates)
is 1 array a rotation (same size + elements) of another? Return True / False

Big O(n) we are going through each array 2x by O(2n) = O(n) since infinite sized limits

1) Select an indexed position in list_1 and get it's value
2) Find the same element in list_2 and check index for index for that value.
   If any variation, then we know to return False
3) Getting to the last item without a False, means True, the two arrays are a rotation of each other.
"""


def rotation(list_1, list_2):

	# Arrays must be same size!
	if len(list_1) != len(list_2):
		return False

	# Variables key: key_index that represent the key and value from list_1
	# We will use key_index to iterate through list_2 and check for same values
	key = list_1[0]
	key_index = 0

	# Looping through list_2 to compare the value (key) of list_1 at position 0 to list_2
	#    If there is a match, then we immediately BREAK out of the loop and continue on
	#        with the code! ~ run away!!
	for i in range(len(list_2)):
		if list_2[i] == key:
			key_index = i
			break

	# Edge check: At this point, if key_index were equal to 0,
	#    then we did NOT find a duplicate/same value in list_2.
	#    AKA list_1 and list_2 are NOT rotations of each other :(
	if key_index == 0:
		return False

	# We have made it this far! yay!
	# Looping through list_1,
	# We are creating a new variable list_2_index
	#    list_2_index is just the index for list_2
	#    it is composed of the key_index + x
	#    key_index is the index that had matching values between list_1 and list_2
	#    x is the iteration we are in in this loop
	#    the reason for the MODULO is to, i like to think about it as:
	#    ~ putting it in terms of list_1~
	#    we are iterating through list_2, but matching up the indices that correlate to list_1
	#    realpython.com/python-modulo-operator/ has good clock example that helped me lol
	#    IF SOMETHING DOES NOT MATCH THEN RETURN FALSE BC THEY ARE NOT ROTATIONS
	for x in range(len(list_1)):
		list_2_index = ((key_index + x) % len(list_1))
		if list_1[x] != list_2[list_2_index]:
			return False
	# Made it here, then they are truly array bestie rotations :)
	return True
