class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        #Min number cpu cycles to complete all tasks
        #Identical tasks must be separated by at least n cycles
        #So greediness is pick by count
        tasks = Counter(tasks)
        #Heap tracks greedy scheduling
        #Dictionary of when task was last run?
        #Oh no just keep track of next cycle task can run
        
        heap = []
        for task in tasks:
            heap.append(-tasks[task])
        
        heapq.heapify(heap)
        #print(heap)
        queue = deque()

        cycle = 1


        while heap:
            #print(cycle, heap, queue)
            count = heapq.heappop(heap)
            if count == 0:
                continue
            cycle += 1
            if count < -1:
                queue.append([count+1, cycle + n])

            if not heap and queue:
                cycle = queue[0][1]
            while queue and queue[0][1] <= cycle:
                heapq.heappush(heap, queue.popleft()[0])
        return cycle - 1

        
        
        