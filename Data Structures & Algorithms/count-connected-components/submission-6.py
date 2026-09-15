class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        adj_list = defaultdict(list)
        for src, dest in edges:
            adj_list[src].append(dest)
            adj_list[dest].append(src)


        num_components = 0

        visited = set()
        def dfs(node):
            if node in visited:
                return
            visited.add(node)

            for nei in adj_list[node]:
                dfs(nei)


        for i in range(n):
            if i not in visited:
                dfs(i)
                num_components += 1
        return num_components


