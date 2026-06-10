# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head

        curr = head
        size = 0
        while curr:
            size += 1
            curr = curr.next
        crr = dummy
        for i in range(size - n):
            crr = crr.next
        if crr.next:
            crr.next = crr.next.next
        return dummy.next




