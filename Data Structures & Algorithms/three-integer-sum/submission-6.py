class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        out = []
        #[-4, -1, -1, 0, 1, 2]
        #nums[i] + nums[j] == -nums[k]

        for i in range(len(nums)):
            if i > 0 and nums[i-1] == nums[i]:
                continue
            target = -nums[i]
            j, k = i+1, len(nums)-1
            while j < k:
                if nums[j] + nums[k] < target:
                    j += 1
                elif nums[j] + nums[k] > target:
                    k -= 1
                else:
                    out.append([nums[i], nums[j], nums[k]])
                    while j < k and nums[j+1] == nums[j]:
                        j += 1
                    j+=1
        return out
                    







            