"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
        #can group rooms where x1.end < x2.start OR x1.end == x2.start
        #conflict exists when x1.end > x2.start
        #we want to match smallest end times with smallest start times
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if len(intervals) == 1:
            return 1

        start = sorted(intervals, key=lambda i: i.start)  # sort by start
        end = sorted(intervals, key=lambda i: i.end)    # sort by end

        #(0),(5),(15) start
        #(10),(20),(40) end

        l, r = 0, 0 
        groups = 0
        while l < len(start) and r < len(end):
            if end[r].end > start[l].start:
                groups += 1
                l += 1
            else:
                r+=1
                l+=1
        return groups






       

       
       


        