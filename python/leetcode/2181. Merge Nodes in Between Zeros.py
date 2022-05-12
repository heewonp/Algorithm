# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        prev = head.next
        cnt = 0
        
        while prev:
            if prev.val == 0:
                node = node.next
                node.val = cnt
                cnt = 0
            else:
                cnt += prev.val
            prev = prev.next
            
        node.next = None
        return head.next