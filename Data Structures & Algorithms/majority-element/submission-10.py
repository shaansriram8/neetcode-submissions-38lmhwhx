class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        majority = 0
        hashmap = {}
        n = len(nums)/2
        print(n)
        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1

        print(hashmap)

        for num, count in hashmap.items():
            if count > n:
                majority = num
        
        return majority

        