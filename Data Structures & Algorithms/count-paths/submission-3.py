class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            dp[i][0] = 1
        for j in range(n):
            dp[0][j] = 1

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[m - 1][n - 1]





























# class Solution:
#     def uniquePaths(self, m: int, n: int) -> int:

#         dp = [[0] * n for _ in range(m)]
#         # dp[i][j] represents the number of unique paths that can be taken to this spot
#         # on the grid 

#         dp[0][0] = 1

#         for i in range(1, m):
#             dp[i][0] = dp[i - 1][0]

#         for j in range(1, n):
#             dp[0][j] = dp[0][j - 1]


#         for i in range(1, m):
#             for j in range(1, n):
#                 dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
#         return dp[m - 1][n - 1]