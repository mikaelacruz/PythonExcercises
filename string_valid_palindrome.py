"""
Valid Palindrome
Given a string s, return true if the s can be palindrome after deleting at most one character from it.




Some information on string slicing:
The notation that is used in

a[::-1]
means that for a given string/list/tuple, you can slice the said object using the format

<object_name>[<start_index>, <stop_index>, <step>]
This means that the object is going to slice every "step" index from the given start index,
 till the stop index (excluding the stop index) and return it to you.

In case the start index or stop index is missing,
 it takes up the default value as the start index and stop index of the given string/list/tuple.
 If the step is left blank, then it takes the default value of 1 i.e it goes through each index.

So,

a = '1234'
print a[::2]
would print

13
Now the indexing here and also the step count, support negative numbers. So, if you give a -1 index,
it translates to len(a)-1 index. And if you give -x as the step count,
then it would step every x'th value from the start index, till the stop index in the reverse direction.
For example

a = '1234'
print a[3:0:-1]
This would return

432
Note, that it doesn't return 4321 because, the stop index is not included.

Now in your case,

str(int(a[::-1]))
would just reverse a given integer, that is stored in a string, and then convert it back to a string

i.e "1234" -> "4321" -> 4321 -> "4321"

If what you are trying to do is just reverse the given string, then simply a[::-1] would work










"""


def valid_palindrome(s):
    n = len(s)

    if s == s[::-1]:
        return True  # return True if the string is already a palindrome
    i = 0
    j = n - 1

    while (i <= j):
        if s[i] != s[j]:  # keep checking if the characters are same
            if s[i + 1: j + 1][::-1] == s[i + 1: j + 1] or s[i: j] == s[i: j][
                                                                      ::-1]:  # if not same then the smaller string
                # excluding 1 charcter from either left or right should be a palindrome
                return True
            else:
                return False
        else:
            i += 1  # keep moving right
            j -= 1  # keep moving left
