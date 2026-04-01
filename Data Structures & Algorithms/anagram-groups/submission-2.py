class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for string in strs:
            arr = [0] * 26
            for c in string:
                arr[ord(c)-ord('a')]+=1 #create a key for each string
            res[tuple(arr)].append(string)
        return list(res.values())