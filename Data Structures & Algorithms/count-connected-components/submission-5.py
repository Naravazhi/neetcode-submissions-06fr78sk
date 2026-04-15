class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # we are going to run dfs 
        components = 0

        adj_list = {i:[] for i in range(n)}
        for src, dest in edges:
            adj_list[src].append(dest)
            adj_list[dest].append(src)

        # undirected graph
        visited = set()
        # we want a parent to make sure that we don't detect cycle cause of undirected graph

        def dfs(node):
            if node in visited:
                # cant decide return type yet
                # return False
                return
            
            visited.add(node)
            for neighbor in adj_list[node]:
                # if neighbor == parent:
                #     continue
                # if not dfs(neighbor, node):
                #     return False
                dfs(neighbor)
            return True

        for i in range(n):
            if i not in visited:
                components += 1
                dfs(i)
            # if i not in visited and dfs(i, -1):
            #     components += 1
        return components



        



             




        return components


























# class Solution:
#     def countComponents(self, n: int, edges: List[List[int]]) -> int:
#         components = 0

#         adj_list = {i : [] for i in range(n)}
#         for v1, v2 in edges:
#             adj_list[v1].append(v2)
#             adj_list[v2].append(v1)

#         visited = set()

#         def dfs(node):
#             visited.add(node)
#             for neighbor in adj_list[node]:
#                 if neighbor not in visited:
#                     dfs(neighbor)

#         for i in range(n):
#             if i not in visited:
#                 dfs(i)
#                 components += 1
#         return components






# class Solution:
#     def countComponents(self, n: int, edges: List[List[int]]) -> int:
        