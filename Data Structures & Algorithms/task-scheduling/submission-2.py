class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # min_cycle = float("inf")

        #O(n * m)

        count = Counter(tasks)
        maxHeap = []
        for count in count.values():
            maxHeap.append(-count)
        heapq.heapify(maxHeap)
        time = 0
        q = deque() # [-count, idleTime]

        while maxHeap or q:
            time += 1
            if maxHeap:
                count = heapq.heappop(maxHeap)
                count += 1
                if count:
                    q.append([count, n + time])
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        return time

