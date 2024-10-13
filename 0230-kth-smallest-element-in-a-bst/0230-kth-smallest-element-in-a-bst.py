# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #brute
        # def inorder(root, values): #left, root, right
        #     if root is None:
        #         return

        #     inorder(root.left, values)
        #     values.append(root.val)
        #     inorder(root.right, values)

        # values = []
        # inorder(root, values)

        # values.sort()

        # return values[k-1]


        #optimal

        self.k = k
        self.result = None
        
        def inorder(root):
            if not root:
                return
            
            inorder(root.left)
            
            self.k -= 1
            if self.k == 0:
                self.result = root.val
                return
        
            inorder(root.right)
        
    
        inorder(root)
        return self.result
        