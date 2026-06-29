class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = defaultdict(list)
        degree = defaultdict(int)
        out = []
        #we want to prepopulate every character to have a degree of 0
        for word in words:
            for char in word:
                if char not in degree:
                    degree[char] = 0

        for i in range(len(words)-1):
            word1 = words[i] #extract paired characters
            word2 = words[i+1]
            length = min(len(word1), len(word2)) #find the length to loop over
            j = 0
            while j < length and word1[j] == word2[j]: #while we have no dependencies 
                j+=1
            if j == length: #if we reached the end of loop
                if len(word1) > len(word2):
                    return "" #ensure that the ordering isnt broken
                continue
            else: #if ordering is valid and not a prefix, add the dependency
                adj[word1[j]].append(word2[j])
                degree[word2[j]] +=1
        
        queue = deque()
        for node, deg in degree.items():
            if deg == 0:
                queue.append(node) #seed the nodes with degree of 0
        
        while queue:
            node = queue.popleft()
            out.append(node)
            for neighbor in adj[node]:
                degree[neighbor] -=1
                if degree[neighbor] == 0:
                    queue.append(neighbor)
        return "".join(out) if len(out) == len(degree) else ""

                
            
