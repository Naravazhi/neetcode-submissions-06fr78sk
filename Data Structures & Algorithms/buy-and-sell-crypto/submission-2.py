class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum_price = prices[0]
        max_profit = 0

        for i in range(1, len(prices)):
            profit = prices[i] - minimum_price
            max_profit = max(profit, max_profit)
            minimum_price = min(minimum_price, prices[i])
        return max_profit
            