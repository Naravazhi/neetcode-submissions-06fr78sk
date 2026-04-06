class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        if x == 1:
            return 1

        halfed = x // 2

        left = 1
        right = halfed

        while left <= right:
            mid = left + (right - left) // 2
            if mid * mid == x:
                return mid
            elif mid * mid > x:
                right = mid - 1
            else:
                left = mid + 1
        return left - 1