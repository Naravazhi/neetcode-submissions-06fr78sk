class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        neg_nums = [-n for n in nums]
        heapq.heapify(neg_nums)
        while k - 1 > 0:
            heapq.heappop(neg_nums)
            k -= 1
        return -heapq.heappop(neg_nums)

