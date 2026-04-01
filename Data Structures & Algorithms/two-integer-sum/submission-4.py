class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}

        for i, n in enumerate(nums):
            comple = target-n
            if comple in prevMap:
                return [prevMap[comple], i]
            prevMap[n] = i