import string_add_strings
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


points = [[1, 2, 3], [1, 5, 1], [3, 1, 1]]

res = max(points[0])

for r in range(1, len(points)):
    dp = points[r - 1]
    for d in range(1, len(points[0])):
        dp[d] = max(dp[d], dp[d - 1] - 1)

    for e in range(len(points[0]) - 2, -1, -1):
        dp[e] = max(dp[e], dp[e + 1] - 1)

    for c in range(len(points[0])):
        points[r][c] += dp[c]

        res = max(res, points[r][c])

print(res)
