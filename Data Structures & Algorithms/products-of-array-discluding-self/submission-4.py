class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        z_cnt = 0
        for n in nums:
            if n:
                prod *= n
            else:
                z_cnt += 1
        
        if z_cnt>1:
            return [0]*len(nums)

        res = [0]*len(nums)
        for i, n in enumerate(nums):
            if z_cnt:
                if n:
                    res[i]=0
                else:
                    res[i]=prod
            else:
                res[i] = prod//n
        return res