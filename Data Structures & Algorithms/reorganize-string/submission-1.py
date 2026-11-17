class Solution:
    def reorganizeString(self, s: str) -> str:
        #Rearrange so any two adjacent characters are not the same
        #if one character makes up over half it is impossible
        counter = defaultdict(int)
        for c in s:
            counter[c] += 1
            if (counter[c] > len(s)/2 and len(s) % 2 == 0) or counter[c] > len(s)//2 +1:
                return ""
            
        to_ret = ["" for _ in range(len(s))]
        heap = []
        heapq.heapify(heap)
        for c in counter:
            heapq.heappush(heap, (-counter[c], c))
        to_ret = ["" for _ in range(len(s))]
        index = 0
        
        while heap:
            ch_cnt, ch = heapq.heappop(heap)
            ch_cnt *= -1
            for _ in range(ch_cnt):
                to_ret[index] = ch
                index += 2
                if index >= len(s):
                    index = 1
        #print(to_ret)
        return "".join(to_ret)
            

            

            