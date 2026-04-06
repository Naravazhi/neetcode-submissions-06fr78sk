class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = amount
        dp = [float("inf")] * (n + 1)

        dp[0] = 0


        for i in range(1, n + 1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], 1 + dp[i - coin])
        return dp[n] if not dp[n] == float("inf") else -1