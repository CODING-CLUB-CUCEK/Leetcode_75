class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n==0:
            return True
        else:
            count = 0
            if len(flowerbed) == 0:
                return False
            elif len(flowerbed) == 1:
                if flowerbed[0] == 0:
                    return True
                else:
                    return False
            else:
                for i in range(len(flowerbed)):
                    if i == 0:
                        if flowerbed[i] == 0:
                            if flowerbed[i + 1] == 0:
                                flowerbed[i] = 1
                                count += 1
                    elif i == len(flowerbed) - 1:
                        if flowerbed[i] == 0:
                            if flowerbed[i - 1] == 0:
                                flowerbed[i] = 1
                                count += 1
                    else:
                        if flowerbed[i] == 0:
                            if flowerbed[i + 1] == 0 and flowerbed[i - 1] == 0:
                                flowerbed[i] = 1
                                count += 1
                if count >= n:
                    return True
                else:
                    return False