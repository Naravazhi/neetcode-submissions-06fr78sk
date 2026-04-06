class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # sliding window technique
        n = len(s)
        if n == 0:
            return 0

        #seen = set()
        longest = 0
        left = 0
        #right = 1
        # idea is that we traverse through the string one char at a time
        # this is kept track of by left

        while left < n:
            seen = set()
            #count = 1
            seen.add(s[left])
            right = left + 1

            while right < n and s[right] not in seen:
                # if s[right] in seen:
                #     break
                seen.add(s[right])
                right += 1
                # else:
                #     seen.add(s[right])
                #     right += 1
                #     #count += 1

            longest = max(longest, right - left)
            #seen.remove(s[left])
            left += 1
        return longest


