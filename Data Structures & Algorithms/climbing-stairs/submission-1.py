class Solution:
    def climbStairs(self, n: int) -> int:
        # Initialize the base cases
        if n == 1:
            return 1
        if n == 2:
            return 2

        # Create a dynamic programming array to store the results
        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2

        # Fill the dp array using the recurrence relation
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]