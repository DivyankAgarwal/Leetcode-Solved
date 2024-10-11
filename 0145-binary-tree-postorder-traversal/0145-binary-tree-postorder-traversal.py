# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        #left-right-root

        def helper(root, postorder):
            if root is None:
                return

            helper(root.left, postorder)
            helper(root.right, postorder)
            postorder.append(root.val)


        postorder = []

        helper(root, postorder)

        return postorder
        