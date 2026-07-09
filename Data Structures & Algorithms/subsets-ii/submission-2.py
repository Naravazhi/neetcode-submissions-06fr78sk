class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        

        res = []
        nums.sort()


        def backtrack(index, sub):
            if index == len(nums):
                res.append(sub[:])
                return

            
            sub.append(nums[index])
            backtrack(index + 1, sub)
            sub.pop()

            while index + 1 < len(nums) and nums[index] == nums[index + 1]:
                index += 1

            backtrack(index + 1, sub)


        backtrack(0, [])
        return res


