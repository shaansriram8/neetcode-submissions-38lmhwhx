class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        path = []

        def backtrack(start, run_sum):
            if run_sum == target:
                res.append(path[:])
                return
            elif run_sum > target:
                return
            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i, run_sum + nums[i])
                path.pop()
        
        backtrack(0, 0)
        return res
