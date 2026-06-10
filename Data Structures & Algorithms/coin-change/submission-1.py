class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #Fewest number of coins to make exact target amount
        #I suppose i just count up
        #t space
        if amount == 0:
            return 0
        memo = {}
        def dfs(amount):
            if amount == 0:
                return 0
            if amount in memo:
                return memo[amount]
            to_ret = math.inf
            for coin in coins:
                if amount - coin >= 0:
                    to_ret = min(to_ret, 1 + dfs(amount-coin))
            memo[amount] = to_ret
            return to_ret
        
        to_ret = dfs(amount)
        if to_ret != math.inf:
            return to_ret
        else:
            return -1
