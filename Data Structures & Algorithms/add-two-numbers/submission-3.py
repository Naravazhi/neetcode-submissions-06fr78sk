# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = ListNode(0)
        curr = dummy

        while l1 and l2:
            digit_sum = l1.val + l2.val + carry
            if digit_sum >= 10:
                carry = 1
            else:
                carry = 0
            curr.next = ListNode(digit_sum % 10)
            curr = curr.next
            l1 = l1.next
            l2 = l2.next
        while l1:
            digit_sum = l1.val + carry
            if digit_sum >= 10:
                carry = 1
            else:
                carry = 0
            curr.next = ListNode(digit_sum % 10)
            curr = curr.next
            l1 = l1.next
        while l2:
            digit_sum = l2.val + carry
            if digit_sum >= 10:
                carry = 1
            else:
                carry = 0
            curr.next = ListNode(digit_sum % 10)
            curr = curr.next
            l2 = l2.next
        if carry:
            curr.next = ListNode(carry)
        return dummy.next
