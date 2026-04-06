class Solution:
    def findMin(self, nums: List[int]) -> int:
        # l = 0
        # r = len(nums) - 1
        # while l < r:
        #     mid = l + (r - 1) // 2
        #     if nums[mid] < nums[r]:
        #         r = mid
        #     else:
        #         l = mid + 1
        # return nums[l]

        if not nums: 
            return 
        if len(nums) == 1:
            return nums[0]
        l = 0
        r = len(nums) - 1
        minimum = float("inf")
        

        while l <= r:
            mid = (l + r)// 2
            if nums[l] <= nums[mid]:
                minimum = min(nums[l], minimum)
                l = mid + 1
            else:
            # elif nums[l] > nums[mid]:
                minimum = min(nums[mid], minimum)
                r = mid - 1
        return minimum

