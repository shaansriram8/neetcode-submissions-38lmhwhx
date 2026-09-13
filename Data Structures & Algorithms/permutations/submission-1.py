class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res, path = [], []
        n = len(nums)
        state = [False] * n
        def backtrack():
            if len(path) == n:
                res.append(path[:])
                return
            
            for i in range(n):
                if state[i] == True:
                    continue
                state[i] = True
                path.append(nums[i])
                backtrack()
                path.pop()
                state[i] = False
        backtrack()
        return res
        