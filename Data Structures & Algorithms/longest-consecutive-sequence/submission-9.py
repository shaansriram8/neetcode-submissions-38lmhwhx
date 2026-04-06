class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        maxcount = 0
        for num in nums:
            ctr = 1
            if num-1 not in seen:
                curr = num
                while curr+1 in seen:
                    ctr+=1
                    curr+=1
            maxcount = max(maxcount, ctr)
        return maxcount


        