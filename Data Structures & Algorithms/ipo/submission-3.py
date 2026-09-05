class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        #k projects before ipo projects must be distinct
        #Max total capital after finishing k projects
        #n projects where project i has profits[i]
        #capital[i] req to start initially
        #You have w capital
        #when finish proj obtain pure profit
        #Not required to spent capital
        if k >= len(profits):
            return sum(profits) + w
        prof_heap = []
        for i, v in enumerate(profits):
            prof_heap.append((-v, i))
        heapq.heapify(prof_heap)
        #print(prof_heap)
        to_ret = w
        while k > 0:
            skipped = []
            #print(prof_heap[0][1])
            #print(capital[prof_heap[0][1]])
            while prof_heap and to_ret < capital[prof_heap[0][1]]:
                skipped.append(heapq.heappop(prof_heap))
            if not prof_heap:
                return to_ret
            prof, index = heapq.heappop(prof_heap)
            to_ret += -1 * prof
            while skipped:
                heapq.heappush(prof_heap, skipped[-1])
                skipped.pop()
            k -= 1

        return to_ret
