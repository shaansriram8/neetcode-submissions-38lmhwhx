class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l, r = 0, 0
        cnt = 0
        maxcnt = 0
        while r < len(nums):
            cnt = 0
            if nums[r] == 1:
                while r < len(nums) and nums[r] == 1:
                    r +=1
                    cnt +=1
            maxcnt = max(cnt, maxcnt)
            r+=1
            l=r
        return maxcnt