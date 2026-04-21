class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # start from the end
        last = m + n - 1


        while m > 0 and n > 0:
            if nums1[m - 1] > nums2[n - 1]:
                nums1[last] = nums1[m - 1]
                m -= 1
            else:
                nums1[last] = nums2[n - 1]
                n -= 1
            last -= 1
        while n > 0:
            nums1[last] = nums2[n - 1]
            n -= 1
            last -= 1


#         # while nums1[ptr1] == 0:
#         #     ptr1 -= 1
        
#         # and ptr1 > 0
#         while place_ptr >= 0 and ptr2 >= 0:
#             if nums1[ptr1] <= nums2[ptr2]:
#                 nums1[place_ptr] = nums2[ptr2]
#                 ptr2 -= 1
#             else:
#                 nums1[place_ptr] = nums1[ptr1]
#                 ptr1 -= 1

#             place_ptr -= 1
#         # while ptr1 > 0:
#         #     nums1[place_ptr] = nums1[ptr1]
#         #     ptr1 -= 1
#         while ptr2 >= 0:
#             nums2[place_ptr] = nums2[ptr2]
#             ptr2 -= 1

        

        




























# # class Solution:
# #     def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
# #         """
#         Do not return anything, modify nums1 in-place instead.
#         """
        