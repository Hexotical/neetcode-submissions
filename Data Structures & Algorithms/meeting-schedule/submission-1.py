"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x:(x.start, x.end))
        if not intervals:
            return True
        start_occupation = intervals[0].start
        end_occupation = intervals[0].end
        possible = True
        for i in range(1, len(intervals)):
            if intervals[i].start < end_occupation:
                return False
            end_occupation = intervals[i].end
        
        return possible
