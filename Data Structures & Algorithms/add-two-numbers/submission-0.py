# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1p = l1
        l2p = l2
        head_new = ListNode(0)
        curr = head_new
        carry = 0

        while l1p and l2p:
            sum_at_i = l1p.val + l2p.val + carry
            carry = 0
            if sum_at_i >= 10:
                sum_at_i = sum_at_i % 10
                carry = 1
            new_node = ListNode(sum_at_i, None)
            curr.next = new_node
            curr = curr.next
            l1p = l1p.next
            l2p = l2p.next

        while l1p:
            sum_at_i = l1p.val + carry
            carry = 0
            if sum_at_i >= 10:
                sum_at_i = sum_at_i % 10
                carry = 1
            new_node = ListNode(sum_at_i, None)
            curr.next = new_node
            curr = curr.next
            l1p = l1p.next

        while l2p:
            sum_at_i = l2p.val + carry
            carry = 0
            if sum_at_i >= 10:
                sum_at_i = sum_at_i % 10
                carry = 1
            new_node = ListNode(sum_at_i, None)
            curr.next = new_node
            curr = curr.next
            l2p = l2p.next
        
        if carry:
            curr.next = ListNode(val=carry)

        return head_new.next

        
