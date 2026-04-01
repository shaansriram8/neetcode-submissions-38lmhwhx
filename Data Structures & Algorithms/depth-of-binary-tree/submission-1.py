# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0
        
        stack = [[root, 1]]
        max_depth = 0

        while stack:
            val, depth = stack.pop()
            max_depth = max(max_depth, depth)
            if val.left:
                stack.append((val.left, depth+1))
            if val.right:
                stack.append((val.right, depth+1))
        return max_depth

        