class Solution:
    #Bottom up version
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [math.inf] * (amount+1)
        dp[0] = 0
        for a in range(len(dp)):
            for c in coins:
                if c + a <= amount:
                    dp[a+c] = min(dp[a+c], dp[a]+1)
        
        if dp[amount] == math.inf:
            return -1
        return dp[amount]
        