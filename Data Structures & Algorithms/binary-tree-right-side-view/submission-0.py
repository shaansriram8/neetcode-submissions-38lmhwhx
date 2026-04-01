# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        out = []

        if not root:
            return out

        queue = deque([root])

        while queue:
            li = []
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                li.append(node.val)
            out.append(li)
        
        for i, n in enumerate(out):
            out[i] = out[i][-1]

        return out


        

        
        