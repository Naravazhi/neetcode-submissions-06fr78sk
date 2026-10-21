# class Solution:
#     def findMin(self, nums: List[int]) -> int:
        

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        curr_min = float("inf")
        ans = 0

        while left <= right:
            mid = left + (right - left) // 2


            # left half sorted
            if nums[left] <= nums[mid]:
                if curr_min > nums[left]:
                    curr_min = nums[left]
                    ans = left
                left = mid + 1
                    
            # right half sorted
            else:
                if curr_min > nums[mid]:
                    curr_min = nums[mid]
                    ans = mid
                right = mid - 1
        return curr_min

