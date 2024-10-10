# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        #recursive

        def helper(root, inorder):

            if root is None:
                return

            helper(root.left, inorder)
            inorder.append(root.val)
            helper(root.right, inorder)
            

        inorder = [] #left->root->right
        helper(root, inorder)

        return inorder
        