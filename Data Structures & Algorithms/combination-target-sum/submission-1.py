class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(index, combination, remaining):
            if remaining == 0:
                res.append(combination.copy())
                return
            if index == len(nums):
                return
                
            
            if remaining >= nums[index]:
                combination.append(nums[index])
                backtrack(index, combination, remaining - nums[index])
                combination.pop()
                # backtrack(index + 1, combination, remaining)
            backtrack(index + 1, combination, remaining) # skip
        backtrack(0, [], target)
        return res























# class Solution:
#     def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
#         res = []

#         def backtrack(index, remainingSum, curr_group):
            
#             if remainingSum == 0:
#                 res.append(curr_group.copy())
#                 return
#             if index >= len(nums) or remainingSum < 0:
#                 return 

            

#             curr_group.append(nums[index])
#             backtrack(index, remainingSum - nums[index], curr_group)
#             curr_group.pop()
#             backtrack(index + 1, remainingSum, curr_group)

            
            
#         backtrack(0, target, [])
        
#         return res


























# # class Solution:
# #     def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        

#         # ans = []


#         # def backtrack(position, curr_combos, amount):

#         #     if amount == 0:
#         #         ans.append(curr_combos[:])
#         #         return

#         #     if amount < 0 or position == len(nums):
#         #         return 

#         #     curr_combos.append(nums[position])
#         #     backtrack(position + 1, curr_combos, amount - nums[position])
#         #     curr_combos.pop()
#         #     backtrack(position + 1, curr_combos, amount)

#         # backtrack(0, [], target)
#         # return ans



