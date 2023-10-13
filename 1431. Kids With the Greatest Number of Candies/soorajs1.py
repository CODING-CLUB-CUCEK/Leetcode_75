class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        def mostcandies(a):
            for i in candies:
                if a<i:
                    return False
            return True
        out=[]
        for i in candies:
            out.append( mostcandies(i+extraCandies) )
        return out
