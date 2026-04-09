class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])

        return max(self.helper(nums[0:n - 1]), self.helper(nums[1:n]))

    def helper(self, arr: List[int]) -> int:
        a = len(arr)
        dp = [0] * a

        for i in range(a):
            dp[i] = max(dp[i - 1], dp[i - 2] + arr[i])

        return dp[a - 1]




    

    















# class Solution:
#     def rob(self, nums: List[int]) -> int:
#         n = len(nums)
#         if n == 1:
#             return nums[0]
#         if n == 2:
#             return max(nums[0], nums[1])
        
#         return max(self.helper(nums[:n - 1]), self.helper(nums[1:]))



#     def helper(self, cost):

#         n = len(cost)
#         dp = [0] * n
#         dp[0] = cost[0]
#         dp[1] = max(cost[0], cost[1])

#         for i in range(2, n):
#             dp[i] = max(dp[i - 1], dp[i - 2] + cost[i])

#         return dp[n - 1]















    #     # strat is to run method on one house, then the house next to it and get max

    #     # 0 to n - 2 and 1 to n - 1
    #     return max(self.house_robber(nums[:-1]), self.house_robber(nums[1:]))
    

    # def house_robber(self, array):

    #     n = len(array)

    #     dp = [0] * n

    #     dp[0] = array[0]
    #     dp[1] = max(array[0], array[1])

    #     for i in range(2, n):
    #         dp[i] = max(dp[i - 1], dp[i - 2] + array[i])

    #     return dp[n - 1]



        