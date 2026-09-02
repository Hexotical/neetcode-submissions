class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        #Least weight capcity of the ship results all packages
        #shipped within days
        #How would i do this
        #Binary search?
        l = max(weights)
        r = sum(weights)
        minWeight = r
        while l <= r:
            mid = (l + (r-l)//2)
            day = 1
            runningTotal = 0
            for w in weights:
                runningTotal += w
                if runningTotal > mid:
                    day += 1
                    runningTotal = w
            if day <= days:
                minWeight = mid
                r = mid - 1
            else:
                l = mid + 1

        
        return minWeight
            
