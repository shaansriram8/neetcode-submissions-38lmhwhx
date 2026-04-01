# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balanced = [True]

        def height(root):
            if not root:
                return 0

            leftHeight = height(root.left)

            if balanced[0] is False:
                return 0
                
            rightHeight = height(root.right)

            if abs(leftHeight - rightHeight) > 1:
                balanced[0] = False
                return 0
            
            return 1 + max(leftHeight, rightHeight)

        height(root)
        return balanced[0]
            

        