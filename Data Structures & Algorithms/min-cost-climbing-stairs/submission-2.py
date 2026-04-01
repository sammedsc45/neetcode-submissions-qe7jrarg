class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Append 0 to the cost list, representing the "top" of the staircase
        cost.append(0)

        # Start from the third-to-last element and move backward
        # Update each cost[i] to be the cost of stepping from i plus the minimum cost
        # of stepping to the next step (i+1) or skipping one step (i+2)
        for i in range(len(cost) - 3, -1, -1):
            cost[i] += min(cost[i + 1], cost[i + 2])

        # Return the minimum cost to start from either step 0 or step 1
        return min(cost[0], cost[1])