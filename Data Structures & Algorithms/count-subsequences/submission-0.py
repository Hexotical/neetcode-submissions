class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        #Distinct subsequences of s equal to t
        #Permutations?
        memo = dict()
        def helper(x, y):
            if (x, y) in memo:
                return memo[(x,y)]
            if x == len(s):
                return 0
            if y == len(t) - 1 and s[x] == t[y] :
                tmp = helper(x+1, y)
                memo[(x,y)] = 1 + tmp
                return memo[(x,y)]
            
            to_ret = 0
            if s[x] == t[y]:
                #Either i increment or don't
                to_ret += helper(x+1, y + 1)
            to_ret += helper(x+1, y)
            memo[(x,y)] = to_ret
            return memo[(x,y)]
        return helper(0,0)

