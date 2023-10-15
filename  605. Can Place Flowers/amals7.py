class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                lpot = (i ==0) or (flowerbed[i-1] ==0)
                rpot = (i == len(flowerbed)-1) or (flowerbed[i+1] ==0)
                if lpot and rpot:
                    flowerbed[i] = 1
                    count +=1
        return count>=n
