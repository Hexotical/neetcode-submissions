class Solution:
    def jump(self, nums: List[int]) -> int:
        #
        #Start at 0
        #Min jumps to reach the last index
        
        #Wait if i start from 0, count which indices are reachable
        #Then keep going until 0 is reachable

        reachable = nums[0]
        reached = 0
        jumps = 0
        
        while reached < len(nums) - 1:
            jumps += 1
            starter = reached
            reached = reachable
            
            if reached < len(nums) - 1:
                #Then calculate out future jump
                future = 0
                for i in range(starter +1, reached + 1):
                    #calculate possible next steps
                    future = max(future, i + nums[i])
                #Future now has max possible jump index from 
                #The next jump
                reachable = future
            

        
        return jumps