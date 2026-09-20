class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapping = defaultdict(list)
        out = []
        for string in strs:
            key = [0] * 26
            for c in string:
                key[ord(c)-ord('a')] +=1
            mapping[tuple(key)].append(string)
        
        for val in mapping.values():
            out.append(val)
        return out
