class Solution:
    def productExceptSelf(self, nums:List[int]) -> List[int]:
        res = [1] * len(nums)

        running_product = 1
        for i in range(len(nums)):
            res[i] *= running_product
            running_product *= nums[i]
        running_product = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= running_product
            running_product *= nums[i]
        return res
































    # def productExceptSelf(self, nums: List[int]) -> List[int]:
    #     output = [0] * len(nums)
    #     running_product = 1

    #     for i in range(len(nums)):
    #         output[i] = running_product
    #         running_product *= nums[i]

    #     running_product = 1
    #     for i in range(len(nums) - 1, -1, -1):
    #         output[i] = output[i] * running_product
    #         running_product *= nums[i]
    #     return output















# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
        










