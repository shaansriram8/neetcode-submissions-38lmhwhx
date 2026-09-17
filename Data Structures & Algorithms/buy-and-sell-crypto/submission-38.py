class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        l, r = 0, 1
        maxprof = 0
        while r < len(prices):
            curr_profit = prices[r] - prices[l]
            if curr_profit < 0:
                l = r
                r+=1
            else:
                maxprof = max(maxprof, curr_profit)
                r +=1
        return maxprof


        