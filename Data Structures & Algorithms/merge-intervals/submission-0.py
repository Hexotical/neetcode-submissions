class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:(x[0],-x[1]))
        if not intervals:
            return []
        #print(intervals)
        to_ret = []
        curr_interval = intervals[0]
        for i in intervals[1:]:
            if curr_interval[1] >= i[0]:
                curr_interval[1] = max(curr_interval[1], i[1])
            else:
                to_ret.append(curr_interval)
                curr_interval = i
        to_ret.append(curr_interval)

        return to_ret