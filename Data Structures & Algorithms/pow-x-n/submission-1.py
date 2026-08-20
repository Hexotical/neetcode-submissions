class Solution:
    def myPow(self, x: float, n: int) -> float:
        #X raised to power n, no in built library functions
        
        #So the naive way is just multiply x by itself n times
        #I dont understand why recursion would be more efficient
        if n == 0:
            return 1
        elif n == 1:
            return x
        elif n < 0:
            return 1/self.myPow(x, -1 * n)
        else:
            if n % 2 == 1:
                return x * self.myPow(x*x, (n-1)//2)
            else:
                return self.myPow(x*x, n//2)
                #2 4 8 16 32 64 128 256 512 1024 2^10
                #4 16 64 256 1024 4^5
            