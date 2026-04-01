class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        #we want to map the character count of each string to the list of anagrams

        res = defaultdict(list)

        for s in strs:
            count = [0] * 26 #a -> z

            for c in s:
                count[ord(c)-ord("a")] += 1 #proper indexing using ascii value

            res[tuple(count)].append(s)
        
        return list(res.values())

        