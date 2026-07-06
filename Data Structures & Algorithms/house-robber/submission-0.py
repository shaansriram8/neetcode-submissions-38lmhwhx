class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        
        def robber(i):  
            if i in memo:
                return memo[i]
            if i >= len(nums):
                return 0
            memo[i] = max(nums[i]+robber(i+2), robber(i+1))
            return memo[i]
        return robber(0)
