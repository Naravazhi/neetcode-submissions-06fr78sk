class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        queue = []
        # heapify it adfter adding distances (pair with hashmap. key: (x, y), value: distance). rank by distance. for i in rnage(k) pop off from heap
    
        for point in points:
            square_distance = point[0] * point[0] + point[1] * point[1]
            queue.append([square_distance, point])
        
        heapq.heapify(queue)

        ans = []
        for i in range(k):
            dist, point = heapq.heappop(queue)
            ans.append(point)
        return ans

        


