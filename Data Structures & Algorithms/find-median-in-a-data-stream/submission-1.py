class MedianFinder:
    def __init__(self):
        self.small = [] # maxHeap, stores smallest half
        self.large = [] # minHeap, stores largest half
        # ^v

    def addNum(self, num: int) -> None:
        if self.large and num > self.large[0]:
            heapq.heappush(self.large, num)
        else:
            heapq.heappush(self.small, -1 * num)
        
        if len(self.small) > len(self.large) + 1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)
            

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return self.small[0] * -1
        elif len(self.small) < len(self.large):
            return self.large[0]
        else:
            return (-1 * self.small[0] + self.large[0]) / 2.0
        # if (len(self.small) + len(self.large) % 2) == 0:
        #     return heapq.heappop(self.small) * -1 + heapq.heappop(self.large) // 2
        # else:
        #     return heapq.heappop(self.large)

        # self.data.sort()
        # n = len(self.data)
        # if n % 2 == 1:
        #     return self.data[n // 2]
        # else:
        #     return (self.data[n // 2] + self.data[n // 2 - 1]) / 2


# class MedianFinder:
#     def __init__(self):
#         self.data = []

#     def addNum(self, num: int) -> None:
#         self.data.append(num)
#     def findMedian(self) -> float:
#         self.data.sort()
#         n = len(self.data)
#         if n % 2 == 1:
#             return self.data[n // 2]
#         else:
#             return (self.data[n // 2] + self.data[n // 2 - 1]) / 2
















# class MedianFinder:

#     def __init__(self):
        

#     def addNum(self, num: int) -> None:
        

#     def findMedian(self) -> float:
        
        