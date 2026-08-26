class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        neg = False
        if x < 0:
            neg = True
            x = -1 * x
        while x:
            digit = x % 10
            x = x // 10
            if (res * 10 + digit) > (2 ** 31 -1) or (res * 10 + digit) < -(2**31):
                return 0
            res = res * 10 + digit
        if neg:
            res *= -1
        return res