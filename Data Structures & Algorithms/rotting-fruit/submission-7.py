class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # run a multi source bfs
        # find all rotten oranges
        # find all fresh fruit

        fresh_fruit = 0
        rotten = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    rotten.add((i, j))
                if grid[i][j] == 1:
                    fresh_fruit += 1

        q = deque(rotten)

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        time = 0

        while fresh_fruit > 0 and q:

            for _ in range(len(q)):

                x, y = q.popleft()
                for dx, dy in directions:
                    new_x, new_y = x + dx, y + dy
                    if new_x < 0 or new_x >= len(grid) or new_y < 0 or new_y >= len(grid[0]) or grid[new_x][new_y] != 1:
                        continue
                    grid[new_x][new_y] = 2
                    fresh_fruit -= 1
                    q.append((new_x, new_y))
            time += 1

        if fresh_fruit > 0:
            return -1
        return time







