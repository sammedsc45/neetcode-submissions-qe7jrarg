class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        longest=0
        for n in s:
            if n-1 not in s:
                m=n
                l=1
                while m+1 in s:
                    l+=1
                    m+=1
                longest = max(longest, l)
        return longest
                