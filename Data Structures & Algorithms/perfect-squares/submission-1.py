class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float("inf")] * (n + 1)
        #dp[0] = 1 # least number fo perfect squares is 0^2 = 0
        dp[0] = 0



        for i in range(1, n + 1):
            # for j in range(1, n // 2 + 1):
            j = 1
            while j * j <= i:
                if i - j * j >= 0:
                    dp[i] = min(dp[i - j * j] + 1, dp[i])
                j += 1

        return dp[n]

