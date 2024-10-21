# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:

        if not head:
            return head

        nums = []
        while head:
            nums.append(head.val)
            head = head.next

        def buildBST(left, right):

            if left > right:
                return None
            
            mid = left + (right-left) // 2
            
            root = TreeNode(nums[mid])
            
            root.left = buildBST(left, mid - 1)
            root.right = buildBST(mid + 1, right)
            
            return root

        return buildBST(0, len(nums) - 1)
        