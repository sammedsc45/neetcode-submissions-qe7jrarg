class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        longest=0
        for i, n in enumerate(nums):
            if n-1 not in s:
                m=n+1
                l=1
                while m in s:
                    l+=1
                    m+=1
                longest = max(longest, l)
        return longest
                