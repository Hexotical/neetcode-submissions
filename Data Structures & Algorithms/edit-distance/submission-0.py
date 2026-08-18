class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        #Three ops on word1 infinitely
        #Insert a character
        #delete a character
        #replace a character
        #Min operations to make word1 into word2
        memo = dict()
        def helper(i1, i2):
            if (i1, i2) in memo:
                return memo[(i1, i2)]
            if i1 == len(word1) and i2 < len(word2):
                return len(word2) - i2
            elif i2 == len(word2) and i1 < len(word1):
                return len(word1) - i1
            elif i1 == len(word1) and i2 == len(word2):
                return 0
            else:
                if word1[i1] == word2[i2]:
                    return helper(i1 + 1, i2 + 1)
                else:
                    #Insert into word1
                    ins = 1 + helper(i1, i2 + 1)
                    #del
                    dele = 1 +helper(i1 + 1, i2)
                    #mod
                    mod = 1 + helper(i1+1, i2 + 1)
                    memo[(i1, i2)] = min(ins, dele, mod)
                    return memo[(i1, i2)]
        
        return helper(0, 0)
