# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def get_height(root):
            if root is None:
                return 0

            left = get_height(root.left)
            right = get_height(root.right)


            return 1 + max(left,right)


        if root is None:
            return True

        left = get_height(root.left)
        right = get_height(root.right)


        if abs(left - right) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right):
            return True
        
        return False

        