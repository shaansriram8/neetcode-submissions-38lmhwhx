class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        profit = 0
        profits = [0]

        while right <= len(prices)-1:
            if prices[right] > prices[left]:
                if prices[right] - prices[left] > profit:
                    profits.append(prices[right] - prices[left])
                right +=1
            else:
                left +=1
                right = left+1

        return max(profits)
                

