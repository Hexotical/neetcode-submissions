class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        #Impossible to finish all classes?
        #Deal with multiple prerequisites?
        requirements = dict()
        rev_req = dict()
        for pre in prerequisites:
            if pre[0] not in requirements:
                requirements[pre[0]] = {pre[1]}
                if pre[1] not in rev_req:
                    rev_req[pre[1]] = {pre[0]}
                else:
                    rev_req[pre[1]].add(pre[0])
            else:
                requirements[pre[0]].add(pre[1])
                if pre[1] not in rev_req:
                    rev_req[pre[1]] = {pre[0]}
                else:
                    rev_req[pre[1]].add(pre[0])
        
        
        bfs = deque([])
        for i in range(numCourses):
            if i not in requirements:
                bfs.append(i)
        taken = []
        #print(bfs)
        #print(rev_req)
        while bfs:
            #Classes that had requirements satisfied
            to_take = bfs.popleft()
            taken.append(to_take)
            if to_take in rev_req:
                for c in rev_req[to_take]:
                    #print(requirements[c])
                    #Classes that require this calass
                    
                    requirements[c].remove(to_take)
                    if not requirements[c]:
                        bfs.append(c)
                    
                        
            

        if len(taken) == numCourses:
            return taken
        return []
        
