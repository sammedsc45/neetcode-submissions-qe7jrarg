class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # Create a DP array where dp[i] represents the number of ways to make up amount i
        dp = [0] * (amount + 1)
        dp[0] = 1  # There's one way to make up amount 0, by choosing no coins

        # For each coin, update the DP array for all amounts that can be reached
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] += dp[i - coin]

        # The result is the number of ways to make up the 'amount'
        return dp[amount]