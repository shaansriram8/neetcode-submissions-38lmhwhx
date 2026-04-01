class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        seen = {}
        for ind, num in enumerate(nums):
            compliment = target - num
            if compliment in seen:
                return [seen[compliment], ind]
            seen[num] = ind

        