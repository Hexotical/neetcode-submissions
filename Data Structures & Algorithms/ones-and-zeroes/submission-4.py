class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        #Largest subset of str with at most m 0's, n 1's
        #So eitr include or not include strs
        easy = []
        for i in strs:
            ones = i.count("1")
            zeros = i.count("0")
            easy.append((zeros, ones))
        memo = {}
        def backtrack(z, o, i):
            if (i,z,o) in memo:
                return memo[(i, z, o)]
            if i == len(easy):
                return 0
            res = backtrack(z, o, i+1)
            if z + easy[i][0] <= m and o + easy[i][1] <= n:
                test = 1 + backtrack(z+ easy[i][0], o + easy[i][1], i+1)
                res = max(test, res)

            memo[(i, z, o)] = res
            return res
            
            
            
        return backtrack(0, 0, 0)
            
            
