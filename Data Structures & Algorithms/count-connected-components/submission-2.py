class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        components = 0

        adj_list = {i : [] for i in range(n)}
        for v1, v2 in edges:
            adj_list[v1].append(v2)
            adj_list[v2].append(v1)

        visited = set()

        def dfs(node):
            visited.add(node)
            for neighbor in adj_list[node]:
                if neighbor not in visited:
                    dfs(neighbor)

        for i in range(n):
            if i not in visited:
                dfs(i)
                components += 1
        return components






# class Solution:
#     def countComponents(self, n: int, edges: List[List[int]]) -> int:
        