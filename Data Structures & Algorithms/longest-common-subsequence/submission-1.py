class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = {}
        def helper(i1, i2):
            if (i1, i2) in memo:
                return memo[(i1, i2)]
            if i1 == len(text1) or i2 == len(text2):
                return 0
            to_ret = 0
            for s1 in range(i1, len(text1)):
                for s2 in range(i2, len(text2)):
                    if text1[s1] == text2[s2]:
                        to_ret = max(to_ret,  1+helper(s1+ 1, s2 + 1))
                        break
            memo[(i1, i2)] = to_ret
            return to_ret
        return helper(0, 0)
