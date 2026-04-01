class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:

        l, r = 0, 1

        while r < len(arr):
            max_curr = 0
            while r < len(arr):
                curr = arr[r]
                max_curr = max(curr, max_curr)
                r+=1
            arr[l] = max_curr
            l+=1
            r = l+1
        arr[-1] = -1
        return arr






            


        