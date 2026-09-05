# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        #if two directly linked houses robbed
        #bad
        memo = dict()
        def dfs(node, to_rob):
            if (node, to_rob) in memo:
                return memo[(node, to_rob)]
            if not node:
                return 0
            if to_rob:
                #can rob
                memo[(node, to_rob)] = max((node.val + dfs(node.left, False) + dfs(node.right, False)), dfs(node.left, True) + dfs(node.right, True))
                return memo[(node, to_rob)]
            else:
                memo[(node, to_rob)] = dfs(node.left, True) + dfs(node.right, True)
                return memo[(node, to_rob)]
            
        return dfs(root, True)