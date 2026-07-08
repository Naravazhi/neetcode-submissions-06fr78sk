class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        rob1, rob2 = self.steal(nums[:-1]), self.steal(nums[1:])
        return max(rob1, rob2)


    def steal(self, arr):
        n = len(arr)
        if n == 0:
            return 0
        if n == 1:
            return arr[0]

        dp = [0] * n

        dp[0] = arr[0]
        dp[1] = max(arr[0], arr[1])
        for i in range(2, n):
            dp[i] = max(dp[i - 1], arr[i] + dp[i - 2])
        return dp[n - 1]

        

    