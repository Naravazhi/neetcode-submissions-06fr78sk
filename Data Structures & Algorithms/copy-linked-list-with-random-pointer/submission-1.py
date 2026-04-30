"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        # create a node
        # map old node to new node
        # have hashmap
        # this is pass 1
        oldToCopy = {None: None} # we should initialize with None : None so if node is not made we aren't erroring
        cur = head
        while cur:
            # first pass create nodes
            oldToCopy[cur] = Node(cur.val)
            cur = cur.next
        
        cur = head
        while cur:
            copy = oldToCopy[cur]
            copy.next = oldToCopy[cur.next]
            copy.random = oldToCopy[cur.random]
            cur = cur.next
        return oldToCopy[head]
        




# class Solution:
#     def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        