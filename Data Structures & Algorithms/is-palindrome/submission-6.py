class Solution:
    def isPalindrome(self, s: str) -> bool:

        


        left, right = 0, len(s) - 1

        while left < right:
            if s[left] == " " or not s[left].isalnum():
                left += 1
                continue
            if s[right] == " " or not s[right].isalnum():
                right -= 1
                continue

            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1

        return True































        # left = 0
        # right = len(s) - 1

        # while left < right:
        #     while left < right and not s[left].isalnum():
        #         left += 1
        #     while left < right and not s[right].isalnum():
        #         right -= 1
        #     if s[left].lower() != s[right].lower():
        #         return False
        #     left += 1
        #     right -= 1
        # return True
        
        
        # stripping spaces
        # s = s.strip()
        # processed_s = ""
        # for i in range(len(s)):
        #     if s[i].isalnum():
        #         processed_s += s[i]
        # processed_s = processed_s.lower()

        # left = 0
        # right = len(processed_s) - 1
        # while left < right:
        #     if processed_s[left] != processed_s[right]:
        #         return False
        #     left += 1
        #     right -= 1
        # return True

    # def isValidChar(self, s: str) -> bool:
    #     if 


