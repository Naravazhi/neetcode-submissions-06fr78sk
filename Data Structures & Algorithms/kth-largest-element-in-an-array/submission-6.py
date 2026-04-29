class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        # heapq.heapify(nums)
        # 2, 3, 1, 5, 4 would be 1, 2, 3, 4, 5
        # with k = 2 we need to pop until len(heap) == k
        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)
        # while len(heap) > k:
        #     heapq.heappop(heap)
        return heap[0]
        