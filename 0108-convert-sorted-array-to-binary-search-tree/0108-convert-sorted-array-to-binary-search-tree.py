# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        if len(nums) == 0:
            return None

        def geneateBst(left,right):
            if left>right:
                return

            mid = left + (right-left) // 2

            root = TreeNode(nums[mid])

            root.left = geneateBst(left, mid-1)
            root.right = geneateBst(mid+1, right)

            return root



        left = 0
        right = len(nums)-1
        return geneateBst(left, right)
        