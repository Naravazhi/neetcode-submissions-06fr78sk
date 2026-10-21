# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
      

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum_cost = prices[0]
        max_profit = 0
        for i in range(1, len(prices)):
            max_profit = max(prices[i] - minimum_cost, max_profit)
            minimum_cost = min(minimum_cost, prices[i])
        return max_profit
