class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        dp = dict()
        print(dp)

        def dfs(s1_ind, s2_ind, s3_ind):
            if s1_ind == len(s1) and s2_ind == len(s2) and s3_ind == len(s3):
                return True
            if (s1_ind, s2_ind) in dp:
                return dp[(s1_ind, s2_ind)]
            to_ret = False
            if s1_ind < len(s1) and s1[s1_ind] == s3[s3_ind]:
                to_ret = dfs(s1_ind + 1, s2_ind, s3_ind + 1)
            if not to_ret:
                if s2_ind < len(s2) and s2[s2_ind] == s3[s3_ind]:
                    to_ret = dfs(s1_ind, s2_ind+1, s3_ind + 1)
            dp[(s1_ind, s2_ind)] = to_ret
            return to_ret
        return dfs(0, 0, 0)

            