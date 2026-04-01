class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        out = []
        if len(nums) < 4:
            return out
        nums.sort() #-3, 0, 1, 2, 3, 3
        for i in range(len(nums)):
            if i > 0 and nums[i-1] == nums[i]:
                continue
            for j in range(i+1, len(nums)):
                if j > i+1 and nums[j-1] == nums[j]:
                    continue
                l, r = j+1, len(nums)-1
                semitarget = target - nums[i] - nums[j]
                while l < r:
                    if nums[l] + nums[r] < semitarget:
                        l+=1
                    elif nums[l] + nums[r] > semitarget:
                        r-=1
                    else:
                        out.append([nums[i], nums[j], nums[l], nums[r]])
                        while l < r and nums[r-1] == nums[r]: #skip duplicates
                            r-=1
                        while l < r and nums[l+1] == nums[l]: #skip duplicates
                            l+=1
                        l+=1
                        r-=1
        return out
                        





        