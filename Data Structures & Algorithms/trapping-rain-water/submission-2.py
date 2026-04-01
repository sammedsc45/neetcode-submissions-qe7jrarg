from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        traped = 0
        l = len(height)
        for i in range(1, l-1):
            max_left = max(height[:i])
            max_right = max(height[i+1:])
            w = min(max_left, max_right) - height[i]
            if w > 0:
                traped += w
        return traped