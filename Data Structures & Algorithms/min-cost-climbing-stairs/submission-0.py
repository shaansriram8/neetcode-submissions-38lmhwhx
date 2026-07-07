class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}
        def Helper(i):
            if i in memo:
                return memo[i]
            if i >= len(cost):
                return 0
            memo[i] = cost[i] + min(Helper(i+1), Helper(i+2))
            return memo[i]
        return min(Helper(0), Helper(1))
