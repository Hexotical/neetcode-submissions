# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        #This seems like dynamic porgramming?
        #yeaaaa
        #a node can only appear once is important
        to_ret = -1001
        def dfs(node):
            if not node:
                return 0

            nonlocal to_ret

            if not node.left and not node.right:
                to_ret = max(to_ret, node.val)
                return node.val
            
            max_left = dfs(node.left)

            max_right = dfs(node.right)

            to_ret = max(node.val + max_left + max_right, to_ret, node.val, node.val + max_left, node.val + max_right)

            return max(node.val + max(max_left, max_right), node.val)
        
        dfs(root)
        

        return to_ret