class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        table = {}

        for ind, num in enumerate(nums):
            if num in table and abs(ind - table[num]) <= k:
                return True
            table[num] = ind
        return False




        

        