class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        store = []

        for i in range(len(nums)):
            heapq.heappush(store, -1 * nums[i])

        for i in range(k - 1):
            heapq.heappop(store)
        return -1 * heapq.heappop(store)
        