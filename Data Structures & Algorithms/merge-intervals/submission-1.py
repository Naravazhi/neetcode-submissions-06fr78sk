class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # so we often just compare two intervals at a time
        # [] []
        # interval1[0], interval1[1].   interval2[0], interval2[1]
        # options:
        # 1)
        # you have interval2 nested in interval1 where 
        # interval1[0] < interval2[0] < interval2[1] < interval1[1]
        # 2)
        # you have interval1 nested so just do opposite
        # 3)
        # if interval1[1] > interval2[0] then we are left with 
        # [interval1[0], interval2[1]]
        # if interval1[1] < interval2[0] then no overlap
        # 

        # no we have to think of approach to compare
        # i was thinking of a queue where you pop two intervals then readd
        # when you are done merging just in case you need that interval in the future

        intervals.sort(key=lambda x: x[0]) # because we want to compare next in queue with merged interval
        merged = []

        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                if interval[1] < merged[-1][1]:
                    continue
                elif interval[0] <= merged[-1][1]:
                    merged[-1][1] = interval[1]
        return merged

                


        # q = deque(intervals)

        # while q:
        #     interval1 = q.popleft()
        #     interval2 = q.popleft()
        #     new_interval = []
        #     if interval[1] > interval2[0]:
        #         if interval[1] > interval2[1]:
        #             new_interval = [interval1[0], interval1[1]]
        #         else:
        #             new_interval = [interval1[0], interval2[1]]
        #         q.append(interval1)
        #     else:
        #         # no merging
        #         q.append(interval1)
        #         q.append(interval2)
        # The key insight

# You only need to compare the current interval with the last merged interval.

        




# class Solution:
#     def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        