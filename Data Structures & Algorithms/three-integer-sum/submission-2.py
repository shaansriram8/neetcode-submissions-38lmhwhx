class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        out = []
        l, r = 0, len(nums)-1
        for i, n in enumerate(nums):
            if i > 0 and nums[i-1] == n:
                continue
            l, r, target = i+1, len(nums)-1, -n
            while l < r:
                if nums[l] + nums[r] > target:
                    r-=1
                elif nums[l] + nums[r] < target:
                    l+=1
                else:
                    out.append([n, nums[l], nums[r]])
                    while l < r and nums[l] == nums[l+1]:
                        l+=1
                    while l < r and nums[r] == nums[r-1]:
                        r-=1
                    l+=1
                    r-=1
        return out
