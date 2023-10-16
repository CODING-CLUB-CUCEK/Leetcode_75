class Solution:
    def maxArea(self, height: List[int]) -> int:
        i,j = 0,len(height)-1
        res=0
        while i<j:
        
            temp = (j-i) * min(height[i],height[j])
            if temp>res:
                res = temp

            if height[i]<height[j]:
                i+=1
            else:
                j-=1
        return res
            