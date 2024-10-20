# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        '''
        Approach
        Start by checking if the current root node is null or matches one of the target 
        nodes (x or y). If the root is null or matches either target node, then return 
        the root, as it could potentially be the LCA or simply indicate the end of the 
        search path.
        Perform a recursive search in the left subtree to find the nodes x and y. 
        This involves calling the LCA function on the left child of the current root.
        Similarly, perform a recursive search in the right subtree. This entails calling 
        the LCA function on the right child of the current root.
        After completing the recursive searches, analyze the results 
        of both subtree searches. If both recursive calls return non-null values, 
        it implies that one target node was found in each subtree. 
        Consequently, the current root node must be the LCA, as it is the common ancestor 
        of both nodes.
        If only one of the subtree searches returns a non-null result, 
        it indicates that both target nodes are located within the same 
        subtree. In this case, return the non-null result, which represents 
        the LCA found in that subtree.
        
        '''
        # if root == None or root == p or root == q:
        #     return root

        # left = self.lowestCommonAncestor(root.left, p,q)
        # right = self.lowestCommonAncestor(root.right, p,q)


        # if left is None:
        #     return right

        # elif right is None:
        #     return left

        # else:
        #     return root


        #better approach
        # Start from the root of the tree
        current = root
        
        while current:
            
            if p.val < current.val and q.val < current.val:
                current = current.left
           
            elif p.val > current.val and q.val > current.val:
                current = current.right
            # If one node is on the left and the other is on the right (or one is equal to current), we've found the LCA
            else:
                return current
            