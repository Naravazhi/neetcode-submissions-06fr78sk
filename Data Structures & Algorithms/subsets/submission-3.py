class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # we should have some form of search where we either add or don't
        res = []
        def backtrack(index, subset):
            if index == len(nums):
                res.append(subset.copy())
                return
            
            subset.append(nums[index])
            backtrack(index + 1, subset)
            subset.pop()
            backtrack(index + 1, subset)
            return
            



        backtrack(0, [])
        return res