class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        # key is number to check if number is in hashmap
        # value is index

        for i in range(len(nums)):
            pair = target - nums[i]
            if pair in hashmap:
                return [hashmap[pair], i]
            hashmap[nums[i]] = i



