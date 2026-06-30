class ListNode:
    def __init__(self, val=0, prev=None, nxt=None):
        self.prev = prev
        self.next = nxt
        self.val = val

class MyCircularQueue:
    # we can use a linked list
    def __init__(self, k: int):
        self.head = ListNode(None)
        self.tail = ListNode(None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = k
        self.curr_node_count = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False

        new_node = ListNode(val = value)
        prev_node = self.tail.prev
        prev_node.next = new_node
        new_node.prev = prev_node
        new_node.next = self.tail
        self.tail.prev = new_node

        self.curr_node_count += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        removed_node = self.head.next
        next_node = removed_node.next
        self.head.next = next_node
        next_node.prev = self.head

        self.curr_node_count -= 1
        return True
        

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.head.next.val

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.tail.prev.val

    def isEmpty(self) -> bool:
        return self.curr_node_count == 0

    def isFull(self) -> bool:
        return self.curr_node_count == self.capacity

        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()