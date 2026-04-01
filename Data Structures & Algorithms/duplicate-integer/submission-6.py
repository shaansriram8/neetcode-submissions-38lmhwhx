class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        len_arr = len(nums)
        seen = set(nums)

        return len(seen) != len_arr