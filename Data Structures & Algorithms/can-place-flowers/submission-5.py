class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        cnt = n
        for i, n in enumerate(flowerbed):
            if i == len(flowerbed)-1:
                if cnt and flowerbed[i] == 0 and flowerbed[i-1] == 0:
                    flowerbed[i] = 1
                    cnt -=1
            elif i == 0:
                if cnt and flowerbed[i] == 0 and flowerbed[i+1] == 0:
                    flowerbed[i] = 1
                    cnt-=1
            else:
                if cnt and flowerbed[i-1] == 0 and flowerbed[i+1] == 0 and flowerbed[i] == 0:
                    flowerbed[i] =1
                    cnt -=1
        return cnt == 0

            

        