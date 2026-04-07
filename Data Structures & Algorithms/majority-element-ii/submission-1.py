class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = len(nums) // 3
        hashmap = {}
        out = []
        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1
        for key, val in hashmap.items():
            if val > count:
                out.append(key)
        return out
