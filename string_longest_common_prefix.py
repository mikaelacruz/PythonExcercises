"""
Longest Common Prefix

"""


def longest_common_prefix(strs):
    # Result is the output of our longest common prefix
    result = ""

    # Iterate through the first word
    for i in range(len(strs[0])):
        # Iterate through the words in strs
        for s in strs:
            # If we are either at the end of the word entirely OR letters aren't matching
            #           THEN WE RETURN WHAT WE HAVE whatever it may be
            if i == len(s) or s[i] != strs[0][i]:
                return result
            # We are adding the letters that have matched each other to the result list
        result += strs[0][i]
    return result
