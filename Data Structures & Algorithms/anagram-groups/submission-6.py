class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        out = []
        hashmap = {}
        for string in strs:
            key = [0] * 26
            for char in string:
                key[ord(char)-ord('a')] += 1
            if tuple(key) not in hashmap:
                hashmap[tuple(key)] = []
                hashmap[tuple(key)].append(string)
            else:
                hashmap[tuple(key)].append(string)
        
        for key, val in hashmap.items():
            out.append(val)
        return out

            
        



            
            
            

         
        