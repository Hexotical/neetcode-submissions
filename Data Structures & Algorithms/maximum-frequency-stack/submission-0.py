class FreqStack:

    def __init__(self):
        self.stack = []
        self.frequencies = defaultdict(int)
        self.heap = []
        heapq.heapify(self.heap)
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.frequencies[val] += 1
        heapq.heappush(self.heap, (-1 * self.frequencies[val], -1 * len(self.stack), val))
        

    def pop(self) -> int:
        freq, index, val = heapq.heappop(self.heap)
        self.frequencies[val] -= 1
        return val
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()

#In event of tie element closest to stack's top is removed
#so order matters
#Now how do i keep track of frequencies?
#Maybe a dict? but then what about in the event of a tie
#How do i keep track of that most frequent element/s
#Ok fine ordered sets are apparently a thing
#