class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        span = 1

        while self.stack and self.stack[-1][0] <= price:
            span += self.stack[-1][1]
            self.stack.pop()

        self.stack.append((price, span))
        return span



        # span = 1 # (price, span)
        # while self.stack and self.stack[-1][0] <= price:
        #     span += self.stack[-1][1]
        #     self.stack.pop()
        # self.stack.append((price, span))
        # return span
        

        # self.stack.append(price)

        # i = len(self.stack) - 2

        # while i >= 0 and self.stack[i] <= price:
        #     i -= 1
        # return len(self.stack) - i - 1
        # # span = 0






        # return span
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)