class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])

        n = len(nums)
        dp = [0] * (n + 1)
        
        dp[0] = 0
        dp[1] = max(nums[0], nums[1])

        for i in range(len(nums)):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

        return max(dp[n - 1], dp[n - 2])