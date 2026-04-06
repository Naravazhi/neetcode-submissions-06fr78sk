class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        max_freq = float("-inf")
        majority_element = -1
        count = {}
        for i in range(len(nums)):
            count[nums[i]] = 1 + count.get(nums[i], 0)
        for key, value in count.items():
            if value > max_freq:
                max_freq = value
                majority_element = key

        return majority_element