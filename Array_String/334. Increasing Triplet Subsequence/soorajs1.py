class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        else:
            a = 10**10
            b = 10**10
            for i in nums:
                if i < a:
                    a = i
                elif i > a and i < b:
                    b = i
                if i > b:
                    return True
        return False
