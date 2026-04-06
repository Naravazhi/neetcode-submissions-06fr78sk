# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        if not head or not head.next or not head.next.next:
            return

        slow = head
        fast = head


        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next


        second = self.reverse(slow.next)
        slow.next = None


        first = head
        while second:
            tmp1 = first.next
            tmp2 = second.next

            first.next = second
            second.next = tmp1

            first = tmp1
            second = tmp2







        




        # fast = head
        # slow = head


        # while fast and fast.next:
        #     fast = fast.next.next
        #     slow = slow.next

        # second = self.reverse(slow.next)
        # # cut list
        # slow.next = None
        # first = head

        # while second:
        #     tmp1 = first.next
        #     tmp2 = second.next

        #     first.next = second
        #     second.next = tmp1

        #     first = tmp1
        #     second = tmp2


        # dummy = ListNode()
        # curr = dummy
        


        # while first and second:
        #     if first.val <= second.val:
        #         curr.next = first
        #         first = first.next
        #     else:
        #         curr.next = second
        #         second = second.next

        #     curr = curr.next


        # if first:
        #     curr.next = first

        # if second:
        #     curr.next = second

        # return dummy.next


        

    def reverse(self, start):

        prev = None
        curr = start

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev