class Solution:
    def partitionLabels(self, s: str) -> List[int]:
   
    
        #Oh i could do this with overlapping intervals as well
        #that might be easier lol
        first_occurs = []
        seen = set()
        for i, c  in enumerate(s):
            if c not in seen:
                first_occurs.append((i, True))
                seen.add(c)
        #How would i get last occurences
        seen = set()
        last_occurs = []
        for i in range(len(s)-1, -1, -1):
            if s[i] not in seen:
                last_occurs.append((i, False))
                seen.add(s[i])
        last_occurs = last_occurs[::-1]
        total_occurs = last_occurs + first_occurs
        total_occurs.sort(key = lambda x:(x[0], not x[1]))
        #print(total_occurs)

        #honestly i just wanna merge and sort 

        
        to_ret = []
        letters = 0
        start = 0
        for i, v in total_occurs:
            if v:
                if letters == 0:
                    start = i
                letters += 1
                
            else:
                letters -= 1
            
            if letters == 0:
                to_ret.append(i-start + 1)


        return to_ret
