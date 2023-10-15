class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        postfix=1
        prefix =1
        n = len(nums)
        result =[-1]*n
        for i in range(n):
            result[i] = prefix 
            prefix *= nums[i]
        for i in range(n-1,-1,-1):
            result[i] *= postfix
            postfix *= nums[i]
        return result