class Solution:
    def climbStairs(self, n: int) -> int:
        self.memo = {}
        return self.helper(n)
    def helper(self, n):
        if n in self.memo:
            return self.memo[n]
        if n == 0 or n == 1:
            return 1
        self.memo[n] = self.helper(n-1) + self.helper(n-2)
        return self.memo[n]

        
        
        