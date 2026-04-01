# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head #init slow and fast pointers

        while fast and fast.next: #while fast is not at the end
            slow = slow.next #slow moves half as fast, so we end up at middle
            fast = fast.next.next

        l2 = slow.next
        slow.next = None

        prev = None
        while l2:
            nxt = l2.next
            l2.next = prev
            prev = l2
            l2 = nxt
        l2 = prev

        l1 = head
        while l2: 
            n1, n2 = l1.next, l2.next
            l1.next = l2
            l2.next = n1
            l1, l2 = n1, n2


            

            






        