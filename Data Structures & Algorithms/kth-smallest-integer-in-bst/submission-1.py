# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #we can find the kth smallest value by traversing along the smallest values
        #decrementing a global counter each time

        res = root.val
        count = k

        def dfs(node):
            nonlocal res, count
            if count <= 0:
                return
            if not node:
                return
            dfs(node.left)
            count-=1
            if count == 0:
                res = node.val
                return
            dfs(node.right)
        dfs(root)
        return res