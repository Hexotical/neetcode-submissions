class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        #maximum number of non rotated envelopes within one another
        #Is this not just sorting?
        #Weird sorting
        #annoying sorting
        #So the brute force way
        #pick envelope
        #try and fit to the next
        #Backtrack?
        #Is there a smart way to do this
        #there's a shit ton of envelopes
        #So i suppose envelopes of min dimension
        #See what fit in them
        #dfs it up?
        envelopes.sort(key=lambda x:(x[0], x[1]))
        print(envelopes)
        smaller = [0]*len(envelopes)
        for i in range(len(envelopes)):
            for j in range(i-1, -1, -1):
                if envelopes[i][0] > envelopes[j][0] and envelopes[i][1] > envelopes[j][1]:
                    smaller[i] = max(smaller[i], 1 + smaller[j])
        
        return max(smaller) + 1
