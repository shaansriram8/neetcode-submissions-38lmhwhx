class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums = sorted(nums)
        res = []
        for i in range(n):
            if i > 0 and nums[i-1] == nums[i]:
                continue
            j, k = i+1, n-1
            target = -nums[i]
            while j < k:
                if nums[j] + nums[k] > target:
                    k-=1
                elif nums[j] + nums[k] < target:
                    j+=1
                else:
                    while j < k and nums[j+1] == nums[j]:
                        j+=1
                    res.append([nums[i], nums[j], nums[k]])
                    j+=1
        return res





