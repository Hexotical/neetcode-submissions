class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        #Of size group size, increasing by one
        #I feel like i'd want a min heap to just keep track
        #of the running minimum
        #I could sort lol
        #ig both?
        #Min heap to figure out the element to start from
        #Counter thing to figure out if i can do group size
        if len(hand) % groupSize != 0:
            return False
        req_dict = dict()
        for c in hand:
            if c not in req_dict:
                req_dict[c] = 1
            else:
                req_dict[c] += 1
        
        hand = set(hand)
        hand = list(hand)
        #print("HEUaoifh")
        min_heap = hand
        heapq.heapify(min_heap)
        #print(min_heap, hand)
        possible = True
        
        while min_heap and possible:
            
            while min_heap and req_dict[min_heap[0]] <= 0:
                #print
                heapq.heappop(min_heap)
                continue
            if min_heap:
                top = min_heap[0]
                #print(top, req_dict)
                for i in range(0, groupSize):
                    if top+i not in req_dict or req_dict[top + i] <= 0:
                        possible = False
                        break
                    req_dict[top + i] -= 1
                #print(req_dict)

        return possible