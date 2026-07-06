class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        first = nums[0:len(nums)-1]
        second = nums[1:len(nums)]
        memo1 ={}
        memo2 ={}
        def robber(i, valid, memo):        
            if i in memo:
                return memo[i]
            if i >= len(valid):
                return 0
            #second base case
            memo[i] = max(valid[i] + robber((i+2), valid, memo), robber((i+1), valid, memo))
            return memo[i]
        return max(robber(0, first, memo1), robber(0, second, memo2))
        