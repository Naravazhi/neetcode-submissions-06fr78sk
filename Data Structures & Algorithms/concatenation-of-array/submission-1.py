class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        m = 2 * n
        new_list = [0] * m
        for i in range(n):
            new_list[i] = nums[i]
            new_list[i + n] = nums[i]
        return new_list

