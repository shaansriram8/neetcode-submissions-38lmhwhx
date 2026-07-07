class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        hashmap = defaultdict(list)
        count = 0
        for ind, num in enumerate(nums):
            hashmap[num].append([ind, num])
        print(hashmap)
        for key, val in hashmap.items():
            print(val)
            for pair in val:
                j = 1
                while j < len(val):
                    if val[j][0] > pair[0]:
                        count +=1
                    j+=1
        return count
                    




        