class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        maxval = -1
        for key, val in freq.items():
            curr = key
            if val == 1:
                maxval = max(curr, maxval)
        return maxval
            


        