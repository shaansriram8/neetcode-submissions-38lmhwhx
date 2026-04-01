class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        hashset = {}
        n = len(nums) / 3
        arr = []

        for num in nums:
            hashset[num] = hashset.get(num, 0) + 1

        for num, count in hashset.items():
            if count > n:
                arr.append(num)
        
        return arr

        