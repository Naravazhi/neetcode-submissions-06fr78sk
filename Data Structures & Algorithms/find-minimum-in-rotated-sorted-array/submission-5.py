class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        res = nums[0]

        while l <= r:


            if nums[l] <= nums[r]:
                res = min(res, nums[l])
                break  # we're done, because this whole segment is sorted

            mid = (l + r) // 2
            res = min(res, nums[mid])

            # If mid is on the LEFT sorted portion
            if nums[mid] >= nums[l]:
                # min must be to the RIGHT of mid
                l = mid + 1
            else:
                # mid is in the rotated/smaller portion
                r = mid - 1

        return res

        #     mid = left + (right - left) // 2
        #     # left side is sorted
        #     if nums[left] <= nums[mid]:
        #         if nums[mid] <= nums[right]:
        #             minimum = min(minimum, nums[mid])
        #             right = mid - 1
        #         else:
        #             minimum = min(minimum, nums[mid])
        #             left = mid + 1

        #     # right side is sorted
        #     elif nums[left] > nums[mid]:
        #         if nums[mid] <= nums[right]:
        #             minimum = min(minimum, nums[mid])
        #             right = mid - 1
        #         else:
        #             minimum = min(minimum, nums[mid])
        #             left = mid + 1
        # return minimum






















        # # res = nums[0]
        # # l = 0
        # # r = len(nums) - 1


        # # while l <= r:
        # #     if nums[l] < nums[r]:
        # #         res = min(res, nums[l])

        # #     mid = (l + r) // 2
        # #     res = min(res, nums[mid])
        # #     if nums[mid] >= nums[l]:
        # #         l = mid + 1
        # #     else:
        # #         r = mid - 1
        # # return res
