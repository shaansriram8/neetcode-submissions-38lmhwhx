class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_seen = -1

        for num in range(len(arr)-1, -1, -1):
            temp = arr[num]
            arr[num] = max_seen
            max_seen = max(temp, max_seen)
        return arr








            


        