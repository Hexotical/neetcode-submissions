class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        #Total distinct combinations that result in the target amount of money
        #Return 0 if impossible to make the amount
        #Annoyingly what I want to do
        #array from 0 to amount
        #for every coin add distinct way to reach
        to_ret = []
        memo = dict()
        def helper(total, index):
            if (total, index) in memo:
                return memo[(total, index)]
            if total > amount:
                return 0
            if total == amount:
                return 1
            if index == len(coins):
                return 0
            to_ret = helper(total + coins[index], index)
            
            to_ret += helper(total, index + 1)
            memo[(total, index)] = to_ret
            return to_ret
        #helper(0, 0)
        return helper(0,0)