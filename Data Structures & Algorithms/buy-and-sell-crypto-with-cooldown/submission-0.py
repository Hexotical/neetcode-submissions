class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #Cannot buy on consecutive days, can only own one coin
        #Return max profit
        memo = dict()
        def helper(i, held):
            if (i, held) in memo:
                return memo[(i, held)]

            #then on each day deterrmine max profit
            if i >= len(prices):
                return 0
            if held:
                memo[(i, held)] = max(helper(i+1, held), prices[i] + helper(i+2, False))
            else:
                memo[(i, held)] = max(helper(i+1, True) - prices[i], helper(i+1, False))
            return memo[(i, held)]
        return helper(0, False)
