# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        tail = dummy
        carry = 0

        while l1 is not None or l2 is not None or carry !=0:
            if l1:
                digit1 = l1.val
            else:
                digit1 = 0
            if l2:
                digit2 = l2.val
            else:
                digit2 = 0
            res = digit1+digit2+carry
            digit = res%10
            carry = res//10

            newNode = ListNode(digit)
            tail.next = newNode
            tail = tail.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        result = dummy.next
        return result
