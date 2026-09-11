class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        to_ret = ""
        def divides(pre, cand):
            if not cand:
                return True
            if not cand.startswith(pre):
                return False
            else:
                return divides(pre, cand[len(pre):])
        #Return largest string such that the string divides both s1 and s2
        for i in range(1, len(str1)+1):
            pref = str1[:i]
            if divides(pref, str1) and divides(pref, str2):
                to_ret = pref


        return to_ret