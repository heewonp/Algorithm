# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        a_head = headA
        b_head = headB
        while a_head != b_head:
            a_head = a_head.next if a_head else headB
            b_head = b_head.next if b_head else headA
        return a_head
        