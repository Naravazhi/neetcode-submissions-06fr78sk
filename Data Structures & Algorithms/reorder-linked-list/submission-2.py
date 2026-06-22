# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        dummy = ListNode(0)
        dummy.next = head

        slow = dummy
        fast = dummy

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # reverse second half
        second = slow.next
        slow.next = None
        second = self.reverseList(second)

        # merge
        self.merge(dummy.next, second)

        

    def reverseList(self, head):
        prev = None
        curr = head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev


    def merge(self, head1, head2):
        # dummy = ListNode(0)
        # curr_ptr = dummy
        curr1, curr2 = head1, head2
        while curr1 and curr2:
            nxt1 = curr1.next
            nxt2 = curr2.next

            curr1.next = curr2
            curr2.next = nxt1

            curr1 = nxt1
            curr2 = nxt2


