# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #brute
        def inorder(root, values): #left, root, right
            if root is None:
                return

            inorder(root.left, values)
            values.append(root.val)
            inorder(root.right, values)

            


        values = []
        inorder(root, values)

        values.sort()

        return values[k-1]
        