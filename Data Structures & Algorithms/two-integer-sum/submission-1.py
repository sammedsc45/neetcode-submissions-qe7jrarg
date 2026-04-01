class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}
        for i,n in enumerate(nums):
            comp = target-n
            if comp in num_map:
                return [num_map[comp], i]
            num_map[n] = i
        return []