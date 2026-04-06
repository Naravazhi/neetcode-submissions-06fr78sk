class Solution:
    def hammingWeight(self, n: int) -> int:

        cnt = 0
        while n:
            cnt += 1 if n & 1 else 0
            n >>= 1
        return cnt




        cnt = 0
        while n:
            cnt += 1 if n & 1 else 0
            n >>= 1
        return cnt



        # cnt = 0
        # while n:
        #     cnt += 1 if n & 1 else 0
        #     n >>= 1
        # return cnt
