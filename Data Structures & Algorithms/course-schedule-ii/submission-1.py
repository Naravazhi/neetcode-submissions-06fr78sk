class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # 0: [] <- list of prereqs
        # 1: [] <- list of prereqs
        # etc.
        preMap = {i : [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        output = []
        visiting = set()
        cycle = set()

        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visiting:
                return True
            
            cycle.add(crs)
            for pre in preMap[crs]:
                if dfs(pre) == False:
                    return False
            
            cycle.remove(crs)
            visiting.add(crs)
            output.append(crs)
            return True

        for c in range(numCourses):
            if dfs(c) == False:
                return []
        return output
