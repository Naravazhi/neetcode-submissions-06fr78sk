class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # python heaps order by smallest on top to largest on bottom
        if len(stones) == 1:
            return stones[0]
        queue = [-stone for stone in stones]
        heapq.heapify(queue)

        while len(queue) > 1:
            obj1 = heapq.heappop(queue)
            obj2 = heapq.heappop(queue)

            if abs(obj1 - obj2) > 0:
                heapq.heappush(queue, -abs(obj1 - obj2))


        return -queue[0] if queue else 0























        # q = [-stone for stone in stones]
        # heapq.heapify(q)

        # while len(q) >= 2:
        #     # first, second = q[0], q[1]
        #     first, second = -heapq.heappop(q), -heapq.heappop(q)
        #     # if first == second:
        #         # heapq.heappop(q)
        #         # heapq.heappop(q)
        #     if first != second:
        #         # heapq.heappop(q)
        #         # heapq.heappop(q)
        #         heapq.heappush(q, -(first - second))
        # return -q[0] if q else 0

