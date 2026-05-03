class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        chars = {}
        left = 0
        longest = 0
        max_freq = 0

        for right in range(len(s)):
            # find most frequent char in the window
            chars[s[right]] = 1 + chars.get(s[right], 0)
            max_freq = max(max_freq, chars[s[right]])

            # window_length = right - left + 1
            # while window_length - max_freq > k:
            #     chars[s[left]] -= 1
            #     left += 1
            while right - left + 1 - max_freq > k:
                chars[s[left]] -= 1
                left += 1

            longest = max(longest, right - left + 1)


        return longest




















# class Solution:
#     def characterReplacement(self, s: str, k: int) -> int:
#         left = 0
#         count = {}


#         longest_substring = 0
#         # curr_length = 0
#         max_freq = 0
#         for right in range(len(s)):
#             count[s[right]] = 1 + count.get(s[right], 0)
#             max_freq = max(max_freq, count[s[right]])

#             while (right - left + 1) - max_freq > k:
#                 count[s[left]] -= 1
#                 left += 1

#             longest_substring = max(longest_substring, right - left + 1)
    

#             # if s[right] == s[right - 1]:
#             #     curr_length += 1
#             #     longest_substring = max(longest_substring, curr_length)
#             # else:

#         return longest_substring





























# # class Solution:
# #     def characterReplacement(self, s: str, k: int) -> int:







        
#         # left = 0
#         # max_freq = 0

#         # res = 0
#         # count = [0] * 26

#         # for right in range(len(s)):
#         #     idx = ord(s[right]) - ord('A')
#         #     count[idx] += 1
#         #     max_freq = max(max_freq, count[idx])

#         #     while (right - left + 1) - max_freq > k: 
#         #         left_idx = ord(s[left]) - ord('A')
#         #         count[left_idx] -= 1
#         #         left += 1

#         #         max_freq = max(count)



#         #     res = max(right - left + 1, res)

#         # return res

        
        
        