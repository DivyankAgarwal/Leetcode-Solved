# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        if l1 is None and l2 is None:
            return [0]

        if l1 is None:
            return l2

        if l2 is None:
            return l1

        temp = ListNode()
        pointer = temp
        carryover = 0

        while l1 or l2 or carryover:

            if l1:
                val1 = l1.val
            else:
                val1 = 0

            if l2:
                val2 = l2.val
            else:
                val2 = 0


            s = val1 + val2 +  carryover

            #if s > 9:
            carryover = s // 10 #get the tenths digit
            newnode = ListNode(s % 10) #get the units digit
            #else:
                #newnode = ListNode(s)

            pointer.next = newnode

            pointer = newnode

            if l1:
                l1 = l1.next
            else: l1 = None

            if l2:
                l2 = l2.next
            else: l2 = None

        
        # if carryover == 1:
        #     newnode = ListNode(carryover)
        #     pointer.next = newnode


        return temp.next









        