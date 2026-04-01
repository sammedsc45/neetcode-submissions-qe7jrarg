class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        max_prof = 0
        min_price = prices[0]
        for price in prices:
            if price<min_price:
                min_price = price
            max_prof = max(max_prof,price-min_price)
        return max_prof