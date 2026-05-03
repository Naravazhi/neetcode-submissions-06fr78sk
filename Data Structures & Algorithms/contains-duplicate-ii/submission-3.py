class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k == 0:
            return False
        # left = 0
        # right = k
        seen = set()
        # while right < len(nums):
        #     if nums[left] == nums[right]:
        #         return True
        #     left += 1
        #     right += 1

        for right in range(len(nums)):
            # if right - left > k:
            #     left += 1
            if nums[right] in seen:
                return True
            seen.add(nums[right])
            if len(seen) > k:
                seen.remove(nums[right - k])

        return False
