class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        hashmap = {}
        for i, c in enumerate(order): #relative ordering of letter->index
            hashmap[c] = i
        
        for i in range(len(words)-1):
            word1, word2 = words[i], words[i+1]

            length = min(len(word1), len(word2))
            flag = False
            for j in range(length):
                print(word1[j], word2[j])
                if word1[j] != word2[j]: 
                    if hashmap[word1[j]] < hashmap[word2[j]]:
                        flag = True
                        break 
                    elif hashmap[word1[j]] > hashmap[word2[j]]:
                        return False
            if len(word1) > len(word2) and flag == False:
                return False
        return True
            


        
        #.  d, d, d
        #check if curr < next
        
        

         
        



        