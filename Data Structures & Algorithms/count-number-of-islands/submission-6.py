class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        ROWS, COLS = len(grid), len(grid[0])
        num_islands = 0

        def dfs(row, col):
            if (row < 0 or row >= ROWS or col < 0 or col >= COLS or grid[row][col] == "0" or grid[row][col] == "#"):
                return 

            grid[row][col] = "#"

            dfs(row + 1, col)
            dfs(row, col + 1)
            dfs(row - 1, col)
            dfs(row, col - 1)


        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == "1":
                    dfs(i, j)
                    num_islands += 1
        return num_islands








        # ROWS, COLS = len(grid), len(grid[0])
        # directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        # islands = 0

        # def dfs(r, c):
        #     if (r < 0 or r >= ROWS or c < 0 or c >= COLS or 
        #         grid[r][c] == "0"):
        #         return 

        #     grid[r][c] = "0"
        #     for dr, dc in directions:
        #         dfs(r + dr, c + dc)


        # for i in range(ROWS):
        #     for j in range(COLS):
        #         if grid[i][j] == "1":
        #             dfs(i, j)
        #             islands += 1
        # return islands