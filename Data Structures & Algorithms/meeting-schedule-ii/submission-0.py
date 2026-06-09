"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        #Min rooms all meetings to occur without conflict
        #I just need to find the tiemstampt where the most meetings 
        #are occuring
        #I think there's a way to do this with heaps?
        #There are a couple ways to do this i suppose
        rooms = 0
        intervals.sort(key = lambda x:(x.start, x.end))
        current_meetings = []
        heapq.heapify(current_meetings)

        for interval in intervals:
            while current_meetings and current_meetings[0] <= interval.start:
                heapq.heappop(current_meetings)
            heapq.heappush(current_meetings, interval.end)
            rooms = max(rooms, len(current_meetings))
        
        return rooms