class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        #number of possible combos that add to target
        #Repeats are allowed
        #elements of nums are unique
        #Combos are not necessarily distinct
        memo = dict()
        def dfs(runner):
            if target - runner in memo:
                return memo[target-runner]
            if runner > target:
                return 0
            if runner == target:
                return 1
            count = 0
            for i in nums:
                count += dfs(runner + i)
            memo[target-runner] = count
            return memo[target-runner]
        
        return dfs(0)