# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        queueP = deque([p])
        queueQ = deque([q])

        while queueP and queueQ:
            p1 = queueP.popleft()
            q1 = queueQ.popleft()

            if not p1 and not q1:
                continue
            
            if not p1 or not q1 or p1.val != q1.val:
                return False
            
            queueP.append(p1.left)
            queueP.append(p1.right)
            queueQ.append(q1.left)
            queueQ.append(q1.right)
        
        return True
        
        