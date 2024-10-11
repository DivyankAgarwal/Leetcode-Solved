from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if root is None:
            return []

        ans = []
        q = deque()

        q.append(root)
        zigzag = False

        while q:
            levels= []

            for _ in range(len(q)):
                root = q.popleft()

                if root:
                    levels.append(root.val)

                if root.left:
                    q.append(root.left)

                if root.right:
                    q.append(root.right)


            if zigzag:
                levels.reverse()
            
            ans.append(levels)
            
            zigzag = not zigzag

        return ans


        