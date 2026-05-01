# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        #Do a dfs
        #give me a string
        #Key on layer?
        to_ret = ""
        woo_stack = [root]
        while woo_stack:
            check = woo_stack.pop()
            if check:
                to_ret += str(check.val) + ","
                woo_stack.append(check.right)
                woo_stack.append(check.left)
            else:
                to_ret += "N,"
        print(to_ret)
        return to_ret

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        nodes = data.split(",")
        nodes = nodes[:-1]
        if nodes[0] == "N":
            return
        
        #print(nodes)
        root = TreeNode(int(nodes[0]))
        parents = [[root, 0]]
        for i in range(1, len(nodes)):
            #If i reach two nulls i pop up a parent
            #print(parents[-1].val, nodes[i])
            if not nodes[i].isdigit():
                #Null
                parents[-1][-1] += 1
                while parents and parents[-1][-1] == 2:
                    parents.pop()
            else:
                
                if parents[-1][-1] == 0:
                    to_add = TreeNode(int(nodes[i]))
                    parents[-1][0].left = to_add
                    parents[-1][-1] += 1
                    parents.append([to_add, 0])
                elif parents[-1][-1] == 1:
                    to_add = TreeNode(int(nodes[i]))
                    parents[-1][0].right = to_add
                    parents[-1][-1] += 1
                    #print(parents[-1].val, parents[-1].right.val)
                    parents.append([to_add, 0])
                
        return root

