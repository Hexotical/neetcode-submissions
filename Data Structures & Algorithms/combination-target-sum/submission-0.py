class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        #Unique combinations of nums where chosen number == target

        to_ret = []

       
        

        def dfs(i, attempt, sum_attempt):
            
          
            if sum_attempt == target:
                to_ret.append(attempt.copy())
                return
            if i >= len(nums) or sum_attempt > target:
                return
            attempt.append(nums[i])
            dfs(i, attempt, sum_attempt + nums[i])
            attempt.pop()
            dfs(i + 1, attempt, sum_attempt)
        dfs(0, [], 0)
        return to_ret