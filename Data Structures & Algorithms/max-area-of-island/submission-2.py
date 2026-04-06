class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r, c):
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS 
                or grid[r][c] != 1):
                return 0
            
            grid[r][c] = 0
            res = 1 + (dfs(r + 1, c) +
            dfs(r - 1, c) +
            dfs(r, c + 1) +
            dfs(r, c - 1))
            return res

        
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    curArea = dfs(i, j)
                    maxArea = max(maxArea, curArea)

        return maxArea