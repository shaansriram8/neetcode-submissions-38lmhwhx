class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        max_prof = 0
        while r < len(prices):
            curr_prof = prices[r] - prices[l]
            if curr_prof < 0:
                l+=1
                r=l+1
            elif curr_prof >= 0:
                r+=1
            max_prof = max(max_prof, curr_prof)
        return max_prof

        