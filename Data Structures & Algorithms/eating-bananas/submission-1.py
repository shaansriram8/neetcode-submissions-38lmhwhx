class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #piles[i] is the number of bananas in ith pile
        #h = number of hours you have to eat bananas
        #k -> bananas/hour

        low, high = 1, max(piles)
        #[1, 2, 3, 4]
        #k starts at 2
        best_k = 0

        while low <= high:
            total = 0
            k = (low + high) // 2 #middle speed
            for pile in piles:
                total += (pile+k-1)//k #find total time
            if total > h: #if total time > allowed
                low = k+1 #increase speed
            if total <= h: #if total time <= allowed
                high = k-1 #decrease k
                best_k = k
        return best_k




        

        