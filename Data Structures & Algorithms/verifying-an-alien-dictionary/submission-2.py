class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        hashmap = {}
        for i, c in enumerate(order): #relative ordering of letter->index
            hashmap[c] = i
        
        for i in range(len(words)-1): #loops over 2 words at a time
            word1, word2 = words[i], words[i+1]
            for j in range(len(word1)):
                if j == len(word2):
                    return False
                if word1[j] != word2[j]: 
                    if hashmap[word1[j]] < hashmap[word2[j]]:
                        break 
                    elif hashmap[word1[j]] > hashmap[word2[j]]:
                        return False
        return True
            


        
        #.  d, d, d
        #check if curr < next
        
        

         
        



        