# class Solution:
#     def search(self, nums: List[int], target: int) -> int:





class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid

            if nums[left] <= nums[mid]:
                if target < nums[left] or target > nums[mid]:
                    left = mid + 1
                # elif target < nums[mid] or target >= nums[left]:
                else:
                    right = mid - 1
            else:
                # nums[left] > nums[mid]

                # 6,0,1,2 2
                if target > nums[mid] and target <= nums[right]:
                    left = mid + 1
                # elif target < nums[mid] or target >= nums[left]:
                else:
                    right = mid - 1
        return -1











        
        # l = 0 
        # r = len(nums) - 1


        # while l <= r:

        #     mid = l + (r - l) // 2

        #     if nums[mid] == target:
        #         return mid

        #     if nums[l] <= nums[mid]:
        #         if target > nums[mid] or target < nums[l]:
        #             l = mid + 1
        #         else:
        #             r = mid - 1


        #     else: # nums[l] > nums[mid]
        #         if target < nums[mid] or target > nums[r]:
        #             r = mid - 1
        #         else:
        #             l = mid + 1

        # return -1



            