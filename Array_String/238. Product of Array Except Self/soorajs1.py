class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        out = [1]*l
        a = 1
        for i in range(1, l):
            out[i] = out[i-1]*nums[i-1]
        for i in range(l-1, -1, -1):
            out[i] = out[i]*a
            a *= nums[i]
        return out
