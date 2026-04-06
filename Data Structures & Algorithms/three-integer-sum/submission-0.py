class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            target = -nums[i]
            l, r = i + 1, len(nums) - 1

            while l < r:
                current_sum = nums[l] + nums[r]
                if current_sum == target:
                    res.append([nums[i], nums[l], nums[r]])
                    # Skip duplicates for the second and third numbers
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1
                elif current_sum < target:
                    l += 1
                else:
                    r -= 1
        return res


        # def twoPointer(x, y, target):
        #     l = 0
        #     r = len(nums) - 1
        #     while l < r:
        #         if nums[l] + nums[r] == target:
        #             return [l, r]
        #         elif nums[l] + nums[r] > target:
        #             r -= 1
        #         else:
        #             l += 1
        #     return [0, 0]


        # for i in range(len(nums) - 1):
        #     arr = twoPointer(i + 1, len(nums) - 1, -nums[i])
        #     if arr == [0, 0]:
        #         continue
        #     else:
        #         x = arr[0]
        #         y = arr[1]
        #         return [nums[i], x, y]
        
        
        
        # # nums.sort()
        # # # res = []

        # # def twoPointer(x, y, target):
        # #     l = 0
        # #     r = len(nums) - 1
        # #     while l < r:
        # #         if nums[l] + nums[r] == target:
        # #             return [l, r]
        # #         elif nums[l] + nums[r] > target:
        # #             r -= 1
        # #         else:
        # #             l += 1
        # #     return [0, 0]


        # # for i in range(len(nums) - 1):
        # #     arr = twoPointer(i + 1, len(nums) - 1, -nums[i])
        # #     if arr == [0, 0]:
        # #         continue
        # #     else:
        # #         x = arr[0]
        # #         y = arr[1]
        # #         return [nums[i], x, y]

