class Solution:
    def maxProfit(self, prices: List[int]) -> int:



        max_profit = float("-inf")

        min_element = prices[0]


        for i in range(1, len(prices)):
            profit = prices[i] - min_element
            max_profit = max(max_profit, profit)
            min_element = min(min_element, prices[i])


        return max_profit if max_profit > 0 else 0
