"""
Longest Common Prefix

"""
def longest_common_prefix(strs):
    first_word = strs[0].split()
    common_prefix = []

    for i in range(1, len(strs)):
        compare_word = strs[i].split()
        for j in first_word:
            if first_word[j] == compare_word[i]:
                common_prefix.append(first_word[j])

    return common_prefix
