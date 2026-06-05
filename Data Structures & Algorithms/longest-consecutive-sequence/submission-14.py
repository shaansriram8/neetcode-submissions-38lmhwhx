class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsT = set(nums)
        longest = 0
        for num in nums:
            counter = 0
            if num-1 not in numsT:
                temp = num
                while temp in numsT:
                    temp+=1
                    counter+=1
            longest = max(longest, counter)
        return longest
            