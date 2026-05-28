class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                profit += (prices[i] - prices[i - 1])
        return profit
        # max_profit = 0
        # curr_min = float("inf")

        # for price in prices:
        #     if price < curr_min:
        #         curr_min = price
        #     profit = max(price - curr_min)
        #     max_profit = max(max_profit, profit)
        # prices=[1,2,3,4,5]
        # prices=[7,1,5,3,6,4]





            
        return max_profit


