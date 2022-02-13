"""
Given an array, what is most frequently occuring element?
"""


def most_frequent(list):
    # Count is the dictionary where we will keep track of each element
    # and how many occurrences there are
    count = {}

    # max_item
    # the most frequent occurring element in the list
    max_item = 0

    # max_count
    # how many of the max_item there are
    max_count = 0

    # Looping through the list
    for i in list:
        # if the element at index i is not in the dictionary count
        # then we go ahead and add it to the dictionary :)
        if i not in count:
            count[i] = 1
        # if the element at the index i IS in the dictionary count
        # then we INCREASE THAT COUNT to make sure we note we have "another one" - dj khaled
        else:
            count[i] += 1
        #
        # comparing the values in the dictionary count
        # we want to update max_count and max_item
        # this is how we are keeping track of what element is getting the most points, ya feel me?
        if count[i] > max_count:
            max_count = count[i]
            max_item = i

    # most frequently occurring element
    return max_item
