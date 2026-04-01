class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def canEatAllBananas(k: int) -> bool:
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / k)
            return hours <= h

        # Initialize binary search boundaries
        left, right = 1, max(piles)

        while left < right:
            mid = (left + right) // 2
            if canEatAllBananas(mid):
                right = mid  # Try a smaller k
            else:
                left = mid + 1  # Increase k

        return left