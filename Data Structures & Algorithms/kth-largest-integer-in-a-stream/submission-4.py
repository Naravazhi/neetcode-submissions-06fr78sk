class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        # 5, 6, 7, 8, 9, 9, 10, 11, 14 k = 3
        self.k = k
        # self.nums = nums
        self.heap = nums
        # heap is good
        heapq.heapify(self.heap)
        while len(self.heap) > self.k:
            heapq.heappop(self.heap)


    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]






# class KthLargest:

#     def __init__(self, k: int, nums: List[int]):
        

#     def add(self, val: int) -> int:
        
