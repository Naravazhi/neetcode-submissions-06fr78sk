class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        res = set()
        nums.sort()
        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1

            while left < right:
                if nums[i] + nums[left] + nums[right] == 0:
                    tmp = [nums[i], nums[left], nums[right]]
                    res.add(tuple(tmp))
                    left += 1
                    right -= 1
                elif nums[i] + nums[left] + nums[right] < 0:
                    left += 1
                else:
                    right -= 1
        return [list(i) for i in res]


        





        # res = set()
        # nums.sort()

        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         for k in range(j + 1, len(nums)):
        #             if nums[i] + nums[j] + nums[k] == 0:
        #                 tmp = [nums[i], nums[j], nums[k]]

        #                 res.add(tuple(tmp))


        # return [list(i) for i in res]





        # res = set()
        # nums.sort()

        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         for k in range(j + 1, len(nums)):
        #             if nums[i] + nums[j] + nums[k] == 0:
        #                 tmp = [nums[i], nums[j], nums[k]]
        #                 res.add(tuple(tmp))
        # return [list(i) for i in res]



        
        # n = len(nums)
        # ans = []

        # for i in range(len(nums) - 2):
        #     for j in range(1, len(nums) - 1):
        #         for k in range(2, len(nums)):
        #             if (i != j and j != k and i != k) and nums[i] + nums[j] + nums[k] == 0:
        #                 ans.append([nums[i], nums[j], nums[k]])
        # return ans
