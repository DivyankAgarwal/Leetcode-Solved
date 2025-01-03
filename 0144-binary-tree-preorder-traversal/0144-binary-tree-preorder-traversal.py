# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        #recursive

        # def helper(root, result):
        #     if root is None:
        #         return

        #     result.append(root.val)
        #     helper(root.left, result)
        #     helper(root.right, result)


        # result = []

        # helper(root, result)

        # return result


        #iterative

        preorder = []
        stack = []

        if root is None:
            return preorder

        stack.append(root)

        while stack:
            root = stack.pop()

            preorder.append(root.val)


            if root.right:
                stack.append(root.right)


            if root.left:
                stack.append(root.left)

        return preorder
        