class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        pairs = {}
        stack = []
        out = [-1]*len(nums1)
        for i, n in enumerate(nums1):
            pairs[n] = i
        
        for i in range(len(nums2)):
            cur = nums2[i]
            while stack and stack[-1] < cur:
                val = stack.pop()
                index = pairs[val]
                out[index] = cur
            if cur in pairs:
                stack.append(cur)
        return out



            

        
                
