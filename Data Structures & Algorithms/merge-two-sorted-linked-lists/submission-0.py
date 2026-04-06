# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        newListDummy = ListNode()
        ptr = newListDummy

        while list1 and list2:
            if list1.val <= list2.val:
                newNode = ListNode(list1.val)
                ptr.next = newNode
                list1 = list1.next
            else:
                newNode = ListNode(list2.val)
                ptr.next = newNode
                list2 = list2.next
            ptr = ptr.next

        if list1:
            ptr.next = list1
        elif list2:
            ptr.next = list2
        
        return newListDummy.next










        # dummy = node = ListNode()

        # while list1 and list2:
        #     if list1.val <= list2.val:
        #         node.next = list1
        #         list1 = list1.next
        #     else:
        #         node.next = list2
        #         list2 = list2.next
        #     node = node.next
        
        # node.next = list1 or list2

        # return dummy.next

