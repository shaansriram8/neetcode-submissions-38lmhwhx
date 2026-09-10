class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        #need to handle two cases:
        #nums[i+1] > nums[i] (increasing)
        #nums[i+1] < nums[i] (decreasing)

        maxseen = 0 
        n = len(nums)
        inc, dec = 1, 1
        if len(nums) == 1:
            return 1
        for i in range(1, n):
            if nums[i] > nums[i-1]:
                inc +=1
                dec = 1
            elif nums[i] < nums[i-1]:
                dec +=1
                inc = 1
            else:
                inc, dec = 1, 1
            maxseen = max(maxseen, inc, dec)
        return maxseen







        