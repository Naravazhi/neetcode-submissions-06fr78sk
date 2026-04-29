class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        heapq.heapify(points)
        # calculate distance
        for point in points:
            distance = point[0] ** 2 + point[1] ** 2
            heapq.heappush(heap, (distance, [point[0], point[1]]))


        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])

        return res
