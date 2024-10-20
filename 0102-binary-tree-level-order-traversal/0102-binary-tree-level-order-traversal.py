from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:


        if root is None:
            return []

        ans = []
        queue = deque()

        queue.append(root)

        while queue:
            levels = []

            for  _ in range(len(queue)):

                root = queue.popleft()

                if root:
                    levels.append(root.val)


                if root.left:
                    queue.append(root.left)


                if root.right:
                    queue.append(root.right)
            
            ans.append(levels)
        
        return ans


        