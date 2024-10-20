# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        '''
        Time Complexity: O(N^2) where N is the number of nodes in the Binary Tree. 
        For each node in the Binary Tree, all other nodes are traversed 
        to calculate its height, resulting in a nested traversal structure, leading 
        to O(N) operations for each of the N nodes, hence O(N * N) = O(N^2).
        
        '''
        
        #Brute O(n2)
        # def get_height(root):
        #     if root is None:
        #         return 0

        #     left = get_height(root.left)
        #     right = get_height(root.right)


        #     return 1 + max(left,right)


        # if root is None:
        #     return True

        # left = get_height(root.left)
        # right = get_height(root.right)


        # if abs(left - right) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right):
        #     return True
        
        # return False

        #Better

        def dfsHeight(root):

            if not root:
                return 0

            
            leftHeight = dfsHeight(root.left)
            
            if leftHeight == -1:
                return -1

            
            rightHeight = dfsHeight(root.right)

            if rightHeight == -1:
                return -1

            
            if abs(leftHeight - rightHeight) > 1:
                return -1

            
            return 1 + max(leftHeight, rightHeight) 

        
        return dfsHeight(root) != -1

        