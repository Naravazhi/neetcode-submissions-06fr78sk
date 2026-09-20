# class ListNode:
#     def __init__(self, val, prev, next):

#         # self.val = val
#         # self.prev = prev
#         # self.next = next
    
class MyStack:

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()
        # linked list

        # self.curr = None


    def push(self, x: int) -> None:
        # new_node = ListNode(x)
        # curr.next = new_node
        self.q2.append(x)
        for i in range(len(self.q1)):
            self.q2.append(self.q1.popleft())
        self.q1, self.q2 = self.q2, self.q1





         
        

    def pop(self) -> int:
        return self.q1.popleft()
        
    def top(self) -> int:
        return self.q1[0]

    def empty(self) -> bool:
        return len(self.q1) == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()