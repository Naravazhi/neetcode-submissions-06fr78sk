class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left = 0
        right = len(arr) - 1

        while right - left + 1 > k:
            if abs(arr[left] - x) > abs(arr[right] - x):
                left += 1
            else:
                right -= 1
                


        return arr[left:right + 1]
            # because sorted we can just find optimal window of length k

        # heap = []

        # for i in range(len(arr)):
        #     heapq.heappush(heap, (abs(arr[i] - x), arr[i]))
        # res = []
        # while k > 0:
        #     value = heapq.heappop(heap)[1]
        #     res.append(value)
        #     k -= 1
        # res.sort()
        # return res
        # but we want to sort by index



# class Solution:
#     def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        