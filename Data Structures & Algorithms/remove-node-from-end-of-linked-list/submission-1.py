# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left = dummy
        right = head

        while n > 0:
            right = right.next
            n -= 1
        while right:
            right = right.next
            left = left.next

        left.next = left.next.next

        return dummy.next


        # fast = head
        # slow = head
        # for i in range(n):
        #     fast = fast.next
        # while fast and fast.next:
        #     slow = slow.next
        #     fast = fast.next.next
        # slow.prev.next = slow.next
        # return head


        # # fast = head
        # # slow = head
        # # for i in range(n):
        # #     fast = fast.next

        # # while fast and fast.next:
        # #     slow = slow.next
        # #     fast = fast.next

        # # if slow.next:
        # #     slow.next = slow.next.next
        # # return head


















        
        # # fast = head
        # # slow = head

        # # for i in range(n):
        # #     if fast.next:
        # #         fast = fast.next
            

        # # while slow and fast:
        # #     slow = slow.next
        # #     fast = fast.next

        # # return slow.next
