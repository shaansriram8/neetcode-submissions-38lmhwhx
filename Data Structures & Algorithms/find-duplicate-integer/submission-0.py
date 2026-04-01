class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        hashset = {}

        for num in nums:
            hashset[num] = hashset.get(num, 0) + 1
        
        for num in hashset:
            if hashset[num] > 1:
                return num
        
        