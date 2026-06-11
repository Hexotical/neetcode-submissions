class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        last_occurs = defaultdict(int)
        for i, c in enumerate(s):
            last_occurs[c] = i
        to_ret = []
        size = end = 0
        for i, c in enumerate(s):
            size += 1
            end = max(end, last_occurs[c])
            if i==end:
                to_ret.append(size)
                size = 0
        return to_ret
        
