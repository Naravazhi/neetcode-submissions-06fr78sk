class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set() # need visit set to avoid repetition
        q = deque() # q to do bfs with
        # bfs with each gate

        def addRoom(r, c):
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS
                or (r, c) in visit or grid[r][c] == -1):
                return
            visit.add((r, c))
            q.append([r, c])

        # find gates
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 0:
                    visit.add((i, j))
                    q.append([i, j])
        
        dist = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist
                addRoom(r + 1, c)
                addRoom(r - 1, c)
                addRoom(r, c + 1)
                addRoom(r, c - 1)
            dist += 1

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # ROWS, COLS = len(grid), len(grid[0])

        # # we are doing bfs, so we need a queue
        # # we also need a visited set so that we don't 
        # # visit the same cell twice
        # visit = set()
        # queue = deque()

        # def addRoom(r, c):
        #     if (r < 0 or c < 0 or r >= ROWS or c >= COLS
        #         or (r, c) in visit or grid[r][c] == -1):
        #         return
        #     queue.append([r, c])
        #     visit.add((r, c))

        # # find all the gates so we can do bfs from there
        # for i in range(ROWS):
        #     for j in range(COLS):
        #         if grid[i][j] == 0:
        #             # add to visit and queue
        #             queue.append([i, j])
        #             visit.add((i, j))

        # # while q is not empty
        # dist = 0
        # while queue:
        #     # iterate through queue
        #     for i in range(len(queue)):
        #         r, c = queue.popleft() # while popping get r and q
        #         grid[r][c] = dist
        #         addRoom(r + 1, c)
        #         addRoom(r - 1, c)
        #         addRoom(r, c + 1)
        #         addRoom(r, c - 1)
        #     dist += 1







                    
        