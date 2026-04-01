class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # If there are no prices or only one price, return 0 profit
        if not prices or len(prices) == 1:
            return 0

        # Initialize three states: hold, sold, and rest
        # hold: the maximum profit when holding a stock on day i
        # sold: the maximum profit when selling a stock on day i
        # rest: the maximum profit when resting (doing nothing) on day i
        n = len(prices)
        hold = [-float('inf')] * n  # initialized to very low because initially you can't hold
        sold = [0] * n
        rest = [0] * n

        # On the first day, the only option is to buy
        hold[0] = -prices[0]  # If we buy on day 0, profit is -prices[0]

        # Process each day, update states
        for i in range(1, n):
            # If we hold, we either carry the previous holding state or buy on this day
            hold[i] = max(hold[i - 1], rest[i - 1] - prices[i])

            # If we sold, we must have sold a stock we were holding
            sold[i] = hold[i - 1] + prices[i]

            # If we rest, we can come from either resting or selling the previous day
            rest[i] = max(rest[i - 1], sold[i - 1])

        # The maximum profit is either selling on the last day or resting (not holding anything)
        return max(sold[-1], rest[-1])