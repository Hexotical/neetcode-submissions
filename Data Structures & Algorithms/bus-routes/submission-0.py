class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        #Array routes representing bus routes
        #routes at i is a route that ith bus repeats forever
        #Start at source
        if source == target:
            return 0
        #Return least number of busese to take from source to target
        graph = defaultdict(list)
        for i, v in enumerate(routes):
            for stop in v:
                graph[stop].append(i)
        bfs = deque([])
        for route in graph[source]:
            bfs.append((source, route, 1))
        #Feels a little like union find lol
        #
        visited = set()
        #I want to return number of bussessss, ohhh
        #Bfs shortest path
        
        while bfs:
            stop, route, transfers = bfs.popleft()
            #print(stop, route, transfers)
            if stop == target:
                return transfers
            if (stop, route) in visited:
                continue
            for s in routes[route]:
                if s != stop:
                    bfs.append((s, route, transfers))
            for t in graph[stop]:
                if t != route:
                    bfs.append((stop, t, transfers + 1))
            visited.add((stop, route))

            
            
        return -1


