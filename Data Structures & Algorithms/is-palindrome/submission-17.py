class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right: # sometimes you can have odd palindrome so leave this
            # lower each character if it is alphanumeric
            # skip if it is a space
            while left < right and not s[left].isalnum():
                left += 1
            while right > left and not s[right].isalnum():
                right -= 1

            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1


        return True # if no issue found return true





























    # def isPalindrome(self, s: str) -> bool:
        # left = 0
        # right = len(s) - 1

        # # while not s[left].isalnum():
        # #     left += 1 

        # # while not s[right].isalnum():
        # #     right -= 1

        # while left < right:
        #     # while s[left]:
        #     #     if not s[left].isalnum():
        #     #        left += 1 

        #     # while s[right]:
        #     #     if not s[right].isalnum():
        #     #         right -= 1
        #     while left < right and not s[left].isalnum():
        #         left += 1 

        #     while left < right and not s[right].isalnum():
        #         right -= 1

        #     if s[left].lower() != s[right].lower():
        #         return False
        #     left += 1
        #     right -= 1

        # return True






        # while 
        
        # left = 0
        # right = len(s) - 1



        # while left <= right:
        #     if 