# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        q = deque()

        q.append([root,0])
        width = 0

        while q:
            n = len(q)
            mini = q[0][1]
            
            first = 0
            last = 0

            for i in range(n):

                cur = q[0][1] - mini

                root =  q[0][0]

                q.popleft()

                if i == 0:
                    first = cur

                if i == n - 1:
                    last = cur

                if root.left:
                    q.append([root.left, 2*cur+1])


                if root.right:
                    q.append([root.right, 2*cur+2])

            width = max(width, last-first+1)

        return width

        