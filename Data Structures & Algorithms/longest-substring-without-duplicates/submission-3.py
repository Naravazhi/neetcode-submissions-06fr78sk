class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        longest = 0
        left = 0
        chars = {}
        
        for right in range(n):
            chars[s[right]] = 1 + chars.get(s[right], 0)
            while chars[s[right]] > 1:
                chars[s[left]] -= 1
                left += 1
            longest = max(longest, right - left + 1)
        return longest



        





# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:



#         n = len(s)
#         # chars = [0] * 26
#         chars = {}
#         left = 0
#         longest = 0

#         for right in range(n):
#             chars[s[right]] = 1 + chars.get(s[right], 0)
#             while chars[s[right]] > 1:
#                 chars[s[left]] -= 1
#                 left += 1
#             longest = max(longest, right - left + 1)

#             # # if chars[s[right]] > 0:
#             #     chars = [0] * 26
#             #     chars[ord(s[left]) - ord('a')] -= 1
#             #     left += 1
#             # else:
#             #     chars[ord(s[right]) - ord('a')] += 1
#             #     longest = max(longest, right - left + 1)
            
#         return longest




#         # need




# # class Solution:
# #     def lengthOfLongestSubstring(self, s: str) -> int:





#         # n = len(s)

        
#         # n = len(s)
#         # seen = set()
#         # longest = 0
#         # left = 0
#         # right = 0
        
#         # while left < n:
#         #     while right < n and s[right] not in seen:
#         #         seen.add(s[right])
#         #         right += 1
#         #         longest = max(longest, right - left)
#         #     if right == n:
#         #         break

#         #     seen.remove(s[left])
#         #     left += 1
#         # return longest




#         # # sliding window technique
#         # n = len(s)
#         # if n == 0:
#         #     return 0

#         # #seen = set()
#         # longest = 0
#         # left = 0
#         # #right = 1
#         # # idea is that we traverse through the string one char at a time
#         # # this is kept track of by left

#         # while left < n:
#         #     seen = set()
#         #     #count = 1
#         #     seen.add(s[left])
#         #     right = left + 1

#         #     while right < n and s[right] not in seen:
#         #         # if s[right] in seen:
#         #         #     break
#         #         seen.add(s[right])
#         #         right += 1
#         #         # else:
#         #         #     seen.add(s[right])
#         #         #     right += 1
#         #         #     #count += 1

#         #     longest = max(longest, right - left)
#         #     #seen.remove(s[left])
#         #     left += 1
#         # return longest


