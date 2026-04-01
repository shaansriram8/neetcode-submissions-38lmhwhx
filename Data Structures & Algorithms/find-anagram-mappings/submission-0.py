class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hashmap = {}
        out = [0] * len(nums1)
        for ind, num in enumerate(nums2):
            hashmap[num] = ind
        
        for i in range(len(nums1)):
            out[i] = hashmap[nums1[i]]
        return out
