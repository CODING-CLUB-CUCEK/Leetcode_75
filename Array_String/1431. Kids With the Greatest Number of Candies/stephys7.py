class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        large=max(candies)
        result=[]
        for ele in candies:
            if ele+extraCandies>=large:
                result.append(True)
            else:
                result.append(False)
        return result
