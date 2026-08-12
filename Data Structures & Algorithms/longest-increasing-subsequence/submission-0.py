class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        #So yea dynamic programming
        dp = [1] * len(nums)
        
        #longest increasing subsequence ending at this elem?
        for ind in range(len(nums)):
            for i in range(0, ind):
                if nums[ind] > nums[i]:
                    dp[ind] = max(dp[ind], 1 + dp[i])
            
        
        print(dp)
        
        return max(dp)