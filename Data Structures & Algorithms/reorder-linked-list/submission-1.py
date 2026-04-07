# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# class Solution:
#     def reorderList(self, head: Optional[ListNode]) -> None:


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        h2 = self.reverseList(slow.next)
        slow.next = None
        head = self.merge(head, h2)
        return





    def reverseList(self, middle: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = middle
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev


    def merge(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        ptr = dummy
        while l1 and l2:
            # if l1.val <= l2.val:
            #     ptr.next = l1
            #     l1 = l1.next
            # else:
            #     ptr.next = l2
            #     l2 = l2.next
            # ptr = ptr.next
            ptr.next = l1
            l1 = l1.next
            ptr = ptr.next
            ptr.next = l2
            l2 = l2.next
            ptr = ptr.next

        if l1:
            ptr.next = l1

        if l2:
            ptr.next = l2
        return dummy.next




        

    #     if not head or not head.next or not head.next.next:
    #         return

    #     slow = head
    #     fast = head


    #     while fast and fast.next:
    #         fast = fast.next.next
    #         slow = slow.next


    #     second = self.reverse(slow.next)
    #     slow.next = None


    #     first = head
    #     while second:
    #         tmp1 = first.next
    #         tmp2 = second.next

    #         first.next = second
    #         second.next = tmp1

    #         first = tmp1
    #         second = tmp2







        




    #     # fast = head
    #     # slow = head


    #     # while fast and fast.next:
    #     #     fast = fast.next.next
    #     #     slow = slow.next

    #     # second = self.reverse(slow.next)
    #     # # cut list
    #     # slow.next = None
    #     # first = head

    #     # while second:
    #     #     tmp1 = first.next
    #     #     tmp2 = second.next

    #     #     first.next = second
    #     #     second.next = tmp1

    #     #     first = tmp1
    #     #     second = tmp2


    #     # dummy = ListNode()
    #     # curr = dummy
        


    #     # while first and second:
    #     #     if first.val <= second.val:
    #     #         curr.next = first
    #     #         first = first.next
    #     #     else:
    #     #         curr.next = second
    #     #         second = second.next

    #     #     curr = curr.next


    #     # if first:
    #     #     curr.next = first

    #     # if second:
    #     #     curr.next = second

    #     # return dummy.next


        

    # def reverse(self, start):

    #     prev = None
    #     curr = start

    #     while curr:
    #         nxt = curr.next
    #         curr.next = prev
    #         prev = curr
    #         curr = nxt
    #     return prev