class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        if n == 0:
            return True

        if len(flowerbed) == 1 and flowerbed[0] == 0:
            return True

        count = 0
        if flowerbed[0] == 0 and flowerbed[1] == 0:
            flowerbed[0] = 1
            count += 1
            if count == n:
                return True

        if flowerbed[-1] == 0 and flowerbed[-2] == 0:
            flowerbed[-1] = 1
            count += 1
            if count == n:
                return True

        for i in range(1, len(flowerbed)-1):
            left = flowerbed[i-1]
            mid = flowerbed[i]
            right = flowerbed[i+1]
            if left == 0 and mid == 0 and right == 0:
                flowerbed[i] = 1
                count += 1
        
            if count == n:
                return True
        return False