class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        #Return true when i can split nums into two
        #equal haves
        #So recursively, permutations
        #While running w/ the sum
        total = sum(nums)
        if total % 2 == 1:
            return False
        dp = dict()
        def backtrack(i, run):
            if (i, run) in dp:
                return dp[(i, run)]
            if run == total//2:
                return True
            if i == len(nums):
                return False
            dp[(i, run)] = backtrack(i+1, run) or backtrack(i+1, run + nums[i])
            
            return dp[(i, run)]

        return backtrack(0, 0)