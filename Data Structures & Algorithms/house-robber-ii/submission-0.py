class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        rob1 = self.helper(nums[1:]) # exclude first house
        rob2 = self.helper(nums[:-1]) # exclude last house
        return max(rob1, rob2)
    

    def helper(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        
        # return max(dp[n - 1], dp[n - 2])
        return dp[-1]

