class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        maxseen = 0
        for num in nums:
            i=0
            if num-1 not in seen:
                curr = num
                while curr in seen:
                    curr+=1
                    i+=1
            maxseen = max(maxseen, i)
        return maxseen
        