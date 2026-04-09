class Solution:
    def rob(self, nums: List[int]) -> int:

        n = len(nums)
        dp = [0] * n
        if len(nums) == 1:
            return nums[0]
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, n):
            dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])
        return dp[n - 1]















# class Solution:
#     def rob(self, nums: List[int]) -> int:


#         # nums: 2, 9, 8, 3, 6
#         n = len(nums)
#         dp = [0] * n
#         dp[0] = nums[0]
#         dp[1] = max(nums[0], nums[1])

#         for i in range(2, n):
#             dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
#         return dp[n - 1]


































        # n = len(nums)

        # if len(nums) == 1:
        #     return nums[0]

        # dp = [0] * (n)
        # dp[0] = nums[0]
        # dp[1] = max(nums[0], nums[1])
        


        # for i in range(2, n):
        #     dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])
        # return dp[n - 1]