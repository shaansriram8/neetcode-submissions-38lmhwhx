class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        hashmap = {}
        for ind, num in enumerate(nums):
            hashmap[num] = ind
        
        n = len(nums)
        for i in range(n + 1):
            if i not in hashmap:
                return i
        return val

          

        