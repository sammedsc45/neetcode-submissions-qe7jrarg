class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        # If the cost array has only two steps, return the minimum of the two
        if n == 2:
            return min(cost[0], cost[1])
        
        # Initialize the first two costs
        prev2 = cost[0]
        prev1 = cost[1]
        
        # Calculate the minimum cost for each subsequent step
        for i in range(2, n):
            current = cost[i] + min(prev1, prev2)
            prev2 = prev1
            prev1 = current
        
        # Return the minimum cost of the last two steps
        return min(prev1, prev2)