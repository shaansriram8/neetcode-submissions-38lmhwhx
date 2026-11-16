# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        maxseen = float('-inf')
        
        ctr = 0
        def dfs(node, maxseen):
            nonlocal ctr
            if not node:
                return
            if node.val >= maxseen:
                maxseen = node.val
                ctr += 1 
            dfs(node.left, maxseen)
            dfs(node.right, maxseen)
        dfs(root, maxseen)
        return ctr


        