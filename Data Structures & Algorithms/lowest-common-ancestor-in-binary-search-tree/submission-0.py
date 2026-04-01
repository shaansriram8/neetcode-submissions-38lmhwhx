# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        if not root:
            return None
        
        if p.val < root.val and q.val < root.val:
             val = root.left
             return self.lowestCommonAncestor(val, p, q)
        
        elif p.val > root.val and q.val > root.val:
            val = root.right
            return self.lowestCommonAncestor(val, p, q)   
        else:
            return root