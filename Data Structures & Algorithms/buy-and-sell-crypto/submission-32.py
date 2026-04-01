class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        max_profit =0
        while r < len(prices):
            curr = prices[r] - prices[l]
            if prices[r] < prices[l]:
                l =r
            max_profit = max(max_profit, curr)
            r +=1
        return max_profit

        
      