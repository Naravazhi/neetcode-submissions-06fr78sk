class Solution:
    def findMin(self, nums: List[int]) -> int:
        # 2, 1
        left = 0
        right = len(nums) - 1
        smallest = float("inf")

        while left <= right:
            mid = left + (right - left) // 2
            # left half is sorted
            if nums[left] <= nums[mid]:
                smallest = min(nums[left], smallest)
                left = mid + 1
            # right half is sorted
            elif nums[mid] < nums[right]:
                smallest = min(nums[mid], smallest)
                right = mid - 1
            # 5781234
        return smallest

