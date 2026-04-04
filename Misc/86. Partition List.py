# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        part1 = ListNode(0)
        part2 = ListNode(0)
        mid = part2
        result = part1

        while head:
            next_node = head.next
            head.next = None
            if head.val < x:
                part1.next = head
                part1 = part1.next
            else:
                part2.next = head
                part2 = part2.next
            head = next_node
        part1.next = mid.next
        return result.next
