class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # left = min(nums1[0], nums2[0])
        len1 = len(nums1)
        len2 = len(nums2)

        merged = nums1 + nums2
        merged.sort()

        totalLen = len(merged)
        median = -1
        if totalLen % 2 == 0:
            median = (merged[totalLen // 2 - 1] + merged[totalLen//2]) / 2
        else:
            median = merged[totalLen // 2]
        return median
