# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        def helper(root):

            if root is None:
                return 0


            left = helper(root.left)
            right = helper(root.right)

            self.diameter = max(self.diameter, left+right)

            #The height of a node is the number of edges on the longest path from that node to a leaf.
            # By returning this value, the recursion ensures that the height of the current node is 
            #passed up to its parent, and so on, until the entire tree is processed.
            return 1 + max(left,right)

        self.diameter = 0

        helper(root)


        return self.diameter



        '''
        Why we can't just sum left + right at each node directly:
        left + right at each node gives the longest path passing through that node. 
        This may contribute to the diameter, but it is not always the diameter of the tree. 
        The true diameter could be in one of the subtrees instead of passing through the current node.
        Height is necessary to determine how far we can "stretch" down both the left and right 
        subtrees when considering the diameter that passes through the current node. But for
         nodes higher up in the tree, the diameter might actually be inside one of the subtrees.

        Key takeaway:
        The height of a node helps calculate the diameter because:

        The diameter through a node depends on the height of its left and right subtrees.
        The height of a node is needed to check the longest path through each node, ensuring we don’t 
        miss diameters inside subtrees.

        In summary:
        The height is returned for each node because you need it for the parent nodes to calculate the 
        diameter (the longest path through the left and right subtrees).
        left + right gives the diameter through the current node but does not give the overall diameter 
        of the tree, which might be inside a subtree.   
        
        
        '''
        
        