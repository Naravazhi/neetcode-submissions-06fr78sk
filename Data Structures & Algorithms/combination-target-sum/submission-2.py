class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(index, cur_sum, combo):
            if index >= len(nums):
                return
            if cur_sum == target:
                res.append(combo.copy())
                return
            if cur_sum > target:
                return

            combo.append(nums[index])
            backtrack(index, cur_sum + nums[index], combo)
            combo.pop()
            backtrack(index + 1, cur_sum, combo)
            return
        backtrack(0, 0, [])
        return res