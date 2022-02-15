"""
Maximum Number of Points with Cost
You are given an m x n integer matrix points (0-indexed). Starting with 0 points, you want to maximize the number of points you can get from the matrix.

To gain points, you must pick one cell in each row. Picking the cell at coordinates (r, c) will add points[r][c] to your score.

However, you will lose points if you pick a cell too far from the cell that you picked in the previous row. For every two adjacent rows r and r + 1 (where 0 <= r < m - 1), picking cells at coordinates (r, c1) and (r + 1, c2) will subtract abs(c1 - c2) from your score.

Return the maximum number of points you can achieve.

abs(x) is defined as:

x for x >= 0.
-x for x < 0.


Example 1:


Input: points = [[1,2,3],[1,5,1],[3,1,1]]
Output: 9
Explanation:
The blue cells denote the optimal cells to pick, which have coordinates (0, 2), (1, 1), and (2, 0).
You add 3 + 5 + 3 = 11 to your score.
However, you must subtract abs(2 - 1) + abs(1 - 0) = 2 from your score.
Your final score is 11 - 2 = 9.


You use dynamic programming! Using
1) Sub problem: Minimum Falling Path MINIMUM FALLING PATH SOLUTION
2) Sub problem 2: Best Sightseeing Pair KADANE'S ALGORITHM

"""


def maxPoints(self, points: List[List[int]]) -> int:
    if not points:
        return 0
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

    return res
