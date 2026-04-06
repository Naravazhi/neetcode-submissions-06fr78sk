class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        
        length = abs(n)
        product = 1
        for i in range(length):
            product *= x
        if n < 0:
            return 1/product
        else:
            return product
