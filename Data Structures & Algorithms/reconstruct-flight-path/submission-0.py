class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        #Assume each ticked used exactly once
        #If multiple, alphabetically smaller
        #So some sort of dfs
        #Dfs enumerate all the possible flight paths 
        #Then sort alphabetically
        #Ok the hint is sorta nice
        #I dfs lexographically smallest first
        #If i find the path it's guaranteed
        #to be the one i want to return
        fun_graph = defaultdict(list)
        for pair in tickets:
            fun_graph[pair[0]].append(pair[1])
        
        for key in fun_graph:
            fun_graph[key].sort()
        print(fun_graph)
        #Oh there are only 300 tickets
        #I could keep track of which tickets are used
        res = []
        def dfs(airport):
            while fun_graph[airport]:
                dest = fun_graph[airport].pop(0)
                dfs(dest)
            res.append(airport)

        dfs("JFK")
       
        return res[::-1]
            