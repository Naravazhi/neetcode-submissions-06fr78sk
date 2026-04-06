# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        carry = 0
        curr = dummy
        while l1 and l2:
            currSum = l1.val + l2.val + carry
            place_this_value = 0
            if currSum > 9:
                place_this_value = currSum % 10
                carry = currSum // 10
            else:
                carry = 0
                place_this_value = currSum
            curr.next = ListNode(place_this_value)
            curr = curr.next
            l1 = l1.next
            l2 = l2.next
        while l1:
            currSum = l1.val + carry
            place_this_value = 0
            if currSum > 9:
                place_this_value = currSum % 10
                carry = currSum // 10
            else:
                carry = 0
                place_this_value = currSum

            curr.next = ListNode(place_this_value)
            curr = curr.next
            l1 = l1.next
        while l2:
            currSum = l2.val + carry
            place_this_value = 0
            if currSum > 9:
                place_this_value = currSum % 10
                carry = currSum // 10
            else:
                carry = 0
                place_this_value = currSum

            curr.next = ListNode(place_this_value)
            curr = curr.next
            l2 = l2.next
        if carry:
            curr.next = ListNode(carry)
        return dummy.next

            

            





