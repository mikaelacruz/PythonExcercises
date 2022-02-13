"""
Coin Change
You are given an integer array coins representing coins of different denominations
    and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount.
If that amount of money cannot be made up by any combination of the coins, return -1.
You may assume that you have an infinite number of each kind of coin.



Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Example 3:

Input: coins = [1], amount = 0
Output: 0


Constraints:

1 <= coins.length <= 12
1 <= coins[i] <= 231 - 1
0 <= amount <= 104
"""


def coin_change(coins, amount) -> int:
    """
    Approach: Linear DP peaking back target-coin
    O(n*m) time: For each coin denomination, we scan from 0 to n
    O(n) space :  Where n is the amount and m is the size of `coins`
    """
    # Example: coins = [1 2 5], amount = 5

    # amount   =  0  1   2   3   4   5
    # mincoins = [0  inf inf inf inf inf]


    mincoins = [float('inf') for _ in range(amount + 1)]
    # Only 1 way to make `0` change: return 0 coin
    mincoins[0] = 0

    # 1st pass: coin = 1 -> mincoins = [0 1 2 3 4 5]
    # 2nd pass: coin = 2 -> mincoins = [0 1 1 2 2 3]
    # 3rd pass: coin = 5 -> mincoins = [0 1 1 2 2 1]
    for coin in coins:
        for target in range(1, len(mincoins)):
            # If coin can be used to make up part of the amount
            if coin <= target:
                # Try use it and check what the min number of coins to make up
                # the rest `mincoins[target-coin]` and add 1 (rest + current coin)
                mincoins[target] = min(mincoins[target], mincoins[target - coin] + 1)

    # if mincoins[amount] couldn't be used then no
    # combination of coins could make up target amount
    return mincoins[amount] if mincoins[amount] != float('inf') else -1
