# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        hashset = {}
        curr = head

        while curr:
            hashset[curr] = hashset.get(curr, 0) + 1
            if hashset[curr] > 1:
                return True
            hashset[curr] = curr.val
            curr = curr.next

        return False
        