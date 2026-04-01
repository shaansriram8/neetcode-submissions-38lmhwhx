class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        out = []
        words.sort(key=len) 
        for i in range(0, len(words)):
            for j in range(i+1, len(words)):
                if words[i] in words[j]:
                    out.append(words[i])
                    break
        return out

        