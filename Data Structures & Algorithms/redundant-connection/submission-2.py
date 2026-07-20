class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parents = {}
        to_ret = edges[0]
        for [x, y] in edges:
            if x in parents and y in parents:
                runner = parents[x]
                seen  = [x]
                while runner != parents[runner]:
                    seen.append(runner)
                    runner = parents[runner]
                for node in seen:
                    parents[node] = runner
                parents[x] = runner
                runner = parents[y]
                seen = [y]
                while runner != parents[runner]:
                    seen.append(runner)
                    runner = parents[runner]
                for node in seen:
                    parents[node] = runner
                if parents[x] == parents[y]:
                    to_ret = [x,y]
                else:
                    parents[parents[x]] = parents[y]
                    parents[x] = parents[y]
            elif x in parents:
                runner = parents[x]
                seen  = [x]
                while runner != parents[runner]:
                    seen.append(runner)
                    runner = parents[runner]
                parents[x] = runner
                parents[y] = runner
                for node in seen:
                    parents[node] = runner
            elif y in parents:
                runner = parents[y]
                seen = [y]
                while runner != parents[runner]:
                    seen.append(runner)
                    runner = parents[runner]
                parents[y] = runner
                parents[x] = runner
                for node in seen:
                    parents[node] = runner
            else:
                parents[y] = parents[x] = x
                
        return to_ret
        