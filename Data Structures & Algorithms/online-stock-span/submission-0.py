class StockSpanner:

    def __init__(self):
        self.stack = []
        

    def next(self, price: int) -> int:
        #Goingn backwards
        to_ret = 1
        for i in range(len(self.stack)-1, -1, -1):
            if self.stack[i] <= price:
                to_ret += 1
            else:
                self.stack.append(price)
                return to_ret
        self.stack.append(price)
        return to_ret


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)