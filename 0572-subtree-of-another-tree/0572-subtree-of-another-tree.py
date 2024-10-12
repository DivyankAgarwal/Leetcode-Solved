# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def check(main_root):
            if main_root is None:
                return False

            elif checkidentical(main_root, subRoot):
                return True
            
            return check(main_root.left) or check(main_root.right)

            

        def checkidentical(root1, root2):
            if root1 is None or root2 is None:
                return root1 is None and root2 is None

            return (root1.val == root2.val) and checkidentical(root1.left, root2.left) and checkidentical(root1.right, root2.right)


        
        

        return check(root)