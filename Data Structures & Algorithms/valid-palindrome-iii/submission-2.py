class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        #Remove at most k characters from it
        #abcdefjedcba
        if k >= len(s) - 1:
            return True
        if len(s) == 1 or not s:
            return True
        if k < 0 or (k == 0 and s[0] != s[-1]):
            return False
        memo = dict()
        def dfs(test, rem):
            if rem >= len(test) - 1:
                return True
            if not test:
                return True
            if rem < 0:
                return False
            if (test, rem) in memo:
                return memo[(test, rem)]
            if test[0] == test[-1]:
                memo[(test, rem)] = dfs(test[1:-1], rem)
            else:
                memo[(test, rem)] = dfs(test[1:], rem-1) | dfs(test[:-1], rem-1)
            return memo[(test, rem)]

        return dfs(s, k)
