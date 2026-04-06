class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        i = 0
        n = len(intervals)

        while i < n and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1

        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        result.append(newInterval)
        
        while i < n: # and intervals[i][0] > newInterval[i]:
            result.append(intervals[i])
            i += 1
        return result




        # for i in range(len(intervals) - 1):



        #     if newInterval[0] > intervals[i][1]:
        #         if newInterval[1] < intervals[i + 1][0]:
        #             # perfectly nested, no merging
        #     elif newInterval[0] < intervals[i][1]:
        #         if newInterval[0] > intervals[i + 1][0]:


            

        