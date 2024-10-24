# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:

        mini = float('inf')
        in_nodes = []


        def inorder(root):
            
            if root is None:
                return
            
            inorder(root.left)
            in_nodes.append(root.val)
            inorder(root.right)


        inorder(root)
        
        for n in range(1, len(in_nodes)):
            mini = min(mini, abs(in_nodes[n] - in_nodes[n-1]))

        
        return mini
        