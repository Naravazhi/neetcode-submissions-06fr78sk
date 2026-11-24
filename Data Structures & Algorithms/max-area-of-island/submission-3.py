class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = float("-inf")
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(row, col):
            if (row < 0 or col < 0 or row >= ROWS or col >= COLS or 
                grid[row][col] == 0
                ):
                return 0
            grid[row][col] = 0
            return (1 + 
                dfs(row + 1, col) + 
                dfs(row - 1, col) + 
                dfs(row, col + 1) + 
                dfs(row, col - 1)
            )

        for i in range(ROWS):
            for j in range(COLS):
                area = dfs(i, j)
                maxArea = max(area, maxArea)

        return maxArea