class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap  = []
        heapq.heapify(heap)
        for p in points:
            dist = math.sqrt((p[0])**2 + (p[1])**2)
            heapq.heappush(heap, (dist, p[0], p[1]))
        to_ret = []
        for _ in range(k):
            to_add = heapq.heappop(heap)
            to_ret.append([to_add[1], to_add[2]])
        return to_ret