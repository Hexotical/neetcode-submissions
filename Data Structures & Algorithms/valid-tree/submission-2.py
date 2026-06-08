class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #Are edges a valid tree
        #Ok so a tree is an undirected graph with no cycles
        #Just dfs and see if we visit 
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
        
        def dfs(parent, node):
            if node in visited:
                return False
            visited.add(node)
            if node in graph:
                for child in graph[node]:
                    if child != parent:
                        if not dfs(node, child):
                            return False
            return True
        return dfs(-1, 0) and len(visited) == n
            