class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hashmap = {}
        out = []
        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1
        
        for key, val in hashmap.items():
            if val > (len(nums) / 3):
                out.append(key)
        return out