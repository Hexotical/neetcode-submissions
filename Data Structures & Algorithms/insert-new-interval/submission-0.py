class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        #Find all overlapping intervals
        #merge
        intervals.sort(key=lambda x:(x[0], -x[1]))
        to_ret = []
        inserted = False
        for i in intervals:
            beg, end = i[0], i[1]
            if newInterval[1] < beg:
                if not inserted:
                    inserted = True
                    to_ret.append(newInterval)
                to_ret.append(i)
            elif newInterval[0] > end:
                to_ret.append(i)
            else:
                newInterval[0] = min(newInterval[0], beg)
                newInterval[1] = max(newInterval[1], end)
        if not inserted:
            inserted = True
            to_ret.append(newInterval)
        return to_ret
            
        