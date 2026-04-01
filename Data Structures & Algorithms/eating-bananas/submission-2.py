import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #koko eating banyanas

        #h hours to eat all bananas
        #k = rate at which we eat
        #we want to search over k
        #can only eat out of one pile per hour
        low, high = 1, max(piles)
        best = 0
        while low <= high:
            mid = (low + high) // 2
            print(mid)
            num_hours = 0
            for pile in piles:
                num_hours += (pile + mid - 1) // mid
            print(num_hours)
            if num_hours > h:
                low = mid + 1
            else:
                high = mid -1
                best = mid
        return best
