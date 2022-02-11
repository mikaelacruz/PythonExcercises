"""
Counting Sort Algorithm

Sort Algorithm that sorts elements with the technique of counting the occurrences of each unique element in
   an array or list. (Hashing technique)

   1. Find k aka max element (largest element) in input list as k (or it will be given as k)
   2. Create an integer list, size n, to store sorted list
   3. Create integer list, size k + 1, intialized to 0
   4. Using the value of each item in the input list as an index, store each integer count in freq[]
   5. Calculate the starting index for each integer
   6. Copy the output list, preserving the order of inputs with equal keys
   7. Copy the output list back to the input list

"""
import array_find_largest_element


def counting_sort_no_k(array):
    # 1 if no k given; find k = max element (largest element)
    k = array_find_largest_element.array_find_largest_element(array)

    # 2 and 3
    output = [0] * len(array)
    freq = [0] * (k + 1)

    # 4
    for i in array:
        freq[i] = freq[i] + 1

    # 5
    total = 0
    for i in range(k + 1):
        old_count = freq[i]
        freq[i] = total
        total += old_count

    # 6
    for i in array:
        output[freq[i]] = i
        freq[i] = freq[i] + 1

    # 7
    for i in range(len(array)):
        array[i] = output[i]

    return array


def counting_sort(array, k):
    # 1 k was given to us! don't need to find it :)
    # 2 and 3
    output = [0] * len(array)
    freq = [0] * (k + 1)

    # 4
    for i in array:
        freq[i] = freq[i] + 1

    # 5
    total = 0
    for i in range(k + 1):
        old_count = freq[i]
        freq[i] = total
        total += old_count

    # 6
    for i in array:
        output[freq[i]] = i
        freq[i] = freq[i] + 1

    # 7
    for i in range(len(array)):
        array[i] = output[i]

    return array
