class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        #Jesus wtf was i doing
        #Anyway the idea is union find
        #Min number of intervals to remove to make the rest
        #non overlapping
        intervals.sort(key = lambda x : (x[1]))
        print(intervals)
        #Not bounded
        to_ret = 0
        prev = intervals[0]
        for i in range(1, len(intervals)): 
            #I should do this in reverse?
            #Parent tree all the way up?
            if prev[1] > intervals[i][0]:
                to_ret += 1
                if prev[1] >= intervals[i][1]:
                    prev = intervals[i]
            else:
                prev = intervals[i]
        
        return to_ret

