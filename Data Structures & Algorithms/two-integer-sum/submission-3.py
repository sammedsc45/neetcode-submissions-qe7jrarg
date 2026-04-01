class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = dict()
        for i, n in enumerate(nums):
            compl = target-n
            if compl in dic:
                return [dic[compl], i]
            else:
                dic[n]=i
        return []