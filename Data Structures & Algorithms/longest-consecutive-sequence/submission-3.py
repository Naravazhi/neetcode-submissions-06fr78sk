class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0


        num_set = set(nums)
        for num in nums:
            curr_seq = 1
            while num + 1 in num_set:
                curr_seq += 1
                num += 1
            longest = max(curr_seq, longest)

        return longest