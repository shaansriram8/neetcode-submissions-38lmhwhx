class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #[10,1,5,6,7,1]
        # l  r
        l, r = 0, 1
        max_prof = 0 #4

        while r < len(prices):
            if prices[r] > prices[l]:
                curr = prices[r] - prices[l]
                max_prof = max(max_prof, curr)
                r+=1
            else:
                l = r
                r+=1
        return max_prof

            


        