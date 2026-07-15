class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x
        mid = (left + right)//2
        to_ret = mid
        while left <= right:
            mid = (left + right)//2
            #print(mid)
            if mid * mid == x:
                return mid
            elif mid *mid < x:
                left = mid + 1
                to_ret = mid
            else:
                right = mid - 1
        
        return to_ret