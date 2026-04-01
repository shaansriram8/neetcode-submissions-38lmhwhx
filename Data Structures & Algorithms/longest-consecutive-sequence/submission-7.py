class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        vals = set(nums)
        maxseen = 0
        for num in nums:
            ctr = 1
            if num-1 not in vals:
                while num+1 in vals:
                    num+=1
                    ctr += 1
            maxseen = max(maxseen, ctr)
        return maxseen

                