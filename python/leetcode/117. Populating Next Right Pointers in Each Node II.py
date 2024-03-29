"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque
class Solution:
    def connect(self, root: 'Node') -> 'Node':

        if not root :
            return 
        
        queue = deque([root])
        
        
        while queue:
            prev = None
            for _ in range(len(queue)):
                p = queue.popleft()
                
                if prev:
                    prev.next = p
                prev = p
                
                if p.left :
                    queue.append(p.left)
                    
                if p.right:
                    queue.append(p.right)
                
        return root
            
                
        