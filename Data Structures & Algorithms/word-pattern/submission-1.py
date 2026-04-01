class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        hashmap = {}

        if len(words) != len(pattern):
            return False

        for i, c in enumerate(pattern):
            if c not in hashmap:
                if words[i] in hashmap.values():
                    return False
                hashmap[c] = words[i]
            else:
                if hashmap[c] != words[i]:
                    return False
        return True
