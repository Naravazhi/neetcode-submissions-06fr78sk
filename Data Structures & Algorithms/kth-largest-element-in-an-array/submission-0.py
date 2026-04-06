class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = []
        for num in nums:
            heapq.heappush(min_heap, num)
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        return min_heap[0]


        # n = nums[:k]
        # heapq.heapify(n)
        # # heapq.heapify(nums)

        # for num in nums[k:]:
        #     if num > n[0]:
        #         heapq.heappushpop(n, num)
        # return n[0]

        # for i in range (0, k):
        #     if i == k:
        #         return heapq.heappop(nums)
        #     heapq.heappop(nums)
            