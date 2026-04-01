class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        min_found = float('inf')

        for string in strs:
            if len(string) < min_found:
                min_found = len(string)
        
        i = 0
        while i < min_found:
            for s in strs:
                if s[i] != strs[0][i]:
                    return s[:i]
            i+=1
        
        return strs[0][:i]


        