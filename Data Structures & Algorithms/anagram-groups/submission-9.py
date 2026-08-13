class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        out = []
        hashmap = defaultdict(list)
        for string in strs:
            keyspace = [0] * 26
            for char in string: 
                keyspace[ord(char)-ord('a')] += 1
            hashmap[tuple(keyspace)].append(string)
        
        for val in hashmap.values():
            out.append(val)
        return out
