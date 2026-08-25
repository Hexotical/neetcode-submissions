class Solution:
    def reverseBits(self, n: int) -> int:
        
        to_ret = 0
        for i in range(32):
            bit = (n >> i) & 1
            to_ret += (bit << (31-i))
        return to_ret