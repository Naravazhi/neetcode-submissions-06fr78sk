class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        reversed_nums = [-num for num in nums]
        heapq.heapify(reversed_nums)

        for i in range(k - 1):
            heapq.heappop(reversed_nums)
        return -reversed_nums[0]
