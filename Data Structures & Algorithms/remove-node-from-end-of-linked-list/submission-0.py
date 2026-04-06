# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev = ListNode(next=head)
        slow = head
        fast = head
        # [1, 4, 6, 5, 2, 4, 4] n = 7
        if not head:
            return []
        
        # n = 3 [1, 4, 7]
        # 0 1 2 -> so need to move twice, do n - 1
        for i in range(n - 1):
            fast = fast.next
        while fast.next is not None:
            slow = slow.next
            fast = fast.next
            prev = prev.next
        prev.next = slow.next
        if slow == head:
            return head.next 
        else:
            return head

        


