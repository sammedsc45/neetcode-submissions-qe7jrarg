class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)<=1:
            return len(nums)
        ns = set(nums)
        max_cnt = 1
        for i in range(len(nums)):
            if nums[i]-1 not in ns:
                cnt = 1
                key = nums[i]+1
                while key in ns:
                    cnt+=1
                    key+=1
                max_cnt = max(max_cnt, cnt)
        
        return max_cnt