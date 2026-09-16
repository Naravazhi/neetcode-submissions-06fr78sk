class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        
        adj_list = defaultdict(list)
        for src, dest in edges:
            adj_list[src].append(dest)
            adj_list[dest].append(src)

        

        # make sure no cycle in tree
        # dont know uet if i need to run dfs on eevery node or just one


        # fully connected to one component
        # n - 1 edges
        # i guess have one run and see if we hit n nodes? (also helps with one conencted component problem)
        visited = set()
        def dfs(node, parent):
            if node in visited:
                return False

            visited.add(node)

            for nei in adj_list[node]:
                # need to keep track of parent
                if nei == parent:
                    continue
                if not dfs(nei, node):
                    return False
            return True


        if not dfs(0, -1):
            return False
        return len(visited) == n


