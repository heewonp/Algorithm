# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        
        if not root :
            return 0
        
        self.visited = defaultdict(list)
        
        def dfs(node,depth):
            if not node:
                return
            
            self.visited[depth].append(node.val)
            dfs(node.left, depth+1)
            dfs(node.right, depth+1)
        
        dfs(root,1)
        
        return sum(self.visited[max(self.visited.keys())])