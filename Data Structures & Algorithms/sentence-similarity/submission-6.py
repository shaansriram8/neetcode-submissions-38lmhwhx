class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:

        if len(sentence1) != len(sentence2):
            return False

        seen = set()
        for a, b in similarPairs:
            seen.add((a, b))

        for i in range(len(sentence1)):
            a, b = sentence1[i], sentence2[i]
            if a!=b and (a, b) not in seen and (b, a) not in seen:
                return False
        return True
        