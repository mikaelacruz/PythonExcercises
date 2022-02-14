import add_strings
import array_find_kth_element
import array_find_largest_element
import array_median_of_two_sorted_arrays
import array_merge_sorted_three_pointer
import array_sort_unsorted_array
import dictionary_anagram
import array_common_elements
import array_largest_sum
import array_maximum_subarray
import array_most_frequently_occurring_element
import array_pair_sum
import array_rotation
import dynamic_programming_best_time_to_buy_and_sell_stock
import dictionary_first_unique_character_in_string
import linked_list_merge_two_sorted_lists
import heap_sort
import string_longest_common_prefix
import string_longest_substring
import string_reverse_words
import string_unique_character_in_string
import string_valid_palindrome
import stack_valid_parentheses
import array_find_largest_element

__name__ == '__main__'

s = "5F3Z-2E-9-W"
k = 4
s = s.upper()
s = s.replace('-', '')
d = [char for char in s]

dash_required = ((len(d)) // k) - 1


for i in range(len(d) - 1, -1, -k):
    if i < k:
        d.insert(i + 1, '-')
d = ''.join(d)
print(d)
