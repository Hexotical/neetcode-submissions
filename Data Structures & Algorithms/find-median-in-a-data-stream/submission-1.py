class MedianFinder:
    #I mean i'd want to just maintain a sorted list somehow
    #i suppose doable with two heaps
    #one max heap, one min heap
    

    def __init__(self):
        self.minHeap = []
        self.maxHeap = []
        heapq.heapify(self.minHeap)
        heapq.heapify(self.maxHeap)
        

    def addNum(self, num: int) -> None:
        #Try and keep them balanced
        if self.minHeap and num * -1 > self.minHeap[0]:
            to_max = heapq.heappop(self.minHeap) * -1
            heapq.heappush(self.maxHeap, to_max)
            heapq.heappush(self.minHeap, num * -1)
        else:
            heapq.heappush(self.maxHeap, num)
        if len(self.maxHeap) - len(self.minHeap) > 1:
            to_add_min = heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, -1 * to_add_min)
        print("adding ", num)
        print(self.minHeap)
        print(self.maxHeap)

    def findMedian(self) -> float:
        if len(self.maxHeap) - len(self.minHeap) == 0:
            return (self.maxHeap[0] + -1 * self.minHeap[0]) / 2
        else:
            return self.maxHeap[0]
        
        