class Solution:
    def canPermutePalindrome(self, s: str) -> bool:

        freq = {}

        for char in s:
            freq[char] = freq.get(char, 0) + 1
        odds = 0
        for val in freq.values():
            if val % 2 != 0:
                odds +=1
        if odds > 1:
            return False
        return True

        