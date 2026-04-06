class Solution:
    def isPalindrome(self, s: str) -> bool:
        # stripping spaces
        s = s.strip()
        processed_s = ""
        for i in range(len(s)):
            if s[i].isalnum():
                processed_s += s[i]
        processed_s = processed_s.lower()

        left = 0
        right = len(processed_s) - 1
        while left < right:
            if processed_s[left] != processed_s[right]:
                return False
            left += 1
            right -= 1
        return True

    # def isValidChar(self, s: str) -> bool:
    #     if 


