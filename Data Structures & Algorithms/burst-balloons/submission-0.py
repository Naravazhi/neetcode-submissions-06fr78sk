class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # were doing a 2d cache
        # what if i pop this number last? 
        # dp[l][r] = left value as first index, right value as second index

        # adding implicit 1 to beginning and end
        # memo for caching
        # n^2 number of subarrays * n items = n ^ 3
        nums = [1] + nums + [1]
        dp = {}
        def dfs(l, r):
            if l > r:
                return 0
            if (l, r) in dp:
                return dp[(l, r)]
            dp[(l, r)] = 0
            for i in range(l, r + 1):
                coins = nums[l - 1] * nums[i] * nums[r + 1]
                coins += dfs(l, i - 1) + dfs(i + 1, r)
                dp[(l, r)] = max(dp[(l, r)], coins)
            return dp[(l, r)]


        return dfs(1, len(nums) - 2) # avoid 1 in beginning and end

