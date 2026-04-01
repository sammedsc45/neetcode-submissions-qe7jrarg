class Solution:
    def climbStairs(self, n: int) -> int:
        cur, prev = 1, 1
        for i in range(n-1):
            temp = cur
            cur = cur+prev
            prev = temp
        return cur