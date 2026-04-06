class Solution:
    def countSubstrings(self, s: str) -> int:
        # memo = {}
        count = 0

        def isPalindrome(word):
            return word == word[::-1]
        
        def dfs(index):
            nonlocal count
            if index == len(s):
                return 
            # if index in memo:
            #     return memo[index]
            

            for end in range(index, len(s)):
                if isPalindrome(s[index: end + 1]):
                    count += 1

            # memo[index] = count
            # return count
            dfs(index + 1)

        dfs(0)
        return count
