# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if root1 == None and root2 == None:
            return None
        
        if root1 == None:
            return root2
        elif root2 == None:
            return root1
        else:
            new_root = TreeNode(root1.val+root2.val)
            left = self.mergeTrees(root1.left,root2.left)
            right = self.mergeTrees(root1.right,root2.right)
            new_root.left = left
            new_root.right = right
            
        return new_root
        