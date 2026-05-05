class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        cleaned = set(nums)
        longest = 0
        for num in cleaned:
            streak = 1
            if num + 1 in cleaned:
                temp = num
                while temp + 1 in cleaned:
                    streak+=1
                    temp+=1
            longest = max(longest, streak)
        return longest
        