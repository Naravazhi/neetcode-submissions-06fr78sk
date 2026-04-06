class Solution:
    def numIslands(self, grid: List[List[int]]) -> int:
        numIslands = 0
        def search(r, c):
            if (r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or 
                grid[r][c] == "0"):
                return 

            grid[r][c] = "0"

            search(r + 1, c)
            search(r - 1, c)
            search(r, c + 1)
            search(r, c - 1)
            return


        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    # perform dfs
                    search(i, j)
                    numIslands += 1
        return numIslands





























# class Solution:
#     # def numIslands(self, grid: List[List[str]]) -> int:
#     def numIslands(self, grid: List[List[str]]) -> int:
#         ROWS, COLS = len(grid), len(grid[0])
#         numIslands = 0

#         def dfs(row, col, ):
#             if (row < 0 or col < 0 or row >= ROWS or col >= COLS or grid[row][col] == "0"):
#                 return 

#             grid[row][col] = "0"
#             dfs(row + 1, col) 
#             dfs(row - 1, col) 
#             dfs(row, col + 1) 
#             dfs(row, col - 1)

#         for i in range(ROWS):
#             for j in range(COLS):
#                 if grid[i][j] == "1":
#                     dfs(i, j)
#                     numIslands += 1

#         return numIslands
