class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        out = []
        for word in strs:
            key = [0]*26
            for char in word:
                key[ord(char)-ord('a')]+=1 #every wored gets a keyspace
            if tuple(key) not in hashmap:
                hashmap[tuple(key)] = []
            hashmap[tuple(key)].append(word)
        for val in hashmap.values():
            out.append(val)
        return out