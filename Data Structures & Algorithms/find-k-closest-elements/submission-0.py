class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l, r = 0, len(arr)-1
        while r-l >= k:
            distl = abs(arr[l] - x)
            distr = abs(arr[r] - x)
            if distl < distr:
                r-=1
            elif distr < distl:
                l+=1
            elif distr == distl:
                r-=1

        return arr[l:r+1]
                