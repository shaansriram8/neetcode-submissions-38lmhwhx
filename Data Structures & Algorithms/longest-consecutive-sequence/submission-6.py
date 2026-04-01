class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        #its important we denote the start of a sequence
        seen = set(nums)
        max_count = 0
        for i in range(len(nums)):
            if nums[i]-1 not in seen: #if we are at the start of a sequence
                count = 1
                curr = nums[i]
                while curr+1 in seen:
                    count +=1
                    curr +=1
                max_count = max(max_count, count)
        return max_count

        