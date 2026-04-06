class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}

        def dfs(index):
            if index in memo:
                return memo[index]
            if index == len(s):
                return 1
            if s[index] == "0":
                return 0
            
            ways = dfs(index + 1)
            if index + 1 < len(s) and 10 <= int(s[index:index + 2]) <= 26:
                ways += dfs(index + 2)
            memo[index] = ways
            return ways


        return dfs(0)
            


        memo = {}
        # num_decodings = 0
        # char_map = {}
        # for i in range(26):
        #     char = chr(ord("A") + i)
        #     char_map[char] = i + 1
        

        def dfs(index):
            if index in memo:
                return memo[index]
            if index == len(s):
                return 1 # reached a valid decoding
            if s[index] == "0":
                return 0 # not a valid decode
            
            # split with 1 
            ways = dfs(index + 1)
            # split by 2 if it's a valid number between 10 and 26

            if index + 1 < len(s) and 10 <= int(s[index: index + 2]) <= 26:
                ways += dfs(index + 2) # skip 2 spots and continue from there


            # for i in range(index, len(s)):
            #     dfs(i)
            memo[index] = ways # store in memo
            return ways

        return dfs(0)
        # return num_decodings

        
        