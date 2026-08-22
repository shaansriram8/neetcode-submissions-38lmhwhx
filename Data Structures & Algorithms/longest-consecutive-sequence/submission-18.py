class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        maxseen = 0
        for num in seen:
            ctr = 0
            if num-1 not in seen:
                curr = num
                ctr = 1
                while curr+1 in seen:
                    ctr+=1
                    curr+=1
            maxseen=max(maxseen, ctr)
        return maxseen
                
        