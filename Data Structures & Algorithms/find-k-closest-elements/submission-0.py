class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        heap = []

        for i in range(len(arr)):
            heapq.heappush(heap, (abs(arr[i] - x), i))
        res = []
        while k > 0:
            index = heapq.heappop(heap)[1]
            res.append(arr[index])
            k -= 1
        res.sort()
        return res
        # but we want to sort by index



# class Solution:
#     def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        