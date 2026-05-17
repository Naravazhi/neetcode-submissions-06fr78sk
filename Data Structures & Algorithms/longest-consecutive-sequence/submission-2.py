
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        num_set = set(nums)
        for num in nums:
                streak = 0
                curr = num
                while curr in num_set:
                        streak += 1
                        curr += 1
                longest = max(longest, streak)
        
                

        return longest

        








#         longest = 0
#         num_set = set(nums)
#         # 2, 20, 4, 10, 3, 4, 5
#         # 2, 3, 4, 5, 10, 20
#         for num in nums:
#             streak = 0
#             curr = num
#             while curr in num_set:
#                 streak += 1
#                 curr += 1
#             longest = max(longest, streak)



#         return longest
        # # brute force
        # # go through each number one by one
        # # then use another pointer to traverse through rest 
        # # for each additional number in nums
        # res = 0
        # num_set = set(nums)

        # for num in nums:
        #     streak, curr = 0, num
        #     while curr in num_set:
        #         streak += 1
        #         curr += 1
        #     res = max(res, streak)

        # return res

            







        





# class Solution: 
#     def longestConsecutive(self, nums: List[int]) -> int:
        


























# class Solution:
#     def longestConsecutive(self, nums: List[int]) -> int:
        
        