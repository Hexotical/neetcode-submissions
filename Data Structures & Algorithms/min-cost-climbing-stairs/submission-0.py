class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        #Either start index 0 or index 1
        #Can step either 1 or 2 floors
        
        for i in range(2, len(cost)):
            #Min cost to reach this square is i-1, i-2
            #So this becomes total cost to walk from here
            cost[i] += min(cost[i-1], cost[i-2])



        return min(cost[-1], cost[-2])


