class Solution:
    def checkValidString(self, s: str) -> bool:
        memo = dict()
        def dfs(i, o):
            if (i,o) in memo:
                return memo[(i, o)]
            if o < 0:
                return False
            if i == len(s):
                return o == 0
            if s[i] == "(":

                memo[(i, o)] = dfs(i+1, o+1)
            elif s[i] == ")":
                memo[(i, o)] = dfs(i+1, o-1)
            else:
                memo[(i, o)] = dfs(i+1, o) or dfs(i+1, o-1) or dfs(i+1, o+1)
            return memo[(i, o)]
        return dfs(0, 0)