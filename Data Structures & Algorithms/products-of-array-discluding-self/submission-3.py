class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        cnt, prod = 0, 1
        for n in nums:
            if n:
                prod *= n
            else:
                cnt+=1
            
        if cnt>1:
            return [0]*len(nums)
        
        res = [0]*len(nums)
        for i,n in enumerate(nums):
            if cnt:
                if n == 0:
                    res[i] = prod
                else:
                    res[i] = 0
            else:
                res[i] = prod//n
        return res