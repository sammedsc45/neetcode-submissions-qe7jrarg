class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        h_set = set(nums)

        return (len(h_set) != len(nums))