class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = dict()
        for e in edges:
            if e[0] not in graph:
                graph[e[0]] = [e[1]]
            else:
                graph[e[0]].append(e[1])
            if e[1] not in graph:
                graph[e[1]] = [e[0]]
            else:
                graph[e[1]].append(e[0])
        visited = set()
        to_ret = 0
        for i in range(n):#There's a guarantee of no self loops which is nice
            if i in visited:
                continue
            to_ret += 1
            search = [i]
            while search:
                node = search.pop()
                if node in visited:
                    continue
                visited.add(node)
                if node in graph:
                    for child in graph[node]:
                        search.append(child)
        
        return to_ret