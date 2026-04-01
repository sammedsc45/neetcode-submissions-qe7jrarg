class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indx_map = {}
        for i, num in enumerate(nums):
            comp = target - num
            if comp in indx_map:
                return [indx_map[comp], i]
            indx_map[num] = i
        return []