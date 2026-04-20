class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #prefix: [1, 2, 8, 48]
        #postfix: [48, 48, 24, 6]

        prefix = [0]*len(nums)
        prefix[0] = nums[0]
        postfix = [0]*len(nums)
        postfix[-1] = nums[-1]

        out = [0]*len(nums)

        for i in range(1, len(nums)):
            prefix[i] = prefix[i-1] * nums[i]

        for j in range(len(nums)-2, -1, -1):
            postfix[j] = postfix[j+1] * nums[j]

        for i in range(0, len(nums)):
            if i == 0:
                out[i] = postfix[i+1]
            elif i == len(nums)-1:
                out[i] = prefix[i-1]
            else:
                out[i] = prefix[i-1] * postfix[i+1]
        return out






        
