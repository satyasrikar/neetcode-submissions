# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        Prev, Head = None, head

        curr = head
        while curr:
            next_node = curr.next
            curr.next = Prev

            Prev = curr
            curr = next_node
        return Prev