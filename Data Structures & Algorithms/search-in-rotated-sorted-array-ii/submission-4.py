class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        



        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                return True
            if nums[left] == nums[mid] == nums[right]:
                left += 1
                right -= 1
            elif nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else: # nums[mid] > nums[right]
                    left = mid + 1
            elif nums[left] > nums[mid]:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else: # nums[mid] < nums[right]
                    right = mid - 1


        return False



            