# class Solution:
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0

        for num in num_set:
            if num - 1 in num_set:
                continue
            
            j = num
            curr_length = 1
            while j + 1 in num_set:
                curr_length += 1
                j += 1
            longest = max(longest, curr_length)
        return longest

        # length = 0
        # for i in range(len(nums)):
        #     if nums[i] - 1 in num_set:
        #         continue

        #     curr_length = 1
        #     j = nums[i]
        #     while j + 1 in num_set:
        #         curr_length += 1
        #         j += 1
        #     length = max(length, curr_length)

            
            
        # return length



























#     def longestConsecutive(self, nums: List[int]) -> int:
        # longest = 0


        # num_set = set(nums)
        # for num in nums:
        #     curr_seq = 1
        #     while num + 1 in num_set:
        #         curr_seq += 1
        #         num += 1
        #     longest = max(curr_seq, longest)

        # return longest

