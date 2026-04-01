class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix = [0] * len(nums)
        prefix[0] = 0
        suffix = [0] * len(nums)
        suffix[len(nums)-1] = 0

        for i in range(1, len(nums)):
            prefix[i] = nums[i-1] + prefix[i-1]

        for i in range(len(nums)-2, -1, -1):
            suffix[i] = nums[i+1] + suffix[i+1]
        
        for i in range(0, len(nums)):
            if prefix[i] == suffix[i]:
                return i
        return -1
        