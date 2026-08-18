class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        q = [-stone for stone in stones]
        heapq.heapify(q)

        while len(q) >= 2:
            # first, second = q[0], q[1]
            first, second = -heapq.heappop(q), -heapq.heappop(q)
            # if first == second:
                # heapq.heappop(q)
                # heapq.heappop(q)
            if first != second:
                # heapq.heappop(q)
                # heapq.heappop(q)
                heapq.heappush(q, -(first - second))
        return -q[0] if q else 0

