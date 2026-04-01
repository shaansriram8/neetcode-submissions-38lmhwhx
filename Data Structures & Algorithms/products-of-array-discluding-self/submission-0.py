class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        out = [0] * len(nums)
        for i in range(len(nums)):
            product = 1
            for j in range(len(nums)):
                if i == j:
                    continue
                else:
                    product = product * nums[j]
            out[i] = product
        return out                


        
        

        

                




        