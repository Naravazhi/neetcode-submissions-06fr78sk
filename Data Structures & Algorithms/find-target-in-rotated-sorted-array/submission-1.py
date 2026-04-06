class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while(l <= r):
            mid = (l + r) // 2

            if (nums[mid] == target):
                return mid
            # elif (nums[mid] < nums[left]):
            #     r = mid
            # else: #nums[mid] > nums[left]
            #     if (nums[mid] > nums[right]):
            #         l = mid + 1
            #     else:
            #         r = mid
            if (nums[l] <= nums[mid]): # left side sorted
                if (nums[l] <= target and target <= nums[mid]):
                    r = mid - 1
                else:
                    l = mid + 1
            else: #right side sorted
                if (nums[mid] <= target and target <= nums[r]):
                    l = mid + 1
                else: 
                    r = mid - 1
        return -1



