class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        #Is there a smarter way to do it than 
        #Just running a simulation starting at each 
        #station
        #I think the answer
        #Find either largest increasing sequence
        #Max starting gas and then try from there
        if sum(gas) < sum(cost):
            return -1

        
        starting_index = 0
        running_total = 0
        for i in range(len(gas)):
            running_total += gas[i] - cost[i]
            if running_total < 0:
                starting_index = i + 1
                running_total = 0
        return starting_index % len(gas)
            
            
            #actually isn't this just total gas must be 
            #greater than equal to cost

            

                
