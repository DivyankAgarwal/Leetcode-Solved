# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:

        #anticlocker - divide in 3 parts like add left boundary, add leaves, add right boundary (reverse of left)

        def addleft(root, result):
            current = root.left

            while current:
                if not checkIfLeaves(current):
                    result.append(current.val)

                if current.left:
                    current = current.left

                else:
                    current = current.right

        def addleaves(root, result): #inorder left-root-right
            if checkIfLeaves(root):
                result.append(root.val)
                return

            if root.left:
                addleaves(root.left, result)

            if root.right:
                addleaves(root.right, result)
                

            

        def addright(root, result):
            current = root.right
            temp = []

            while current:
                if not checkIfLeaves(current):
                    temp.append(current.val)

                if current.right:
                    current = current.right

                else: 
                    current = current.left
            
            result.extend(temp[::-1])


        def checkIfLeaves(current):
            return current and not current.left and not current.right
        if not root:
            return []

        result = []

        if not checkIfLeaves(root):
            result.append(root.val)

        addleft(root, result)
        addleaves(root, result)
        addright(root, result)

        return result
        