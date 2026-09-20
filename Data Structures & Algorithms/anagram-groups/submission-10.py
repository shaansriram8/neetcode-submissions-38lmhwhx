class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #act -> [1, 0, 1]
        #if [1, 0, 1] not in keys:
            #make a key, val pair for it, append act
        #else:
            #append act to value list
        out = []
        hashmap = defaultdict(list)
        for string in strs:
            key = [0] * 26
            for c in string:
                key[ord(c) - ord('a')] +=1
            hashmap[tuple(key)].append(string)
        for value in hashmap.values():
            out.append(value)
        return out

        