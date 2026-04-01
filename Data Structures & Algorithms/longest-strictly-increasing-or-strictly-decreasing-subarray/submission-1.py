class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        res = 0
        inc, dec = 1, 1
        for i in range(1, len(nums)):
            if nums[i-1] == nums[i]:
                inc, dec = 1, 1
            elif nums[i] > nums[i-1]: #increasing
                inc +=1
                dec = 1
            elif nums[i] < nums[i-1]: #decresing
                dec +=1
                inc = 1
            res = max(res, dec, inc)
        return res
            




        