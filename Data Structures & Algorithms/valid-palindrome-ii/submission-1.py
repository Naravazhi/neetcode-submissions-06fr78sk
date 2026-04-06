class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPalindrome(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                
                left += 1
                right -= 1
            return True

        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return(isPalindrome(l + 1, r) or isPalindrome(l, r - 1))
            l += 1
            r -= 1
        return True
        
        # left = 0
        # right = len(s) - 1

        # used = False
        # while left < right:
        #     if s[left] == s[right]:
        #         left += 1
        #         right -= 1
        #     else:
        #         if not used:
        #             if left + 1 < right and s[left + 1] == s[right]:
        #                 left += 1
        #             elif left < right - 1 and s[left] == s[right - 1]:
        #                 right -= 1
        #             used = True
        #         else:
        #             return False
        # return True
    
    # def isPalindrome(left, right):
    #     while left < right:
    #         if s[left] != s[right]:
    #             return False
    #         else:
    #             left += 1
    #             right -= 1
    #     return True