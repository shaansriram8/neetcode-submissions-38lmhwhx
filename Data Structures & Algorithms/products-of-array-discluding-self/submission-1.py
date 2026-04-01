class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)
        prefix = [0] * n
        suff = [0] * n
        res = [0] * n
        prefix[0], suff[n-1] = 1, 1

        for i in range(1, n):
            prefix[i] = prefix[i-1] * nums[i-1]

        for i in range(n-2, -1, -1):
            suff[i] = nums[i+1] * suff[i+1]

        for i in range(n):
            res[i] = suff[i] * prefix[i]
        
        return res


                 


        
        

        

                




        