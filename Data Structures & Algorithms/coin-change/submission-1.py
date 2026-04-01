class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Initialize dp array with a large value (float('inf'))
        # dp[i] will hold the minimum number of coins needed to make amount i
        dp = [float('inf')] * (amount + 1)
        
        # Base case: 0 coins are needed to make the amount 0
        dp[0] = 0
        
        # Fill the dp array
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], dp[i - coin] + 1)
        
        # If dp[amount] is still float('inf'), return -1 (no solution)
        return dp[amount] if dp[amount] != float('inf') else -1