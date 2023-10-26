class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        #brute force approach won't work for all test cases
        # time complexity O(n*2k)

        
        # maxsum = sum( nums[:k])
        # j=1
        # currentsum=0
        # for i in range(1,len(nums)):
        #     if len(nums[i:k+i]) == k :
        #       currentsum = sum(nums[i:k+i]) 
        #     else:
        #       break
        #     if currentsum > maxsum:
        #         maxsum = currentsum
        # return maxsum/k

# this is a better solution ,passes all test case
#time complexity of O(n) 

        maxsum = currentsum = sum(nums[:k])
        n = len(nums)
        j =0
        for i in range(k,n):
          currentsum +=nums[i] -nums[j]
          maxsum = max(currentsum,maxsum)
          j +=1
        return maxsum/k
                

            


        