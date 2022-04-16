# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        self.r_sum = 0
        self.inorder(root)
        return root
        
    def inorder(self,root):
        if not root:
            return

        self.inorder(root.right)
        root.val += self.r_sum
        self.r_sum = root.val
        self.inorder(root.left)

        