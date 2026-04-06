class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # prefix_array = []
        # running_product = 1

        # for i in range(len(nums)):
        #     prefix_array.append(running_product)
        #     running_product *= nums[i]
        #     # [1, 2, 4, 6]
        #     # [1, 2, 4, 8] 42
        # suffix_array = []
        # new_running = 1
        # for i in range(len(nums) -1, -1, -1):
        #     suffix_array = [new_running] + suffix_array
        #     new_running *= nums[i]
        # res = []
        # for i in range(len(nums)):
        #     res.append(prefix_array[i] * suffix_array[i])
        # return res

        prefix = 1
        res = [1] * len(nums)
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res





# [-1, 0, 1, 2, 3]
# [1, -1, 0, 0, 0]
# [0, 6, 6, 3, 1]
# [0, -6, 0, 0, 0]

























# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
        # prefix_array = []
        # running_product = 1
        # for i in range(len(nums)):
            
        #     prefix_array.append(running_product)
        #     running_product *= nums[i]
        
        # suffix_array = []
        # for i in range(len(nums))












        # prefix_array = []

        # running_product = 1
        # for i in range(len(nums)):

        #     prefix_array.append(running_product)
        #     running_product *= nums[i]

        # suffix_array = []
        # new_running = 1
        # for i in range(len(nums) - 1, -1, -1):
        #     suffix_array = [new_running] + suffix_array
        #     new_running *= nums[i]

        # ans = []
        # for i in range(len(nums)):
        #     ans.append(prefix_array[i] * suffix_array[i])
        # return ans
