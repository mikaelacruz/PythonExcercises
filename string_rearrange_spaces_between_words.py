"""
Rearrange Spaces Between Words
You are given a string text of words that are placed among some number of spaces. Each word consists of one or more lowercase English letters and are separated by at least one space. It's guaranteed that text contains at least one word.

Rearrange the spaces so that there is an equal number of spaces between every pair of adjacent words and that number is maximized. If you cannot redistribute all the spaces equally, place the extra spaces at the end, meaning the returned string should be the same length as text.

Return the string after rearranging the spaces.



Example 1:

Input: text = "  this   is  a sentence "
Output: "this   is   a   sentence"
Explanation: There are a total of 9 spaces and 4 words. We can evenly divide the 9 spaces between the words: 9 / (4-1) = 3 spaces.
Example 2:

Input: text = " practice   makes   perfect"
Output: "practice   makes   perfect "
Explanation: There are a total of 7 spaces and 3 words. 7 / (3-1) = 3 spaces plus 1 extra space. We place this extra space at the end of the string.


Constraints:

1 <= text.length <= 100
text consists of lowercase English letters and ' '.
text contains at least one word.

"""


def rearrange_spaces(text):
    """
    Given a text string consisting of words in lowercase
    English letters and variable spacing among the words,
    this program rearranges the text spaces such that there
    are no leading spaces, the number of spaces between
    words is equal and maximum, and the leftover spaces
    trail the words.

    :param text: text string of words and spaces
    :type text: str
    :return: text string with spaces rearranged
    :rtype: str
    """

    """
    Preprocessing:
    - Extract array of words (words) from text
    - Determine number of words (len_words)
    - Determine number of spaces (spaces)
    """
    words = text.split()
    len_words = len(words)
    spaces = text.count(' ')

    """
    Base Case: one word
    - Return word with spaces trailing, if any.
    """
    if len_words == 1:
        return ''.join([words[0], ' ' * spaces])

    """
    General Case: two or more words
    - Create separator to divide spaces evenly between words.
    - Create trailing to capture remaining spaces
    - Combine words, separators, and trailing and return
      result
    """
    separator = ' ' * (spaces // (len_words - 1))
    trailing = ' ' * (spaces % (len_words - 1))
    sentence = separator.join(words)
    return ''.join([sentence, trailing])
