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
        l, r = 0, 1
        while r < len(intervals):
            if intervals[l].end > intervals[r].start:
                return False
            l+=1
            r+=1
        return True
