class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        #s contains only letters a,b,c
        #no aaa, bbb, ccc as a substring
        #a occurences of a, b occurences of b, c occurences of c
        #Return longest possible happy string
        #I mean I just want to have a heap
        #Tho it's also at most? is there ever a way to make an unhappy string?
        #Like i don't think it's 
        heap = []
        heapq.heapify(heap)
        if a != 0:
            heapq.heappush(heap, (-a, "a"))
        if b != 0:
            heapq.heappush(heap, (-b, "b"))
        if c != 0:
            heapq.heappush(heap, (-c, "c"))
        to_ret = ""
        while heap:
            
            total, c = heapq.heappop(heap)
            to_ret += c * min(2, -1 * total)
            total += min(2, -1 * total)
            if total == 0:
                continue
            #Must desal with the case where we're still dealing with largest elem
            if not heap:
                return to_ret
            if total <= heap[0][0]:
                filler_total, filler = heapq.heappop(heap)
                to_ret += filler
                if -1 * filler_total > 1:
                    heapq.heappush(heap, (filler_total + 1, filler))
            heapq.heappush(heap, (total, c))
        return to_ret