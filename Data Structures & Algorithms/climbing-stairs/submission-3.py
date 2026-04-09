class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1

        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]









# class Solution:
#     def climbStairs(self, n: int) -> int:



#         # dp[i] will represent the number of distinct ways to climb up i steps
#         dp = [0] * (n + 1)
#         # so if n = 2: 0 0 0
#         dp[0] = 1
#         dp[1] = 1


#         for i in range(2, n + 1):
#             dp[i] = dp[i - 1] + dp[i - 2]
#         return dp[n]










        
        # dp = [0] * (n + 1)

        # dp[0] = 1
        # dp[1] = 1
        


        # for i in range(2, n + 1):
        #     dp[i] = dp[i - 1] + dp[i - 2]

        # return dp[n]