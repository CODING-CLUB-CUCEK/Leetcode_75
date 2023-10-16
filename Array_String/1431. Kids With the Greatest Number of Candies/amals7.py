class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxc = max(candies)
        res = []
        
        for candie in candies:
            if candie + extraCandies >= maxc:
                res.append(True)
            else:
                res.append(False)
        return res