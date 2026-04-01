"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldToNew = {}

        def dfs(node): #node we are visiting is passed
            if node in oldToNew: #if node in hashmap, we alr made a clone
                return oldToNew[node] #return that clone, no need to make a new one
            copy = Node(node.val)
            oldToNew[node] = copy #map old node to copy
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            return copy
        return dfs(node) if node else None