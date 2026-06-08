class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        #Min time for all n nodes to reveive the signal
        #ui is source node
        #Bfs all nodes

        graph = dict()
        travel = dict()

        for s, d, t in times:
            if s not in graph:
                graph[s] = [d]
            else:
                graph[s].append(d)
            travel[(s, d)] = t
        time_delay = dict()
        bfs = deque([(k, 0)])
        while bfs:
            node, time = bfs.popleft()
            if node not in time_delay:
                time_delay[node] = time
            else:
                if time_delay[node] <= time:
                    continue
            time_delay[node] = time
            if node in graph:
                for child in graph[node]:
                    bfs.append((child, time + travel[(node, child)]))


        if len(time_delay) != n:
            return -1
        else:
            max_time = 0
            for child in time_delay:
                max_time = max(max_time, time_delay[child])
            return max_time
        
