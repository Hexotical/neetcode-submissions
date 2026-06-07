"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    seen = dict()
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return
        if node in self.seen:
            return self.seen[node]
        
        new_node = Node(val = node.val)
        self.seen[node] = new_node
        for neighbor in node.neighbors:
            new_node.neighbors.append(self.cloneGraph(neighbor))
        #Ok there are loops
        return new_node