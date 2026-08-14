class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #Bottom up???
        #How tf do i bottom up this
        #For each day i can 
        #Buy, sell, hold
        #If i buy, the next act
        max_buy_arr = [0, 0]
        max_sell_arr = [0, 0]
        for i in range(len(prices)-1, -1, -1):
            #For each day calculate max profit
            
            #selling
            max_sell = max(prices[i] + max_buy_arr[-2], max_sell_arr[-1])
            max_buy = max(max_sell_arr[-1] - prices[i], max_buy_arr[-1])
            max_sell_arr.append(max_sell)
            max_buy_arr.append(max_buy)
        print(max_sell_arr, max_buy_arr)
        return max_buy_arr[-1]
        