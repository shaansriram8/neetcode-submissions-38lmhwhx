class Solution:
    def maxDifference(self, s: str) -> int:
        freq = {}
        for c in s:
            freq[c] = freq.get(c, 0) + 1
        
        max_odd = 0
        min_even = float('inf')
        for key, val in freq.items():
            if val%2 == 1:
                max_odd = max(max_odd, val)
            elif val%2 == 0:
                min_even = min(min_even, val)
        
        print(max_odd)
        print(min_even)
        return (max_odd - min_even)


        