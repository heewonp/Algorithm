# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        
        node = head
        res = []
        
        while node:
            res.append(node.val)
            node = node.next
        
        s = len(res)
        
        return max(res[i]+res[s-1-i]for i in range(s//2))
            