class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        ROWS, COLS = len(grid), len(grid[0])

        visited = set() # set with treasure cells
        q = deque() # initialize deque with visited
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 0:
                    visited.add((i, j))
                    q.append((i, j))

        # we have to undergo a bfs search
        # i think multi-source works here
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        # q = deque(visited) # initialize deque with visited
        dist = 0

        # logic is that we start from the treasure cells and move level by level
        # whenever a free cell is hit that is updated the "count"
        while q:
            for i in range(len(q)):

                row, col = q.popleft()
                visited.add((row, col))
                for dr, dc in directions:
                    sr, sc = row + dr, col + dc
                    if (0 <= sr < ROWS and 0 <= sc < COLS
                        and grid[sr][sc] == INF
                        #(sr, sc) not in visited
                        ):
                        grid[sr][sc] = dist + 1 # curr dist is dist but neighbors will be dist + 1 so we do this
                        q.append((sr, sc))
            dist += 1 # because we cant have inside or that would mean each cell in one layer ahs different distance which is wrong
            # advancing time






        






# class Solution:
#     def islandsAndTreasure(self, grid: List[List[int]]) -> None:
#         # bfs is good for shortest path in unweighted grid
#         # expand from each inf cell level by level
#         # the first time we reach a treasure cell that is the min distance
#         # needed
#         ROWS = len(grid)
#         COLS = len(grid[0])
#         INF = 2147483647
#         directions = [(-1, 0), (0, 1), (0, -1), (1, 0)]

#         def bfs(sr, sc):
#             queue = deque([(sr, sc)])
#             steps = 0
#             visited = [[False for _ in range(COLS)] for _ in range(ROWS)]
#             visited[sr][sc] = True
            
#             while queue:
#                 for _ in range(len(queue)):
#                     row, col = queue.popleft()
#                     if grid[row][col] == 0:
#                         return steps
#                     for dr, dc in directions:
#                         new_r, new_c = dr + row, dc + col
#                         if (0 <= new_r < ROWS and 0 <= new_c < COLS and
#                             not visited[new_r][new_c] and grid[new_r][new_c] != -1):
#                             visited[new_r][new_c] = True
#                             queue.append((new_r, new_c))
#                 steps += 1
#             return INF




#                 # curr_r, curr_c = queue.popleft()
#                 # # visited[curr_r][curr_c] = True
#                 # steps += 1
#                 # for dr, dc in directions:
#                 #     queue.append((sr + dr, sc + dc))


#         for i in range(ROWS):
#             for j in range(COLS):
#                 if grid[i][j] == INF:
#                     # we run BFS
#                     grid[i][j] = bfs(i, j)




# # class Solution:
# #     def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        