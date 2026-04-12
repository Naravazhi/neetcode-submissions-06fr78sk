class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list = {i: [] for i in range(numCourses)}
        indegree = [0] * numCourses

        for course, prereq in prerequisites:
            adj_list[prereq].append(course)
            indegree[course] += 1


        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        res = []
        while q:
            # for i in range(len(q)):
            c = q.popleft()
            res.append(c)
            for nei in adj_list[c]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        return res if len(res) == numCourses else []

                



        # res = []
        # def bfs(crs):
        #     q = deque([crs])
        #     for i in range(len(q)):
        #         new_crs = q.popleft()
        #         for adj_crs in adj_list[crs]:
        #             q.append(adj_crs)
        #         res.append(crs)    


        # for crs, prereqs in adj_list.items():
        #     if not prereqs:
        #         bfs(crs)
        # return res

        # # adj_list = {i: [] for i in range(numCourses)}

        # # for pre, dest in prerequisites:
        # #     adj_list[pre].append(dest)

        # # res = []
        # # def bfs(crs):
        # #     q = deque([crs])
        # #     for i in range(len(q)):
        # #         new_crs = q.popleft()
        # #         for adj_crs in adj_list[crs]:
        # #             q.append(adj_crs)
        # #         res.append(crs)    


        # # for crs, prereqs in adj_list.items():
        # #     if not prereqs:
        # #         bfs(crs)
        # # return res


