"""
Open the Lock

You have a lock in front of you with 4 circular wheels. Each wheel has 10 slots: '0', '1', '2', '3', '4', '5', '6',
'7', '8', '9'. The wheels can rotate freely and wrap around: for example we can turn '9' to be '0', or '0' to be '9'.
Each move consists of turning one wheel one slot.

The lock initially starts at '0000', a string representing the state of the 4 wheels.

You are given a list of deadends dead ends, meaning if the lock displays any of these codes, the wheels of the lock
will stop turning and you will be unable to open it.

Given a target representing the value of the wheels that will unlock the lock, return the minimum total number of
turns required to open the lock, or -1 if it is impossible.



Example 1:

Input: deadends = ["0201","0101","0102","1212","2002"], target = "0202"
Output: 6
Explanation:
A sequence of valid moves would be "0000" -> "1000" -> "1100" -> "1200" -> "1201" -> "1202" -> "0202".
Note that a sequence like "0000" -> "0001" -> "0002" -> "0102" -> "0202" would be invalid,
because the wheels of the lock become stuck after the display becomes the dead end "0102".
Example 2:

Input: deadends = ["8888"], target = "0009"
Output: 1
Explanation: We can turn the last wheel in reverse to move from "0000" -> "0009".
Example 3:

Input: deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"], target = "8888"
Output: -1
Explanation: We cannot reach the target without getting stuck.


Constraints:

1 <= deadends.length <= 500
deadends[i].length == 4
target.length == 4
target will not be in the list deadends.
target and deadends[i] consist of digits only.


Shortest path finding, when the weights are constant, as in this case = 1, BFS is the best way to go.
Best way to avoid TLE is by using deque and popleft() .
[Using list() and pop(0) is a linear operation in Python, resulting in TLE]

"""
from collections import deque


def open_lock(deadends, target):
    # Initial case; if starting point is deadends
    if "0000" in deadends:
        return -1

    # Helper function
    def children(lock):
        res = []
        # range 4 bc 4 digits _ _ _ _ in lock
        for i in range(4):
            # math follows our walkthrough algorithm drawing
            # convert it back to a string for output
            digit = str((int(lock[i]) + 1) % 10)
            res.append(lock[:i] + digit + lock[i + 1:])
            digit = str((int(lock[i]) - 1 + 10) % 10)
            res.append(lock[:i] + digit + lock[i + 1:])
        return res

    # double ended queue
    q = deque()
    # every value in our queue
    # is a pair of values
    # starting value is 0000 and the other is how many turns it took us to reach there
    # ["0000", 0] [lock, turns]
    q.append(["0000", 0])
    # hash set initialized to deadends so we can compare to our deadends we're importing
    visit = set(deadends)

    while q:
        lock, turns = q.popleft()
        # if the lock reaches the target
        # return the the number of turns it took shortest path :)
        if lock == target:
            return turns
        # if we didn't find the target we gotta look at all the children here we gooooo
        for child in children(lock):
            # making sure we are not revisiting a child lol
            if child not in visit:
                # adding to the visit set so we don't visit it again
                visit.add(child)
                # it already took us turns amount to get to the child
                q.append([child, turns + 1])
    # we didn't reach any target
    return -1
