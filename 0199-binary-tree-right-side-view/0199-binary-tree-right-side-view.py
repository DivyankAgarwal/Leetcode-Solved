from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        if root is None:
            return []

        q = deque()

        ans = []

        q.append(root)

        while q:
            n = len(q)

            for i in range(n):

                node = q.popleft()
                
                if i == n-1:
                    ans.append(node.val)

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

        return ans

        



        