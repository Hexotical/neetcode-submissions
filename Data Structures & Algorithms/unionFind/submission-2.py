class UnionFind:
    
    def __init__(self, n: int):
        self.parents = {}
        self.heights = {}
        for i in range(n):
            self.parents[i] = i
            self.heights[i] = 0
        

    def find(self, x: int) -> int:
        runner = x
        while self.parents[runner] != runner:
            runner = self.parents[runner]
        return runner
        

    def isSameComponent(self, x: int, y: int) -> bool:
        root_x = self.find(x)
        root_y = self.find(y)
        return root_x == root_y

    def union(self, x: int, y: int) -> bool:
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return False
        self.parents[root_x] = root_y
        return True
        

    def getNumComponents(self) -> int:
        to_ret = 0
        for k in self.parents:
            if k == self.parents[k]:
                to_ret += 1
        return to_ret

