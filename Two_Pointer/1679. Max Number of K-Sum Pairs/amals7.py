class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        i,j = 0 ,len(nums)-1
        n = len(nums)
        count =0
        nums.sort()

        while i < j :
            s = nums[i]+nums[j]
            if s>k:
                j -=1
            elif s<k:
                i +=1
            else:
                count +=1
                i+=1
                j-=1
        return count 
            