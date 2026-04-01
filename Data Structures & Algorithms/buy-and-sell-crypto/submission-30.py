class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0      # buy day
        profit = 0    # max profit

        for right in range(1, len(prices)):
            if prices[right] < prices[left]:
                left = right   # found a new lower buy price
            else:
                profit = max(profit, prices[right] - prices[left])
        
        return profit