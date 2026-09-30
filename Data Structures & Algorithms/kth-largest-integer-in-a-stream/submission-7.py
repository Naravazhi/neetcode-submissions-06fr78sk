
class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.heap = nums
        heapq.heapify(self.heap)
        self.k = k
        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        # only keep k elements at a time
        while len(self.heap) > self.k:
            heapq.heappop(self.heap) # we added value then pop it
        return self.heap[0]


