class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        seen = 0
        count = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count = 1
                while i < len(nums)-1 and nums[i+1] == 1:
                    count +=1
                    i+=1
            seen = max(seen, count)
        return seen
