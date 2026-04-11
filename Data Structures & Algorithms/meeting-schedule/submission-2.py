"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x: x.start)
        # sorting helps with issue of not having a merged interval that grows to compare to

        
        for i in range(1, len(intervals)):
            if intervals[i].start < intervals[i - 1].end:
                return False
            else:
                continue
            
        return True

# class Solution:
#     def canAttendMeetings(self, intervals: List[Interval]) -> bool:
