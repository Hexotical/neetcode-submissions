class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        #Try to go bottom up
        easy = []
        for i in strs:
            ones = i.count("1")
            zeros = i.count("0")
            easy.append((zeros, ones))
        to_ret = 0
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        #Max strings using at least zeros and ones
        for z, o in easy:
            for i in range(m, z - 1, -1):
                for j in range(n, o -1, -1):
                    dp[i][j] = max(dp[i][j], 1 + dp[i-z][j-o])
        return dp[m][n]