class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # [1, 2, -3, 4]
        # product = 1
        product = nums[0]
        for i in range(len(nums)):
            curr_product = nums[i]
            product = max(product, curr_product)
            for j in range(i + 1, len(nums)):
                curr_product *= nums[j]
                product = max(product, curr_product)
        return product


        # for i 







        # n = len(nums)
        # dp = [1] * n


        # [1, 2, -3, 4]
        # 


        # for i in range(n):
        #     dp[i] = dp[i - 1] * nums[i]
        #     nums[i] * 
