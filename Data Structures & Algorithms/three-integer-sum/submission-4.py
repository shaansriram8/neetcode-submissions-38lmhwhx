class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        out = []
        nums.sort()
        #[-4, -1, -1, 0, 1, 2]
        #      i   j        k  


        for i, n in enumerate(nums):
            target = -n
            if i > 0 and nums[i-1] == nums[i]:
                continue
            #print(i)
            j, k = i+1, len(nums)-1
            while j < k:
                if nums[j] + nums[k] > target: #if greater, decrement right
                    k-=1
                elif nums[j] + nums[k] < target: #if smaller, incrememnt left
                    j+=1
                else:
                    out.append([n, nums[j], nums[k]]) #if equal, append
                    while j < k and nums[k-1] == nums[k]: #skip duplicates
                        k-=1
                    while j < k and nums[j+1] == nums[j]: #skip duplicates
                        j+=1
                    j+=1
                    k-=1
        return out


