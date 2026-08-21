class Solution:
    def isHappy(self, n: int) -> bool:
        #Cycle not including 1
        
        visited = set()
        while n != 1:
            if n in visited:
                return False
            visited.add(n)
            ones = n % 10
            tens = max(0, (n % 100 - ones) / 10)
            hundreds = max(0, (n % 1000 - tens * 10 - ones) / 100)
            thousands = n // 1000
            n = ones ** 2 + tens ** 2 + hundreds ** 2 + thousands ** 2
            #print(n)
        return True