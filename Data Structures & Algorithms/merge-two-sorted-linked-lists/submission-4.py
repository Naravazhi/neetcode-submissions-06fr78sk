# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:


        ptr1 = list1
        ptr2 = list2
        dummy = ListNode(None)
        curr = dummy

        while ptr1 and ptr2:
            if ptr1.val <= ptr2.val:
                curr.next = ptr1
                ptr1 = ptr1.next
            else:
                curr.next = ptr2
                ptr2 = ptr2.next
            curr = curr.next

        if ptr1:
            curr.next = ptr1
        if ptr2:
            curr.next = ptr2
        return dummy.next




        
















        # if not list1:
        #     return list2

        # if not list2:
        #     return list1


        # s1, s2 = list1, list2
        # dummy = ListNode()
        # curr = dummy

        # while s1 and s2:
        #     if s1.val <= s2.val:
        #         curr.next = s1
        #         s1 = s1.next

        #     else:
        #         curr.next = s2
        #         s2 = s2.next

        #     curr = curr.next



        # if s1:
        #     curr.next = s1

        # if s2:
        #     curr.next = s2

        # return dummy.next
