# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:


        def findmin(root):
            while root.left:
                root = root.left
            return root

        if not root:
            return None


        if key < root.val:
            root.left = self.deleteNode(root.left, key)

        elif key > root.val:
            root.right = self.deleteNode(root.right, key)

        else:
            #equal case.
            #1. no left and no right children

            if not root.left and not root.right:
                return None

            elif not root.left and root.right:
                return root.right

            elif not root.right and root.left:
                return root.left

            else:
                #it has both children. We Inorder auccessdor

                successor = findmin(root.right)

                root.val = successor.val

                root.right =  self.deleteNode(root.right,successor.val)

        return root

        