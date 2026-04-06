class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])

        def dfs(r, c, i):
            if i == len(word):
                return True
            
            # check conditions for returning False
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS
                or board[r][c] != word[i] or board[r][c] == "#"):
                return False
            board[r][c] = "#"
            res = (
                dfs(r + 1, c, i + 1) or
                dfs(r - 1, c, i + 1) or
                dfs(r, c + 1, i + 1) or 
                dfs(r, c - 1, i + 1)
            )
            board[r][c] = word[i]
            return res

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        return False



        
        
        # ROWS, COLS = len(board), len(board[0])
        # path = set() # hashset implementation
        # def dfs(row, col, i):
        #     if i == len(word):
        #         return True
        #     if (min(row, col) < 0 or 
        #         row >= ROWS or col >= COLS or 
        #         word[i] != board[row][col] or 
        #         (row, col) in path):
        #         return False
        #     path.add((row, col))
        #     res = (
        #         dfs(row + 1, col, i + 1) or
        #         dfs(row - 1, col, i + 1) or
        #         dfs(row, col + 1, i + 1) or
        #         dfs(row, col - 1, i + 1) 
        #     )
        #     path.remove((row, col))
        #     return res
            
        # for i in range(ROWS):
        #     for j in range(COLS):
        #         if dfs(i, j, 0):
        #             return True
        # return False
