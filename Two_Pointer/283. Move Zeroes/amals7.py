class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # n = len(nums)
        # c = nums.count(0)
        # for _ in range(c):
        #     nums.remove(0)
        #     nums.append(0)
        

        #two pointer approach
        
        n = len(nums)
        l=r=0
        while r < n:
            if nums[r]!=0:
                nums[r],nums[l]=nums[l],nums[r]
                r +=1
                l +=1
            else:
                r +=1
        