class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        out = []
        for word in strs:
            key = [0] * 26
            for c in word:
                key[ord(c) - ord('a')] +=1
            hashmap[tuple(key)].append(word)
        for key, val in hashmap.items():
            out.append(val)
        return out
        